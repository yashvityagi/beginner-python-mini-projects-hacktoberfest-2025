from PIL import Image

class ascii_art_generator:

    ASCII_CHARACTERS = ' _.,-=+:;cba!?0123456789$W#@Ñ'

    def _resize_image(self, image, new_width: float):

        width, height = image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.43)   # 0.43 is correction factor
        
        resized_image = image.resize((new_width, new_height))

        return resized_image
    
    def _read_image(self, image):

        image = image.convert("L")    # Convert image to grayscale
        pixels_data = image.getdata()

        return list(pixels_data)
    
    def display_ascii_image(self, path: str, new_width: int = 110):

        image = self._resize_image(image=Image.open(path), new_width=new_width)

        pixels_data = self._read_image(image=image)
        pixel_count = len(pixels_data)

        # Normalize pixel color values and map ASCII characters
        characters = "".join([self.ASCII_CHARACTERS[pixel // 30] for pixel in pixels_data])
        ascii_image = "\n".join(characters[i : (i + new_width)] for i in range(0, pixel_count, new_width))

        return ascii_image
    
if __name__ == "__main__":

    generator = ascii_art_generator()