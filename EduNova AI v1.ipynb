{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPzf2/y4QRAq+ybiA4qQhMR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MithravindaU/EduNova-AI/blob/main/chatbot.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "ymLas6xveEOY",
        "outputId": "f68a3a3e-69d4-4c23-eac4-1f4df6c839e8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.12/dist-packages (1.57.0)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<8,>=5.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.2.6)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.3.3)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.47)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (26.1)\n",
            "Requirement already satisfied: pandas<4,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<13,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.9.2)\n",
            "Requirement already satisfied: protobuf<8,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (9.1.4)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)\n",
            "Requirement already satisfied: starlette>=0.40.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.52.1)\n",
            "Requirement already satisfied: uvicorn>=0.30.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.46.0)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.7.1)\n",
            "Requirement already satisfied: anyio>=4.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.13.0)\n",
            "Requirement already satisfied: python-multipart>=0.0.10 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.0.26)\n",
            "Requirement already satisfied: websockets>=12.0.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (15.0.1)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.0)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.26.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2.20.0)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio>=4.0.0->streamlit) (3.13)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<4,>=1.4.0->streamlit) (2026.1)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2026.4.22)\n",
            "Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.12/dist-packages (from uvicorn>=0.30.0->streamlit) (0.16.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.3)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (26.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2025.9.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.37.0)\n",
            "Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pyngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "RGCGChD6jrI5",
        "outputId": "2ce67204-476f-46f0-e593-5f7076b756ab"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.12/dist-packages (8.1.2)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.12/dist-packages (from pyngrok) (6.0.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wZBx08y0fNpT",
        "outputId": "2bd835d3-98ad-490d-c34f-8eef6f336a33"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "responses = {\n",
        "\n",
        "    \"greeting\": {\n",
        "        \"inputs\": [\"hi\", \"hello\", \"hey\"],\n",
        "\n",
        "        \"responses\": [\n",
        "            \"Hello 👋\",\n",
        "            \"Hey there!\",\n",
        "            \"Hi student 🚀\"\n",
        "        ]\n",
        "    },\n",
        "\n",
        "    \"ml\": {\n",
        "        \"inputs\": [\n",
        "            \"ml\",\n",
        "            \"machine learning\",\n",
        "            \"what is ml\"\n",
        "        ],\n",
        "\n",
        "        \"responses\": [\n",
        "            \"Machine Learning is AI that learns from data.\",\n",
        "            \"ML helps systems recognize patterns.\"\n",
        "        ]\n",
        "    },\n",
        "\n",
        "    \"robotics\": {\n",
        "        \"inputs\": [\n",
        "            \"robotics\",\n",
        "            \"robot\",\n",
        "            \"what is robotics\"\n",
        "        ],\n",
        "\n",
        "        \"responses\": [\n",
        "            \"Robotics combines AI with machines.\",\n",
        "            \"Robots use sensors and intelligent control.\"\n",
        "        ]\n",
        "    },\n",
        "\n",
        "    \"bye\": {\n",
        "        \"inputs\": [\"bye\", \"goodbye\"],\n",
        "\n",
        "        \"responses\": [\n",
        "            \"Goodbye 👋\",\n",
        "            \"See you later!\"\n",
        "        ]\n",
        "    }\n",
        "}\n",
        "\n",
        "st.title(\"🤖 EduNova AI\")\n",
        "\n",
        "user_input = st.text_input(\"Ask something:\")\n",
        "\n",
        "if user_input:\n",
        "\n",
        "    user_input = user_input.lower()\n",
        "\n",
        "    found = False\n",
        "\n",
        "    for category in responses:\n",
        "\n",
        "        if user_input in responses[category][\"inputs\"]:\n",
        "\n",
        "            st.success(\n",
        "                random.choice(\n",
        "                    responses[category][\"responses\"]\n",
        "                )\n",
        "            )\n",
        "\n",
        "            found = True\n",
        "\n",
        "            break\n",
        "\n",
        "    if not found:\n",
        "\n",
        "        st.error(\n",
        "            \"Sorry, I don't understand yet.\"\n",
        "        )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "9amYpfBslbJ4",
        "outputId": "1e06392e-f390-4229-f505-1efa73480dc5"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-05-21 12:53:20.645 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.649 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.652 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.658 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.664 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.665 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.673 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.680 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:53:20.695 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if \"memory\" not in st.session_state:\n",
        "\n",
        "    st.session_state.memory = {}"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YYe1prROmsAV",
        "outputId": "8ab9998b-bf42-42e2-e346-5331814bf016"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-05-21 12:55:45.244 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:45.246 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:45.247 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "user_input = st.text_input(\"Ask something:\")\n",
        "\n",
        "if user_input:\n",
        "\n",
        "    user_input = user_input.lower()\n",
        "\n",
        "    if \"my name is\" in user_input:\n",
        "\n",
        "        name = user_input.replace(\"my name is\", \"\").strip()\n",
        "\n",
        "        st.session_state.memory[\"name\"] = name\n",
        "\n",
        "        st.success(f\"Nice to meet you, {name}!\")\n",
        "\n",
        "    elif \"what is my name\" in user_input:\n",
        "\n",
        "        if \"name\" in st.session_state.memory:\n",
        "\n",
        "            st.success(\n",
        "                f\"Your name is {st.session_state.memory['name']}\"\n",
        "            )\n",
        "\n",
        "        else:\n",
        "\n",
        "            st.error(\"I don't know your name yet.\")\n",
        "\n",
        "    else:\n",
        "\n",
        "        st.write(\"Interesting 👀\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tHxhnE7vmxmM",
        "outputId": "d19981b4-b9fa-4f98-ee5d-12c702e53720"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-05-21 12:55:49.993 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:49.995 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:49.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:49.999 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:50.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:50.003 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-05-21 12:55:50.004 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!npm install -g localtunnel"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ti3tH_BChjOd",
        "outputId": "daad8a5b-9a8d-4a1f-e229-3076369720c2"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K\n",
            "changed 22 packages in 852ms\n",
            "\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K\n",
            "\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K3 packages are looking for funding\n",
            "\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K  run `npm fund` for details\n",
            "\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py &>/content/logs.txt &"
      ],
      "metadata": {
        "id": "2uxAHluRiL4V"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "ngrok.set_auth_token(\"3E2CqrJNRmmZXpOrD7iuB94JY9y_3asDXQQmLKNCKiY3U8dz5\")"
      ],
      "metadata": {
        "id": "BoaaDh_Zj2A9"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "public_url = ngrok.connect(8501)\n",
        "\n",
        "print(public_url)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HMBJ1rwektX9",
        "outputId": "f89ff9f4-9b1d-4bdc-adf3-3c70914fe4dd"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NgrokTunnel: \"https://glider-spirits-plop.ngrok-free.dev\" -> \"http://localhost:8501\"\n"
          ]
        }
      ]
    }
  ]
}
