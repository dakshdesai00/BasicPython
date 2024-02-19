import pyglet
while True:
    animation = pyglet.image.load_animation('JARVISGIF.gif')
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

    pyglet.gl.glClearColor(r, g, b, alpha)
    label = pyglet.text.Label('Hello, world',
                                   font_name='Times New Roman',
                                   font_size=36,
                                   x=w// 2,
                                   y=h // 2,
                                   anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
        label.draw()

    pyglet.app.run()