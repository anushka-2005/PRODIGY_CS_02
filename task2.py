from PIL import Image

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Example encryption: swapping red and blue channels
            pixels[i, j] = (b, g, r)
    
    return image

def swap_back_pixels(image):
    width, height = image.size
    pixels = image.load()
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Example decryption: swapping red and blue channels back
            pixels[i, j] = (b, g, r)
    
    return image

def encrypt_image(input_path, output_path):
    # Open the image
    image = Image.open(input_path)
    
    # Encrypt the image
    encrypted_image = swap_pixels(image.copy())
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path):
    # Open the encrypted image
    encrypted_image = Image.open(input_path)
    
    # Decrypt the image
    decrypted_image = swap_back_pixels(encrypted_image.copy())
    
    # Save the decrypted image
    decrypted_image.save(output_path)
    
    print(f"Image decrypted and saved as {output_path}")

# Example usage:
if __name__ == "__main__":
    input_image = r"C:\Users\91971\Desktop\example.jpg"
    encrypted_output = r"C:\Users\91971\Desktop\encrypted_example.jpg"
    decrypted_output = r"C:\Users\91971\Desktop\decrypted_example.jpg"
    
    # Encrypt the image
    encrypt_image(input_image, encrypted_output)
    
    # Decrypt the encrypted image
    decrypt_image(encrypted_output, decrypted_output)
