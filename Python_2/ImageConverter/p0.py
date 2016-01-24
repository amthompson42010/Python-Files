import sys

height = eval(sys.argv[1])

def main():
   width = height * 2
   center = width/2
   remaining = center + center 
   if(height <= 1280):
     print_ppm(height,width,center,remaining)
   else: 
     print("The image cannot be more than 1280 pixels high!", file=sys.stderr)

def print_ppm(height,width,center,remaining):
     print("P3")
     print(width, height)
     print("255")
     first_color_change = int(center)
     second_color_change = int(remaining)
     for y in range(0, height, 1):
        first_color_change -= 1
        second_color_change -= 1
        for x in range(0, first_color_change, 1):   
           if(x == y):
             print("255 255 255")
           else:
             print("255 0 0")
        for z in range(first_color_change, second_color_change, 1):
           if(z == y):
             print("255 255 255")
           elif((z-(width/2)) == y):
             print("255 255 255")
           else:
             print("0 0 255")
        for l in range(second_color_change, width, 1):
           if((l-(width/2)) == y):
             print("255 255 255")
           else:
             print("0 255 0")
     
main()
