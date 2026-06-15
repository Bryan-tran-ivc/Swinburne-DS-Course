require 'gosu'

SCREEN_HEIGHT = 400
SCREEN_WIDTH  = 400

class GameWindow < Gosu::Window
  def initialize
    super(SCREEN_WIDTH, SCREEN_HEIGHT)
    self.caption = "Gosu Example"

    @done    = false
    @is_blue = true
    @x       = 30
    @y       = 30
    @size    = 60
  end

  def update
    close if @done

    @x -= 3 if button_down?(Gosu::KB_LEFT)
    @x += 3 if button_down?(Gosu::KB_RIGHT)
    @y -= 3 if button_down?(Gosu::KB_UP)
    @y += 3 if button_down?(Gosu::KB_DOWN)

    @size = [@size + 2, 120].min if button_down?(Gosu::KB_W)
    @size = [@size - 2,   0].max if button_down?(Gosu::KB_Q)

    @x = @x.clamp(0, SCREEN_WIDTH  - @size)
    @y = @y.clamp(0, SCREEN_HEIGHT - @size)
  end

  def draw
    Gosu.draw_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, Gosu::Color::BLACK)

    color = @is_blue ? Gosu::Color.rgb(0, 128, 255) : Gosu::Color.rgb(255, 100, 0)
    Gosu.draw_rect(@x, @y, @size, @size, color)
  end

  def button_down(id)
    @done = true if id == Gosu::KB_ESCAPE
    @is_blue = !@is_blue if id == Gosu::KB_SPACE
  end
end

GameWindow.new.show