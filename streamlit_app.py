# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define function to plot Reeb vector field
def plot_reeb_vector_field():
    # Define the grid for visualization
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    # Reeb vector field components
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
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

# Display the visualization
st.pyplot(plot_reeb_vector_field())
