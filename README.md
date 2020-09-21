# MonsterHunter

This project contains the game implementation of fight between monsters and hero.

The aim of the game is to kill the monsters.
The monsters will kill the hero if the hero does not kill the monsters.

The initial health of the hero - 40
The initial health of the orc - 7
The initial health of the dragon - 20
The orc attacks the hero every 1.5s for 1 health damage.
The dragon attacks the hero every 2s for 3 health damage.
The hero attacks depend on the user input. Hero inflict 2 damage to monsters with respective attacks.
Please read the instructions before starting the game.

Folder structure:

a. 01_Executsble : Contain .exe file to run the game. The executable file is present in \01_Executable\dist\MonsterHunter.exe.
                   The file \01_Executable\MonsterHunter.py is the source code.

b. 02_PycharmCode : The source code developed in Pycharm IDE. The whole project with environment.

c. 03_Testting : The example implementation of testing using 'unittest' library.
                 To run the tests please run below script.
                 \03_Testing\test_MonsterHunter.py
                 command: python test_MonsterHunter.py

