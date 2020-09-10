# from flask import Flask
# app = Flask(__name__)

# @app.route("/index1.html")
# def hello():
#     for i in range(0,1000):
#         if i % 2 == 0 :continue
#     return i
# if __name__=="__main__":
#     app.run()

import numpy as np

list1= np.array([3,6,9,12])
print(list1/3.0)
# [1,2,3,4]
list2=[3,6,9,12]
print(list2/3.0)
# unsupported operand type(s) for /: 'list' and 'float'