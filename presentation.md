---
title: Benchmarking framework for real-time operating system applications
subtitle: Study and implementation with Contiki and Riot
author: Julien Gomez and Trong-Vu Tran
date: June 24th, 2019
institute: Université catholique de Louvain
theme: metropolis
...

# Introduction

## Embedded systems

1,000,000,000,000

## Objectives

- Theoretical summary
- Benchmarking tool

## Theory

TODO Mindmap here

# Why is this important

## Benchmarking tool for RTOS applications

TODO source

## Interest of the community

TODO RIOT Summit 2018

## link with communities

TODO contact with communities mailing list

# Developpement and implementation

## Benchmark definition

> > "A tool designed to assess the performances of a system."

In our case, a benchmarking tool to assess the performances of applications running on different RTOS.

## RTOS

### Contiki
- Cooperative scheduling
- Event-driven

### RIOT
- Preemptive scheduling
- Multithreading

## Metrics

### Framework metric
- Context switching time

### Other metrics
- Interrupt latency
- Memory usage
- Power consumption

## Multiple approaches

### Kernel approach
Implementing the framework in the RTOS kernel.

- Tedious approach
- Strongly platform-dependent

### Extension approach
Implementing the framework as a RTOS extension.

- Contiki app and RIOT module
- Internal clock

### Devices approach
Implementing the framework with external devices.

- Pocket Science Lab board to measure the context switching time
- Laptop to communicate with the PSLab

# Results

## Performances gathering

- Reference value
- Oscilloscope

---

![oscilloscope setup](assets/1.jpg)

## Overhead measurements

TODO comparisons of overhead
TODO discussion

## Framework measurements

TODO assessment of the different approaches

# Conclusion

## Parallel works

Embench (June 11th, 2019)

---

Embench: Recruiting for the Long Overdue and Deserved Demise of Dhrystone as a Benchmark for Embedded Computing by Prof David Patterson

## Future possible improvements

- Add metrics
- Improve the devices framework

## Demonstration

TODO video ou live demo

---

![more oscilloscope setup](assets/2.jpg)

---

![more oscilloscope setup](assets/3.jpg)
