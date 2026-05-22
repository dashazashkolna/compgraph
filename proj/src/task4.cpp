#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "shader_utils.h"
#include "texture.h"

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

bool isMouseOverRectangle(float mouseX, float mouseY, float rectX, float rectY, float rectWidth, float rectHeight) {
    float glMouseX = (mouseX / 400.0f) - 1.0f;
    float glMouseY = 1.0f - (mouseY / 300.0f);

    return (glMouseX >= rectX - rectWidth/2 && glMouseX <= rectX + rectWidth/2 &&
            glMouseY >= rectY - rectHeight/2 && glMouseY <= rectY + rectHeight/2);
}

int main(void)
{
    GLFWwindow* window;

    if (!glfwInit())
        return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);


    /* Create a windowed mode window and its OpenGL context */
    window = glfwCreateWindow(800, 600, "Rectangles", NULL, NULL);
    if (!window)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    /* Make the window's context current */
    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glClearColor(1.0, 1.0, 1.0, 1.0);

    std::string vertexShaderName = "res/shaders/animated_rect.vert";
    std::string fragmentShaderName = "res/shaders/triangle.frag";
    GLuint program = createProgram(vertexShaderName, fragmentShaderName);

    GLint texture_loc = glGetUniformLocation(program, "uTexture");

    float vertices[] = {
        -0.5f,  0.5f,     0.0f, 0.0f,
        -0.5f, -0.5f,     0.0f, 1.0f,
         0.5f, -0.5f,     1.0f, 1.0f,

        -0.5f,  0.5f,     0.0f, 0.0f,
         0.5f, -0.5f,     1.0f, 1.0f,
         0.5f,  0.5f,     1.0f, 0.0f
    };

    GLuint VAO, VBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);

    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    GLint posAttribLocation = glGetAttribLocation(program, "aPos");
    GLint textureCoordsAttribLocation = glGetAttribLocation(program, "aUV");
    GLint transform_loc = glGetUniformLocation(program, "uTransformation");

    glVertexAttribPointer(posAttribLocation, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(posAttribLocation);
    glVertexAttribPointer(textureCoordsAttribLocation, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));
    glEnableVertexAttribArray(textureCoordsAttribLocation);
    glBindVertexArray(0);

    GLuint texture1 = loadTexture("res/textures/img3.png");

    float posX = 0.0f;
    float posY = 0.0f;
    float angle = 0.0f;

    bool isHovered = false;

    double mouseX, mouseY;
    float rectWidth = 1.0f;
    float rectHeight = 1.0f;
    float rotationSpeed = 2.0f;

    double lastTime = glfwGetTime();

    do
    {
        double currentTime = glfwGetTime();
        float deltaTime = (float)(currentTime - lastTime);
        lastTime = currentTime;

        glClear(GL_COLOR_BUFFER_BIT);

        float speed = 3.0f * deltaTime;;

        if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS)
            posX -= speed;
        if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS)
            posX += speed;
        if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS)
            posY += speed;
        if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS)
            posY -= speed;

        posX = std::max(-0.8f, std::min(0.8f, posX));
        posY = std::max(-0.8f, std::min(0.8f, posY));

        glfwGetCursorPos(window, &mouseX, &mouseY);

        bool currentlyHovered = isMouseOverRectangle(mouseX, mouseY, posX, posY, rectWidth, rectHeight);

        if (currentlyHovered && !isHovered) {
            glfwSetCursor(window, glfwCreateStandardCursor(GLFW_HAND_CURSOR));
        } else if (!currentlyHovered && isHovered) {
            glfwSetCursor(window, NULL);
        }

        isHovered = currentlyHovered;
        if (isHovered) {
            angle += rotationSpeed * deltaTime;
            if (angle > 2 * M_PI) angle -= 2 * M_PI;
        }

        glm::mat4 transform = glm::mat4(1.0f);

        transform = glm::translate(transform, glm::vec3(posX, posY, 0.0f));

        transform = glm::rotate(transform, angle, glm::vec3(0.0f, 0.0f, 1.0f));
        glUseProgram(program);

        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, glm::value_ptr(transform));
        glBindVertexArray(VAO);

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture1);
        glUniform1i(texture_loc, 0);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        /* Swap front and back buffers */
        glfwSwapBuffers(window);

        /* Poll for and process events */
        glfwPollEvents();
    } while (!glfwWindowShouldClose(window) && !glfwGetKey(window, GLFW_KEY_ESCAPE));

    glDeleteBuffers(1, &VBO);
    glDeleteVertexArrays(1, &VAO);
    glDeleteProgram(program);
    glDeleteTextures(1, &texture1);
    glfwTerminate();
    return 0;
}
