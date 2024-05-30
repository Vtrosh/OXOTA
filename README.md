
# <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/logo.jpeg" alt="Охота Крепкое Logo" width="50" height="50"> Охота Крепкое - Drone Project

## Introduction

Welcome to the Охота Крепкое drone project! Our team has developed an advanced drone with numerous features and capabilities.

Our team, working on the cargo drone project (MIRP), consisted of experienced engineers, enthusiasts, and technological wizards. We combined our skills and knowledge in engineering, programming, and design to create an innovative device for exploring the planet "MIFIORIS".

Throughout the development process, each team member contributed their unique expertise and ideas to the project. Our team was not just a group of engineers but a cohesive team capable of effectively tackling challenges and overcoming obstacles.

We take pride in creating not just a drone, but an innovative technological solution that opens up new possibilities in exploring and resource gathering on the planet "MIFIORIS". Our team is ready for new challenges and looks forward to continuing work on future projects.

<img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/team.jpg" alt="Охота Крепкое Team" width="auto" height="250">

## Code Explanation

### Drone Control via Bluetooth Low Energy (BLE)

This code enables control of the drone through Bluetooth Low Energy (BLE). The drone features several functions including motor control, servo control, and color detection. Let's break down the key components and functions:

- **BLE Control**: The drone can be controlled via BLE using a mobile app or any other BLE-compatible device.
  
- **Motor Control**: The drone has four motors controlled using MX1508 modules. It can move forward, backward, left, and right.

- **Servo Control**: There are two servos: one controls the grabber (serv180), and the other rotates 360 degrees (serv360).

- **Color Detection**: The drone is equipped with a TCS34725 color sensor used for detecting the color of objects in front of it. This is implemented in the `color_det()` function.

- **Data Transmission**: Color data is transmitted via BLE using the BLEUART object.

- **Asynchronous Event Handling**: The code utilizes the `uasyncio` module for asynchronous event handling, such as motor control and color detection.

- **NeoPixel Usage**: NeoPixel is used for displaying the color detected by the color sensor.

This code allows for controlling and monitoring the drone's state via BLE, as well as detecting the color of objects around it.


## Drone Model

Our cargo drone, designed for exploration and resource gathering on the planet "MIFIORIS," features innovative engineering solutions tailored to maximize efficiency and functionality.

### Features:

- **Bucket Grabber Mechanism**: Cargo capture is facilitated through a robust bucket mechanism, allowing for efficient and secure retrieval of resources.

- **Cargo Release System**: Cargo unloading is achieved through the strategic tipping of the cargo box, enabling precise and controlled release of materials.

### Engineering Solutions:

- **Multi-Load Capability**: To ensure maximum transport speed, our drone is equipped with a cutting-edge mechanism capable of handling multiple loads simultaneously. This feature, designed to streamline the transportation process, allows for rapid placement of objects into the cargo box.

- **Precision Cargo Drop System**: We have developed a high-precision cargo drop system to ensure accurate and reliable delivery of resources. This system enhances the overall efficiency of the drone's operations by optimizing the release process.

Our drone model embodies a fusion of advanced technology and practical design, making it an indispensable tool for exploration and resource collection missions on the challenging terrain of planet "MIFIORIS."


### Evolution of the Drone

Below is the evolution of our drone model, showcasing the development stages from the initial concept to the final design.

<table>
  <tr>
    <td style="text-align: center;">
      <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/v1.jpg" alt="Drone Stage 1" style="width: 150px; height: auto;">
      <p>Stage 1</p>
    </td>
    <td style="font-size: 2em; text-align: center;">➡️</td>
    <td style="text-align: center;">
      <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/v2.jpg" alt="Drone Stage 2" style="width: 150px; height: auto;">
      <p>Stage 2</p>
    </td>
    <td style="font-size: 2em; text-align: center;">➡️</td>
    <td style="text-align: center;">
      <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/v3.jpg" alt="Drone Stage 3" style="width: 150px; height: auto;">
      <p>Stage 3</p>
    </td>
    <td style="font-size: 2em; text-align: center;">➡️</td>
    <td style="text-align: center;">
      <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/v4.jpg" alt="Drone Stage 4" style="width: 150px; height: auto;">
      <p>Stage 4</p>
    </td>
  </tr>
</table>


## Gallery

<div style="display: flex; flex-wrap: wrap;">
    <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/dronemodel.jpg" alt="Drone Image 3" style="margin: 10px; max-width: 200px; height: 300px;">
    <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/ddd.jpeg" alt="Drone Image 1" style="margin: 10px; max-width: auto; height: 300px;">
    <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/code.jpeg" alt="Drone Image 2" style="margin: 10px; max-width: auto; height: 500px;">
  <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/grisha.jpeg" alt="Drone Image 2" style="margin: 10px; max-width: auto; height: 500px;">
  <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/teamchill.jpg" alt="Drone Image 2" style="margin: 10px; max-width: auto; height: 100px;">
    <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/logo_demo.jpg" alt="Drone Image 2" style="margin: 10px; max-width: auto; height: 300px;">
    <img src="https://github.com/Vtrosh/OXOTA/blob/main/Пикчи/78Li8wuaLSU.jpg" alt="Drone Image 3" style="margin: 10px; max-width: auto; height: 300px;">
</div>

