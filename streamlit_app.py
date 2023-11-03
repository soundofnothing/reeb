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
st.markdown(
    """
    Reeb vector fields are fundamental objects in the study of contact geometry and symplectic topology. They arise from the structure of a contact manifold, which is a smooth manifold endowed with a specific type of geometric structure called a contact structure. A contact structure on a manifold \(M\) is given by a hyperplane field \(\xi\) which is maximally non-integrable. The Reeb vector field is then defined uniquely by the contact form \(\alpha\) associated with the contact structure, satisfying the conditions:

    \[
    \alpha(\text{Reeb}) = 1
    \]

    \[
    d\alpha(\text{Reeb}, \cdot) = 0
    \]

    In simpler terms, the Reeb vector field is a vector field on the contact manifold that flows along the directions where the contact form is constant, and it is transverse to the contact distribution (the hyperplane field \(\xi\)) everywhere.

    In the context of the Weinstein Conjecture, the conjecture asserts the existence of closed orbits of the Reeb vector field on a compact contact manifold. These orbits are crucial for studying the dynamical properties of the manifold.
    """
)

st.write('Visualizing the Reeb vector field on a simple contact manifold.')

# Explanation and Manifold Equation
st.markdown(
    """
    The contact form $\\alpha$ is given by the expression:
    $\\alpha = dz - a y dx - b x dy$
    Here, $a$ and $b$ are coefficients that determine the behavior of the contact form and the Reeb vector field.
    The manifold's equation can be expressed as a level set of a Hamiltonian function $H$ such that $H(x, y, z) = 0$.
    """
)

# User input for parameters a and b
a = st.slider('Parameter a', -10.0, 10.0, 0.0)
b = st.slider('Parameter b', -10.0, 10.0, 0.0)

# Display the visualization
st.pyplot(plot_reeb_vector_field(a, b))
