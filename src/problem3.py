"""
Exam 1, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Ryan Walter.  March 2018.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the  problem3   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 and 2 of problem3'
    window = rg.RoseWindow(500, 400, title)

    # Test 1:
    rect = rg.Rectangle(rg.Point(25, 50),
                        rg.Point(75, 125))
    rect.fill_color = 'green'
    problem3(rect, 5, window)

    # Test 2:
    rect = rg.Rectangle(rg.Point(150, 50),
                        rg.Point(250, 70))
    rect.fill_color = 'blue'
    problem3(rect, 17, window)

    window.render()  # In case students forget to do so.
    window.close_on_mouse_click()

    # A third test on ANOTHER window.problem3.py:43
    title = 'Test 3 of problem3'
    window = rg.RoseWindow(500, 500, title)

    # Test 3:
    rect = rg.Rectangle(rg.Point(100, 50),
                        rg.Point(50, 100))
    rect.fill_color = 'red'
    problem3(rect, 8, window)

    window.render()  # In case students forget to do so.
    window.close_on_mouse_click()

###############################################################################
#
# IMPORTANT:  In the following problem:
#   -- Write ONLY the code for a simple PART of the problem.
#        TEST and get it correct.
#   -- Then add ONLY the code for another PART of the problem.
#        TEST and get it correct.
#   -- Etc. writing chunks of code and testing them ** ONE AT A TIME. **
#
###############################################################################
def problem3(rect, n, window):
    """
    See    problem3_pictures.pdf     for pictures that may help you
    better understand the following specification:

    What comes in:
      -- An rg.Rectangle object.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. Draws the given rg.Rectangle object on the given rg.RoseWindow.
      2. Draws  n  rg.Circle objects on the given rg.RoseWindow such that:
           -- The radius of each rg.Circle
                is half of the height of the given rg.Rectangle.
           -- The first (leftmost) rg.Circle is centered at the lower-right
                corner of the given rg.Rectangle.
           -- Subsequent rg.Circles are drawn down and to the right,
                at a 45 degree angle, barely touching.
                ***  SEE THE PDF to make this clear. ***
        ** See  problem3_pictures.pdf  for examples. **

      Must render but   ** NOT close **   the window.

    Type hints:
      :type rect:    rg.Rectangle
      :type n:       int
      :type window:  rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function, TESTING each step as you go.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------

    rect.attach_to(window)
    window.render(.05)
    radius = (rect.get_height())/2
    circle = rg.Circle(rect.get_lower_right_corner(),radius)
    circle.attach_to(window)
    window.render()
    for k in range(n):
        center = rg.Point(circle.center.x + 1.5*radius, circle.center.y + 1.5*radius)
        circle = rg.Circle(center,radius)
        circle.attach_to(window)
    window.render(.05)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
