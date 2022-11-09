def dutch_flag(color_list):
  """ (list of str) -> list of str
  Return color_list rearranged so that 'red' strings come first, 'green' second, and 'blue' third.
  >>> color_list = ['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green']
  >>> dutch_flag(['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green'])
  >>> color_list ['red', 'red', 'red', 'red', 'green', 'green', 'blue', 'blue']
  """
  i = 0
  # The start of the green section.
  start_green = 0

  # The index of the first unexamined color.
  start_unknown = 0

  # The index of the last unexamined color.
  end_unknown = len(color_list) - 1
  print(color_list)
  print('start')

  while start_unknown <= end_unknown:
    # If it is red, swap it with the item to the right of the red section.
    if color_list[start_unknown] == 'red':
      color_list[start_green], color_list[start_unknown] \
        = color_list[start_unknown], color_list[start_green]
      start_green += 1
      start_unknown += 1
    # If it is green, leave it where it is.
    elif color_list[start_unknown] == 'green':
      start_unknown += 1
    # If it is blue, swap it with the item to the left of the blue section.
    else:
      color_list[start_unknown], color_list[end_unknown] \
        = color_list[end_unknown], color_list[start_unknown]
      end_unknown -= 1
