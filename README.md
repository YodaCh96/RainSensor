<!--https://create.arduino.cc/projecthub/MisterBotBreak/how-to-use-a-rain-sensor-bcecd9-->

# Rain-Sensor

A rain sensor is composed of a rain detection plate with a comparator who manages intelligence. The rain sensor detects water that comes short circuiting the tape of the printed circuits.

![Rainsensor](images/Rainsensor.png)

The sensor acts as a variable resistance that will change status : the resistance increases when the sensor is wet and the resistance is lower when the sensor is dry.

The comparator has 2 outputs connected to the rain sensor, a digital output (0/1) and an analog output (0 to 1023).

## Connections

- Arduino &rarr; Comparator
- 5V &rarr; VCC
- GND &rarr; GND
- DO &rarr; D4
- AO &rarr; A0

## Contributing

This is a personal learning project for me. Please feel free to fork this repo. Pull request to submit more programs.

## Feedback

If you find any bug or have any suggestion, please do file issues. I am graceful for any feedback and will do my best to improve this package.

## License

[MIT](LICENSE) © 2020 Ioannis Christodoulakis
