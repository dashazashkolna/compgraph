#version 330 core
in vec2 aPos;
in vec2 aUV;

uniform mat4 uTransformation;

out vec2 vTexCoords;

void main() {
    vTexCoords = aUV;
    gl_Position = uTransformation * vec4(aPos, 0.0, 1.0);
}
