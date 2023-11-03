# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define function to plot Reeb vector field
def plot_reeb_vector_field(a, b):
    # Define the grid for visualization
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    # Reeb vector field components for the new contact form
    U = -b * np.ones_like(X)
    V = a * np.ones_like(Y)
    W = np.ones_like(Z)

    # Create the figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the vector field
    ax.quiver(X, Y, Z, U, V, W, length=0.1, normalize=True)

    # Setting labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Reeb Vector Field')

    return fig

# Streamlit app
st.title('Reeb Vector Field Visualization')
st.write('Visualizing the Reeb vector field on a simple contact manifold.')

# User input for parameters a and b
a = st.slider('Parameter a', -10.0, 10.0, 0.0)
b = st.slider('Parameter b', -10.0, 10.0, 0.0)

# Display the visualization
st.pyplot(plot_reeb_vector_field(a, b))
