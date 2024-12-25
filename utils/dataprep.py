import numpy as np

# Example tones of red, green, and blue
red = np.array([255, 71, 71])
green = np.array([0, 255, 0])
blue = np.array([77, 77, 243])

def blend_colors(red, green, blue, weight_r, weight_g, weight_b):
    total_weight = weight_r + weight_g + weight_b
    weights = np.array([weight_r, weight_g, weight_b]) / total_weight
    
    blended_color = np.round(np.dot(weights, np.array([red, green, blue]))).astype(int)

    return blended_color, weights.tolist()

def generate_color_lists(step=0.05, list_length=255):
    colors = []
    values = np.arange(0, 1.1, step)
    
    for r in values:
        for g in values:
            for b in values:
                # Ensure the sum of r, g, b equals 1
                if np.isclose(r + g + b, 1):
                    # Round each value to 2 decimal places
                    colors.append([round(r, 5), round(g, 5), round(b, 5)])
                if len(colors) >= list_length:
                    return colors
    return colors

# Generate the list

def generate_data():
    colors = generate_color_lists()
    input_list = []
    output_list = []
    for color in colors:
        blended_color = blend_colors(red, green, blue, color[0], color[1], color[2])
        input_list.append(blended_color[0])
        output_list.append(color)
    return input_list, output_list

if __name__ == "__main__":
    input_list, output_list = generate_data()

    blend_test = blend_colors(red, green, blue, 0.5, 0.5, 0.0)
    print(blend_test)