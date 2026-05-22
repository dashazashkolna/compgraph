#version 330 core

in vec4 aPos;
in vec2 aUV;
out vec2 vTexCoords;

void main() {
    vTexCoords = aUV;
    gl_Position = aPos;
}