{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMeWqBV2q/Cx+N4s7Q9ZPi6",
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
        "<a href=\"https://colab.research.google.com/github/Marion-Anyango/binary-tree-/blob/main/practises.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oNr3svSmlKQQ",
        "outputId": "2b25f8e1-87bb-47b2-fdda-e73b1e7bcbd7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.11.11 (main, Dec  4 2024, 08:55:07) [GCC 11.4.0]\n"
          ]
        }
      ],
      "source": [
        "import sys   #checks python version\n",
        "print(sys.version)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if(15>2): #indentation\n",
        "  print(\"fifteen is greator than two\")\n",
        "else:\n",
        "    print(\"two is less than fifteen\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FNI9JmoVsdvr",
        "outputId": "e2b478f8-b282-4e3e-aae9-90ff558f92bd"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fifteen is greator than two\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "this is my line of comments\n",
        "which is in more than two lines\n",
        "happy coding!\n",
        "\"\"\"\n",
        "print(\"python is interesting and I must be a guru in coding using python\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v4xmCDw1tPym",
        "outputId": "00aded84-3f1f-4284-d19b-c24a0a8f3d31"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "python is interesting and I must be a guru in coding using python\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#variables"
      ],
      "metadata": {
        "id": "Uz4fx6PPuw0j"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a=4\n",
        "A=\"marion\"\n",
        "(A)='anyango'\n",
        "b='muhandale'\n",
        "print(a)\n",
        "print(A)\n",
        "print((A))\n",
        "print(b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GT5XWPaXu1VP",
        "outputId": "ed8a7ecc-3ce9-4b43-de33-5b3bab353b13"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "anyango\n",
            "anyango\n",
            "muhandale\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=int(3)\n",
        "b=float(3)\n",
        "c=str(3)\n",
        "print(a)\n",
        "print(b)\n",
        "print(c)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kUEsKjgQwX5y",
        "outputId": "5b5d3cec-e522-4659-dc45-b7d2d77c55cc"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "3.0\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=3\n",
        "b='mercy'\n",
        "c=3.0\n",
        "print(type(a))\n",
        "print(type(b))\n",
        "print(type(c))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a9f6kLV1xBGO",
        "outputId": "9139c7a2-fb93-4ef6-8fdd-a7f435607afd"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'str'>\n",
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x,y,z=\"marion\",\"anyango\",\"muhandale\"\n",
        "print(x)\n",
        "print(y)\n",
        "print(z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JHYd6NwYxa9w",
        "outputId": "f13b02e2-93ee-40b3-cd28-0dbb2362baa4"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "marion\n",
            "anyango\n",
            "muhandale\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=y=z=\"orange\"\n",
        "print(y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WRakxemi0MPe",
        "outputId": "51e2bd21-07c3-4d11-edaf-25f24de78a68"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "orange\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "family=['father','mother','sister']\n",
        "a,b,c=family\n",
        "print(c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "03hLzuyb0TQ0",
        "outputId": "c8b4b67f-8278-412d-8ee8-ce285ab8b325"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sister\n"
          ]
        }
      ]
    }
  ]
}