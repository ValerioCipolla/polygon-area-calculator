from turtle import width


class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return self.height * 2 + self.width * 2

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      result = ""
      for y in range(self.height):
        for x in range(self.width):
          result += "*"
        result += "\n"
      return result

  #todo
  def get_amount_inside(self, shape):
    object_area = self.get_area()
    shape_area = shape.get_area()
    count = 0
    while object_area > 0:
      object_area -= shape_area
      if object_area >= 0:
        count += 1
    return count


  def __str__(self):
    if self.__class__.__name__ == "Rectangle":
      return f"Rectangle(width={self.width}, height={self.height})" 
    elif self.__class__.__name__ == "Square":
      return f"Square(side={self.width})"

class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
    self.height = side
    self.width = side

  def set_height(self, height):
      self.height = height
      self.width = height

  def set_width(self, width):
      self.width = width
      self.heigth = width


#rect = Rectangle(10, 5)
#print(rect.get_area())
#rect.set_height(3)
#print(rect.get_perimeter())
#print(rect)
#print(rect.get_picture())
#
#sq = Square(9)
#print(sq.get_area())
#sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)
#print(sq.get_picture())
#
#rect.set_height(8)
#rect.set_width(16)
#print(rect.get_amount_inside(sq))