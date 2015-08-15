#coding:utf-8

def temp(x,y,z):
	print "{x}時の{y}は{z}".format(**{"x":x,"y":y,"z":z}) ##.format(**hoge)でhoge内の辞書をしようするように設定

if __name__ == "__main__":
	temp(12,"気温",22.4)
