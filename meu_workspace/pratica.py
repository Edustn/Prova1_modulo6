#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time
from threading import Timer
from collections import deque

# Essa parte do codigo peguei da minha ponderada 
class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move_turtle(self, linear, angular):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.y = angular
        self.publisher.publish(twist)

def desenho(controller, dq):
    count = 10

        
    controller.move_turtle(float(dq[0]), float(dq[1]))



def main(args=None):
    rclpy.init(args=args)
    controller = TurtleController()

    # print("Desenhando no Turtlesim...")
    print("Digite valores para vx, vy, velocidade e tempo(ms)")
    x = input()
    # while(len(x) > 3):
    #     print("Comando invalido tente novamente ")
    #     x = input()
        
    valores = x.split()

    dq = deque()

    for i in range(len(valores)):
        dq.append(valores[i])


    desenho(controller, dq)




if __name__ == '__main__':
    main()
