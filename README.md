
## **Table of Contents**
1. [About](#about)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

---

## **About**
In this project, I am attempting to take a audio sample, and transcribe it into piano notes. This will allow me free access to my favourite piano songs just by getting an audio sample of them.

Example:
If I download a song from youtube, I can run it through the program and get a out a music sheet or something of the like to help me learn the play the song on piano.

---

## **Inner Workings**
The program that I wrote works as follows:
- first I will read in the audio file as a .wav file
- using fourier transformations, we will decompose the audio file
- using the decomposed files at a frame length of 0.1 seconds, I will assign note(s) to each segment
- then we will convert the assigned notes into midi

---

## **Installation**
Provide clear instructions to set up your project locally.

```bash
# Clone the repository
git clone https://github.com/yourusername/yourrepo.git

# Navigate to the project directory
cd yourrepo

# Install dependencies
pip install -r requirements.txt