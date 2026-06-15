# write code that reads in a user's name from the terminal.  If the name matches
# your name or your tutor's name, then print out "<Name> is an awesome name!"
# Otherwise call a function called print_silly_name(name) - which you must write -
# that prints out "<Name> is a " then print 'silly' (60 times) on one long line
# then print ' name.'
require './input_functions'

def print_silly_name(name)
   # complete this
    print "#{name} is a "
    index = 0
    while (index < 60)
        print "silly "
        index += 1
    end
    puts " name."
end

def main
  name = read_string("What is your name?")
  if name == "Huy" or name == "Ms.Tram"
    puts name + " is an awesome name!"
  else # replace the code below with a call to print_silly_name()
    print_silly_name(name)
  end
end

main