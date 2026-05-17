#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <chrono>
#include <thread>

#include "shader_utils.h"
#include "texture.h"

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

bool isAnimating = true;

void keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    if (key == GLFW_KEY_SPACE && action == GLFW_PRESS) {
        isAnimating = !isAnimating;
        std::cout << "Animation " << (isAnimating ? "resumed" : "paused") << std::endl;
    }
}

// Функція обробки кнопок миші
void mouseButtonCallback(GLFWwindow* window, int button, int action, int mods) {
    if (button == GLFW_MOUSE_BUTTON_LEFT && action == GLFW_PRESS) {
        isAnimating = !isAnimating;
        std::cout << "Animation " << (isAnimating ? "resumed" : "paused") << std::endl;
    }
}

// Функція для обмеження FPS
void limitFPS(double targetFPS) {
    static double lastFrameTime = 0.0;
    double currentTime = glfwGetTime();
    double deltaTime = currentTime - lastFrameTime;
    double targetDelta = 1.0 / targetFPS;

    if (deltaTime < targetDelta) {
        std::this_thread::sleep_for(
            std::chrono::milliseconds(static_cast<int>((targetDelta - deltaTime) * 1000))
        );
    }
    lastFrameTime = glfwGetTime();
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
    window = glfwCreateWindow(800, 600, "Rectangle", NULL, NULL);
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

    glfwSetKeyCallback(window, keyCallback);
    glfwSetMouseButtonCallback(window, mouseButtonCallback);

    glClearColor(1.0, 1.0, 1.0, 1.0);

    std::string vertexShaderName = "res/shaders/triangle.vert";
    std::string fragmentShaderName = "res/shaders/triangle.frag";
    GLuint program = createProgram(vertexShaderName, fragmentShaderName);

    GLint texture_loc = glGetUniformLocation(program, "uTexture");

    float vertices[] = {
        // Трикутник 1
        -0.5f,  0.5f,   0.0f, 1.0f,
        -0.5f, -0.5f,   0.0f, 0.0f,
         0.5f, -0.5f,   1.0f, 0.0f,

        // Трикутник 2
        -0.5f,  0.5f,   0.0f, 1.0f,
         0.5f, -0.5f,   1.0f, 0.0f,
         0.5f,  0.5f,   1.0f, 1.0f
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

    GLuint texture = loadTexture("res/textures/img3.png");

    auto transformation = glm::mat4(1.0f);

    float rotationAngle = 0.0f;
    double lastTime = glfwGetTime();
    const double TARGET_FPS = 60.0;
    const float ROTATION_SPEED = 90.0f;

    /* Loop until the user closes the window */
    do
    {

        double currentTime = glfwGetTime();
        float deltaTime = static_cast<float>(currentTime - lastTime);
        lastTime = currentTime;

        if (isAnimating) {
            rotationAngle += ROTATION_SPEED * deltaTime;
            if (rotationAngle > 360.0f) {
                rotationAngle -= 360.0f;
            }
        }

        glm::mat4 transformation = glm::mat4(1.0f);
        transformation = glm::rotate(transformation, glm::radians(rotationAngle), glm::vec3(0.0f, 0.0f, 1.0f));

        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(program);
        glBindVertexArray(VAO);

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture);
        glUniform1i(texture_loc, 0);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        transformation = glm::rotate(transformation, glm::radians(1.0f), glm::vec3(0.0f, 0.0f, 1.0f));
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, glm::value_ptr(transformation));

        /* Swap front and back buffers */
        glfwSwapBuffers(window);

        /* Poll for and process events */
        glfwPollEvents();
        limitFPS(TARGET_FPS);
    } while (!glfwWindowShouldClose(window) && !glfwGetKey(window, GLFW_KEY_ESCAPE));

    glDeleteBuffers(1, &VBO);
    glDeleteVertexArrays(1, &VAO);
    glDeleteProgram(program);
    glDeleteTextures(1, &texture);
    glfwTerminate();
    return 0;
}
