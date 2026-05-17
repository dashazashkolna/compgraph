#version 330 core
in vec4 aPos;
in vec2 aUV;

uniform mat4 uTransformation;

out vec2 vTexCoords;

void main() {
    vTexCoords = aUV;
    vTexCoords.y = 1.0 - vTexCoords.y;
    gl_Position = uTransformation * aPos;
}