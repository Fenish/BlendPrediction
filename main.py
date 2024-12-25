import numpy as np
from utils.dataprep import generate_data, blend_colors, red, green, blue
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


# THE GOAL IS

# I HAVE AND RGB COLOR THAT I WANT FOR EXAMPLE 174, 113, 252
# I WANT TO GET THE PERCENTAGE OF EACH DYE IN THE BLENDED COLOR
# MY RED, GREEN, AND BLUE COLORS FROM DIFFERENT BRANDS SO I DON'T KNOW THEIR ORIGINAL RGB VALUES
# For example i want to get the percentage of each dye in this rgb color: 128, 163, 36
# Model should give me output like this: [0.5, 0.5, 0.0] # 50% red, 50% green, 0% blue, i tested this data
# 
# Details:
# I don't know the original RGB values of the colors
# I want to get the percentage of each dye in the blended color
#
# Problem is:
# For example i want to get percentage of 174, 113, 252
# Model will give me [0.02602029 0.23185349 0.74212636]
# When i try to blend my colors with this weights it gives me 64 118 182

def train():
    # Generate the data
    input_list, output_list = generate_data()

    # Convert the input_list and output_list to numpy arrays
    inputs = np.array(input_list, dtype=np.float32)
    outputs = np.array(output_list, dtype=np.float32)

    # Normalize inputs to range [0, 1]
    scaler = StandardScaler()
    inputs = scaler.fit_transform(inputs)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(inputs, outputs)

    print("Training completed!")
    return model, scaler

def test(model, scaler, test_input):
    # Normalize the test input using the same scaler
    test_input_normalized = scaler.transform([test_input])

    # Predict the dye percentages
    predicted_output = model.predict(test_input_normalized)
    return predicted_output[0]  # Return the first prediction

if __name__ == "__main__":
    # Train the model
    trained_model, scaler = train()

    # Test the model with new data
    test_input = [76, 139, 192]  # Input data (RGB)
    predicted_output = test(trained_model, scaler, test_input)

    print(f"\nPredicted Dye Percentages: {predicted_output}")
    
    # This is testing to check if my model is working and weights are correct
    # This part won't be in the final code
    # Blend colors using the predicted percentages
    blend_test = blend_colors(red, green, blue, predicted_output[0], predicted_output[1], predicted_output[2])
    print(f"\nEXPECTED WEIGHTS BLEND COLOR: {test_input}")
    print(f"OUTPUT WEIGHTS BLEND COLOR: {blend_test[0]}")
