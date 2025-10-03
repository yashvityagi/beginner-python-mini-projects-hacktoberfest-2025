import streamlit as st
import socket
import threading
import json
import time
from datetime import datetime
import uuid

class ChatApp:
    def __init__(self):
        """Initialize the Chat App with socket programming capabilities"""
        self.host = "localhost"
        self.port = 9999
        self.socket = None
        self.client_socket = None
        self.server_running = False
        self.client_connected = False
        self.messages = []
        
    def find_available_port(self, start_port=9999):
        """Find an available port starting from start_port"""
        for port in range(start_port, start_port + 100):
            try:
                test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                test_socket.bind(('localhost', port))
                test_socket.close()
                return port
            except OSError:
                continue
        return None
    
    def start_server(self):
        """Start the chat server using socket programming"""
        try:
            # Find an available port
            available_port = self.find_available_port()
            if available_port is None:
                st.error("❌ No available ports found. Please try again later.")
                return False
            
            # Update port if different from default
            if available_port != self.port:
                self.port = available_port
                st.info(f"ℹ️ Using port {self.port} (default port was busy)")
            
            # Create a socket object
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Allow socket reuse
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Bind the socket to the host and port
            self.socket.bind((self.host, self.port))
            # Start listening for connections
            self.socket.listen(1)
            self.server_running = True
            
            st.success(f"🚀 Server started on {self.host}:{self.port}")
            
            # Start a thread to accept client connections
            server_thread = threading.Thread(target=self.accept_connections)
            server_thread.daemon = True
            server_thread.start()
            
            return True
        except Exception as e:
            st.error(f"❌ Failed to start server: {str(e)}")
            st.info("💡 Try stopping any existing servers or restart the application")
            return False
    
    def accept_connections(self):
        """Accept incoming client connections"""
        while self.server_running:
            try:
                # Accept a connection
                self.client_socket, address = self.socket.accept()
                self.client_connected = True
                st.success(f"✅ Client connected from {address}")
                
                # Start a thread to handle client messages
                client_thread = threading.Thread(target=self.handle_client, args=(self.client_socket,))
                client_thread.daemon = True
                client_thread.start()
                
            except Exception as e:
                if self.server_running:
                    st.error(f"❌ Error accepting connection: {str(e)}")
                break
    
    def handle_client(self, client_socket):
        """Handle messages from connected client"""
        while self.client_connected:
            try:
                # Receive message from client
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    # Parse the JSON message
                    message_data = json.loads(message)
                    message_data['timestamp'] = datetime.now().strftime("%H:%M:%S")
                    message_data['type'] = 'received'
                    
                    # Add to messages list
                    self.messages.append(message_data)
                    
            except Exception as e:
                if self.client_connected:
                    st.error(f"❌ Error handling client: {str(e)}")
                break
    
    def connect_to_server(self, server_host, server_port):
        """Connect to a chat server"""
        try:
            # Create a socket object
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the server
            self.client_socket.connect((server_host, server_port))
            self.client_connected = True
            
            st.success(f"✅ Connected to server at {server_host}:{server_port}")
            
            # Start a thread to receive messages from server
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            return True
        except Exception as e:
            st.error(f"❌ Failed to connect to server: {str(e)}")
            return False
    
    def receive_messages(self):
        """Receive messages from the server"""
        while self.client_connected:
            try:
                # Receive message from server
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    # Parse the JSON message
                    message_data = json.loads(message)
                    message_data['timestamp'] = datetime.now().strftime("%H:%M:%S")
                    message_data['type'] = 'received'
                    
                    # Add to messages list
                    self.messages.append(message_data)
                    
            except Exception as e:
                if self.client_connected:
                    st.error(f"❌ Error receiving messages: {str(e)}")
                break
    
    def send_message(self, message_text, sender_name):
        """Send a message using socket programming"""
        if not self.client_connected:
            st.error("❌ Not connected to any server")
            return False
        
        try:
            # Check if socket is still valid
            if self.client_socket is None:
                st.error("❌ Connection lost. Please reconnect to the server.")
                self.client_connected = False
                return False
            
            # Create message object
            message_data = {
                'id': str(uuid.uuid4()),
                'text': message_text,
                'sender': sender_name,
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'type': 'sent'
            }
            
            # Send message as JSON
            self.client_socket.send(json.dumps(message_data).encode('utf-8'))
            
            # Add to local messages list
            self.messages.append(message_data)
            
            return True
        except ConnectionResetError:
            st.error("❌ Connection lost. The server may have stopped.")
            self.client_connected = False
            return False
        except BrokenPipeError:
            st.error("❌ Connection broken. Please reconnect to the server.")
            self.client_connected = False
            return False
        except Exception as e:
            st.error(f"❌ Failed to send message: {str(e)}")
            # Check if it's a connection error
            if "Broken pipe" in str(e) or "Connection reset" in str(e):
                st.info("💡 Try reconnecting to the server")
                self.client_connected = False
            return False
    
    def stop_server(self):
        """Stop the chat server"""
        self.server_running = False
        if self.socket:
            self.socket.close()
        if self.client_socket:
            self.client_socket.close()
        self.client_connected = False
        st.info("🛑 Server stopped")
    
    def check_connection(self):
        """Check if the connection is still alive"""
        if not self.client_connected or self.client_socket is None:
            return False
        
        try:
            # Try to send a small test message to check connection
            self.client_socket.send(b'')
            return True
        except:
            self.client_connected = False
            return False
    
    def disconnect(self):
        """Disconnect from server"""
        try:
            if self.client_socket:
                self.client_socket.close()
        except:
            pass  # Ignore errors when closing
        finally:
            self.client_connected = False
            self.client_socket = None
            st.info("🔌 Disconnected from server")

def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="Socket Programming Chat App",
        page_icon="💬",
        layout="wide"
    )
    
    st.title("💬 Socket Programming Chat App")
    st.markdown("---")
    
    # Initialize chat app
    if 'chat_app' not in st.session_state:
        st.session_state.chat_app = ChatApp()
    
    chat_app = st.session_state.chat_app
    
    # Sidebar for connection settings
    with st.sidebar:
        st.header("🔧 Connection Settings")
        
        # Server mode
        if st.button("🚀 Start Server", type="primary"):
            chat_app.start_server()
        
        if st.button("🛑 Stop Server"):
            chat_app.stop_server()
        
        st.markdown("---")
        
        # Client mode
        st.subheader("Connect to Server")
        server_host = st.text_input("Server Host", value="localhost")
        server_port = st.number_input("Server Port", value=chat_app.port, min_value=1000, max_value=65535)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔌 Connect"):
                chat_app.connect_to_server(server_host, server_port)
        
        with col2:
            if st.button("🔌 Disconnect"):
                chat_app.disconnect()
        
        with col3:
            if st.button("🔄 Reconnect"):
                chat_app.disconnect()
                time.sleep(0.5)  # Small delay
                chat_app.connect_to_server(server_host, server_port)
        
        st.markdown("---")
        
        # Connection status
        st.subheader("📊 Status")
        if chat_app.server_running:
            st.success("🟢 Server Running")
        else:
            st.error("🔴 Server Stopped")
        
        if chat_app.client_connected:
            st.success("🟢 Client Connected")
        else:
            st.error("🔴 Client Disconnected")
    
    # Main chat interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("💬 Chat Messages")
        
        # Display messages
        if chat_app.messages:
            for message in chat_app.messages:
                # Create message bubble
                if message['type'] == 'sent':
                    st.markdown(f"""
                    <div style="background-color: #007bff; color: white; padding: 10px; 
                                border-radius: 10px; margin: 5px 0; text-align: right;">
                        <strong>{message['sender']}</strong> ({message['timestamp']})<br>
                        {message['text']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background-color: #f1f1f1; color: black; padding: 10px; 
                                border-radius: 10px; margin: 5px 0; text-align: left;">
                        <strong>{message['sender']}</strong> ({message['timestamp']})<br>
                        {message['text']}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("No messages yet. Start a conversation!")
    
    with col2:
        st.subheader("✍️ Send Message")
        
        # Message input
        sender_name = st.text_input("Your Name", value="User", key="sender_name")
        message_text = st.text_area("Message", height=100, key="message_input")
        
        # Send button
        if st.button("📤 Send Message", type="primary"):
            if message_text.strip():
                if chat_app.send_message(message_text, sender_name):
                    st.success("Message sent!")
                    # Clear the message input
                    st.rerun()
                else:
                    st.error("Failed to send message")
            else:
                st.warning("Please enter a message")
        
        # Clear messages button
        if st.button("🗑️ Clear Messages"):
            chat_app.messages = []
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🚀 Built with Streamlit & Socket Programming | 
        <a href="https://github.com" target="_blank">GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)
video
if __name__ == "__main__":
    main()
