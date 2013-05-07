def does_intersect(point1, point2):
  if is_after(point1, point2):
    first = point2
    second = point1
  else:
    first = point1
    second = point2
  if first[1] + 1 == second[0]:
    return True
  if first[1] >= second[0]:
    return True

def get_new_range(point1, point2):
  return min(point1[0], point2[0]), max(point1[1], point2[1])

def is_after(point1, point2):
  return point1[1] > point2[0]


class Timeline:
  def __init__(self):
    self.range = []

  def add(self, start, end):
    new_point = (start, end)
    if not self.range:
      self.range.append(new_point)
    else:
      new_range = []
      added = False
      for idx, point in enumerate(self.range):
        if not added and does_intersect(new_point, point):
          new_point = get_new_range(new_point, point)
        elif not added and is_after(new_point, point):
          new_range.append(point)
          new_range.append(new_point)
          added = True
        else:
          new_range.append(point)
      if not added:
        new_range.append(new_point)
      self.range = new_range

  def get(self):
    return self.range

class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def does_intersect(self, r):
        # put the points in order
        # am I contained fully in the other range
        return not self.is_less_than(r) and not r.is_less_than(self)
    
    def is_less_than(self, r):
        return self.end < r.start
        
    def merge(self, r):
        # throw an exception if the ranges do not intersect
        self.start = min(self.start, r.start)
        self.end = max(self.end, r.end)
    
    def __str__(self):
        return "%d, %d" % (self.start, self.end)

class Timeline(object):
    def __init__(self):
        self.ranges = []
    
    def add(self, r):
        if not self.ranges:
            self.ranges.append(r)
        else:
            new_ranges = []
            while self.ranges:
                head = self.ranges[0]
                if r.is_less_than(head):
                    break
                elif r.does_intersect(head):
                    r.merge(head)
                else:
                    new_ranges.append(head)
                self.ranges = self.ranges[1:]
            self.ranges = new_ranges + [r] + self.ranges

    def get(self):
        return self.ranges
    
    def __str__(self):
        return ", ".join([r.__str__() for r in self.ranges])
        

r = Range(0, 10)
r2 = Range(1, 2)
r3 = Range(12, 15)

t = Timeline()
t.add(Range(1,3))
t.add(Range(2,5))
print t
t.add(Range(7,9))
print t
t.add(Range(12,14))
print t
t.add(Range(0,10))
print t
