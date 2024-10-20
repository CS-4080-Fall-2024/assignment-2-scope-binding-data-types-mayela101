# Generate rubiks cube based on user-input size (n)
def rubiks_faces(n):
    YELLOW ='Y'
    WHITE = 'W'
    BLUE = 'B'
    GREEN = 'G'
    ORANGE ='O'
    RED = 'R'

    return [
        [[YELLOW] * n for i in range(n)],
        [[WHITE] * n for i in range(n)],
        [[BLUE] * n for i in range(n)],
        [[GREEN] * n for i in range(n)],
        [[ORANGE] * n for i in range(n)],
        [[RED] * n for i in range(n)]
    ]

# Display generated rubiks cube 
def print_rubiks(cube):
    for i, face in enumerate(cube, start=1):
        print(f"Face {i}")
        for row in face:
            print(" ".join(row))
        print()

# Single Layer Rotation
def rotate(cube, layer, size):
    top = cube[0]
    front = cube[2]
    bottom = cube[1]
    back = cube[3]

    # Save top layer
    save = top[layer][:]

    for i in range(n):
        top[layer][i] = back[n-1-i][layer]
        back[n-1-i][layer] = bottom[n-1-layer][n-1-i]
        bottom[n-1-layer][n-1-i] = front[i][layer]
        front[i][layer] = save[i]

# Clockwise rotation
def rotate_clockwise(face):
    size = len(face)
    new_face = [[None] * size for _ in range(size)]  

    for i in range(size):
        for j in range(size):
            new_face[j][size - 1 - i] = face[i][j]  

    return new_face

# Counter-clockwise rotation
def rotate_counterclockwise(face):
    new_face = [[None] * len(face) for _ in range(len(face))]  

    for i in range(len(face)):
        for j in range(len(face)):
            new_face[len(face) - 1 - j][i] = face[i][j]  

    return new_face


if __name__ == "__main__":
    # User-input size
    n=int(input("Enter the size of the cube: "))

    # Cube generation
    cube = rubiks_faces(n)
    print_rubiks(cube)

    # TEST
    print("Top Layer Rotation Demo")
    rotate(cube, 0, n)
    print_rubiks(cube)

    print("Clockwise Rotation Demo")
    cube[0] = rotate_clockwise(cube[0])
    print_rubiks(cube)

    print("Counter-Clockwise Rotation Demo")
    cube[0] = rotate_counterclockwise(cube[0])
    print_rubiks(cube)