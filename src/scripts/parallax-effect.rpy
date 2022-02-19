
# hippity hoppity
    # ur code
        # is now my property :P
# thanks to aquapaulo (github.com/aquapaulo)!

init python:
    class CursorTracker(renpy.Displayable):
        def __init__(self, child, paramod, **kwargs):
            super(CursorTracker, self).__init__()

            self.child = renpy.displayable(child)
            self.x, self.y, self.actual_x, self.actual_y = 0, 0, 0, 0

            self.paramod = paramod
            self.last_st = 0

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            min_speed = 0.5
            max_speed = 3
            speed = 1 + min_speed

            mouse_distance_x = min(max_speed, max(min_speed, (self.x - self.actual_x)))
            mouse_distance_y = (self.y - self.actual_y)

            if self.x is not None:
                st_change = st - self.last_st

                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )) * self.paramod)
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)) * self.paramod)

                if mouse_distance_y <= min_speed:
                    mouse_distance_y = min_speed
                elif mouse_distance_y >= max_speed:
                    mouse_distance_y = max_speed

                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.actual_x, self.actual_y))

            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            focus = pygame.mouse.get_focused()
            
            
            if hover:
                if (x != self.x) or (y != self.y) or click:
                    self.x = -x /self.paramod
                    self.y = -y /self.paramod