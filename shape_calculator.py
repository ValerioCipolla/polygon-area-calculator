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
      return "Too big for picture"
    else:
      result = ""
      for y in range(self.height):
        for x in range(self.width):
          result += "*"
        result += "\n"
      return result

  def __str__(self):
    return f"Rectangle(width={self.width}, height = {self.height})"

class Square:
  pass

rect = Rectangle(10, 5)

print(rect.get_picture())
print(rect)