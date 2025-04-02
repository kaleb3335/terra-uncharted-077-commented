@namespace
class SpriteKind:
    slope = SpriteKind.create()
def pick_song():
    global song
    song = 0

def on_overlap_tile(sprite, location):
    while player1.tilemap_location() == location:
        sprite.y += -0.01
    if sprite.is_hitting_tile(CollisionDirection.RIGHT) or sprite.is_hitting_tile(CollisionDirection.LEFT):
        sprite.y += -3
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile76
        """),
    on_overlap_tile)

def on_up_pressed():
    if world_gen_done == 1:
        if inmenu == 0:
            player1.ay = 500
            if player1.is_hitting_tile(CollisionDirection.BOTTOM):
                player1.vy = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global inmenu, myMenu
    if inmenu == 0:
        if inbuild == 1:
            inmenu = 1
            myMenu = miniMenu.create_menu(miniMenu.create_menu_item("dirt", assets.tile("""
                    myTile1
                    """)),
                miniMenu.create_menu_item("Craft Tb", assets.tile("""
                    myTile9
                    """)),
                miniMenu.create_menu_item("stone wall", assets.tile("""
                    myTile8
                    """)),
                miniMenu.create_menu_item("blk stone wall", assets.tile("""
                    myTile7
                    """)),
                miniMenu.create_menu_item("wood backing", assets.tile("""
                    myTile17
                    """)),
                miniMenu.create_menu_item("wood floor", assets.tile("""
                    myTile18
                    """)),
                miniMenu.create_menu_item("wood ceiling", assets.tile("""
                    myTile23
                    """)),
                miniMenu.create_menu_item("wood roof", assets.tile("""
                    myTile21
                    """)))
            myMenu.set_dimensions(120, 100)
            myMenu.set_title("Building")
            myMenu.set_menu_style_property(miniMenu.MenuStyleProperty.SCROLL_INDICATOR_COLOR, 3)
            myMenu.x = 60
            myMenu.y = 80
            myMenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
            
            def on_button_pressed(selection2, selectedIndex2):
                global inmenu
                if selectedIndex2 == 0:
                    if dirt >= 1:
                        
                        def on_after():
                            global buildM
                            buildM = 1
                        timer.after(500, on_after)
                        
                    else:
                        game.show_long_text("you do not have dirt ", DialogLayout.BOTTOM)
                elif selectedIndex2 == 1:
                    if wood >= 1:
                        
                        def on_after2():
                            global buildM
                            buildM = 2
                        timer.after(500, on_after2)
                        
                    else:
                        game.show_long_text("you do not have wood", DialogLayout.BOTTOM)
                elif selectedIndex2 == 2:
                    if stone_wall >= 1:
                        
                        def on_after3():
                            global buildM
                            buildM = 3
                        timer.after(500, on_after3)
                        
                    else:
                        game.show_long_text("you do not have stone wall", DialogLayout.BOTTOM)
                elif selectedIndex2 == 3:
                    if blk_stone_wall >= 1:
                        
                        def on_after4():
                            global buildM
                            buildM = 4
                        timer.after(500, on_after4)
                        
                    else:
                        game.show_long_text("you do not have blk stone wall", DialogLayout.BOTTOM)
                elif selectedIndex2 == 4:
                    if wdBacking >= 1:
                        
                        def on_after5():
                            global buildM
                            buildM = 5
                        timer.after(500, on_after5)
                        
                    else:
                        game.show_long_text("you do not have wood backing", DialogLayout.BOTTOM)
                elif selectedIndex2 == 5:
                    if wdfloor >= 1:
                        
                        def on_after6():
                            global buildM
                            buildM = 6
                        timer.after(500, on_after6)
                        
                    else:
                        game.show_long_text("you do not have wood floor", DialogLayout.BOTTOM)
                elif selectedIndex2 == 6:
                    if wdciling >= 1:
                        
                        def on_after7():
                            global buildM
                            buildM = 7
                        timer.after(500, on_after7)
                        
                    else:
                        game.show_long_text("you do not have wood ceiling", DialogLayout.BOTTOM)
                elif selectedIndex2 == 7:
                    if wood_roof >= 1:
                        
                        def on_after8():
                            global buildM
                            buildM = 7
                        timer.after(500, on_after8)
                        
                    else:
                        game.show_long_text("you do not have wood roof", DialogLayout.BOTTOM)
                sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                inmenu = 0
            myMenu.on_button_pressed(controller.A, on_button_pressed)
            
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile2(sprite2, location2):
    while player1.tilemap_location() == location2:
        sprite2.y += -0.01
    if sprite2.is_hitting_tile(CollisionDirection.RIGHT) or sprite2.is_hitting_tile(CollisionDirection.LEFT):
        sprite2.y += -3
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile75
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    while player1.tilemap_location() == location3:
        sprite3.y += -0.01
    if sprite3.is_hitting_tile(CollisionDirection.RIGHT) or sprite3.is_hitting_tile(CollisionDirection.LEFT):
        sprite3.y += -3
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile24
        """),
    on_overlap_tile3)

def make_trees(num: number):
    statusbar.value += load_p
    pause(100)
    for value8 in tiles.get_tiles_by_type(assets.tile("""
        myTile15
        """)):
        if tiles.tile_at_location_equals(value8.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(randint(45, 75)):
                tiles.set_tile_at(value8.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile10
                        """))
    for value9 in tiles.get_tiles_by_type(assets.tile("""
        myTile10
        """)):
        if tiles.tile_at_location_equals(value9.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value9.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile11
                    """))
    for index in range(2):
        for index2 in range(randint(1, 4)):
            for value10 in tiles.get_tiles_by_type(assets.tile("""
                myTile11
                """)):
                if tiles.tile_at_location_equals(value10.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value10.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile11
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value10.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile91
                                """))
    for value11 in tiles.get_tiles_by_type(assets.tile("""
        myTile11
        """)):
        if tiles.tile_at_location_equals(value11.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value11.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile12
                    """))
    for value112 in tiles.get_tiles_by_type(assets.tile("""
        myTile91
        """)):
        if tiles.tile_at_location_equals(value112.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value112.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile12
                    """))
    for value12 in tiles.get_tiles_by_type(assets.tile("""
        myTile12
        """)):
        if tiles.tile_at_location_equals(value12.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value12.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile20
                    """))
        if tiles.tile_at_location_equals(value12.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value12.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile49
                    """))
    for value82 in tiles.get_tiles_by_type(assets.tile("""
        myTile65
        """)):
        if tiles.tile_at_location_equals(value82.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(randint(50, 100)):
                tiles.set_tile_at(value82.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile70
                        """))
    for value83 in tiles.get_tiles_by_type(assets.tile("""
        myTile70
        """)):
        if tiles.tile_at_location_equals(value83.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value83.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile79
                    """))
    for index3 in range(2):
        for index4 in range(randint(1, 4)):
            for value102 in tiles.get_tiles_by_type(assets.tile("""
                myTile79
                """)):
                if tiles.tile_at_location_equals(value102.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value102.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile80
                                """))
            for value103 in tiles.get_tiles_by_type(assets.tile("""
                myTile80
                """)):
                if tiles.tile_at_location_equals(value103.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value103.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile79
                                """))
    for value113 in tiles.get_tiles_by_type(assets.tile("""
        myTile80
        """)):
        if tiles.tile_at_location_equals(value113.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value113.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile78
                    """))
    for value114 in tiles.get_tiles_by_type(assets.tile("""
        myTile80
        """)):
        if tiles.tile_at_location_equals(value114.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value114.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile77
                    """))
    for value115 in tiles.get_tiles_by_type(assets.tile("""
        myTile74
        """)):
        if tiles.tile_at_location_equals(value115.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value115.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile80
                    """))
    for value116 in tiles.get_tiles_by_type(assets.tile("""
        myTile79
        """)):
        if tiles.tile_at_location_equals(value116.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value116.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile80
                    """))
    for value117 in tiles.get_tiles_by_type(assets.tile("""
        myTile80
        """)):
        if tiles.tile_at_location_equals(value117.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value117.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile80
                    """))
    for value118 in tiles.get_tiles_by_type(assets.tile("""
        myTile80
        """)):
        if tiles.tile_at_location_equals(value118.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value118.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile81
                    """))
    for value119 in tiles.get_tiles_by_type(assets.tile("""
        myTile81
        """)):
        if tiles.tile_at_location_equals(value119.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value119.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile83
                    """))
    for value1110 in tiles.get_tiles_by_type(assets.tile("""
        myTile81
        """)):
        if tiles.tile_at_location_equals(value1110.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value1110.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile82
                    """))
    for value84 in tiles.get_tiles_by_type(assets.tile("""
        myTile60
        """)):
        if tiles.tile_at_location_equals(value84.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(randint(40, 75)):
                tiles.set_tile_at(value84.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile86
                        """))
    for value92 in tiles.get_tiles_by_type(assets.tile("""
        myTile86
        """)):
        if tiles.tile_at_location_equals(value92.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value92.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile87
                    """))
    for index5 in range(3):
        for index6 in range(randint(1, 4)):
            for value104 in tiles.get_tiles_by_type(assets.tile("""
                myTile87
                """)):
                if tiles.tile_at_location_equals(value104.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value104.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile87
                                """))
    for value1111 in tiles.get_tiles_by_type(assets.tile("""
        myTile87
        """)):
        if tiles.tile_at_location_equals(value1111.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value1111.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile95
                    """))
    for value122 in tiles.get_tiles_by_type(assets.tile("""
        myTile95
        """)):
        if tiles.tile_at_location_equals(value122.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value122.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile94
                    """))
        if tiles.tile_at_location_equals(value122.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value122.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile96
                    """))
    for value85 in tiles.get_tiles_by_type(assets.tile("""
        myTile65
        """)):
        if tiles.tile_at_location_equals(value85.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(randint(45, 80)):
                tiles.set_tile_at(value85.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile67
                        """))
    for index7 in range(3):
        for index8 in range(randint(1, 4)):
            for value105 in tiles.get_tiles_by_type(assets.tile("""
                myTile67
                """)):
                if tiles.tile_at_location_equals(value105.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value105.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile69
                                """))
            for value106 in tiles.get_tiles_by_type(assets.tile("""
                myTile69
                """)):
                if tiles.tile_at_location_equals(value106.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value106.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile67
                                """))
    for value1112 in tiles.get_tiles_by_type(assets.tile("""
        myTile67
        """)):
        if tiles.tile_at_location_equals(value1112.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value1112.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile68
                    """))
    for value1113 in tiles.get_tiles_by_type(assets.tile("""
        myTile69
        """)):
        if tiles.tile_at_location_equals(value1113.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value1113.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile68
                    """))
def makeplayer():
    global player1, select, player_health, world, world_gen_done
    player1 = sprites.create(img("""
            . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
            """),
        SpriteKind.player)
    select = sprites.create(img("""
            5 5 5 5 . . . . . . . . 5 5 5 5
            5 5 . . . . . . . . . . . . 5 5
            5 . . . . . . . . . . . . . . 5
            5 . . . . . . . . . . . . . . 5
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            5 . . . . . . . . . . . . . . 5
            5 . . . . . . . . . . . . . . 5
            5 5 . . . . . . . . . . . . 5 5
            5 5 5 5 . . . . . . . . 5 5 5 5
            """),
        SpriteKind.player)
    tiles.place_on_random_tile(player1, assets.tile("""
        myTile28
        """))
    player1.set_flag(SpriteFlag.SHOW_PHYSICS, True)
    player1.ay = 500
    sprites.destroy(statusbar)
    player_health = statusbars.create(60, 5, StatusBarKind.health)
    player_health.set_position(20, 3)
    scene.camera_follow_sprite(player1)
    stats.turn_stats(True)
    world = 0
    if secworld == 1:
        tiles.set_current_tilemap(tilemaps[world])
    else:
        tiles.set_current_tilemap(tilemap_1)
    world_gen_done = 1
def make_underworld():
    global col
    statusbar.value += load_p
    col = 16
    pause(100)
    for index9 in range(16):
        tiles.set_tile_at(tiles.get_tile_location(col, 245),
            assets.tile("""
                myTile3
                """))
        col += 16
    for index10 in range(16):
        for value53 in tiles.get_tiles_by_type(assets.tile("""
            myTile3
            """)):
            tiles.set_tile_at(value53.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile3
                    """))
            tiles.set_tile_at(value53.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile3
                    """))
            if Math.percent_chance(randint(50, 80)):
                tiles.set_tile_at(value53.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile3
                        """))
    for index11 in range(10):
        for value62 in tiles.get_tiles_by_type(assets.tile("""
            myTile3
            """)):
            if tiles.tile_at_location_equals(value62.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value62.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile3
                        """))
    for value63 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
        """)):
        if tiles.tile_at_location_equals(value63.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value63.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile6
                    """))
    for value1132 in tiles.get_tiles_by_type(assets.tile("""
        myTile6
        """)):
        if tiles.tile_at_location_equals(value1132.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile3
                """)):
            if Math.percent_chance(10):
                tiles.set_tile_at(value1132.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """))
    for index12 in range(25):
        for value132 in tiles.get_tiles_by_type(assets.tile("""
            transparency16
            """)):
            if Math.percent_chance(randint(0, 80)):
                if tiles.tile_at_location_equals(value132.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile3
                        """)):
                    tiles.set_tile_at(value132.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            transparency16
                            """))
            elif Math.percent_chance(randint(0, 80)):
                if tiles.tile_at_location_equals(value132.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile3
                        """)) or tiles.tile_at_location_equals(value132.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile6
                        """)):
                    tiles.set_tile_at(value132.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            transparency16
                            """))
            elif Math.percent_chance(randint(0, 30)):
                if tiles.tile_at_location_equals(value132.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        myTile3
                        """)):
                    tiles.set_tile_at(value132.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            transparency16
                            """))
            elif Math.percent_chance(randint(0, 30)):
                if tiles.tile_at_location_equals(value132.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        myTile3
                        """)):
                    tiles.set_tile_at(value132.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            transparency16
                            """))
    col = 0
    for index13 in range(255):
        if tiles.tile_at_location_equals(tiles.get_tile_location(col, 240),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(tiles.get_tile_location(col, 240),
                assets.tile("""
                    myTile50
                    """))
        col += 1
    for value632 in tiles.get_tiles_by_type(assets.tile("""
        myTile50
        """)):
        tiles.set_tile_at(value632.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile44
                """))
    for index14 in range(15):
        for value6322 in tiles.get_tiles_by_type(assets.tile("""
            myTile44
            """)):
            if tiles.tile_at_location_equals(value6322.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value6322.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile44
                        """))
            if tiles.tile_at_location_equals(value6322.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value6322.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        myTile44
                        """))
            if tiles.tile_at_location_equals(value6322.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value6322.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        myTile44
                        """))
    for value633 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
        """)):
        if tiles.tile_at_location_equals(value633.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)) and tiles.tile_at_location_equals(value633.get_neighboring_location(CollisionDirection.TOP).get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value633.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile6
                    """))
    for value6323 in tiles.get_tiles_by_type(assets.tile("""
        myTile6
        """)):
        if Math.percent_chance(10):
            tiles.set_tile_at(value6323.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile42
                    """))
        elif Math.percent_chance(10):
            tiles.set_tile_at(value6323.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile39
                    """))
        elif Math.percent_chance(10):
            tiles.set_tile_at(value6323.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile52
                    """))
        elif Math.percent_chance(10):
            tiles.set_tile_at(value6323.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile33
                    """))
    for value822 in tiles.get_tiles_by_type(assets.tile("""
        myTile6
        """)):
        if tiles.tile_at_location_equals(value822.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(randint(35, 75)):
                tiles.set_tile_at(value822.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile43
                        """))
    for value922 in tiles.get_tiles_by_type(assets.tile("""
        myTile43
        """)):
        if tiles.tile_at_location_equals(value922.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value922.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile41
                    """))
    for index15 in range(2):
        for index16 in range(randint(1, 4)):
            for value1022 in tiles.get_tiles_by_type(assets.tile("""
                myTile41
                """)):
                if tiles.tile_at_location_equals(value1022.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value1022.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile45
                                """))
            for value1032 in tiles.get_tiles_by_type(assets.tile("""
                myTile45
                """)):
                if tiles.tile_at_location_equals(value1032.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value1032.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile41
                                """))
    for value1122 in tiles.get_tiles_by_type(assets.tile("""
        myTile41
        """)):
        if tiles.tile_at_location_equals(value1122.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value1122.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile47
                    """))
    for value1133 in tiles.get_tiles_by_type(assets.tile("""
        myTile45
        """)):
        if tiles.tile_at_location_equals(value1133.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value1133.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile47
                    """))
def world_gen():
    draw_map()
    pause(100)
    make_stone()
    make_dirt()
    make_caves()
    make_trees(1)
    make_underworld()
    make_sticks()
    wg_done()
    print("new world")
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile13
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile14
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile16
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile34
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile35
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile36
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile37
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile38
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile15
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile1
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile28
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile26
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile19
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile10
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile11
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile46
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile49
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile60
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile61
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile62
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile63
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile64
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile65
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile66
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile67
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile68
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile69
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile71
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile12
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile20
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile39
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile40
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile41
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile42
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile44
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile45
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile47
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile50
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile52
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile53
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile55
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile56
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile57
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile6
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile3
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile2
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile70
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile71
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile74
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile75
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile76
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile77
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile78
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile79
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile80
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile81
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile82
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile83
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile84
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile86
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile87
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile94
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile95
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile96
        """))))
    print(len(tiles.get_tiles_by_type(assets.tile("""
        myTile96
        """))))
def wg_done():
    tileUtil.set_walls(assets.tile("""
        myTile14
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile16
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile3
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile55
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile6
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile56
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile57
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile53
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile13
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile1
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile15
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile60
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile61
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile65
        """), True)
    tileUtil.set_walls(assets.tile("""
        myTile64
        """), True)
def make_caves():
    statusbar.value += load_p
    pause(100)
    for index17 in range(40):
        for index18 in range(randint(0, 4)):
            tiles.set_tile_at(tiles.get_tile_location(randint(0, 255), randint(100, 160)),
                assets.tile("""
                    myTile34
                    """))
            for value13 in tiles.get_tiles_by_type(assets.tile("""
                myTile34
                """)):
                if Math.percent_chance(randint(0, 80)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.LEFT),
                            assets.tile("""
                                myTile34
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.LEFT),
                            assets.tile("""
                                myTile38
                                """))
                elif Math.percent_chance(randint(0, 10)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile34
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile38
                                """))
                elif Math.percent_chance(randint(0, 80)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.RIGHT),
                            assets.tile("""
                                myTile34
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.RIGHT),
                            assets.tile("""
                                myTile38
                                """))
                elif Math.percent_chance(randint(0, 10)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile34
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value13.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile38
                                """))
            tiles.set_tile_at(tiles.get_tile_location(randint(0, 255), randint(70, 120)),
                assets.tile("""
                    myTile35
                    """))
            for value1322 in tiles.get_tiles_by_type(assets.tile("""
                myTile35
                """)):
                if Math.percent_chance(randint(0, 80)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.LEFT),
                            assets.tile("""
                                myTile35
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.LEFT),
                            assets.tile("""
                                myTile36
                                """))
                elif Math.percent_chance(randint(0, 10)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile35
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile36
                                """))
                elif Math.percent_chance(randint(0, 80)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.RIGHT),
                            assets.tile("""
                                myTile35
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.RIGHT),
                            assets.tile("""
                                myTile36
                                """))
                elif Math.percent_chance(randint(0, 10)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile35
                                """))
                    elif Math.percent_chance(50):
                        tiles.set_tile_at(value1322.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile36
                                """))
        tiles.set_tile_at(tiles.get_tile_location(randint(0, 255), randint(188, 220)),
            assets.tile("""
                myTile54
                """))
        for value1323 in tiles.get_tiles_by_type(assets.tile("""
            myTile54
            """)):
            if Math.percent_chance(randint(0, 80)):
                if Math.percent_chance(50):
                    tiles.set_tile_at(value1323.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile54
                            """))
            elif Math.percent_chance(randint(0, 10)):
                if Math.percent_chance(50):
                    tiles.set_tile_at(value1323.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile54
                            """))
            elif Math.percent_chance(randint(0, 80)):
                if Math.percent_chance(50):
                    tiles.set_tile_at(value1323.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile54
                            """))
            elif Math.percent_chance(randint(0, 10)):
                if Math.percent_chance(50):
                    tiles.set_tile_at(value1323.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile54
                            """))
    for value1324 in tiles.get_tiles_by_type(assets.tile("""
        myTile54
        """)):
        if tiles.tile_at_location_equals(value1324.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                myTile16
                """)):
            tiles.set_tile_at(value1324.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile56
                    """))
        if tiles.tile_at_location_equals(value1324.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                myTile16
                """)):
            tiles.set_tile_at(value1324.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile57
                    """))
        if tiles.tile_at_location_equals(value1324.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                myTile16
                """)):
            tiles.set_tile_at(value1324.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile55
                    """))
        if tiles.tile_at_location_equals(value1324.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile16
                """)):
            tiles.set_tile_at(value1324.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile53
                    """))
def make_sticks():
    statusbar.value += load_p
    pause(100)
    for value8222 in tiles.get_tiles_by_type(assets.tile("""
        myTile15
        """)):
        if tiles.tile_at_location_equals(value8222.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(20):
                tiles.set_tile_at(value8222.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile19
                        """))

def on_menu_pressed():
    global inmenu, gamemenu
    if inmenu == 0:
        inmenu = 1
        gamemenu = miniMenu.create_menu(miniMenu.create_menu_item("mining  mode"),
            miniMenu.create_menu_item("building mode"),
            miniMenu.create_menu_item("invantory"),
            miniMenu.create_menu_item("Settings"))
        gamemenu.x = 50
        gamemenu.y = 30
        gamemenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
        
        def on_button_pressed2(selection3, selectedIndex3):
            global inbuild, inmenu, myMenu
            if selectedIndex3 == 0:
                inbuild = 0
                inmenu = 0
                sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
            elif selectedIndex3 == 1:
                inbuild = 1
                inmenu = 0
                sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
            elif selectedIndex3 == 2:
                inmenu = 0
                if inmenu == 0:
                    inmenu = 1
                    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                    myMenu = miniMenu.create_menu(miniMenu.create_menu_item("dirt= " + ("" + str(dirt))),
                        miniMenu.create_menu_item("stone= " + ("" + str(stone))),
                        miniMenu.create_menu_item("blk stone= " + ("" + str(blk_stone))),
                        miniMenu.create_menu_item("sticks= " + ("" + str(sticks))),
                        miniMenu.create_menu_item("wood= " + ("" + str(wood))),
                        miniMenu.create_menu_item("treeseeds " + ("" + str(treeseed))))
                    myMenu.set_dimensions(100, 80)
                    myMenu.x = 60
                    myMenu.y = 40
                    myMenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
                    
                    def on_button_pressed3(selection4, selectedIndex4):
                        global inmenu
                        sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                        inmenu = 0
                    myMenu.on_button_pressed(controller.A, on_button_pressed3)
                    
            elif selectedIndex3 == 3:
                inmenu = 0
                if inmenu == 0:
                    inmenu = 1
                    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                    myMenu = miniMenu.create_menu(miniMenu.create_menu_item("Lighting system"))
                    myMenu.set_dimensions(100, 80)
                    myMenu.x = 60
                    myMenu.y = 40
                    myMenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
                    
                    def on_button_pressed4(selection42, selectedIndex42):
                        global myMenu
                        if selectedIndex42 == 0:
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            myMenu = miniMenu.create_menu(miniMenu.create_menu_item("turn on"),
                                miniMenu.create_menu_item("Turn off"))
                            myMenu.x = 60
                            myMenu.y = 40
                            myMenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
                            
                            def on_button_pressed5(selection43, selectedIndex43):
                                global inmenu, lighting
                                if selectedIndex43 == 0:
                                    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                                    inmenu = 0
                                    lighting = 1
                                elif selectedIndex43 == 1:
                                    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                                    inmenu = 0
                                    lighting = 0
                            myMenu.on_button_pressed(controller.A, on_button_pressed5)
                            
                        else:
                            pass
                    myMenu.on_button_pressed(controller.A, on_button_pressed4)
                    
        gamemenu.on_button_pressed(controller.A, on_button_pressed2)
        
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def draw_map():
    global myMinimap, mySprite
    myMinimap = minimap.minimap(MinimapScale.SIXTEENTH, 2, 0)
    mySprite = sprites.create(minimap.get_image(myMinimap), SpriteKind.player)
    mySprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    mySprite.set_position(0, 0)

def on_overlap_tile4(sprite22, location22):
    while player1.tilemap_location() == location22:
        sprite22.y += -0.01
    if sprite22.is_hitting_tile(CollisionDirection.RIGHT) or sprite22.is_hitting_tile(CollisionDirection.LEFT):
        sprite22.y += -3
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile25
        """),
    on_overlap_tile4)

def on_overlap_tile5(sprite4, location4):
    while player1.tilemap_location() == location4:
        sprite4.y += -0.01
    if sprite4.is_hitting_tile(CollisionDirection.RIGHT) or sprite4.is_hitting_tile(CollisionDirection.LEFT):
        sprite4.y += -3
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile62
        """),
    on_overlap_tile5)

def make_stone():
    global col, row
    statusbar.value += load_p
    pause(100)
    for index19 in range(16):
        tiles.set_tile_at(tiles.get_tile_location(col, 144),
            assets.tile("""
                myTile14
                """))
        tiles.set_tile_at(tiles.get_tile_location(col, row),
            assets.tile("""
                myTile14
                """))
        col += 16
    for index20 in range(16):
        for value3 in tiles.get_tiles_by_type(assets.tile("""
            myTile14
            """)):
            tiles.set_tile_at(value3.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile14
                    """))
            tiles.set_tile_at(value3.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile14
                    """))
            tiles.set_tile_at(value3.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile14
                    """))
            if Math.percent_chance(50):
                tiles.set_tile_at(value3.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile14
                        """))
    for index21 in range(16):
        for value4 in tiles.get_tiles_by_type(assets.tile("""
            myTile14
            """)):
            tiles.set_tile_at(value4.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile14
                    """))
    col = 16
    row = 80
    for index22 in range(16):
        tiles.set_tile_at(tiles.get_tile_location(col, 96),
            assets.tile("""
                myTile13
                """))
        tiles.set_tile_at(tiles.get_tile_location(col, row),
            assets.tile("""
                myTile13
                """))
        col += 16
    for index23 in range(16):
        for value in tiles.get_tiles_by_type(assets.tile("""
            myTile13
            """)):
            tiles.set_tile_at(value.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile13
                    """))
            tiles.set_tile_at(value.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile13
                    """))
            if Math.percent_chance(50):
                tiles.set_tile_at(value.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile13
                        """))
                tiles.set_tile_at(value.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile13
                        """))
    for index24 in range(16):
        for value2 in tiles.get_tiles_by_type(assets.tile("""
            myTile13
            """)):
            tiles.set_tile_at(value2.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile13
                    """))
    for index25 in range(16):
        for value22 in tiles.get_tiles_by_type(assets.tile("""
            myTile13
            """)):
            if tiles.tile_at_location_equals(value22.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile35
                    """)):
                if Math.percent_chance(50):
                    tiles.set_tile_at(value22.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile37
                            """))
    col = 16
    row = 204
    for index26 in range(16):
        tiles.set_tile_at(tiles.get_tile_location(col, 172),
            assets.tile("""
                myTile16
                """))
        tiles.set_tile_at(tiles.get_tile_location(col, row),
            assets.tile("""
                myTile16
                """))
        col += 16
    for index27 in range(16):
        for value5 in tiles.get_tiles_by_type(assets.tile("""
            myTile16
            """)):
            tiles.set_tile_at(value5.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile16
                    """))
            tiles.set_tile_at(value5.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile16
                    """))
            if Math.percent_chance(50):
                tiles.set_tile_at(value5.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile16
                        """))
                tiles.set_tile_at(value5.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile16
                        """))
    for index28 in range(16):
        for value222 in tiles.get_tiles_by_type(assets.tile("""
            myTile16
            """)):
            if tiles.tile_at_location_equals(value222.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    transparency16
                    """)):
                if Math.percent_chance(50):
                    tiles.set_tile_at(value222.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile16
                            """))
    for value2222 in tiles.get_tiles_by_type(assets.tile("""
        myTile16
        """)):
        if tiles.tile_at_location_equals(value2222.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(65):
                tiles.set_tile_at(value2222.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile55
                        """))

def on_overlap_tile6(sprite23, location23):
    while player1.tilemap_location() == location23:
        sprite23.y += -0.01
    if sprite23.is_hitting_tile(CollisionDirection.RIGHT) or sprite23.is_hitting_tile(CollisionDirection.LEFT):
        sprite23.y += -3
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile63
        """),
    on_overlap_tile6)

def on_overlap_tile7(sprite5, location5):
    if location5.column == 0 and (characterAnimations.matches_rule(player1, characterAnimations.rule(Predicate.MOVING_LEFT)) and secworld == 1):
        
        def on_throttle():
            global world
            if world >= len(tilemaps) - 1:
                world = 0
            else:
                world += 1
            tiles.set_current_tilemap(tilemaps[world])
            tiles.place_on_tile(player1,
                tiles.get_tile_location(254, player1.tilemap_location().row))
            tileUtil.set_tile_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(254, player1.tilemap_location().row),
                assets.tile("""
                    transparency16
                    """))
            tileUtil.set_tile_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(254, player1.tilemap_location().row + 1),
                assets.tile("""
                    transparency16
                    """))
            tileUtil.set_wall_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(254, player1.tilemap_location().row),
                False)
            tileUtil.set_wall_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(254, player1.tilemap_location().row + 1),
                False)
        timer.throttle("action", 500, on_throttle)
        
    elif location5.column == 254 and (characterAnimations.matches_rule(player1, characterAnimations.rule(Predicate.MOVING_RIGHT)) and secworld == 1):
        
        def on_throttle2():
            global world
            if world <= 0:
                world = len(tilemaps) - 1
            else:
                world += -1
            tiles.set_current_tilemap(tilemaps[world])
            tiles.place_on_tile(player1,
                tiles.get_tile_location(0, player1.tilemap_location().row))
            tileUtil.set_tile_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(0, player1.tilemap_location().row),
                assets.tile("""
                    transparency16
                    """))
            tileUtil.set_tile_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(0, player1.tilemap_location().row + 1),
                assets.tile("""
                    transparency16
                    """))
            tileUtil.set_wall_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(0, player1.tilemap_location().row),
                False)
            tileUtil.set_wall_at(tileUtil.current_tilemap(),
                tiles.get_tile_location(0, player1.tilemap_location().row + 1),
                False)
        timer.throttle("action", 500, on_throttle2)
        
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        transparency16
        """),
    on_overlap_tile7)

def make_dirt():
    global col, biomes
    statusbar.value += load_p
    pause(100)
    col = 16
    if Math.percent_chance(25):
        for index29 in range(6):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile61
                    """))
            col += 16
        for index30 in range(6):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile1
                    """))
            col += 16
        for index31 in range(6):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile64
                    """))
            col += 16
        biomes = 3
    elif Math.percent_chance(25):
        for index32 in range(8):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile61
                    """))
            col += 16
        for index33 in range(8):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile1
                    """))
            col += 16
        biomes = 1
    elif Math.percent_chance(25):
        for index34 in range(8):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile1
                    """))
            col += 16
        for index35 in range(8):
            col += 16
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile61
                    """))
        biomes = 1
    elif Math.percent_chance(25):
        for index36 in range(6):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile1
                    """))
            col += 16
        for index37 in range(6):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile64
                    """))
            col += 16
        for index38 in range(6):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile61
                    """))
            col += 16
        biomes = 3
    else:
        for index39 in range(16):
            tiles.set_tile_at(tiles.get_tile_location(col, 64),
                assets.tile("""
                    myTile64
                    """))
            col += 16
        biomes = 3
    for index40 in range(16):
        if biomes == 1:
            for value52 in tiles.get_tiles_by_type(assets.tile("""
                myTile1
                """)):
                if tiles.tile_at_location_equals(value52.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value52.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile1
                            """))
                if tiles.tile_at_location_equals(value52.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value52.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile1
                            """))
                if Math.percent_chance(randint(15, 25)):
                    if tiles.tile_at_location_equals(value52.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            transparency16
                            """)):
                        tiles.set_tile_at(value52.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile1
                                """))
            for value522 in tiles.get_tiles_by_type(assets.tile("""
                myTile61
                """)):
                if tiles.tile_at_location_equals(value522.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value522.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile61
                            """))
                if tiles.tile_at_location_equals(value522.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value522.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile61
                            """))
                if Math.percent_chance(randint(50, 60)):
                    if tiles.tile_at_location_equals(value522.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            transparency16
                            """)):
                        tiles.set_tile_at(value522.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile61
                                """))
        if biomes == 3:
            for value523 in tiles.get_tiles_by_type(assets.tile("""
                myTile64
                """)):
                if tiles.tile_at_location_equals(value523.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value523.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile64
                            """))
                if tiles.tile_at_location_equals(value523.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value523.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile64
                            """))
                if Math.percent_chance(randint(60, 80)):
                    if tiles.tile_at_location_equals(value523.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            transparency16
                            """)):
                        tiles.set_tile_at(value523.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile64
                                """))
            for value524 in tiles.get_tiles_by_type(assets.tile("""
                myTile1
                """)):
                if tiles.tile_at_location_equals(value524.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value524.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile1
                            """))
                if tiles.tile_at_location_equals(value524.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value524.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile1
                            """))
                if Math.percent_chance(randint(15, 25)):
                    if tiles.tile_at_location_equals(value524.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            transparency16
                            """)):
                        tiles.set_tile_at(value524.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile1
                                """))
            for value525 in tiles.get_tiles_by_type(assets.tile("""
                myTile61
                """)):
                if tiles.tile_at_location_equals(value525.get_neighboring_location(CollisionDirection.LEFT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value525.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile61
                            """))
                if tiles.tile_at_location_equals(value525.get_neighboring_location(CollisionDirection.RIGHT),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value525.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile61
                            """))
                if Math.percent_chance(randint(50, 60)):
                    if tiles.tile_at_location_equals(value525.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            transparency16
                            """)):
                        tiles.set_tile_at(value525.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                myTile61
                                """))
    for index41 in range(16):
        for value6 in tiles.get_tiles_by_type(assets.tile("""
            myTile1
            """)):
            if tiles.tile_at_location_equals(value6.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value6.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile1
                        """))
        if biomes >= 1:
            for value64 in tiles.get_tiles_by_type(assets.tile("""
                myTile61
                """)):
                if tiles.tile_at_location_equals(value64.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value64.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile61
                            """))
        if biomes >= 3:
            for value65 in tiles.get_tiles_by_type(assets.tile("""
                myTile64
                """)):
                if tiles.tile_at_location_equals(value65.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value65.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile64
                            """))
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        myTile1
        """)):
        if tiles.tile_at_location_equals(value7.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value7.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile15
                    """))
    if biomes >= 1:
        for value72 in tiles.get_tiles_by_type(assets.tile("""
            myTile61
            """)):
            if tiles.tile_at_location_equals(value72.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value72.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile60
                        """))
    if biomes >= 3:
        for value73 in tiles.get_tiles_by_type(assets.tile("""
            myTile64
            """)):
            if tiles.tile_at_location_equals(value73.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value73.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile65
                        """))
        for value1134 in tiles.get_tiles_by_type(assets.tile("""
            myTile65
            """)):
            if tiles.tile_at_location_equals(value1134.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile64
                    """)):
                if Math.percent_chance(15):
                    tiles.set_tile_at(value1134.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            transparency16
                            """))
        for index42 in range(25):
            for value1325 in tiles.get_tiles_by_type(assets.tile("""
                transparency16
                """)):
                if Math.percent_chance(randint(0, 30)):
                    if tiles.tile_at_location_equals(value1325.get_neighboring_location(CollisionDirection.LEFT),
                        assets.tile("""
                            myTile64
                            """)):
                        tiles.set_tile_at(value1325.get_neighboring_location(CollisionDirection.LEFT),
                            assets.tile("""
                                transparency16
                                """))
                elif Math.percent_chance(randint(0, 50)):
                    if tiles.tile_at_location_equals(value1325.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile64
                            """)) or tiles.tile_at_location_equals(value1325.get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile65
                            """)):
                        tiles.set_tile_at(value1325.get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                transparency16
                                """))
                elif Math.percent_chance(randint(0, 30)):
                    if tiles.tile_at_location_equals(value1325.get_neighboring_location(CollisionDirection.RIGHT),
                        assets.tile("""
                            myTile64
                            """)):
                        tiles.set_tile_at(value1325.get_neighboring_location(CollisionDirection.RIGHT),
                            assets.tile("""
                                transparency16
                                """))
                elif Math.percent_chance(randint(0, 50)):
                    if tiles.tile_at_location_equals(value1325.get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile64
                            """)):
                        tiles.set_tile_at(value1325.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                transparency16
                                """))
        for value74 in tiles.get_tiles_by_type(assets.tile("""
            myTile64
            """)):
            if tiles.tile_at_location_equals(value74.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    transparency16
                    """)):
                tiles.set_tile_at(value74.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile65
                        """))
        for value75 in tiles.get_tiles_by_type(assets.tile("""
            myTile64
            """)):
            if tiles.tile_at_location_equals(value75.get_neighboring_location(CollisionDirection.TOP),
                assets.tile("""
                    myTile65
                    """)):
                tiles.set_tile_at(value75.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile64
                        """))
    for value722 in tiles.get_tiles_by_type(assets.tile("""
        myTile15
        """)):
        if tiles.tile_at_location_equals(value722.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value722.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile24
                    """))
        if tiles.tile_at_location_equals(value722.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value722.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile25
                    """))
    for value723 in tiles.get_tiles_by_type(assets.tile("""
        myTile60
        """)):
        if tiles.tile_at_location_equals(value723.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value723.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile62
                    """))
        if tiles.tile_at_location_equals(value723.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)):
            tiles.set_tile_at(value723.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile63
                    """))
    for value724 in tiles.get_tiles_by_type(assets.tile("""
        myTile65
        """)):
        if tiles.tile_at_location_equals(value724.get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                transparency16
                """)) and tiles.tile_at_location_equals(value724.get_neighboring_location(CollisionDirection.BOTTOM).get_neighboring_location(CollisionDirection.LEFT),
            assets.tile("""
                myTile65
                """)):
            tiles.set_tile_at(value724.get_neighboring_location(CollisionDirection.LEFT),
                assets.tile("""
                    myTile76
                    """))
        if tiles.tile_at_location_equals(value724.get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                transparency16
                """)) and tiles.tile_at_location_equals(value724.get_neighboring_location(CollisionDirection.BOTTOM).get_neighboring_location(CollisionDirection.RIGHT),
            assets.tile("""
                myTile65
                """)):
            tiles.set_tile_at(value724.get_neighboring_location(CollisionDirection.RIGHT),
                assets.tile("""
                    myTile75
                    """))
    for value742 in tiles.get_tiles_by_type(assets.tile("""
        myTile75
        """)):
        if tiles.tile_at_location_equals(value742.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile65
                """)):
            tiles.set_tile_at(value742.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile64
                    """))
    for value743 in tiles.get_tiles_by_type(assets.tile("""
        myTile76
        """)):
        if tiles.tile_at_location_equals(value743.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile65
                """)):
            tiles.set_tile_at(value743.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile64
                    """))
    for value744 in tiles.get_tiles_by_type(assets.tile("""
        myTile63
        """)):
        if tiles.tile_at_location_equals(value744.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile60
                """)):
            tiles.set_tile_at(value744.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile61
                    """))
    for value745 in tiles.get_tiles_by_type(assets.tile("""
        myTile62
        """)):
        if tiles.tile_at_location_equals(value745.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile60
                """)):
            tiles.set_tile_at(value745.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile61
                    """))
    for value732 in tiles.get_tiles_by_type(assets.tile("""
        myTile24
        """)):
        if tiles.tile_at_location_equals(value732.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile15
                """)):
            tiles.set_tile_at(value732.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile1
                    """))
    for value746 in tiles.get_tiles_by_type(assets.tile("""
        myTile25
        """)):
        if tiles.tile_at_location_equals(value746.get_neighboring_location(CollisionDirection.BOTTOM),
            assets.tile("""
                myTile15
                """)):
            tiles.set_tile_at(value746.get_neighboring_location(CollisionDirection.BOTTOM),
                assets.tile("""
                    myTile1
                    """))
    for value832 in tiles.get_tiles_by_type(assets.tile("""
        myTile15
        """)):
        if tiles.tile_at_location_equals(value832.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(25):
                tiles.set_tile_at(value832.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile26
                        """))
            elif Math.percent_chance(25):
                tiles.set_tile_at(value832.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile28
                        """))
            elif Math.percent_chance(25):
                tiles.set_tile_at(value832.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile46
                        """))
    for value833 in tiles.get_tiles_by_type(assets.tile("""
        myTile65
        """)):
        if tiles.tile_at_location_equals(value833.get_neighboring_location(CollisionDirection.TOP),
            assets.tile("""
                transparency16
                """)):
            if Math.percent_chance(25):
                tiles.set_tile_at(value833.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile2
                        """))
            elif Math.percent_chance(25):
                tiles.set_tile_at(value833.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile66
                        """))
            elif Math.percent_chance(25):
                tiles.set_tile_at(value833.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile71
                        """))
            elif Math.percent_chance(25):
                tiles.set_tile_at(value833.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile46
                        """))
            elif Math.percent_chance(25):
                tiles.set_tile_at(value833.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        myTile84
                        """))
nextspot: tiles.Location = None
biomes = 0
mySprite: Sprite = None
myMinimap: minimap.Minimap = None
lighting = 0
treeseed = 0
sticks = 0
blk_stone = 0
stone = 0
gamemenu: miniMenu.MenuSprite = None
player_health: StatusBarSprite = None
select: Sprite = None
wood_roof = 0
wdciling = 0
wdfloor = 0
wdBacking = 0
blk_stone_wall = 0
stone_wall = 0
wood = 0
buildM = 0
dirt = 0
myMenu: miniMenu.MenuSprite = None
inbuild = 0
inmenu = 0
world_gen_done = 0
player1: Sprite = None
song = 0
secnum = 0
tilemaps: List[tiles.TileMapData] = []
world = 0
secworld = 0
row = 0
load_p = 0
col = 0
tilemap_1: tiles.TileMapData = None
statusbar: StatusBarSprite = None
myMenu2 = miniMenu.create_menu(miniMenu.create_menu_item("Normal "),
    miniMenu.create_menu_item("sectional"))
myMenu2.x = 160
myMenu2.y = 120
myMenu2.set_style_property(miniMenu.StyleKind.DEFAULT, miniMenu.StyleProperty.MARGIN, 4)
scene.set_background_image(img("""
    fff3ffcfffffffffffffffffffffcf3cf3e3e3f3ffcfffffffcfffffffffffffcfffcfc3fc3cfc3cfffcffcfffcfffc3cc3cf3e3e3ec3fec3fffffffffc3cfe3ee3e7e7e7c6b6b6b6b69b9b6b6b9b6b6b6b6b6b6b99b9b9b99b6b69b69b9b9bb6e3fcffcf3c6cfffff3c3cf3cffc3fffffffffffcfffffffffffffc3fffcffcfff3fcff3cffcffcff8fffcfcfcfffcf3fcfcffffffffffffffcfffffffffffcf
    f3cff3f3ffffcffffcffcffcfcf3cffe3e3efe3efff3ffc3cff3fcf3fcffcfc3fcf3ffcc3cc3c3ef3cf3fcffcffef3fc3fcfc3cfec3fc3c3fcf3fcf3f3fef3e37e7c6bc7cb6b6b69a9a69a69b9b96b69a969a6b69a99b99b9b969a69a69a9b96f3fff3ff3fc7c3cf3cfe7c3cf3cffefffffcfffffffffffffffff3ec3fcf3ff3cff3e3fff3f3fc3cffcf8f3c3c3f7fcfcf3fcfcffcf8fcf8fffcffcfffcfffc3
    fffcfcfcffffff8ffff8ff8ff3fe3ef3e3e3e3ecfccfcffffcefffffff3fcffcf8fcf3ffcfcfcc3cffcfffcffc3cffccef3fcff3c3ee7ee7fcfcffffcff3cc347ec7b67c6b6b69a66b9b69a6a669a6a66a6b698b69a9b9a9b69a69a69a69b9bbcfcffcfcf3c3fffffc3c3ef3effe3cfffcf3fcfff3fffffffffcff3ecfcffc3fc3cf3cf3cfcfcfc38fff3cc3cffcc3ff3ccf3ffcffffffffcfff8fffcfffcfff
    cf3f3f3fffcfffffcffffffcfcf3e3ffc3e3eff3e3fffcfef3ffcffcffcfc3f83fffcfcf3f3f3fffc3fcfcfcfffef3cf3cfcf3ee3e3cf3bbe3cfff3ff3fff3e3e37c6b6b6b66a6a6a969bb696b9a696a69a69a69a69b9b969a9a6b69a69a6b63f3fcf3f3fe3fff3cf3e3c3eefc3e3fcffffcffcffffffffff3ffffcf3e3cffcffcfcf3fcff3f8fccf3fccfc3fcf3fc3ccf3fcfcffcffcf8ff3cfffcff3ffffcf
    ffccfecff3c3cfcff8f3fcf3ff3ffe3fe3ec3fcfcffcf3ef3ebfffff3ffc8fcfcfcf38f3fcfcfcfcfcffcfffcfc3cfe3ffc3cc3eee3c3c3c3cf3ffcffefe3ec3eec7b6b6b6bb6a66b69b69a6a6a6b6a6b66a6b6a6b6b669a69a696a66b696b6cfffffeffc3ecffcf3e3fcc3f3fcfe3e3cfffffffffffcff3ffcffff3e3e3cff3f33fcfcf3cfcf3c3ff8f3c3ccf3fcfeffcffffffff8fffffcfffcff3fffcf3fc
    3ff3f3fc3cfc3ff8fffcffcfc3fcffc3e3e3fcfc3ef3efffef3f3fcffcfffcf8ff3ffcfcfcff3fe3ffcffc3fc3fcf3cfcffcfe3e3ecffc3e3e3fcff3fc3ef3ee33e3c7c7b6b6b69a6b9a98b6b669a696a69a69a69a69a6a9a66b6a9a96b9a6b3e3cf3cfffcff3c3fc3fef3feffc3e3ee3fcffffffffffffcfffcfffffcfcf3fcfccf3f3ffff3fcffcfcfcfc3fcfcf3c3fc3cc3fcf3ffcf3fffcff3ffcffffcff
    cfffefffff3ccfff3fcf6c3cffffff3efe3efcffefeffcff3eecffffff3f83f3cfcfcf3ff3fcfefcfcfc3ffefcfe3fc3fc3c3cc3e77c3cc3e3ee3fccf3efee3eee7e7e7cb6b69a6b69a9b6b69a6a6b6a9a66b6b66b6a696b69a696b6b6989a6b343cff3ffffffffe3e3f3e3cf3e3ce3fe3fff3fffffffffcfff3cfcfff3c3cff3e3ffcfc3cfcf8fcf83f8f3cc3c3ecffcfcf3cffffffffcf8ffcfffcff8fffff
    3ffff3cf3fe3c3fcff3cf3c3cfc3ffc3e3efffcf3c3fffcffef3efc3fcfcfcf8fcf3fcfcffcf3cffcfcfefefcf3ccc3ef3eef3fee79bb3e3ee3ecf3fefc33e37e534c7e7b69a6a69a6b9b9a6a696b69a66b9a69a9a96bb69a69ab69a9a6a66b7e3e3cfff3ff3ff3fc3ec3e3cfe3cf3efcfffcffcffc3cf3c3cfc3f3cffe3ffc3f7fc3f3ff3cf3f3fcfcfccfc3cfc3cff3c3fffcf8fcf8fffffff8ffffffccf8f
    c3fcffffc3fe3ffffcf3fcffcf3ffcfe3fcf3cffe3efcffe3fcfcffffcfcffcf3ffcff3fcf3eff3fcffcff3f3efc3fcf3ef3cfc3cb6b9bbc3e3e7fef3cfee3ee7ce77b6b7b6b6b6a69a6b6b69ab69a6b6b6a69a6b6b969a69a69b9a669b9b9a77cf3f3ffffffcfff3c3ec3e3c3e3fff3cfffffffffff3e3ffc3efcfcf73e3ffcfe3ffec3cffcfcfc3f8f38ffcf3ce3fc3fcfcfffffffffcfcf8fffcfcfc3ffff
    3cff3f3cfe3cfffcfcfcff3cf3efcf3fecfcfffffffffc3fee3fef3fcf3f8f3fcfff3fcffcfcfcfefc3fefecfe3cfcfcfc3fcf3e7b9b6b7c3c3ecfffcf3fe3e3e3e7cbb6b6b6b9a9a6b69a9a669ab69a9b9b9a69b9a6a9b9a9b6b69b9a69a69ce3ecffcfcfcffffcc3ec7ce3ef3ee3effffffcfcff3eceee3ec3cf3f3ee3ef3e3e3e33fcf3cf3fcffcfc8f3f3cc3fcffffc3f3cf3fcfcffffff3ffffff8ffcff
    cf3cfef3cfcfcfcfff3f3fffcffcfceeff3cfcffcfffffce3ffcffcf8f8fffcffcfcfcfc3fcfffcffefcf3ef3ef3e3f3cfe3c3ecb9b99b9ce3e7cf3ffcf3c3e347e776b6b7b6b6b69b6b9a69ab69a9a6b6b6b9bb69b9b9a9b69b9a9a969b9b67e33fefff3fff3ff3fe3cc7c3c3e3e3efffcffffffff3e73cc3fe3ffe3e3e3c3e3e3cef3cff3cfcf3f83ffcfcc3fe3fc3cfffcfffcff8f3fcfcffcf8fcfffff3f
    3effe3cff3ff3ffcffcfcc3c3ef3f3f3fe3c3fffffcfcffce3e3ffff3ffc3fcfcfffffffcff3fcfc3fefec3ef3ec3feff3cc3e7b96b9b9b7bbbc3fcf3cccce343b7ebbb76b9a9a9a6b9a6b6b9bb6b6b9b9b9a69b9a9b9a9b99b9b9b9b9b9a9b7c3e33f3cff3fcff3ef3c367cf3fe343cff3fc3cffcfe7cc3fe3eef3ee3e3e3e3e3e3e3ef3ecf3fccf3fcf3c3fcccc3fff3ff3fcff8f3ffff8ffcffff3f3cfcff
    cf3f3ffffcfcfcff3fff3fcffcfffeffc3efefcffffffc3cefcef3cc8f3ffff3ff3fcfcffcffffefefc3cfc3ef3eeff3efc3ec7bb9b9b6b6b6b6fff3fc3c3e3be3b77b6b9a6b69b69a69b9b6b69b9b9b9a9a9b9a9b69b969b9b9b99b9b9a96c3cfcccffe3ffc3cfe3c3ccc3e3fe3fe3f3fcffcffff3c3e3fe3e3c3e73e3e3e3e74e7cf3ec3c3e3f3cfcf8ffcf3f3ccfcfcfcfcf8ffcfcfcffff8fc3fccffffff
    3eccfcfcfff3fcf3fcf8fffc3fcfcfc3cfc3c3ffcfcf3ffe3ff7ec3fcffcfcfccffff3fcffcfeffe3fefc3fefcf3fc3cf3ec37cb6b9b6b9b6b7cf3fec3fee3e3ee3ee7bb69b6bb6bb9bb6a9b9a9a69a9b9b69b69b9b9a69b9b9a9b9b9a996b77f3cf3fe3cfcff3c3c3c3c73e3e3fc3ece3cff3cffcc3eee3c3cfff7e3e3e3e3ecb7e3e3c3fc3ecfc3fc3ffcffcfe3c3fff3fcfff3ffcf8ffcfffcffcf3cf8cff
    e33cff3ffcfcf3fcfcfff3c3cff3f3ffe3fefcfffffcfece3fef7fe3c3fcff3cffcfcfffcffcfc3efef3efe3f3ecffcf3fc7cb7b79b69a6b9b6cfcf3cef3efce3e3e3e7bb6b9b69a6b69a96b69b9b9b9b9b9b9a9a69a9b9b9b99b9a6969a9b6ec3e3e3ff3f3f6cff3ecc6b7f3feffc33e3cfcfffc3ee73e3fe3c3e7ee3ffe3fc3bbb4e3cf3fcf3efc3ffcf3c3fc3ffcc3fcf3cfcfcffcffff8f3fcffccffffcf
    3ef3effcf3ffcffcf3fccf3ffe3effcfcc3c3ffcff3fff3cfcf7e347cff3cfccfffccfefc3cf3efee3fefcfcef3c3f3ecf3c3c7cbb6bb9b6b6b3f3fe3cfc3cf3e7e7be6b69a69a69b9a69bb9a9b69b9b9b9b9a969b969a9a9b9a969b9a6b69b77e3fefcffccfb677e3c6b67ee3f3f3fe3efffff3fcc3e34e3cccc3e33eff3fcffeed7be3e3fcfc3f3ef3cffcfc3cc3ffff8fcf3f8ff8f3fcfffff8f3cfcf3fff
    3e3e3f3fcffef3cf3fff3ccf3ef3fff3c3fcefffffcfccceff3ce3e7ffcfcfcffcf3ee3fecfcfee7fffcf3ff3cfefecf3fcfec7c7bb9b69a9b6cfcf3ef3ef3fe3e7b77b7bb9a69bb6b9bb69a9b9bb9b9b9a69b6b9a6b96b969a9b9a69a969a6b3ec3c3ffcf3c6cce3e3c6bc33e3ecfefe3ffffcfffc343e7ec3f3e7cfc3ffcfff3ccbb7eec3fe3cfefcff3cf3cf3efcfcff3fcfcf3fffffffcfcffc3cf3fcfcf
    cf3e3efffcf3cf3fcfcfcf3ff3efcfcfccf3eff3fffcfce3ccf347e7fcfcf3e3f3ce7e4e3efcc34fcfcf3cffff3e3e7cfcf3e7c777b6bb6b6b6cc7cfefc3eeffe7cbc7bb6b69bb69a9a69b9b9b99b9b9b9b9a9b9a9b9a69a9a969a9a66b9a69b3e3fccf3fccc6637e3f3b6b7e3ffc3c3e3fffcccf3ec343c3cfcfe3effff3ff3fff3cdb7c3ec3ffcf3f3cf3fcfcfcf3ff8fcf6f3fcfcfcf8ffff8f3efcfffff8
    3e3ec3cfffcfffeff3cf3ffccc3fff3ffcccfffffcffc3eeffcfe7e7c3ffccfcffe3e3e7e3cfee3fff3fffcf3ec3ef3ef3e3e3e7e7bb69b9a9b6bcc3f3fe3c3c3b7c7b7c79bb9b9a9b9b9a9b99b9b9b9b9a96b9a69b69b96b99bb669b98b69b7e343c3efff3c9bc3efffb667c3e3fe3e7efcfc63fc3ce7e3c3c3c343f3fecfffffcb7bbbeececec3ffffcfcffc3f3cffcf3cf3cfcfcfcffff3fffffc3ff8fcff
    c3fc3fcffff3fc3cfcffc3f3c3ef3fefc3cff3fcffcfee3ef3f34347effc3efffe3ee7474e3e3fef3fcfcf3fffcc3ef3efe343e7e77b6bb6b6b9c76bcfc3ebc3ec7b6b6b9b69a69b6b9b9b9b9b9b9b9b9b9b9b69b69a99a9b6b69a9a69a9a6b673cc3fc3ffc3c63e3e3fc6bb3e3ef3e37c3c67bfcfc7e3e3cffc3c3e3ff3f3fff3fc3c3ebc7cecccfcfff3fc3fcfcf8fffcfcc3cf3f8ffcfff8fcfccfcfffff3
    ffffffc3fcffcff3f3fffcf3ef3effcfcff3ffffffcfe34f3fe3e7e7f3fcef3fe3e343e7743fcfcfffff3ffcf3e3e3efe3e7e7e7e7cb9b69b9a69b9bc7fcc6bc3cc69b6bb6b69a9b9b9b9b9b9b9db9b9b9b9b9b9a9b9b9b69a9b9b69a6969a9bb3e3efcfcf3fb7e3fef3c96b7cf3efc7bcc6b66bc3e77b7e3cf3fef3fcfffcffcfc3ccc7f7ebc7cccfcfffcffcfc3cffcfc83c3fcfcf3ff8fcfc3c3c3f8ffcfc
    fcfcf3efffcff3cfcfcff3ec3ec3fccf3cffcfffcfc3ec3cfffe3e7e3ffe3cfe3ee7e534347e3c3f3fcffef3fefcccf3e3c3e7c7c7b6b6bb6b9bb6b6b6c7bd6c3c3bb6b9b69ab9b6b9b9b99b9b999d9b9b9a9a9a9b69b9b9a9b69a9a9bb6b696bb7c3f3c3fe3b67e3cfcc6b6b7e3c3c666b6b9b6b77cb7c7fc3ee3ee3f3ffff3c3ec3f3cccc7cf7c3cfccffc7f3fff8f3c3cffc3fcfcff8fc3cfbccfcfc3ff8f
    ff3fcc3cf3f3cffe3fc3cfe3e3feff3effeffffcffcfecefff3e3e34efeeef3e343e7347e7e7efccfcf3f3fcff3e3c3efcc343b7cb79b9b9a6b69b9b6b6c69bccc6b69b69ab96b69b9b99b9d9b9bb9b9b9b9b9b69b9b9a9b969b96b6969a9b9a96b7c3e3fc3cc7e3e3f37a69a73e3fb6b9696b69b6b7b6bc67c3e3c3fcfe3fcfc37ccfc3f3cc3cfecccffcfffcfc8f3fc8cc3c3cfc3ffcfffc3cc3fc3c6c8fff
    3fcf3e3cfccfcf3fcffcff3eecffc3ffeffffcffcfce3e3cfcf3ee3e3e3c3fe347347434343477e3e3ffcffc3cf3ecc3e3ee3e7bb9bb6b9a9b9bb6b9b6bb9b66b7b6bb9a69b6b9b9a9b9b9d9bd9d9d9d9b9b9b9b9b9a969a9b9a9a9b9a969a69bbb7e7fccc6b6b3e3effc96b6b7e7c6b9a6b969a7b7cd676ccc7e7fe3c3eeff3cec3c3cfc3f6cfccf3c3cf3ff3cf3cffcf3ccccfffcfcfffc3fc3cfcc6ccfcfc
    f3c3e3fc3f3f3fcf3ef3cfe3ef3fcfef3ffcfffffcfcee3eff3e3e3e7eeee34e3ee73434347747e7efcff3fcffef3e3e3c3e3e77b69a9a6b6b69b9a6b9b6b6b9b96b9b69bb9b9a9a9b9a9b99d9d9b9b9b9d9b9b9a9b9b9a9b9a9b9b69bb9a9b6969b6bc3b6b6b7b3eff3c69b69bb3e6b69b9a9a69b766b6c3c3b3e3cffe3e3fc7c3c3c3c3ccc3c3cfefb3ecfcffc8f8fc3cc33c3cfcf3fcffce3fcc3c3fff3ff
    c3ec3effcfefcf3cf3efc3fcfcffc3fcfcfffffcfccf3ec3ffcfe3e3e347fe37e734e7e7e747e753e3cf3ffe3c3ce3efe3e3e3e3bbb9b9b9b9bbb69b9b69b9b9b69b9b9a9b69a9b9b9b9b9db9d9bd9b9d9b99b9b9b9b9b969b9b9b9b9b9a969a9bbd3b3c6b9b6d7e3fc3cb69a69bb679a9696b9b6b7b9b6c37ce7e3e3e3e3ffcf7e3cfcfcf38c3fe7fee3e3fffffcff3fc3ccfcfcf3ffff8ffbccfb7ffcf8fcf
    3e3effff3c3c3cfc3e3effefe3fcfefffffffcffcfcefe3fcf3e7efce7e7e7e3e743535e573574743e7cfcffffc3ef3e3e7e3e3e7b6b6b9b6b9b9bb9b9bb9b9a9b9a9a69b9a9b9b9b99b9d99d9b9d9b9b9b9b999b99b9b9b9a99b9b9a969b9b9b96b7fc7b969b6e7cffcc6b969a96bc69a69a969b6b96b6c3e7347e3e3e3effffc3e3c3c63cfcf7cccc3e3fcf3f8f3cf8fc3c3ff3cff8ffffc3e3ebfcfffff8f
    fcfffc3ce3fcf3cfffe3cffffcfc3cf3efcffffcf3fe3efcff3f3e33ce747e7e7e7e7e77745e535e5343ef3c3ffe3ce3e7e3e3e3e79b9b6b9b9a9b9b9a9b9a9b9b9b9b9b9b9b9b9b9b9d9b9b9d9b9b9b9b9b9ab9bb69a9a9b9b9b99a9b9b9a9b69bb7c3c6b9a9b773c3f79a9a69ab69b69a9b69a7b6b9b6bc347753e3e3ff3c3c3bbe3c3cc83c3cfc3beecf3ccf3fffc8ffc3cffffcffcfcfc7fc7bffc8fcffc
    ff3fcfffffffcfffcf3efcf3ffcffcfcfffffcfffefee3cf3fee7ecc3e7e73e73e7347435357e57535e7e3fffe3fef3e3c7fcfe3ebb9b9b9b9b6b9b9b9b9b9b9b9b9b9b9a9b9b9b99b9b9b9bb9b9b9b9b9b9a99a99a9b969b69a9b969b9a9699a9b9b6e6b9b69bbb7c3eb969b9b96d69b9b9b9a9b79b69b67b34347ef3fcffcffb3e3c3c3ccc8fc3c3ec7fcfc3ecff8ffc6ccffccf8ffcff3ccffb7cffcff8f3
    ffcff3fcfcfcffffffe3ffcfcffcf3fffcffff3cffe7ce3fcff3e73ec3e7ee7e534e734747e57e5347e7ffccf3e3e3cfc3e3c3c3e76b9b9a9b9b9b9a9b9b9b9b9bb9b9a9b9b9b9b9b9b9b9a99b9b9a9b9b9b9b9b69b9b6b9b9b9b9a9b9a9b9a9b9b9b97b9b9b969bdc7c9a9a9b69b9b9a9b9a969b9b9b9bb7b3e7e73eefcf3c3c3e3c3cfc383c3cffc3ec7cf7fe3fffc3f3e3c3fc3cfcfcfc3c3fcc3f83ccfff
    fcffcffffff3f3fc3fcfccfff3cfcfeffffcfffcfefc3ecff3cc34c3ee7e73e3e735e535347e757475343cf3eccc3fe3fe3e3ef3c3db9bb9bb9b9b9b9b9b9b9b69b69a9b9b69a9a9b9b9b9b9b9b9a9b9a9a9b9b9b9a9b9b9a9b9b69b9a969b9b9b9b9a9b969b9b996db6b9b969b9b9b9b9b96b9b9b9b9b96bb73e3c43e33cfcfee3e3cc3cc3cc3e73cfc7ec3ecfffcfffcc3ccfc3cfff3cfcfcfffccfccc3cfc
    fff3fcf3fcffffcff3cff3e3fff3fffcfffffcffc3fec3cfff3e343e3747e3e7e343e743535743435e7ee3fcf3e3ee3ef3ee3c3ee7b9b9b9b9b9b9b9b9b9b9b9b9b9a96b69b9b69b69b9b99a9a9b9b9a9b9b9b9a9b9b9b9a9b9a9b9a96b9b9a9b69b96b9b9a9b9a9b99b99b9b9b9b9b9b9b9b9b9b9b9b9b9d7be3e3e7e3ef3f3e3e3e3cc63c3e7e3ef7c3fe3f3cffff8c3cc3fc3cfcfccff7f3fc3c3cfcffcff
    ffcff3fcff3fcff3fef3efc3efcfcffffcffffcfcfcfe3f3ccfe3e3e343343e3ee7e73474e7e7743e7e3cfcfcfee3e3e3cf3efe33ebb9b6b9b9b9b9b9b9b9b9b9a9b9b9b9a9a9b9b9a9b9a9b9b9b9a96b9b9b9b969b69a969b69b69b69b9b969b9a9b99b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b99b9b99b9d7c3e7e7e3ee3e3e3cc7c7c3f3c3ef7c3e3eefcfcfcffccfec3fcffc3c6ffccffcfcff3cfcfcf
    8f3fcfff3fcff3fec3efe3fef3fcfcfcfff3fff3fefe3efeff3e347e3e7e343e334343437e77e347e3b3e3fe3e37e3e3efc3f3cce779b9b9b9b9b9b9b9b9a9b9b9b6b9b6b9b9b9a9b9b9a9b9b9a9b9b99b9b69b9a9b9a9b9a9b9b9a99b9a9b9a9b9b9a9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9d9bd9dbdc3ec7cc3e3e3c3e7c3c3e7ffff3ffcfcfc3fff3cffc3e3c3cfcfc3fcffc3cffc3fcfcf3f8ff
    ffcff3cfcffffcfcecfc3e3cfcfef3ffcfffcfcfefc3eff3c3ef3e7e3e343e3ee73e3534353434377befefc3c3ec3e3e3efccf3e3ceb9b9b9bb9bb9b9a9b9b9a9b9b9a9b9b6b9b69b9a9b9b69b9b69bb9b99a9b9b9a969b69b969a9b69b969a969b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9d9b9d9b9d9b9d97b3e7bc3be3ccf7e7e3bc3be3b3efc3e3efcf3ffcf3cc3cfefc3cfcfcf3fffcffc3cf3fcff3c
    fff3ffff3f3effc3f3fe3ef3cf3fefcfffcfffcffccef3fcff3ee7e343e3e3e334343435e347e7ee7b3e6e3fee3e3e3e3c3f3cfe337b9b9bb9b9b9b9b9b9b6b9b6b9a9b9b9b9b9b9a9b9b9b9b9b9b9b9a9a9b9b969b9b9b9b9a9a96b9a9b9b9b9b9b9b9b9b69b9b9b99b9b9b9b9b9b9b9b9b9b9b9d9dd9bd9d9b9de9b9db9b7c3e77e3e73fe3ee7e3fe3ef3fcfcfffc3ccf3fc3cf3fffcffcf8ffcefcfcf8fc3
    f8ffcf3ffcfcf3ffcfcfe3efe3fcffffffffcffecfe3bfe3ccc3e7e3e3e343e3e3e7e7e3543e7e7e7bc33be37e7e3434e3cfe3e3e47b9b9b9b9b9b9bb9bb9b9b9b9b96b69a9b9a9b9b9b9b9b9a9b9a9b969b9a9a9b9b9a9b9b9b9b69b9b9a9b9b9a969b969b9a99a9b9b9b9b9b9db9d9b9b9d9b9db9d9d9d9dd9dd7dd99d9db7ebe7e343ecff7f3fe3cfffcf3e3c3fcffeccffcfcfcfcfcffffcf3bcfcfc3cf8
    ffff3fcf3fc3ccffcfcf3e3efefef3cffcfffcf3ecece3fcf3ce3e7e3e3e3e3ee343435e7343e37e7bbcbb6bb7f343b7c3c3e3ce3e7b9b9b9b9b9bb9b9b9b9b9a9b6b9b9b9b9b9b9b9b69b9a9b9b9b9b9b9b969b9b9a9b9b9b9b9b9b9b9b9b9b9b9b9b9a9b9b9b9b9b9b9b9b9d9b9b9b9d9b9b9d9d9b9d9dd9d9d99d6dd9d9dc7c3e3b3e3e3e3ec3fefc3fcfe3efcf3e3ff3cffc3fc3f8ffc8fffc7e3c38f8c3
    ffcfcf3efe3ffcff3ffcfcfcf3c3fffffffcffcfe3e3ef3fef3e3e3e3e3e3ee3e7e35e3747e734b7b976bdbb7c3e347ce3ebc3e3e3bdb9b9b9b9d9b9b9b6b9b69b9b9b9b9b9b69b9b69b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b969b9b9b9a99b9a9b9b9b9b9b9b9db9d9d9db9d9d9db9bd9d9d9d9dd9dd9d919dd9b77c3fefe3ee3cfcc3e3efcf3fec3fcfcfcfffcf3cfcfffc3fffcfbccccfccffc
    fff3fcfc3fffefcfcfff3fc3ccfcffcffcff3feceee3fcf3f3e3e343c3e3e3e3e3e735e7e7347bbb7bbd696d6e3e3e7b3477c3cc3b79b9bd9bdb9b9b9b9b9b9bb9b9b9b9a9b9b9bb9b9b9b9b9b9b9b9b9b9a9b9b9b9b9b99b9b9b9b9b9b9b9b9b9b9b9b9b99b9b9b9b9b9bd9b9b9b9b9d9bd9bd9d9dd9b9d9d9b19d19d9d91dd7c3ef3fc3e3ef3fe3ff3f3ffc3ffcf3fcfcfffffcf8fcffcfffff83ff3c63cff
    cfcf3ffffcffc3fcfcfffcfffcffcfffffffcfc3e3eef3efeffe3e3efe3e3ef3e34343e77ee7e7d6d79b9bbdc3e3e7b7c3e7ce3e7bdd9b9bb99bd9dbb9b9b9b9b9b9bb9b9b9b9a99b9b9b9a9b9b69b9b9a9b9b9b9b9b9b9a9b9b9b9b9b9b9b9b9b9b9b9b9a9b99b9b9b9d9b9b9db9d9dbd9ddd91dd91d9b9b9b919d91d9d9db7b3eefcfee3cc3ecfcfefffcffec3fcffffff8ff8fff3fcff3cf8fcc3fcfc8fcf
    3f3fcfc3ff3cffe3ef3fff3fcf3ffcffcfcffcfeee3fcf3c3f3e3e7c3fe3fe347e3e7e7e773e7c9bd6b9b9b93e3e3db7c3e77b7c7b9b9bd99db9db99db9bb9b9b9bb9b9b9bb9b9bb9b9b9b9b9b9b9b9a9b9b9b9b9b9b9b9b99b99b99b99b9d9b9b9b99b9b9b9b9b9b9b9b9b9d9bd9bd9d9dd9dd19d1d9d9d9b9d9d9d99b9bb7743e73e73cff3ef3c3ffcfc3ef3efcfcc3cfffcfffcfcc3cffcfff7fc3fc3cffc
    ffcfffffcfcfe3fef3ffcfcffccff3ffffffcfeceefcf3fcfe3ce343c3cc3fc3e3e3e77e74e7cbb9b9b9b9bb7e3ee7dc3e3bcbb7cbd9b9bdb9d9b9db9db9db9bdb9d9b9bb99b9b9b9b9a9b9b9b9b9b9b9b9b9b9b9b9b9b9d9b9b9b9b9db9d9d9b9b9b9b99b9b9b9d9d9d9dd9d9d9dd9ddd9ddd1d1191ddd1d999b9db9b9bd7747e34e3ee3ee3cfcfc3e3fe3ef7cf3fffccfcffffff83fff8ffcff6ccc3fcc8ff
    3fc3fcff3ef3cff3fcffffff3fcfcfffcf3fcf3ec7c3fe3e3fc3c3e3fc3fef347c353e757b7e79b79b9b9b9b7ce3db9b3ce7d9bd69dd9d99db9b9db9d9b9b9b9d9b9bd9d9bb9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9d9db9b9b9db9d9dd9dddddd9d9dbd9ddddddd9dddd9ddd9d9dd9d9dd919d9dd9d9999bd99b99b9d9b7e7e7e33e3ef3cff3f3cfcf3fe3ce3fcfff3c3fcff8ffcccfcf3cffcc33cccf3f8f
    ffcfff3fcffffffcffcf3f3fcfeffcfffffcfceceeff3fcf3cf3fe7efcfc3fe3e3ee7e7e7b7e7d9b9b9bb9bb73e7bd9be3edd69ddd6d9bb9b9d9b9d9bd9d9d9d9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9d9d9dd9d9d9bd9db99dbd9ddd9d9d1ddd91bdd191d911dd1d1d1dddd9dddd1d1d11d9d9d9b9b99b9d9b9b9b7e7e7c34f3e3e3f3cfe3c3ccfcfcfecfefcffcefcffffffcff3fcfcf3ccc3cffcfcf
    cf3fcfffff3f3cfff3ffffcfff3f3ffffcffffe3e3cfc3e3efcc3e3e3f3fc3fe3e73475e7d7ddbb9bb9b9bd9be7dd7d97cb9b9d9b9d9b9dd9db9db9d9bdb9bdb9db9d9b9b9b9b9b9b9b9b9b9b9b9b9b9b9d9dbd9d9dbdb9b9b9b9bd9d9d9ddddd9d9dd1db9d1d111dd1191d19d9d91d919d9d99d9d9b99d9d9b9b9b999b34343e343ce3eec3fc3eccf3e3ef3e7f3c3c3fc3cfcfcff3f3fcfffffcf3cf3ffc83f
    fffff3fcfcfefff3ffe3ef3ffcfcfcfffffcfeceeef3cf3fc33fe343fefcfe3e3e347e77475d7dbb9bdbd9bdb7d9b9bdb9b9dd9b9d9bd9b9b9db9db9b9d9d9b9b9b9bb9b9b9b9b9b9b9b9b9b9b9b9b9d9dbd9d9dbd9d9d9bd9d9d9b9bd9d9d9d9ddd91d1bb19191d1191119119d91d1d9d9d9b99b999b9b9b99d9b9b9bd7e3e3ee3efe3c3fefcc3e3eec3fcf3ecfecfecfecf3fffcfffcfc3c3fcfc3fcf8f3cc
    ffcffcffff3ff3fcff3f3ecc3fcffffcfcff3cc3e3fe3efe3fef3e3ef3f3f3fe347e75e7747477d777b9bd99d9bd9b99dd9dd9bdd9dd9dbd9b9db9bd9b9bb9b9b9b9b9b9bd9bd9bb9bb9b9b9b9bd9db9db9dd9bd9dbd9dd9d9b9bd9d9dbb9d9dd9ddd191b9d91d19d9d9d9d9dd9dd919d9d99d9d9d9d9d999b9b99d9b99b7e343e3c3cffc3e3e3e3e3c3fcf3ec3e3ec3ecfccffcffffcfcffcfcf8fcfcffcf88
    ff3ffff3fffc3fcffccec3e3eff3cfffff3cffeeee3fcf3cff3cfe3ffcfefe3e347e774747747475dd7b7d9b9b9d9d9d9dd9b9d9db9db9d9ddb9b9d9b9d9b9b9b9bd9b9d9b9db9d9b9db9db9bd9bd9db9dd9bdd9dd9db9dbd9dd9dd9d9b9dbd9d9d9d9d19d9d99b9d9d9d9d99d9d91dd1d1dd9d99b9d9b9d9d9d9b9b9d9be7434fcfffe3cfe3ee3e3efff3cc3efc3e3ec3cffcfff8ffffcff3ffffffcfc3c3fc
    ffffcffffcffe3cfff3e3e3effcfffcffcffcfe3e3ef3ec3cfc3c3ef3f3f3cce73e7e74774747747d5d7dbdd9d9bd9bdb9dd9dd9d9d9d9db9d9d9db9bdb9b9db9d9b9db9bdb9dbdddd9db9dd9bd9db9dd9ddd9dd9ddddd9dbb9ddd9dbbbd9dd9dd9dd1d9d99b9d9d99d99d9d9d9d9d9d919d9d9dd9d9d9d9b9b9d9999bd7473e3cf3fcf3fe7e3e3ec3efcff3fe3fecfcfecc3cfffffcff3fcfcfcf8f3fcfcf8f
    ffcff8ff3f3fcc3fc3e3e3e3e3fefffffffffeceee7ccf3fcffcfe3fcfccf3e347c5343ee7e74774747d7db9bdd9d9d9d9b9d9db9ddd9d9dd9ddb9db9b9b9b9db9bdb9dd9d9dd9d9d9dd9db9dd9dddd9dddddddddd9d9dd9d9dd9ddd1b61d19d9dd9d9d99d99d999d99d9d9d99d9d9d9d9d9dd9d9dd9dd9ddd9d9bd9d9b7743efffcf3cfe7e7e343e3c3fc3fc3cf3cf3ffcecfcfcffffffcfffff3fcff3fc3fc
    3fffcffcfffcf3efcfe3efe3ffcffffcfcfcc3e3e3e3c3fcf3f3f3ef3ff3ec3e7e3e73477e77ee57475475d7db9dbd9d9dd9dd9dd9d9dbd9dd9dd9d9d9dd9db9dd9d9db9ddddddddddddd9dd9ddd9ddddd1d1919dd1d1d1dbd9dd19d19bd9dd9d99d9d9d99d99d9d9d9b9d9bd9999d9d9d9d919dd9d19dd99d9d9d9d9dd7e7e3fcffeffc3e3e7e7e3e3ee3efce3effefcf3cccfcfcff8ffff8f3fcfffcc3cfc3
    fff8ff3fffcfffc3e3e3e3eccf3ffcfff3fffeeee3e3efe3fefcc3e3fefcf34343e3437e347e357e7e77477d7dd9d9ddd9dd9d9d9dbd9d9d9dd9dd9dbd9bd9dd9bddd9dddd9dd9dd9dd9ddddd9ddd1d11d1d1ddd19d1d9d9b9d9d9d9dd6d99d9d9d9d99d9d9dbd9d9bd9d9d9d9dd9d99d9dd9dd91d9d9d91d9dd9d9d9d9b5ccfc3f3cc3e3e3e53e3e343ccf3ffcfcf3ffcfe3fcf3fcffff8fffccc3cf3ffc3fc
    fcffffffcff3ffcf3e3e3e3c3cffcff3ffcfe3e34cee3eff3f3ffe3ef3f3ee773e3e7ee7e33e7e3575e75e57d7dddd99dbd9dbd9d9d9ddddd9dd9ddd9ddd9dd9dd9d9ddd9ddddd1dddddd9d9dd9d9d1d9d9d19d9dd9d9dd9d9d9d9d999d9d9d9d9d99d9d9bd9d99d9d9d9d9d9d99d9d9d9d9d9d9d91d191d9119d19d9dd7e3c3effc3efce34347e3e3e3c3efcf3cf3fe3cfeccfcffffffffff3f3fc83fcf8fc8
    ff3fc3cff3ffcf3ecfe3e3fefcffffffcfffccee3c3e3e3cfcfc3ee3cfe3e3e5e3e3e3e73ee3e347e75347e57d7b9ddbd9dd9ddddd9d9d9d9dd9dd9dd9d9dd9ddddddd9dddd91d1d11d91ddd9dd1d19dd1d9d9d9d9d9d9d9d99d9d9dd9d99d99d99dd9d9d9d99d9d9d9d9d9d9d9d9d9d9d9d9d919d9d9d91d9d19dd9d9dd643e3cfecf3f3ee7e3e3c3befeff3fffccffe3f3fe3ccfcfcffcffcfecf3fcf8ffff
    fffcf3f3cfffffcf3c3eee3fcfcffcfcffcf3e34fee3ecffff3fc3c3fc343e37e3e3e33e343e3e3e7e747e57e5bdb9d9dd9dd9d9d9ddd9ddd9ddd9dd9dddddddd9d9dddd1dd1dd1dd1d1d191d9d9d9d9d9d9d9d9d9d9d9d9d9d9b9d99d9d9d9d9db9d9d9d99dd9d9d9d9d9d9d9d9d9d9d9dd9dd9d19d191d919d9d9d9d9db7cec3b3c3fcf3e73e3cee3f3c3fcfcfff3ffcfcc3efefcfffffff3fe3fcfc3fc83f
    cf3f3fcf3cffcf3e3ef3c3fcf3cfffffcfffcfee3fee3e3c3ffcfe3ef3e3e7e7e33e3ee3437e7e3e7e7753747e77dddd9d9d9d9dbd9d9bd9bd9d9dd9dd9d9d19d1ddd1d1d91d1d1d19d19dd9d9d9d9d9d9d9d9d9d9d9d9d9d99d9d9d9d9d9d9d9d9d9d9b9dd99d9d9d9d9d9d9d9d9dd9dd9d9d9d9d19dd9ddd19d91d9d9d9c7d7bfcffefee3fecc3e3eecfffff3f3ce3fffffc3e3cffcf8ffcfccecfc3cf3fcc
    fffcfffcf3cfffcfe3fefcfcfcffffcffcfffe7cfe3ec3efffcf3e3e3ec3e3e77cc3e3c3e3473473475e747e757d7d9d9bd9bd9dd9dbd9dd9ddbd9dd9dddddddbd1d1d1d9dd1d9d1d19dd9d9d9d9d9d9d9d9d9d9d9d9d9d99d9d9d9d9d9d9d9d9d9d9d9dd99d9d9d9d9d9d9d9dddd9dd9d9dd91d9d9d919199dd1d9d9d9dd6d9b6c3ff7e7e343c3e3e3cfc3fcfefcffcfcf3fcfeec3cfcfff3f3e7fcfecccc3f
    fff3c3ffcc3fffc3ce3c3fefffffcffcffcf3efe3e3e3e7fcfffcfe3e3c3e3e3e3c3fe3e3e7e7e743e77d7b77e74dd9db9b9db9d9dd9d9d9dbd9dd9dd9d9d9d9d1d1d1d1d1d9d1d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9dd9d9d9d9d9d9d9d9d9d9d9dd919d9dd9dd9d91d9d9d9d9dd9d19d99d9d9d9d9b79bc3ce3435be3cfe3ec3fcfcf3fcff3cf3ffcff7e7ecf3fcfc3ebc3e7f3c3ccf
    8fcfcfcf3fcfcfef3efccf3fc3ef3fffcffefe3ececec3eef3f3f3e3ccf3e3e3cf3e3c3e3e77e75e77eddb7dd7d7b9d9b9bb9bb9db9dbd9dd9dd9dd9ddddd1ddd9d19d1dd1d1d9d9d9d9d9d9d9dd9d9d9d9d9d9d9d9d9d9d9d9dbd9d9dd9dd9d9dd9d9d9d9dd9dd9dd9dd9ddddd9d19d91dd9d9d19dd9d91d9d9d9d9d9d9bd9bc3cfc3e347e7cc3ef3fef3ff3fcf3fffcffffffcee7eefcf3fcf7ffeef3cc36f
    fff3c3f3ff3ef3effe3efcfffecfffcfff3fc3e3f3f3efe3fffcc3e3e3fe3e3c3cc3ec3e7e347e77e737ddd9dd7d7d6bd6d6d9bb9d9d9dd9dddddddd9d9d9d9d1d9dd1d19d19d9d9d9dd9d9d9d9d9dd9d9d9d9d9d9d9d9d9dbd9d9d9d9dd9dd9d9d9dd9dd9d9d9dd9dd9dd919d91d91dd919d19d9d9d19d9d19d1d9d9db69b7b7c3e7e435e3e3ee3ecfcfcfecffffcfcfcfcf3fc3e74c3fefe3cc3e3cfc3c6c3
    fffef3fefcf3fc3fcfff3fcfcfffcfffcffcfeefffefe3ec3fcf3cfef3f3ef3ccf3e3e34343e77e343447d7dd7dd9bd69b9b6b9b9bd9d9ddd9d9d9dddddddd1d9d1d191d11dd9d9d9d9d9d9dd9d9d9d9d9d9d9d9dd9dd9ddd9dd9d9dd9d9d9dd9dd9d9d9dd9ddd9dd9d191d9d1d91d9d1d919d191d19d9d19d19d9b9d6dd6c6b6bb7b75e7e7e3c3cff3f3c33cf3fc3ff3ffffcfecee7eef3effe3fffbf3f8ccc
    ff3fe3fcf3fcffefff3cfff3cf3fffcffcffe3eceff3cc3eef3ff3e3ffe3e3fc3ce3ee7e7347e747347777d7d9d6d69bb6b9b9b7b9dddd9d9ddddd9d9d9d9d9d1d91dd9d9d9dd9dd9dd9ddd9d9d9d9d9d9d9dd9d9d9ddd9dd9d1ddd9d9dddd9dd9dd91dd9dd9d919d19dd9d19d91d91d91ddd9dd9d9d9d9d9b9d9dd9bd9cd7b97bb7e343e3e3efcf3fcfcee3effcfecfcc3fff3ff3ebc3efc3c3fccf3ccffff3
    ffff3e3c3ef3cfcffcfffcffcffffffff3fccfeff3cfecf3e3fccf3cf3fe3cc3c3e3e7e7e73477e74734e77b7b79bb79b9b79bd6d6d9b9dd9d9d9dddddd9d19d9d9d9d1d9d911d19d1d1119d9d9d9dd9dddd9d9d9dd9d9dd9d1919d9dd9d9dd9dd9dd9d9d9d1dddd9dd91d9d191d91d9d9d91d919d9dd9d9b9d9d9bd6b796b7c7bc7e5353e3e3ef3cfff33ef3fc3fff3fffcfcfcffe3ee3cfcfc3fffc3fcfcfc
    ffffffcfffcfef3cfcffffffcffcffcfcfcfec3fcffef3eceff3fcf3fe3e3f3efc3e3e73ee7747e774735e7477bb79b69b6b96b9b9b9dd9d9d9d9d99d9dd9dd9dd9d9d9d9dd919dd1d9d1d1d9d9dbdddd9dd9d91d9ddddd9dd1ddddd9ddd9db19d9d9ddd919d919d191d9d19dd9dd9d1d19d91d9dd9d9d9b9d9dbd97d9bbb6ccc3c3e7e3e3e3ef3ccf3fee3ef3fcfcfcfeffff3ccffe3ec3c3cfef3fccf3fcf3
    fcfcfff3ff3f3cfcffffcf3f3ffffffcfcffefefffcffeff3cff3e3ee7e7e3e3e3ee7e3437e77e77434374774777b7bd6b9bbd6d6db9d9d9dbd9d9dd9d9dd9dd9dd91d9dd9ddd1d91d1d1d19d9dd9d91dd1dddd91dd9d91d19d11911d191dd19d9ddd19dddd9d9d9dd9d19d19d191d919d1d9d9d9d9d9b9b9bdd97dd6b9767b67c3e3e343ee3fcf3efe73e3cfcfff3c3f3fc3ffc3ffe3e3effc3fcff3ffff3cf
    fffffc3fcffcfcfefffffffecffcfcffcfc3ee3fcff3fc3ff3fcfec3fc73e7e3e3433e3e3e347e777774774774747b7bd6b96d6dd6ddd9dbd9dd9d9dd9d9dd9dd9dd9d9d9d19d1d1d1d1d1dd9ddd1d1d91d9d9ddd9dd1dd9ddd9d1d91d1d11d1d19d9d9d919d1d9d919d9d9d19dd91d9d9191d19d19d9b9bd7d7b7b7d976b67ccce7e3e3e3e3e3ff3c3ef3ef3cf3cfffcfefccf3efe7e3e3efcfcfcfcfc3fcff
    ffffffcff3fcfff3f3ffcfff3fffffcf3fecc3eeffffcfe3fef3c3fffffc3e343e3e3e3e3e77c77be7b7e7e74775777b7d6db9bd6d979dd9dd9dddd9dddd9d9d9d9dd9d91dd1d9d1d1d9d19ddd919d9ddd1dd19dddd9d9dd9d9dd91d11d1d1191119d19d19d9d91dd9d19d19d9d9dd91dd1d19d19d9d9b9b67c7d77b77c67b67c7c7c3ee3e3efe3ee3c3ee3ff3ffffcfff3fe3fccf7c3e3e3e3ffcffc3ffcf3f
    cffcff3e3ef3ffccffcff3fcfcfffcfcfcfceecff3fff3cffcffffcf3f3ee74743e3e3e3e3eb7e7b7b7e7e77747be5e7b9b96b79d6d9dd9d1dd9dddd9d9d9d19dd9d9ddd9d9d9d1d9d1d1d1d91ddd1d19d9d9ddd9d91dd9db9d1dd1d1d1d1d1d1ddb9dd9ddd9dd919d9dd9d9dd1d91d9d919d119d9db9b9bbd7d7b7d7c7c7cc7c7bc3e3fe3e3e3e3c3ef3e3cfcfcf3ff3ccfc3ff3efe3eccfecfffc3fffc3fcf
    ffffffc3cfcfff3feff3fffcfffcfffcfcfe3e3cffcfffef3fe3fcf3fcff3f77743e3fe3e7e7b7b7e7b777be77b57777d7bb9d69b9bdd9d1d91d19d1d1d1d9dd91d9d19dd9ddd19dd9d1d1d1dd9d9d9dddddd9d9dddd9dd9dd9d9d1d1d11d11119d9d9d19d91d9ddd1d91d91d991d9b9d9d119dbdd9b9b9b76b7b7b3c7c76b76b6c7e3e3fe3ec3fffef7e3ef3ff3fffceef3efcfe7c343c3e3effffcfcffcfcf
    ffffff3ef3ff3fef3f3ffcfc3ffffcf3fcfeeee3ffffcffcfc3fcf3fcffff474757e3e3e3e7b77b7b7b7b7e7e777ee5e7d79b79bdd79bd9d1d1d1d1d9d9d1d91d9dd9dd9dd9d9dd9dd9d91d9d9ddd9d9d99d9ddd19d9d19ddd9dd9d1d1d91d1d11bb1d9dd1d9d191911d9ddd91d9b9b9bd9db9d9d9d9b9b9ddd7b77e77bbb9bb7b7bcf3ef3e3ee3cf3c34c3effcffcf3c3fc3ffc3e7e3cefbecc3cf3cf8ffffc
    fffcfffc3fffcfcfcffcfffefcffffcfefe3e3efcfcff3f3fcfff3fcff3f3e7574743c3e3c7bb7b7b7d6b777747b77757dbb9b9b969d9dd1d9d9d9d1d1d19d1dd191d9d19dd9d9d9d9d1d1d1dd9d9dd19dd9d9d9d9dd9ddd9d19dd19d11d1191d19d91d191d19dd1dd91d91d1d9db9b9b9d9b9bd9bd9b9bd9b7b7e76bd7d7b76b6bc7cf3cc3cf3fc3fcf3ce7c3ffff3cfcfecf3fec7ee3e7e3e3ecce3ffc8fc3
    ffffcffcfcffffff3ef3ff3f3ffcff3cfcfecfcffff3fcfffffcfeff3fcfe3e3477d3ee37e7b7b79b9b7bbbb77b747e7477d6d6bddd79d9d9d1d1d9d9d9d1d9d9ddd1d9dd191ddd9dd1d9d9d9d1dd9d9dd9ddd9ddd9dd9d9d9dd9dd19d91d9dd9d1d19d1d19d1d1911d9d19d9d9b96b69bb9bb9b9d9bd9d9b9b777bd7db9b7bb6b6e3e3fcfefcf3fcf3cfe7bee3e3ffcf3c3fffe73e77efbcfec3f3fefcff3fc
    ffffff3fcf3fc3ffcf3fcffffeffcfffcfc3ee3cf3ffcffcf3f3cf3feff3e7e77475d3e7bc796bd6d7b97b7b7b77b7e7747dd6d979b9ddd9dd9d9dd9d1d9d1d1d1919d1d9dd191d119d1d1d1d9d9d1dd9dd9d9d9d9d9dd9d9d9dd9d9ddd9d1d1d9d91d1d9d1d9d1d9d1d9d9dd9b9bb9bb96b9b6bb9b9bb9bb7b7bb7dd7d7bb67b3c3c3ef3e33e3ef3efc3e7e3e7ceff3fcff3c3e7b7cec7c3c3fece3c3cfccff
    ffffcfff3fcffecff3ec3fc3fcffffefcfefe3effcffcf3fffeffcfeffffc3e3e34747e3e7bbb79bd6dbd79bb7b7b74747b79b9b9b9b9d9dd9dd9d9d9d9d9d9d9d1d1d91d19dd19dd19d9d9d1d1d9d91d1d1d9dd9dd9d9dd9dd9d9d9d9dd9d9d1d1d1d91d1d1d19dd9d9ddd9d9bb66b69b9b6d96b6bb9b9b9bb7d7d7dd7b76b7cc3ccc3e3efeffce3ce7e7e7b3e73e3fc3fec347cefe7fecfcf3f3fefc3fc3cf
    cfc3c3efccffc3fccfc3ecfcc3ffcffcfc3ecfc3ffcf3fcffcf3e3cff3ffc3ee7e7575e73e779b796d96d6d79b7bd77b777db79b79bd9bd9d1d91dd9dd9dd9d9d9d9d1d191d11d191dd1d1d9d9d1d11d9d9d1d9dd9d9dd9d9d9d9d9dd9d9dd9d9d91d1d1d19d1d19d19d9d9d9b69b9b9b6b9d6b9b9b6d6b6b79b7dd7d7b6bb7cc3c3f3cfe3b3c37ee7e3ec3ece7ee3cffc3e3ee3c3e3cfc3e3fccfc3cfccffcc
    f3ec3ef3fef3cfefff3fcf3fcfffcf3fefceccffcffcffff3fef3ff3fff3fe33e347477ee3ec7b9bbd6db9bdbbd7dbb7dd77dbd9bd97d9db9d9dd91d9d1d9dd1dd9d9d9d1d1d9dd1d919d91d1d9d1d9d1dd19dd9d9dd9dd9ddddddd9dd9d19dd1dd1dd1d9d1d9d9dd9dd9b9bb9bb6b6b9b9b6d6b9b6d6bd6d6b7d7bb7b6b76b7d7ce7c37e7be3ede77b77ee33e73c3ec3fe3437e3eee3efec7cf3fff3c3fcfb3
    cc3ee3cfc3ccf3c3fcfcf3efffcfefcfcfc343fffcffcfcfcf3ffcfffcffc3e3e3e77477c37e7cb9b79b9b97979b97dd7bd7b79b96b9b9bd9dd19dd9d9d9dd9d9d9dd9dd9191d19d1dd1d1d919119d1d919d19d1dd1d191dd19d9dd9d9dd91d9d19d19d1d19d1dd19dd9b9b9b6b9b9b9b6b6d6d6b9b6b66b6b7b6b79b6b9bbdd97b7fee7b7e3efe7b7bde37ee3fe3e3cc3e7c3e3ef7e3cc37cf3fc3cffe3fc7f
    3ec3ee3e3ef3ffcf3f3fcffeffcff3fcfceceefcff3ff3fffcfffffcffff3e3e347e745e3e3e77e79bd79b9bdb9bb9b79b7ddb9b7d9b9b9bd9b9d9d1dd9d9dd9d9d9dd9ddd1d1d11d191d91d1dd1d19d1d1dd19d9d9dddd1d1d1d1d1d191dd1d9d1d91d9ddd19d9d19d9bb9c9b6b6b6b69b9b6b9b6d69bd676b6bd6b6b7b6979c7c777e7e7ee7e77e743ebc7cc3ecff3fc3e3e3ee774fc7bc3cfc3fcfcfc3ccc
    c3ec3eccfe3cf3cffccf3cf3ef3cfefcff3e3cf3fcfcfcfff3fcf3ffff3fe3e3e375377e3e3e3e7bb79b9b796d79b9b9bdbb7d79b9b7d7d97d9ddd9d9bdbd9d9dddd9d19d9d9d91d91d11d19d919d9d19d19ddd1d1d1911d9d1d1d9d9ddd19dd1d9d1d1d191dd119ddb9b69b69b9b9b9bb6b9b9b6b6b6b6b9b6b66b6b796dbd6d7bce77be7e7e3747d7e7c3e3ee3c3ec3fc3cfe3e3d7fe7b7cc3fcfcf3ffcff3
    ef3fe3e3c3fcfc3cf3fcffcffffffcfcfececefffffffffcfcffffc3fcffc3ee343b4e5dc3ece7e77bbd6d6db9bd7d7d79b9d7db9b9b9b7d9b979bdd6d69bd9dd99d19dd9d1d9dd1d19d91d1d9d1d1d9d1d1919d9d9ddd1d11d9d1d1d19d9dd9d91d9d9d1d9d9d9d9b9b6bb6b9a69a69b9b6b6b6b9b9b6d66b6b6b6b69b6d6d7c7c77be77473e7e7e7e7ce7ec7cffc3fc3fcf3e734e7e3b76c6ccf3fcfcf3cfc
    3eeccfcc3ef3ffcf3e3e7cfcfffefefc3ffe3e3fcf3cfcfffff3f3ffcff3fe3e3e3437743ef3e3e3e76b79b9bd69b9b9bd7d79b9b7dd6d9b6b7bd96d9bb9b6bd9dd9dd9d9d9d9d9d9d9dd9d9d1d9d9d1d9d91d1d1d1111d9d91d19d1d1dd19d19dd91d19d9d9d9bb9b6b9b9b9b6b9b9b69b9b9b96b6bd66b6b6b6d6b6b6b6b6db7b7e7e7b7ee3e7e7e77e3b7f3c3fe3ffc3c3e3ee7eefcccc3cc6fcf3fffcfff
    e3fe3e3ec3cfc3fcfcffcffffff3cf3fecceeefffcffff3fcfffcfe33fffcf3fc3e34747b3c3ec3e3e7bbd6b9b9b9bd6969b9bd6d96b9bd9d9b9b9b79b6b9b79bd9d9d9dd9d9d1d9d9d19d9d9d9d9d9d9d9dd9d9d9d19d1d1d9ddd191d91dd9dd91dd9dd9d9bb9b9bb9b69b6b9b9b6b9bb9b6b6bb9b66bb6b6b6b6b6b79b6d79b7b7c7bee7e7e3e347e7e7b3ece3effcf3ffe7e7343c3f63c3c3cc3fcfcfcf8f
    ce3ee3e3cf3ffc3ffff3ffcf3fffcefcffe3cffcf3fcfcfff3cf3f3fc3cf3fe3cc3e7e7743fe73ec7e37c7d6d79b796dbdb9b6db7bd6b76bb9b7d79bb97d69bd9bdd9dd9d1d9d9d9d19dd1d1d911d9d19dd9d11d119dd9d9d1d919d1d1d9d9d19dd9d19b9bb9b9bb96b9bb9d6b9b69b9b9b9b9b96b6b96b9b6b96b6b6b6b96b9b7b7ce77e73e7e3437e7e3eb3e3e3f3f3cfe3e3e7e3ec3e7cfc3c3cffff6fcff
    3ee3eeee3cfc3fcfcfcfe3fccffff3ffefeee3fffcf3fffcffffcfc3ccf3fcfc3ce3b7477ec3ec3e3ee7cc9bd6b9bbd696b79b69b96b9bd7d79d6db97b69b79b79b79d9dd9dd9d9d9dd99d9d91d9d19d9d9d9d9d9d1d1d1d9d9dd1d9d9d1d1d9d19d9db9b9b9b696b9b69b9b9bb9b9bb69b6b9bb9b9bb6b6b6b6b6b6796b6d6d6bc7347e7474343c3e7e7e7ee7eeccfcff3e7343e7e7cc6b3ffcfffcfc3fcfff
    e3e3e33e3fcffcf3fffcfcfffffcfcfef3e3efff3fcffcfffcfcf3fc3c3cf3c3f3c3e74747fe3c7c7c3e3776b9b796bd6d9b6bd6b6b7b66b6db9db7d9bd6b6b9db9bb9b9dd9dd9dd9d91d19d1d9d9dd9d9dd9d9d9d9d919d1d119dd1d19d9d9d9d9d9b9b9b9b9bb9b6b9bb6dd9d9bd69db9b9b69b6b6b6b6b6b6b6b6b6b6d6d9b77ce3e3e3c34343e3e7f7e77e7c3cff3cf7e3437e7c3ce7bf3fcf3ffcffffff
    3ee3eee3ef3fcfffcff3cfeffcffffcfcfee4ffcff3ff3fcff3fff3cf3ffcfcfcfc3e34347ec7ccc7c3e7ceb6b9bbd6b6b6b76b6b79b6bd6b7d7b96bc76b9b9b79b9bd7d6d79dd9d9d1d9d19d9d1d9d9dd9d9d9d9d9dd91d919dd919d9d9d9db9db9b9b9b6b6b9b6b9b9b9b96d79d6dd6d6d6b9b6b9b6b9b6b6b6b6b6b6d69b9b7c3e3e3e7477e7e343e7b3eb7cff3c3ff3fe3e7e7ccff8fccff3ffff3fcf8ff
    cf3e3e3ec3fcf3ff3fffc37fffffcffcfee7cfff3fcfcfff3fffcff3ecfcfc3cf3cfe37e77e3c7c7c3c3e3c7d6b769b79b6b6b9b6b6b976d76bb9e7c6b7b6d79bb9769b9b9b9b9dd9d9d9d9d1d9d9d1d9d9dd9d9d9d9dd9d9dd9dd9d9dd9bd9d9b9b9bb9b9b9b6b9b9b6b6bb9b9b9d9b9d9b9bb9b6b6d6b6b6b6b6b6b6d6b6b7bc3e3e7e73fe3e3e3e3e3e7ee3f7cfcfcfc3e7e3e3e3cff3cffffcfcccffffcf
    3eecfec3efcf3fcfcfcfeeeffffffcf3cfeee3fcff3cffcffcfff3cf3fcf3cfcfc3c3ee747e7c6bc7cce3e3c796b6b6b6b6b6b6b6bb7bb6ec7c777c3c3b6d6bd97bdbd6b79bd9d97d9d9d9d9d9d9d9d9d9d9dd9d9d9d9d9d9d9b9d9db9b9d9b9b9b9b9b6b9b6b9b6b6b9b9d6b79b79b9b9bd6d6d6d6b9b6b6bd6b6b6b66b9b9d7b7e7e3e3e3e7e3e7e3ee3e7e3cc3e3ff3fe3c347c3ffffcfcf3fcf3ff3cffff
    cf3c3fcf3e3eeffffe7e33ffffcf3fcfe3ee7fff3cff3f3fff3cfcfcc3fcff3cfcffc3e3e77bc7c7c67cee3eb6b6b6b6b6b6b6b7b76b67b3c37c7e7e3ec7bb96b9b966d6d6d97dd9db9dd9d9d9d9d9d9d1d9d9d9d9d9d9b9d9b9d9b9d9d9b9b9b9b9b69b9b6d9b9b9b9b6b6d9b9b9bd6d79dd69b9b9b6b6b966b6b6b6b76b7d6b77d7747ee7e7e3e3e3e3ee7c3e3efcf3fc3cfe3e3ceff3c83fffcffcfc3ccff
    3cfcfe3ecc3c3ec3f3fecee7fffffcfefeeeef3fcf3fc3cf3fff3f33fe3c3cff3c3cfc7e74c7c7b6c7c6c7c3bb6b6b6b6b6b76b67c7c7c77c7c7e7c7e3c76b7b97d6db79b9b7d9bd9bd9dd9d9d9dd9d9d9d9dd9ddd9db9db9b9b9b9b9b9b9b9b9b9b9bb9b6d6b6b6b9b6d9b69b6d96d9b9b96db9b6b9b6b6bb6b6b76b6b9b9bd7d474bd77e73e343e3e3e3e3ec3ee3cffc3ef3c3eccf3ffcfcfcff3fffffff3f
    fcfcf3fcfcfcf3ccfe3f3e75e3fcffcfe3e3e3cf3fc3cf3cfcfc3ecfc3cfcfc3fcf8ff7e773e3c3e7b6b3e3e3b6b6b6b6b66b7b3c7c7c3ec7f3c3c3e7e7bb79bbd6d69b6d6d6d79dbd9b9dd9dd9d9d9d9d9d9d9d99d9b99b9b9d9b9d9b9b9b9bb9bd69b9b9b9b9b9b6b9b6d9b9b9bd6b9b9bd96b9b9b6d6b6b6b69b6b79bd7d7777b7d5b747e7e7e3efc3e3e3be7ce3cf3ce7e3cf3c3fc3c38fffcfcf3fc3ffc
    ff3fcffe3cf3efc343efe3e7efffcfcfeceeeffcf3cf3e3f3f3ff3c3ffc3f3fcfc3fc3c3ee7ece7c6b6bbc3ce7b6b6b6b6b7b6c3c3c3fc63c3c3c7e777b79b6d679b9b6d6d6d9bd9b9db979d9d9d9d9d9dd9d9b9bdb9b9b9d9b9b9b9b9b9b9b9bd69bd6b6b6b9b6b9b9b9b9b6dd6b9d9b9b9b79bbd6b6b9bd6b9b6b6bdb7db74d44747e3477e3e3cc3e3eec3b3ee73ff3ef3efe3cc3cffcfcf3cff3ffcfcfcff
    fcffcfcffe3fe3ee3e3ecc347fffff3fcc34cf3f3f3c3fc3efc3c3cfc3fcfccf63ccfcfe3e3e33e7b7b67cc3c76b6b6b6b6c3c3cc3fcc6e3cc3c3e7e7e7bb9b6d9b7d6d6d6d6d96bd979bdb9b9d9d9d9d99b9b9d99b9db9b9b9b9db9bd9b9bd69b9b9b9b9b9b6b9bb9b6b9b9b96dd6b9b97d9b9b96b9b9b66b6b6b7b97bb77d7e77e747d7e75743e3e3ef3ee347cce3ffcf3e3ccf3fcf3f3fcffcfbf8f3fffff
    ff3fcf3cf3efff347ee3efcfeffcfcfefeee3ffcfcf3cf3cf3fc3cf3fcf3ff3cfcf3c3c3e7e3ecc7b6b6b6c3e7b6b6b6b67c6c3c3c3f3c3c3cf3e7e3e76b6b976b6d6d6d6b9b79b797b7979bd9bd9b9d9bd9b9d9bb9b9b9b9b9db9b9b9b9b9b9bd6bd6dd6d6d9b9b9b6d6bbd6bd69b97db9b9b96dd6b6b6bd6b6b7b7bb7b7be75e743e5e5d74e7e3e3e3c3e3be37cfcf3c3fbd3fcfcffcfcfffff6ff3ccf8fcf
    cfef3ffcffc3ee7e347e73e3ffffffcfc3eefcff3fcf3cfe3cf3c3cc3fcfc3fc3cfcfcc3cc7e63e7bb6b6b3e3c7c6b6b6b6c3fc3cfc8f3cc7c3cc37e3bb6b7bd6d6db9bd6d6d9b6bd69b6b797d9d9b9b9b9b9db9b9b9b9d9b9b9b9b9b9b9b9b96d69b9b9b9bb9b9b69b9b969b99b9bd696b9b79b6d6d9b96b96b76b67b77477477e757e734777e7e3ecfcf7e3ebc3f3ffeec7bef3cf3cf3cc8fcffc3cfffffff
    3f3cfeff3fffc3e3e3c3efcfffcf3ffcfeee3ffccf3cf3f3e3fcfcf3cf3c3ccfcf3c3c3c7c7cec7b976b6bcccec7b6b6bc7cc38fc3c3cc67cc677ee7c77b6d6d6b796b96b79b6b96b6b6d9bd9b9b9d9d9b9d9b9b9b9d9b9b9db9d9b9b9bdb9bbd6db9b9bd6d9b9b9bb9b9bb9bdb9b9b9bd9b9b9b9b9b6b796bb7b7b7b7b7e747e7e7ed743e7e3e3e3e3e3fe3b3e3ccf3f3e3e3eff3cff3cc3ff383fcff8f3c8f
    fcfffcfcfcfcfcfecfefc3fcfffffefcce3eeff3cffc3efe3cf3f3cfcfcfcf3f3cfcf3cc7c773e7cbd6b6b633e76b6b676b63cf6c6c6c7cc67bcc37e3cb6b66b9b6bd6b9b6d6d6b9b9b96b97d97d9b9b9b9b9b9b9b9b9b9bb9b9b9b9db99d6d99b9b9b79b9bd9dd9d9b9b9b9b9b9b9bd6d6d6db9b9b79bb6b9b76c7c7b7e77e7e743e757e3e5347ce3e3c3ce3e3fcf3fec3efc3cfc3ffcf6ccfcfc8f8f3cffc3
    fffeffff3fef3fe3e3fc3effffcffcfcfeee3cfcffcfcf3c3cfc3fff3f3c3cfcfc3cfc3cb6ebc7b79b9b6b7ce3bc6b6bb6bcc3c6c6c76c6c7cc7bc3e77b76b76b796b7d6b9b76d6b676bb7d6b7d9b9b9b9d9b9b9d9b9b9b99b9b9b9b9b9b9d9bd9d9b9b9b9d9d9db9bdb9b9b9b9b9b9b9d69b9b9b79bb77b9b76b3c7c7e7e7e734343cf7473e3e3e3e3fcf3ef3ec3fcff3ec3fc7c3cfc3c3fff83fc3fccfc3fc
    ff3ff3fcff3fcfe7cccfccffffffcffc3eeec3fccff3fc3ef3cffcfcfcfffc3f3fc3c3cc7c77b6b6b7b6b6b6c3e7b6b6c766c6c6c6c6b6b6b6c3c7e3cfc6b6b6b6bb96b976b9b6b9bb96b979dd6d9b9d9b9b9b9b9b9b9b9b9b9b9b9b9b9bd6d9d9b9b9b9d9dd9dd9d99b9bd6d9b9b9b9b9b9b9bd6db67cc7b9b3e7c77e7e7347e3e7c3ef7e3e7e7e3ee3ccf3efc3fcf3ce3eeff7bc3cfffccfffc3c8ff3f8fcf
    ffcfffffcffcf3ef3e3cf3effcfffcfcfe343effeffcf3fc3efcf3ff3fc3cfcccf3cfc3c6c7b6db9b9d9b6b6ec3cb6b6b6bb76c36b6bc6b6c63c3c7c3c3c76b6bb6b6b7b9b6b6d6b697b79bb679b7d7d79b9b9d9b9b9b9b9b9b9b9b9b9b9b9d9bd9bd9bd9b9dd9dd9bd9d9b9b9b9b9b9b9b9b9b9b67be7b9b7c3c3c7e7e7e3c3473e3c3f3e3c3e3e3e3ef3fc3e3fcfffc3ef3ecc7c3f3fc3fffffc3c3cffc3ff
    cff3fcf3fcffcffefee3efcffff3ffcfeeee3ee3cffecec3fff3ffcfcfcf3c3f3cfc3cc7c3cc7b7b79b79b6b63ec7b6b7bb6b6cb6b67b6c67cc3c7e7c3c3bc67c77b796b6bd6b9b7b6b6d6d6d9b9b9d69b9d79bd9b9b9b9b9b9b9b9b9bd6d9dd9b9d9b9d9bd9dd9dd9dd9b9ddd79b9b9b9b9b9b9db7c7bb79c3cf7bc7e73e3e3e7e3e3e3fe3fe7e3e3efe3cfcfcf3cf3cc3ccf7e7cfcf3e3ffcf3fcf8fc8fcff
    3fffcfcfff3ffcf3f7eefcffffcffcf3cc3ee77feff7f3ecfcffcf8f3c3fffc3fc3cfc7ccc3c7b9d6b9b9b6bcc3e6b6b6d6b6b76c6bc6b6bc6c3c3e7e7e3b7c7b7b6b6b9b66bd6696b79b79b6b77979b9b79b696b9b9b9b9bd9b9bd6d69d9d9b9dd9b9dd9d9d9dd9dd9dd9b9b99bd9d7d9b9dd9b9b9bb7cbb73c7c77e7c3e7e3e3c3efccf3e3c3efc3c3fcf3f3fcffef3ec3ee7fc7f3c3cfc3fccf3c3c3f3c3c
    ffcfffffcfcffffcfe3f3e3fffffcfcfecee3effcffc3f3ff3c3cf3fffcfc3fcfcfc3cf3f6c7cb6bdd6db9b67ccc7b6bb6b6b7b7b6c6c6c6c7c3e7c3c77c7c3c77e76b6b6b766bbbb6b6b6b6b96b6bd6b9b6dbb97b79b79b9bd6d9b9d9b9bd9dd9b9dd9b9dddd9dd9dd9bd9d9bd9b9b9dd9b9b9b9bd97c797bc7bcc7c73e3e7e3e3ec3c3fc7ffe3c3efe3fefef3cf3fee7b3fcce3cfcfcf3bc7ffcf3cfefcfff
    cff3f3fffff3fcff3cfee3efffcffcfefe3effcfff3efec3ffc3c3cc3fc3fcf3f3c3fc3cc3cc7cb976d9b79b6b3c6bb6d6b76b767b676b67b6c3c3c3c3cc3c3c3e7bc76b769bb9676d6d6b797b6bb6d7979b979b79b79b9b979d6d6d6d9b9dd9b9dd9dd9d9d9d9d9d9d9d9dd9d9b9dd9b9b9b979d99dd7c7bbd767c77ec3e3c3ec3cf8ff3fc3f7fef3e3fe3cf3efcfe37ccc3f3ecc3f3fcc7cb7f3cfe3fc3fcf
    f3ffffcf3fcff3fefe3f34cffffcf3fccceeee3cfcfcf3ccf3cfcfe3cffc3fccfcfcc3cf3c3c777bbd6d9bdd6b6c76b96b6c7c7e7c6b6cb6cc6c3cfcfc3fcfc3e7e76b6b6bb66bb9b6b6b9b6b6b796b6bd79b96d69b96b79bb6d6d9d9bd9d9b9dd9d9d9dd9d9dd1ddd9d9d9b9b9dd9b9d9d9d7b77d9b977e7b9bbb7c73ecc3ec3c3cf38fc83ffcf3cf3efef3fcf3f3fce3e7ce3c3fceeffffc67cc3c7efefcf3
    fffcfffffffcfeff3fece7cffcfffefcc3e3e3efffcf3fc3cfc3f3ecf3cfcf3fc3cf3cfcccc7ccc77bd6d96d9b6bbbd6b67c37c7c7b6b6c6b67cc3c3c3fc3c3f7e77c6c6b6bd6b66b6b6b66b6d69bb9b79bd6bd6d6d6dd6b9796d6b79d9b9d9d9d9dd9d9dd9d9d9d9d9dd9dd9dd9d9d9b97d666b6d9b7cb7bd7b79c7e3e3c3e3fcfc3fcf8ffcfc3c3ccf3c3ef3fcfe33f7bb7cfeffe7b3cff3fc3cfcbfc3c3ff
    cfcf3ffcf3ffcfcfcfe3e5fffff3fcffeecfcc3cffecf3fcfe7fe3f7c3e37fcfff3cfc3b3c3bc37cb79b9bd6bd6bd66b6bc6c3c6c6c76b6b6cc63c6c3cfc3c8e3e747c76b676b7b76b76b6b6b6b6b676d6679b979b9b6979b6bd6d9bd6d9ddd9d9d9ddd9d9dd9d9d9d9d9d9bd9d9bd9d9b67c67667b977e7c7bd6b7fcc3c3eccf3c3fc3c3cf8f8ffff3e3ef3ffcf3fec3ec7f3c3eebbcefffff3e3ff7efcfeff
    3ffffcffffcff3fcf3ef3cfffcffffe3c3e3eefcff7fce3f3e3eee3c3e3ee3fc3ccf3cc3cc3c3be77b9bd6d9b9b76b6b67c3c3c37c7c6b6cc76bc67b8383bc37e777e76b6b6b96d6d6bb6b6b6b6b6b6b6bbd676bd7d7d6d6d79b79b96d9b9b9bdbd9d9dd9d9dd9dd9dd9db9d9d9b6d9b77b63c67c6b7b7c37c67b7c73c3ec3c3cfccc63e3c3f3f3fcf3efc3ef3fcf3c3f7c3cc3fe7be3fcff8fcffcfec3f3c3c
    ff3cfff3fffffcffcf3efeffffffc3efee347e7fcfc3c3ccc3e33e7efce3e7fcf3fcc3cc3cc3c37cbdd6d9bd9b9b9b6b6b6f3c3cc3c7c6b67b66bc6ccc3cc3ce7e746bc6c7b6b7b6d6d6d6b976b7b79b7966bb6d6d9dd6dd69b9bd6b9b97d9b99b9bdd9ddd9d9d9dd9bd9d9dd67676d6c667b6c677797c67c3e79c6c3cc3c3e3c33f3ee3b3bb7dce7ec3e3fe3fcf3efefe3e3feccd7bfcf3ff3ff3feecfffc3c
    ffcff3fffff3fff3eee3e3ffcfcffcfc3ece5e343fffcc3ffc3ec3c73e3e7e3c3cc3c3e3c3ccec7b79b9b796d79b6b6b6c3c83c6c3c63b6b6cb676c63c6c67c37e7c77c76b6b7b6b7b76b96b6b96b6b6b6b76b67967b9b79b79b979d97d9d9dbd9d979b979dd9dd6d6d9b9c66c6c6b7667c663b6c6cc67fc3c6cc7f3c3fc3ce3ffc3e37b7d74d7dd7d3e3e3cfcfcfc3f3e3fec7ffed7cffcffc3efcc3fcc3cc3
    fff3cffffcfffcfc33ecfee7e3ffcfcec3e3743efcfe3fec3cf3fe3ee3e34343fc3c3cc3ce3c7c7bb79b6bb7b9bd6b6b76c3c6b3c3c7c67b6c6cc67c6c6e7c7cc7b7cb6b6b6b6b76b6dd6b7b6b6b6b676b6b6b7bbb7971b79b79b9b7dd9b7d797b7d6b6d9b76b79c7b7b7663c66676c6c36c7c6c7636c63c3c3c783cfc3cfc3cc3fe7d5b5d7d5d57474becfe3ff3f3fe3fe3f7ff3fbcfffff3cc7cfe3c3ffc3c
    f3fffcfffffcff3ffe3e3e7e3ebefc3cee3eecffffe3fe3cf3cc3ee3e7e3e7e3cfcfc3cc3c7c7c77b6b6d66cc7b6b796b66b6b6cc3cc7b6b673c3b6c7c76b7b3e7c7b7b6b67b76bc7b76b76b9b6bb6bb7d76b6966d6bd979b9b97d9b9b9d9d6b976b66c676b6b6b6767d6c3b67c3c3c36c6c6766c38c3e7c37c73cc3c3f83cc3ce7c34dddd5e7ee75d777e7e3efccfcfc3fc3ff3fc3e3ffcffc7fc3efccffffc
    ffcff3fcfc3cfcfefcefef75eff3fce3e7eff3fc3c3ef3e3cc3fc3c3c3e3e3743f3c3c3ec7c7b7cb9b79c7c33c7e7bd6b6b6b6b6c63c7b6bbcf3ecc7b6bb6b6b7c7b7b7b7b6b6b6676d6d9b6b6b79676c76b6b6b79b67dd6b79bd6b97d7d76b76b6b976c6b6767c76c6c676c6c36b66c83c76c63c3c3c7e743e7e73e3c3fc3be7c3ddd7d5e77437ee74b74343e3f3f3cfc3fe3cfcc3cfff3f7cf3efe3c3ffff3
    fff3fcff3ee3fffff3c3cf3e3effff343e3fffcffcfe3ecf3fe3fe3e3e3e3ee77cc3cfc3e3eb7b7b76bc3fffc33e37bb6b7b6d6b7c7b6b96c7c7c76d6b6b79b6b6b7e7b67b76b67cb7b76b79bd6b6bb67b7b6b7b6bd6d6b9b9b79b9b9b9d96b66b66c6c76c6cc67b63c3cc63c6c6c6c636c36c3c86c37e7e7575747e7e3cc7e7e7e747e7e747e7e3e3ee7747e3efccf3cfef3e3f3cfc6fffc3c3cfccfcfcfcff
    cffcffffff3e3ef3ec3feffe3fcfcee3efcfcff3fe3fcf7fe3fec3efcfe3e3c3e3cf3c3ec3c7b6b6dc63fc3f3e3e7e779b69b6b97c67c7b6c3e77bb6b7b9b6b7b67c77c7b6b7b6bc6b6bd6bb6b7b7d3c7c76b6b6bd6b6d7976d6d6d97d76b76b6c76766b67c767c3c6c663b6c63c3c6cc66b676c3c3c7e57e347e3e73e7f7e77747e7b343e3e7e7e3e3ce7e3e3e3f3fcff3cfc3cf3f3cfc3c3fcf3c3c3ffffff
    f3fff3fc3c3ee3ef3fef3ffffffff7ee34347ffefcccf3fefc3f3cf3e3c3fe3e3e3cfc3e3e7b6b7b63fc3fc3fc3c37eb6d6b9b7b79b7b6c3c63b7b76b7777b79cc67c7c7c7b6c7c7c76b7b7d696766c63c7bd6cc66b796bb9b6d9b7d9b9b6b6c66c6bc67b66b6c6c63c3cc3c3c6c83636c7c7c7c36c3473e3e3e7e3e3e3c374d47b743e3c3e3e3e3cc3cf3e7e3e3fcf3cffff7fcfccf3c3c3fcfcfeefef3cf8f
    fffcfff3ecc3e3e3ee3ecfcffcfcfc7ee7c3ef3cfe3fce3c3fe3fe3e3e3e3e3ee3ec3cc3c7c7db9c3fcffc3cc3c3ee77b79b776b7b7b3f3c3ec7b6b76c7c77b776e3bc6c7b7b767c6bb796b6db7c7c3c3c767b63bc9bb96b6b9b6d96b9b76b66c76b67b6b7b7c7c63cc838c36c3c3cbc3c766c76ccc73e3e7cf3c3e3e3e34d77d74e3e3e3ef3cf3e3ef3e343e3e3fe3fffcff7f3c3c3cf3cf3f3cfcffcfcf3ff
    c3ff3fce3c3e3e3e3e3fe7e3fcffffe34fffe7e3c3e3c3e3cf3e3e3ee3ee3e3e7e3e3c3ec7b7c7b6f3c383c3f3e3e737bb76bc7c7c7cc3cc3c7b67bc7c7c77e7c7c637c3b767bc6c767bbb9d6d6cc3c3c7c7b6cc6e76b6b97b7b9bb9b79b66c6c6b7b76b77b6c63cc383c83c83c8c66366b7c767c37e3ef7e3ff3e3e7f3b7474de347e3cf3ff3cfe3e3fefe3e3ee3fccffffc3cffc3fcc3e3fef3c3e3e3c3ccf
    3fc3fc3e3e3ee3ec3ee3e3eee7ef3e7e3ef3e5eefecfcefe3cce3ef3e3e3e3e3e7e3efc3c3ec7b7c3fcf3c3fe3e353477cb763c63b63c8f3c3b6eb76c767b73c3c7ebc3b6b7b6c7ccb6b6b6d6d67c6c3c63cc3cc3c6bb7b6b77b797b7b66bc767c6c76b7b67b3c63cc38c3cfcc3c6c7cc7c67c7c6c37ef3e3efff3c3c3e7e7d753477ee3c3cff3c3e7fe3c3e3e33ef3cfffffcffcc6c3cc3ccfccfee3ccfcfff
    fc3fcfe3ee3e3e3e3e3e3e353e7ee347e3e3e773fe3c3e3c3c3ec3ec3e3ee3cc3e3e3e3cce3c76b6c3c3cfc3c3e3ee7e777cc63bc3cc33ccccc767c73c37c7e3b7c777c7c3c67c6767c7b7b9b6c33c3c6cc7cc3c6cc6b96b7c77b76d6d67c66c6767b6c6cc767c3c6cc3c83c3c3c3c367c3e77e7c7bc3c3c3f3ffcff3c3e7474347743e3fcf3cc3e3e3ef3ec3ccffc3f3ff8ffc3c7b3cc6c7fe7e3e3ef3cfcff
    3fcf3c3e3e3ee7c3e3e3fee3ee3e3ece3ecf347ef7cc3e3fe3f3e3e3ee3e3ef7e343e3cf3e37b7c3f6b3c3f3c3e33e77e3e63cb76c73cf363c7c3c3cc7b77e7c373e77c3cc7cb6cc3c6c667b7c7ccc6c3c3c77b6e7c7b6b76b676b7b76b6c767cb766b6c76cc6c6c3c3c6cc6c67c3c7e7747e7e7c63c3c3e3eff3c3efe347747e34e3e3cf3ee3ce3eec3cfc3cf3e3fecfffff3ecf7ccf67bbc3e3ee3efcf3ffc
    ff3fcf7e7cfe3c3eee3ecff43ee343e34f3efcc3cef3e3e3efe3ec3e3e3e3e3c3e7c3ef7c3cf7b6fc3cffcf3fe3ee3e7e73e7b6b6c6c3cccc3c6cc3c3c7cc3e3cc3e7e7c67c7c3b6c7b7b7b6c63c3c3c3cc76c777b79bb9b9bc77b76b7c76b6b66b6b63c67c3c63cc6c63c7c3c3e7e75e57e757c3e7cc7e3fc3fc3e3c7e7477e3473e3e3ce3cf3e3c3eff3cf3e3fc3f3fcfcce3e3e6cffc7b7c3e3efe3ffcffc
    3fcf3fc3ff3e3e3e3c3fcf3ee3e3ee3ee3ef3ffefc3e3ecf3e3e3ee3ee7e3e3ec3efc3e3cfc3c7c3f8f3c3cf3c3f3e775343c76b7c63b63c3c63c38c3c67c37e3fe3c77e3c7c6c7c3cc7c3c3cc7c63c3c67cc7cbc7bc79c76b6c7c677c66b6c76c6c6c67c6c63cc3c73cc3c3cc7cc7e77e753e57473e7c3fe3efc3e3c374747343e7e3cf3e3c3e3e3e3ffffffcef3cfcffff3efe3e3bf3cc6e3e3ec3effffc3f
    fcf3cfefffcf7ce3e3e3fef3e7ee3e53e43eecfc3fefe3e3c3ee7e3473e3e3e3e3e3fcfc3e3ec3cf3f3fcf3cf3ec34343477c67c63bc3cc3c3cc3cc3b63c3e7cf6c3c3b7c6c7c6c3b63cc77c3c37cc3cc3c7c67c7c7b7b7b77d6c3cc67b7676c67c63c6c73ccc3b6ccc3cc6c3c3c77e347e7475375475fe3e3e3fe3c3e7e774737e3e3e3e3c3e7e3c3e7cfcf3f3feff3fcffe3e3e3ecfff3cf3fece3fcfcffff
    f3fff3f3ffffc3e3ecfe3fc3e3efe3e47743cff3efe3e3cfee3e343eee7e34c3cf3ef3e3ec3f3f3fcfcf3cff3c3e3e3e77e73ec6cc3c3c3cc3cc83c3c3ffc3e3cf3c7e3b73c673cc6cc3ccc7c7cc3c77bc3c7cc7c7c6b63c6c776c773c7cc676c67c6c63cc36c6c373cc63c3c6c3e7433e757e34e77e7e3c3e7e3e3ef7457434e7343e3eee3ee3fe3fcf3c3eeee3f3cfcff3ee3ee3e3ffcccec3e3fecfff3fc3
    fcfcfcffcff3e3ee3e3fcffcfe3c3e3ee7e7fcfcfe3e3e3c33e7e3437e3ee3cfe3c3efe3f3cfcfcf3f3cf3c3fe3e343e7473e3c33c6c3cc3cf63cc3c3c3cf3e3c3c3b7e7cc3ecc3c3c3c33c7cc3cc7cc77bc7c7c7c7b7b7c3c6c73c7c7673bc77c663c6c6c6c3c7ccc63ccc7c3cc353e347e3e3e3e3e3efe3e3e3e3c347e7e73e7e7c3e3e3e3ff3cfe3fcff3e7cfcfff3ffc3ffe3efff3e3f3fefcf3cf3fcfff
    cf3ffffcffffe3e3e3ef3fcf3ffffe35343e3fc3fec3fc3ece3ee7ee7ef3e3e3ffe3e3ce3ef3cf3fcfcf3f3e3c3e3e3e37e7c3ccc3c3c3c83cfc3c63ffc7e3cc3ffcc777c3c36c6c3cc6cc3c3c3c3c77c7b7c6c6c7c6c6c6c3c3c67c7c7c767c63cc6c3c3c3cc7c3c3cc3c3c3c3c7e3e753e7e3e3e3e3c3c3ee3ec3f74757e3e3e3e3ec3e3cfcffc3cfff3fcf3e3fc3fcfffffc3eff3ccc3eccf3fef3ffcf3fc
    ffcf3cff3fcf3e3e3cffc3fffe3e3ecee74ee3fef7fcf3cf3e7e343e3e7f3cfe3ef3cf3fc3cf3fcf3f3fcffc3fef3fe3e535cc3c3c8cc3c3bc3c63cfc37c7c37ccf3fc7c3c3c37e3c3c3c3cc3cc6c6c7c7c7c73e6c3c7c3c3c3c3cc63c6c7cc7cc673c6cc6c63c6cc63cfc3cc6c3c3e3ee3e3e3c3ef3e3ce3e3fcfc3e7e7e7e3e3e7f43e3cf3fc3ffcf3ffcfccccfffcfcfffffff3cc3c3efcfcfc3fcffcfcff
    f3fcff3fffffe3e3cf3cffc3ffffc3e3e5774e3cfe3fcfc3e3e343e343effc3cf3fc3efefc3ecf3fcff3f3f3fe3ce3e3e7e73e3c83c37cc7c6bc3c3cfc77c3b7c7fcfc3be3c7bc7b7c3cc3c6e763c3c3b3b7cc63c7cc3c77bc3cc337c3c3c76363c6c3c73b7cc7c3c3cc36c3c3cc3ee7e73e3efef3ef3fe3e3ff3f3e34343e3e3e3e347c3effffcff3ffcfc3ef3c3cff3fffcfc3cf3fcecf3c3fefcffcf3ff3f
    ffff3ffcffcf3c3cffcf3ffefc3e3fe3e34734f3ecfc3fc3434343ee3ef3c3c3cf3ffc3cf3f3ffcff3fcffcfffe33e3e35343ec3cc7cc3c3c377c7ff3c377e777c3f3c3e77cc3c37b3c3cc3c3ccc3cc3e7ec7ccc3c6c7cc76c3c3ccc7c63c3cc6c3c6c7c7c3c73c3cc3cc3cc8c3ce7757e3ec3f3cf3ec3c3ec3fefc3e347e3e3fefe7e3fe3f3f3fcfcfff3ecf3eefcf3ffffff3fcec3c3cccfef3ffc3fcf3fcf
    fcf3fcfffffcfcfff3fcfe3f3fcfe3ee343453fe3ef3cfe3e343ee3ef3fffcff3ecefff3fefcf3f3fcff3ffc3f3e3e3e3e343e3c3c3c3cf3cfcc7c7fc3cc3ccc77bcc3c7c77c3cc3be7c7c7c7c3cc37b77b7c76c7c3c67c7c7c83c3637cc63c73c6c37c3c3c3cc3c7cc3cc63c3c37e343e3efe3cf3f3cfcc3fcfc3c3e343e3efc3c7e7e3effcfcff3fcffe3fffcf3cfcfcf3ffcf3efcfe3fc3fcfcf3ffffcfff
    f3ffcffcf3f3f3cfc3ef7fccc3c3e3e7eee347eefe3cf343ee7e3e3e3cfc3fcff3f3c3efc3cffcffff3fcfffc3fe3c3e7e3477c3cc3c3c3cfc73c3ef3cffcf3c3b73c3c3c3c3c3fc3c3b77c7c37c3cc3cc77c37c6c7cc6c67c3cc6cccc763c7cc3c7c7c3cc3c3c7c3c3c63cc3cc347e7e3e3e3ef3ecf3e3e3f3fe3e3ee7e3e3cfe3e3efc3c3cff3fffff3cffff3efff3fffcfff3ec3c3cfe3effcfcfcf3fffcf
    cfcfff3ffffcfcf3cf3c3c3fefc3ee34357ee775e7ffcf7e343e34fcfcfffcf3fcfcfe3cf3ef3ff3fcff3f3ffcf3fe3e3c3e7e3e37c7c7fc3fc3f77cc3c33cf3e3c3cfc3cc3cfc3c37c3fc777be7c7cf3f7b3bc7c3c63c3cc7c3c3c363c7cc767b7e7cc3c3c3c3c3c6c6cc3cc3c7e77e7e3e3c3c3e3ef3e3ecc3e3e3e7e7eff3c3e4e3e3cfcf3cfffcffffcffcfcfccfcfcff3cfe3efeffcecff3ffffcffcfff
    fff3fcffffcf3f3cfcfefc3ef3ec3e3ee3434ee7ccf3e3e343ee3c3cf3fcfffcff3f3e3ec3effcffff3cfcfe3f3fcfe3ef3e3e73e7c3cf3fc3cfece7377be3cc3cfc33fc3c377c7cb7c3c3cc773b7c3cf7b3ec3cc6ccc3c3c6c6c67c7cc3c3c7e73e77c3c3cc3c3c3c3c3c3c3cc73e7e3e3ce3fcc3e3e3ee3e3c3e3e347c3cfe3e3e3e3cff3ffffcff3cfcf3fcfffffff3f3fffc7bbeef3f7c3ffec3ffffff3f
    3ffcffff3ff3fcfc3f3e3ecf3cf3fee3e34e75e3e7fc3e3e343ee3ffcf3f3fff3fcffcf3e3e3f3fcf3ff3f3cf3cf3e3e3e3e7e3e3f3f3cc3ffc3c33ee3e3e773cf3c7c3fc7bec3c3c7cfcf63e5e3c3cc37ec7c6c63c3cccc6c3c3e6e67c7c3c77e7c3e3cc3c3cc3c3c3c3cc3c83fe3e7c3e3e3e3feff3f3e3fe3e3e3e3e3cf3cfee7e3ef3fcfc3ff3fcc73cffc3fcf3fcfcffcf7cbefcfccc7cfcffcfcfcffff
    fcff3ffcffcfcf3fcc3e3c3fcfcfc3e343e75e7eee3fe3ee7e73fccf3cffcfcffffcf3ec3e3effffffcfcfc3fc3e3e353e3e3473e3cc3e3fcffcfcf3ccfcfc3cc3cc3bcc3e77c3c3c3c383ee737c3b6cc67cc6c7ccc6c63c7cc7c63cc7c777e7e3e3b3c3c3c83cc3c3c7c3c6c3c7e7e3cfc343cf3f3efe3ef3fcfc3e343e3efe3f343ee3fc3cfffcffcfee7ff3fffffcfffcfffbc7bcf3c3c3fcffffff3ffcfc
    ff3ffcfffffffccf3e3efcfe3c3cfe3ee343e743e7ef34347e3ecffcfcfffffffcffff3ee3e3cf3fcf3ff3fff3ccf3e7e3e3e3e3eff3e3ef3cff3cfc33e3f3c3e7f7c3c3c7e77c3cfc3ccc3c347ce6c763c3c63c637c3cc6c3c6cc7c637e7b7e77cc3ec3cc3fc3c3cc7c3cc3cc3cc3e3e3e3e3efe3c3c3c3ec3f3cf3e7eefcf3e343ee3ffcfffcffff3c3dcfcffcf3cf3cff3fc3ccf3cf8c3fcf6cff3fffffff
    ffffcf3c3ff3ff3fe3fc3c3cf3fc3fe3e7ee3ce5ee7ce3e3e3ecf3ff3fc3fc3fcff3fcf3cc3efcfffffcffc3fe3e3e347e3e3e3e3f3c3e3e7e3cff3fcc3cfcc7c7c7c3e3c7347ec36fc8f3c3b747c7c6ecc6ccc7ccc7b67c7c6c3c67e7b7e7e7e73e3c3c3cc73cfc33c3b63c3c63e3e3fe3e3e3cf3feffceffccc3e3c3e3c3fce7ee3eecff3cf3ff3fced7ff3ffcfcbcff3fffbfbbffc3c8c8fccf3ffcffcfff
    3fcf3fcffcffcfffcfe3cffe3ecfc3fcf3e7e3e7e7c3e34343e3cfcffc3fffffffffffcf3ef7fff3f3ff3ffcf3fcf3e7343e7e3e3e3fefcf3ecc3cfcf3e7c3f7e3e347ce7b7e77c3c3c3cf8c7e77c67c67c37c76c7c6c7cc6c7c7c7cc7e37e73ec3cc3c3c33cc3c7cc63c3e6e7c3b3e3e7e3ecf3fcf3c3f3cf3f3e3e3e3efef3473cfe3c3cffffffcff7ccc3ffc3c77c3fffccc3b3cfccf3c3c3fcfffffffffc
    ffffcff3fffff3fc3f3fcfc3fc3fcffffffce7e747e3e3e7e3effff3ffcfcfcf3fcfcffcf3ecf3ffffcffcf3fcf3e3e347e3e73e3cf3f3ffc33fe3c3fe3cfc3e7fc7c73f3e77e77e3c3cf3c3e77b7b67c67b6b6b7b67cb67c7c6b6bc777e77e73cc3c3ec3cc3c7c3c3c3cc73c3c3e3ce3e3e3e3cf3fcfcccfcccfcf3efc3c3ee3ee3e3eff3fcffcfffff7f3bff3fbcecffcfe7fbc3fffcfc3cfffcfcfffcffff
    cf3ff3fec3cffffffecfff3fefc3fe3e3e3e3e343ee7e343ec3cfffcff3cf3ffcff3ff3ee3ffffcfcff3ff3fcf3c3e3e7347343e3e3cffc3fcf3fc3ec3c33fe7c73c3cfc3c77e7e7f6c3c8f3c3eb6bb6b7cc76b7b6bb67cb6bb7b76b7b7e77ec3c3e3c3cc3cf3cc3c3cc33cc3c3c3c3e7e3ef3ef3fcfcf3e3c3ff3e3c34fcc3e3e3cfe3cfcff3ff3fcfccffe7bcfcf3ffcfccfc7cfcff3ffcccfc3fffffff8ff
    f3ffcfcf3ff3fcffff3cffec3fccf3cfcee3ece3e7ee343ef3ffc3cf3effcffffffffff3cfe3ffff3fffcfcff3cfe3e3ee743473efc3cfff3c3cfce3e3eec3777cf3c3c3fcce7e7c7c3c3c3cfc7b79b7c63c7b7b6b6bb6b7b6b6bbb7b7e7e73e3cc3ccf3cf3cc3cc3c3c3c3c38f8ff3e73e3ec3fecf3c3fee3efcfcf3ec3fe3e3ffc3eef3fffffffff3ffe3fe7ff3fffffc3fcf3c3cffcfff83c3cffcff8ffff
    cffcff3fcffcffffcfcfff3fcf3fefc3c3fe73ee7e347ee3efefec3eecfff3fcfcfcfcffc3ffcf3ffcf3ff3fcfc3c3e3e73e37e3f3ff3fffcfef3e33c3e3ccfe77cffcfc3c33e737c3cfc3cc3c3bb7b67c7c6c67b7b7b7b6b7bb797bb7737cc3e3cc3cc3ccc3cc3cc3cc6cf8f3c3c3c7e3ec3cf3e3effee73e3f3f3cfe7fc343fcfff3e3fcffcffcfc3e3ccc3efffffcf3fcffcfc3cffcffffccffcfffffffff
    3fcfffcff3ffffffff3fffef3ecf3fefce3e3473ee7eb7eee3e7ceec3e3efcfff3ff6f3fffcffffcfffcfcf3ff3fcc3e3ee7e7e3ef3fcfcff3cff3ecfe3cf3f3e7e3c38ffcfe3e7c3e63cc3c3e3b79bc6c3c3c7b6b6d667b7d777e7b77e7e3cc3efcc3cf3c3fc3cf6c3c3c33c3fcf8f7e3efc3ee7e77e73ee3efcfcf3e7fe7c3ef3cce3fffcff3ff3ec7cfffffc3ffff7bcff3f3c3cffc3ffcf3fccffcfffcff
    fcff3fc3efcfc3cffffcffc3fc3ccf3c3fc7e34b7e7e343e34c3e3e3eecffff3ffcfffcfcfff3ffff3f3f3fcffcf3ce3e73e73e3e3cfcff3fcf3c3e3f3f3fcfc3e7e7c3f3c3c3e7e73e76c3cc7c7b677c3c6c3c637b67bc6c7b7c7c7c7e3ec3cfc3c3c3cc3cc3fc3c3c3c3cf8c3c3c3e3e3cfe3e75e7e3e3efe3e3f3e3e3fe3ef7c3c3eefff3ffc3e7bcff3fcffefffccccffcfc7cffffcffcfffcffcffcfffc
    ff3fffffcf3fffffffffffcfcfef3ccfcf3fec347e7ee7e7e3ecfffe3e3ec3ffcff3fffff3fffcf3fcfcfcfff3fcf3c3e343e7e3ef3f3cffc3c3ec3ecfcfcf3fc3e7c3fcc3fc77e7e7cc7c63c3cc7bc3c63c3c63cc7cc73c7c77c3c3c37c3ec3e3e3cfc3cc3cc3cc3cfc8fc3f3f3e7e343ef7f3473e3ee3e3e3e3ece7ee3c3e3ecfecef3cfcfcffcfc7ffdefcf3effff3c7cff3bccf8fc3fc3fcfffcf3ffffcf
    3fcffcfffcfcfc3cf3ffcf3cfe3fef3cfee3fe3ec7534743ee3e3e3fefc3cccffffcff3fffcffffcff3ff3c3fcff3fc3e3c3e3c3c3fcff3ffffc3ce3c3f3ffc3fc3c3ccf3cf3ec77c763c7cc3c7c63b7c3b7c63e63c63cc3c37c3e3c3ee3e3e3cc3cf3c3cfc3fcfcf83c3c3c8fc73e73cf3ef3e3e7e3e3e3e3efc3e7c3e3ecc3f3c3f7cfcf3ffff3c7ff7c3fcfccffcffffcffcc63ffc3cefcffc3f8fc8fcf3f
    cffffff3ff3f7cfffffffcf3c3efc3cf33ce3ce73ec3e34e3ec3effcf3cfff3cfffffcffcfff3fff3ffcfffcfff3cfcff3e3e3e3eff3fcfcf3fff3f3ec3cf3ffc3e3c3fcf3cc37f3e3e6c63cc3c3cc767cc63ec6c3c3c63c7c3ec3c3ec7ec3cc3cc3cecc3c3cfc3c3cfc3c3c3c3e73ef3fe3ee7e3e3e3e3ecc3cfe7c343ef3efe3efccfc3feff3fffcfffcff3eb7ffffcfff3c3fccfcc7c3ffc3fcff3ff8ffff
    cff3fcfe3ffecf3fffffffcfcfcf3efceff3e3fee3ee747ee3efcf3fcfe3ccffff3ffffff3fffcfffcf3cffff3ffcf3c3c3e3e3e3cfcfff3ffc3ffc3e3cffcfcf3eefcf6c3fc34c3cfc7c7c3ccc3c3cbc63bc63c3cc3c3cc63e3c3cfc3c3c3e3f3cc3c3c3ecf3cc3c83c3c7e3c3e3e3cfe3e3e7e3e3efff3cf3f3e3e7ec3ec3f3e3e3f3efcf3fffcff3fcf3fe7bbcffffffc3ccf3c3c7cffcffc83cffccfffcf
    ffcffff3cfcf3fcfc3ffcf3e3efcfc3f7f3fe7e37e734747ee3e3ceff3feffcfcffcf3cfffcfff3ffffffc3fcfcf3cf3fcfe3e3e3f3cf3fffffcf3fc3e3fcfc3cf77ff3ffc3c37cf3c3c67cc73cc6c763c7c7c3cc36c83c3e3e3cfc3c3c3ec3ccc3cfc3cc3cc3c3cf3cf7e73e73e3cf3f3ee74774743e3ff3ecfc7e3e3e3e3efcce3ecfe3cffcfcf3ffcfcffc7bbef3fff3cccfc3fccfcfcfffcf8fcfffcffff
    3fffffcffcffc3ffffcfffc3fef3efcfcfcf3e7ef343e7475ee3eff3fcfc3e3ffffffff3fff3fffcffcffffcff3cffccf3e3e3e3e3c3fcffcffffccfcfcf3f3f3cc3cfcc3fc3ee3cf83cc3c3cc3c3c3cc6c3c6c63cc3cc3c3b7c3c3c3e3c3cf3fcf3cfc3fc3cfcf8c3c3c3e7e3e3e3cfc3e73e7e747effcfcf3ffc3e3e3effc3e37e3c3effcffffcfcc3fcfffebb3ffffcfc3fffcfcf7ff3ffffc3c3ffff8f8f
    cff3ff3f3ff3cce3cffff3fec3ffc3f3cf3fefe7e3e3e347474ee3fcfffe3cfef3fcf3ffcfcfcfffffff3ffffffc3f3fe3e3e3e3ef3cffcff3fcf3f3f3fcfccfc3ee3cf3c3ce77cc3fc3cc6c3c3c3cc3c3c6c73cc3c63cc3b3c3c3cc3cc3c3cc3c3cf3cfcfc3c3c3cc3e3e73e7fe3c3f3e3ee7e3e3e3e3ff3fcf3c3effc3e3e3b3ec3ce3e3ff3ff3f3fc3fffc3bbffcfffc3fcff3cfcffcfcffffc8cf8fcfffc
    fffffccffcffff3fffcfcffefec3fccf3cfcf3e34e3ece5e74774cffff3cefefcfffffcff3f3fc3ff3ffcfcf3fcffcf3c3e33e3e3e3cf3ffcffffc3efcff3f3fcf37c3cfcc7fe7c6c3cc63c7c3ccc3c83c3c3cc67c63c3cc3e3ccc3c3c3cfc3c3cc3cfc383fcc3c3c3c3e3e3e3e3fcfcfc3e3e3f3e343fcffcffffe3cffcfc3ee3e3e3b3effcffcfffffcffffce7fffcffcfffffffc3ff3c3fcfff3ccffffcff
    f3fcfffcff3fcffcff3fffc3cf3eef3fef3fce3e3e7f3e3474347efcfffc3e3ffffcfff3fcffcffcffcffffffffcf3fcff3e3e3e3e3cfcf3ff3f3ffcff3ffcff3ee7ec67c773e7777b63e7c3cc3c3c3cc8c6c63e63eccc7c3cc3c3c3cfc3c3cfc3fc3cfcfc3c3fcc3c7e3e3e7e3c3f3f3cc343cffe3cf7c3ff3fc3cfc3c3fcc37e7cc343e3ffcfffcfcfffcff3ccfffff3ffcffcffeffcfcfffffcff3fcff3fc
    fcffff3fcfcfffcf3fccfffc3efcfccf3cfe3fee7fe3e4e7e5eee7ef3fffe3fef3fff3cfcf3cf3fffffffcffcff3fcf3fc3c3ef3c3e33f3fcfcffc3f3ffcf3fcf3c77c7b7cc77bc7c7ec7c7b7c3cc8c3c3c3c7c7c7c7763c73e3cfc3c3cc3c3c3cc3fc3c3cfcc3c3c3c3e3e3e3f3fcfcf3e3e3fcf3e3ee3eeffcfcf3cc3e3c3e3c3e3e743cf3ff3fff3fcffcffc3fcf3fcfcf3f3f7fcf3cffcffffffcfffff8f
    fffffcff3fffcf3ccff3cffcffef3e3fcf3cff73e3ec734343e5e3e3ffcf3efcffffcff3f3fcfcf3cfff3fcff3ffcffcf3fc3c3c3c3cfcfcf3fcffccfcfcfcf3e3ee79b66c3ec77e3e77b77e7e7c3cc6c6c7c7c6c3c3cc3ec3cc3c3cfc3cfc3cf3cc3c8fc3c3fc3c3c3e3e3e3e3cff3fcf3e3ef3fecc3ee3cfff7c3fe3ec3efec3e3e37343feffffcffffff3ff7efffffcf3cffcfcfffcfffffcff3fffffcfff
    f3fff3fcffc3fffc3e3cffffeffccfcf3efcf3efe3fcf4feee3ee43efffffc3fcfc3fc3cfcf3ffcfff3ffff3ffcfff3fcf3fefcf3e3c3f3fcf3f3c3fc3f3cfc3cc3b76b6c3c7c7b7e7c77c73e7ccc3c7c7c3c7c7c7c7c7c3c7c3cfc3c3c3c3c3ec3fc3f3cfcc63c3cfc7e73e3cffc3ff3fec3cfcf3ffe3e7ef3fc3ec3e3fef3c3c3ecee73ef3fcf3ffcf3cfcffe3ffffc3fff8ff7f3fcfff3fcfffcfff8fffff
    fffffcffcffef3ffe7ffffcf3ffffcfcfcf3fe3e3ec3ee3c3e4343ecffffffefff3fcf3ff3fcf3f3fffcfcffcffcfcff3fcf3c3cf3c3ecc3cfcc3fc3ec3c63c3e3e7b967c63c7c7c3e3e3e3e7e77c6cd6c7c6c7c7c6c63cc3c3c3c3fc3c3c3cc3fc3cc3c3c33e3e3cf3e3e3cf33cfcfcfc3e3cff3fc3fe3e3cfece3ccccf3fcfffe3c33e3b3effcfff3ffffcf7bcffcf3cfcfffcfcfffffffffff3ff8ffffffc
    ffcfffcff3efffcf3fcff3fffcffff3f3cfefe3fe3fe3fcfefe3eeeef3fcfff3c3fcf3fcfcffcffcfcffffcffc3f3ffcff3cf3f3cc3c33c6c3f3cfe3c7b6cc3fe3c6b79c63c673e73e37e7e7e7c7cc7db7c77c3c77c3ec3cc3e3cfc3c3cfc3cfc3cc3c7cc3e7c3cf3cf7c3e3e3ef3f3ffe3e3fcfcffc3e3ffcf7c3e3e3fcfcf3cfc3ec3e3ecf3efcfcfffffefe7ffffcccf8fcf7fffcffcfffcffcfcfffcffff
    ffff3fffffff3fffcf3cffcfcfecffcffe3fc3ee3efeee3e3fee7e73effff3ffcfcf3fff3fc3ff3ff3fcf3f3ffcff3ff3ff3fecf3fe3cf7cc3ee3e3c3b6b3cc3fc3e6c7c3c3ec7e7e3e3e3c373e76b79bc7c7c7c6e7c6c63c3cc3c3ccf3c3c3c3c3c3c3e3e7e7c3cf3cf3e3e3cf3fcfc3e3ee3f3ffcfcfee3e3e7ece3c3fcf3ffc3c3ff3cf7ffff3ffffcffc3c7cf3f3f7ffc3cfcfffffffffffff3fffcfffff
    cfffcfcf3fcffcff3fcf3cfefe3ecffefef3efc3ef3e34eebe3cceee3cf3ffff3cf3fcfccfffc3cfefc3cffcf3f3cfcfcfcfcf3cf3cf3c3e3e3e7ffcfc3bc3cfcfc3e67c3cc7e7e7e7e37e3e343b7cbd77c7c7c37c7c7c3ccc3cfc3c3cc3ccfc3cc3e7e37c3c3f3fcff3e3c3f3fcff3ec3c3cfcfcf3ff3f3e3e7c33cfcfcf3fcf3fcfc3f3ffc3fcffcfffffec3c3ffcfecf3cfcf3ff3fffc37e37eccf3fffcff
    ff3fff3fffffcfffcf3cfcf3fefe3ef3f3cfc3efe3e3e7747ee3e3e3efcfcfcfcfcffc3f3cf3ffc3c3cf3e3ffcffcff3ff3f3fcf3e3cfc3e3e7e3cf3f3c3c3c3337c3c3c37c33e773c3ec3e7c347e7b7bc77c3c7e7b6c6c3c3c3c3c83c3e3c3cc3c7c3e3e3e3fc3cf3c3e3c3fcf3f3f7e3fc3f3f3cffcfcfec3eece3e3f3effffffc3cfffc3efff3fff3fcf3e3efffcf3cfcfcf3ffcffc7e3e3ee3ff3fcf8ff8
    fffffcffcffffff3ffc3cfccfecceccfeff3ef3fe3fceee7e74fccee3c3f3f3f3f3fffcff3fcfcfffe3e3ee3ff3f3ffffcfcfcf3cfc3c3e3e3e7c3cfffc3cfcccc7c3cf3cc3ec3ce7c3c3c3e7e77c7c7c7c7c37e7c7e7cc3cc3c83c3cc37c7f3c3e3c3e73e3f3cf3c3c3c3ffcf3cee3e3e3ecfcfffcfff3f3effc7cf3fcf7cfc3cfff3ef3fff3cffcfcffffec3c3fff3e3fcf3fcffff7e3ee3e3ffffcffcfcff
    f3fcfffffffffffffcffe3fccefcfccefe3fe3ec3ef3f3ee7eee3fe3efcccfecfcfc3cf3fcffcf3c3c3e3e3e3fcfcf3ff3ff3f3fcf3ffe3fe7e3ecf3c3fc33c3c73e3c3cf3c3c3c7c3e3c3e3c3e73e7c3e3e3ec7c7c7c37c3cc3ccfc3ccc7c7e7c3e3e3e3c3e3e3c3e3c3c3f3fc3e7e7ee7e3fc3cff3fcfef3e3fe3cffcf343ffcffcf3fff3fefffffffcff3c3effcfc3ff3cfffffe7e3e3ceffffcfff8f3ffc
    fffff3fcfffffffff3fcfcfffcfe3fe3ccecfe7ec3ee347eee7eecce3ef3fc3ff3fcf3cfcff3fffc3fe3e343ffff3ffcffcfcffcfffc3ce3e3e3e3c3cfc3cc3c3c7c3ccfcfc3cf3e3ec3c3e3e3e7e3e7e3e7e3c3e37c7c7c7c6c3c3cc3c3c3c3c73e3e3c3fe3e3cf73efff3ffce7e73e3e3cfcfcf3fcffe3cfffcfc3cfff73e3fffcffcfffcff3fc3fcff3fb3c3fffffeffcffcfe7e3ccfefffcffcffffcffff
    fffcfffffffffffffcf3fffccfececffec3efee3ee3ce7e73ee3e3ccfcfc3fc3fcf3cff3fcfcfc3ce3fe3e3ecf3fcfff3ff3ff3f3f3fe3cc3e3e3e3e3c3f3e7f37c3c3c3f3c3cc3cc3cfc3c3c73e3e3e773e3e3e7ec3b7ccc37cccc3c3cf3c3e73e33c33c3e33e3e3e3c3cfcf3e7347e343e3f3ffcfffcfcfc3ef3fef3ffe347fcfffcf3ffff3efffff3fffb3fefcf3fc3fcff3e7f3ef3cffff3fcf3f8f3fcfc
    ffffffcfffffcffcfffec3ffc3eccefffffe3eec3e3e3e74e34eece3c3fcc3cfcf3fc3cf3f3ffff3e3fe3ec3efcffc3ffcfffcffcffc3e3cfe3e3e3e3cfc7c7e7c7c3c3ccfc3c3c3fc3cfc3fee37e37c3ee3e3c3c3e7e7c7c3cc33c63cf3cc3e3e3ef3cfe3c3e73e7f3c3e3f3e7e53e3e3efccfcfffcff3f7ffcfcf3fcfc3e3e7fffc3fcfffffcffcfccfff7c3cfffcf3ffcfee3eccfcffcf3ffcffcfffffcff
    ffffffffffffff3fffcfffffcffe3eeefffffcfeefc3fef3ec3c3ecfeff3fec3c3ecfcfefcfcf3c3ecf3e3ce3cf3f3cfff3fff3fffffcfe3e3e3e3e3f7c3c3c3c3e3e3c383fcfcfc3cf3c3c3c3ee3ee3473e3c3e7e73e7c63cc3cc3ec3fc3c3e7e73ef3c33c3e3e3c3cc3ec3e3e3e7e3e3e3f3cf3ffffffffeffffcfffff3e3e34f3ffffff3ff3fffff7fcc3fc3ffffcfcff3e3ef3fff3f3fcfffcf8ffcccf3f
    ff3fffffffcfffffcff3ffcfffecec3eceecffcf3e3ee3cc3cfeee3efcce3c3e3cf3c3e3c3c3fffc3c3efc3fe3cfcffc3fcf3ffcf3f3c3ecf3ec3e3ec3cc3e7c3e7e7e3cffc3c3ffc3ccfc3c3e77fc3e3e7e3ce3e7e7e7ccc3c3c3e3cf3fc3e7e7ee7e3fcf3b3e3e3c3e73e3e37e3e3ee7eecffffcf3fcfc3c3cf3fcf8fcfe3c3e7ffcf3cffcffcf3ffbffc3e3fcf3cf3fce3ef3fffcfccfcfffcfcf3e3fffcf
    fcffcfff3ff3fcfff3ffffffcffe3efe3e3e3effefe3ee3ffefc3eecf3f3efe3cc3cfc3c3e3cfcf3e3fc3cc3e3fff3f7fc3cfcfffffcfc3c3e3ec3e3cc7c3cf3c3e7e7e3c3fcfc83fcf33fcc3e7e33e3e3e3c3e3e3e37e373ccc3e3c3fc3e3e73e73e7e3f3ee3e3be3e3e3e3ee3e3e3f7e77c3fcffffcfffffefffcffffff7e3e3e3fcfffffff3fffff7cf7e3cffffcfcf3ef3ffffffcf3f8fffff3ccffcffff
    ff3ff3ffffffcf3cfcfffcfefcfeefefc3ee3e3f3c343efe3c3fee3fe3ee3efc3efeffffec3c3fcfec3fcf3ccc3fcfcf3cfe7e3fcfff3efe3cf3ce3e3e3c3cfc3e7e3e3c3cf38f3fcfcfcc3fc3e3ec3e3c3cfe3e3c3e7c3ee33e7e3cf7ee7e7e3e3433e7e3e3e3e3e3e3e3e3e3e3e3efc3ccc3fff3fffff7c3f7ffffcf3fcc3ef347ff3fcfffffcfcffc7f7cf3cf3fcffe3fcfcffcf3fcfcfcfcfccffcfff3ff
    3ffcffffcffcfcffff3fffcf3efe3eceff343eeffee3434feffefeeefe3ce3c3fe3e3cf3f7ecf3f33efe3fcf3cfcf3cfff37e7e3ff3fcf3efe3fcfe3e7e3c3f3c3ee73e3cc3c3cf83f83f8fc3c7c3ec3cf3c3c3ffe3c3e3e3ee3e3f3e373c3c3e3e3e3e3e3c3e3e7e7e7e3e3c3e3efe3fc3c7ccfcffcffc3fcffcfcfffcff3e3e3e3cfef3ff3cff3fc3c7fe3e3fffcff3cfffffffffcfcff3ff3cfff3fffffff
    fcfffcffffff3ff3cfcfcfcffe3feff3ecfce3e3e3fe3e3e3f3c3e3e3cc3ef3e3e3e7c3cff7fcfcfe3cfcf3ef3cffff3c7e777e7ffffc3e3c3ef3c3e3e3cfc3cce73e3ec3c3cfc3fcf3cc3f3c3cfe3c3fff3e3e3c3fe3e3e73e3c3ee7ce3c3e3e3e3e3e7e3c3c777e73e3e3ef3cc3c3ff3cfc3effffff3cc3fcf3effcfffff7fe3e34f3ffcffff3fffc3bf7c3c3ffeffcff3ffff3ffcff3cffcff3fcfcffcfff
    cf3ff3ffc3fcffcff3ff3ffefcefffcfef4f3eee3e3eee3efcfccf4efe3e3ecccfe3eefcfcf7c3c3fe3f3cf3ef3fcf3c3e3ee7e3e3fcfcfcfcfcfcfc3e3e3cf3e3ee3e3f3fc3f8fcfcfc3ccfcfc37c347fcf3cfc3c3fc3e3fe3f3e7c3c3e3ee3fe3e3c3e3cf3ece3ec3e73c3fc3cfcfcfcf3e3c3fcf3cc3cff3ffc3ff8fcff7e3fe3e3fcf3fffffcff7e7fe3fefff7fcf3ffcfffcff3ffcffcffcfffffffffcf
    fffcfffffff3fcf3cfcfffeff3efcffef3cffcf3e3ef3cf3e3f3e3e3e3fec3e33e343e3e3e3cec3c3e3cffcf3cff3ccfefe3c3e3ecff3c3e3fc3f3fef3e7e3e3e3e3e3fc3cfcf3f383f6f7c33c3ec343b3c3cf3fe3e3c3e3e3fecff3cf3ee3fcf7ffc3c3cf3e37c3c3e3e3fc3ffe3f3fe3fcfc3cfffc3cf3fcfcffefffff8fe3e3c3eef3ffcff3ff3fefd3e3c3cffff3fffffffcffffcffcf3ffffcffcfffcff
    f3fff3fcfc3ff3ffc3c3efffcfe3efe3efe3f3ecef3cf3efefe3cfee3ee3ce3efe3e343ee3ef3cffc3fcf3cfcf3fcf3e3c3c3e3e3c3cffcfc3ffcfc3e3e3ef3e3e3e3fc3e3c3cfcf3cfc3f7fc3c3c3e7e7effcf3fc3ee3e7ec3f3f3fcfe3e3e3cfc3fccf3ece7cfe3e3e3ee3fe3ccfcffcff3cec3ffcc3cf8fff3c3cffcf3f3e3cfe37feffcfffffcfb3de3e3cffefcfffcffff3ffcfffffcffcfff3ff3fcffc
    ffcfffffffcffecf3feff3fffefeccfecffefff3fff3ee3e33cfe3cee3ef3e3e3fe3e3e3e3e3fe3cfe3cfcf3fcfe3e3fc3ee3ce3e3fcff3fcfcffcfcfe3e3e3e3e3efc3e7b3cf3c3fc3fc3cfcffc3cf73e73f3fef3f3c3c3e3e3fcfcf7f3ec3ff3fcf3fef777ec3e3e3cf3fec3ef3cff3fffc33cffc3cc3fffffcffef3ffcffe3ef3e3eef3ffffcf3fbf7e3cf3cf7fcffffff3ffcffffcf3fcffcfcfcfffffff
    fff3fcffffffc3fcfcf3effcf3efecefe3efc3efc3ef3e3efe3e3ef3e3e3e3e3e3eeee34343efcf3c3fef3fcf3c3ece3ce3e3e3e7cc3cfcf3ffcf3f3c3e3cfe3ee3cf3e3e7e7f3fccfc3cfc3f3c3cf3ee7eefcf3fecffcff3e7eff3fe3cc3cfc3effcf3f3ccc73e3c3cfe7c3cf3ee3ffffcffcfc7fc3fcf3ffcf3ff3cfff3c3e3e3e3e7ffef3ffffff7c743e3cffcff3fcffffcfffffffcfcc3cf3ffcfcfcf3f
    cffffffffffffcffffcfcfffefccfe3eccf3fefe3fe3e3e3e343c3e3ee3e3ee3fe3c3e3ee3eff3cffe3cff3fcfe3e3ef3e3fe3e3e3ff3f3efcf3fcfcfc3ef3e3e3cf3ee3e347efc33cff3cffcf3efec73e37c3ffc3e3cf3fff3f3fcf3cf3e3fffcf3f3fcfc3ec3c3fff3ffc3fec3fcffcfff3c3c3ccc3cfcffffc3efcffc7e7e3effe34f3ecfff3fcfbf7e3cf3cffcffffffcf3fcf3fc77e7cb7bcc3ffff3fff
    f3fcffffcffffff3cf3f3fcf3ffe3efeccceef3ccc3cce343e3ecfce3cfe3e3ec3ec3ec3efe3fcfc3fc3e3cf3e3e3e3e3ee7fe3e3e7cccfffffcfff3c3efe3fe3fc3e7e7e3e73e3ec3c3fc3c3cc3c33cf7e3bfc3e73e3ffcfcfcfffcf3c3e3c3ff3fcc3c3ec73cfcfcfec3fe3c3cfcffff3ffffcf3c3cf3fcff3fcfcf7fe3e3e3e3c3e3ec3ecfffff3bf7e3e3fc3fcffcffffffcffccccc3cfffc3bb7c3fcfff
    cfff3fffffffffcfffcffffcfefeecefc3effcfc3ec3fe347e3e3e3fe3e3e3fc3e3eef3e3c3fcf3fcf3fcfe3e3cf3ec3cf3c3cffe3ef3c3cf3fffcffcfc3e3e3e3eee3e3473ee7e77e3cf3fff3fcfcf3c3e3ef3e3e3ee3cff3fffcf3ffcc3efc3fffc3fe3e7ce3cf3fc3fec7fcffef3ffcfffc3fcc3fcfff3ffcffff3ec7e7e3efcfe343ee3e3fcfff7f7e3fe3fcf3ffffff3fcf3cf3cfffcfc3fffcccccfffc
    ff3ffcfffffffc3fc3fcf3fcffc3efe3ffccf3efe3fe3e3e3e3e3ef3e3ccce3ece3e3ecccecf3ffcfcfcf3e3ef3e3e3fffe3e3c3cf7cffc3fcfcff3c3c3c3fef3e33e3e334343e3e7e73cfc38fc3f3cffec3e3c3e3e33e3fffff3ffcfc3e3c3ffcf3fc3e7e373ef3fc3e3efc3fe3fcfcfffcfffc3cfcf3fcfc3ec3eff3e3e7e3c3c3ebec3ee7cfff3fef7ec3feffffff3fffcf3cf3cff3ffffffcffff3c3ecfc
    fcffff3fffff3ffcfcf3fffcfefcfeceeffe3fe3fe3ee347ee3efe3e3e3e3ef3e3eef3c3f73efcff3fcfcfcf3ef3e3eff3ffc3e3e3e3f3cfcff3ffcff3efe3c3efe3ef3e3e73e3e3e57e3cffc3fcfc3c33e3ec3fcfe3ecfef3fffcf3fc3cc3fcf3cffc3e3ec3e3fcfecfc3cfe3fcf3fcf3fc3cf3fe3fffffc3ec7d7be7e7e3ecfeee73c3e7cefffffc3fb3fef3ffeffcffff3fc3cffcfffcffcfffcfffc3c3ff
    fffcffcfcfffcfc3fffcfcff3fcfefcfcfcfefff3ce3e3e3e3e3e3e3fe3e3e3e3e3e3ece34e7ff3fcf3ff3fe3e3ecc3fffcf3fe3ef3efc3cf3cfc3f3efe3cf3e3c3ef3fe3ee7e3e773e7e3cffcf3f3fc3e3c3cc3f3c3fef3fffcfffc3c6e7c3ee3ee3e343c3ecff3f3c3fc3fcfcfccfcfcfccfcf3cfc3cf3cc3ece7b7e3e343c3e3e7ecc3e7f3cffffcf7ecf3effcfffffffcc3cffcfcfffffffcfffcffffccf
    3ffffffffffffc3cf3ffff3cfecfc3eefcfc3e3ee3fe3e7e3eec3cce3ec3efe3ee3ec3c3e7e7effffcfcffffc34f3eeffffcfcf3c3e3e3e3cf3cffcf3c3f3ee3e3e3e3e3e33e3e3ee343e3f3cf3ccc3cc3fec3fccffe3f3fffff3fcfcc7ccc3e3e3e3ee3e3cc3fccccfccfc3fc3c3c3c3cf3c3ecfc3cffccf3c3e3eb7e7e7e3ec3ee3e3efe3efff3fcf3e3cfcfcfcffcffff3cfffffffffc3cfff3cffffcff3c
    ffcf3f3fffcf3fccccfc3fffcf3ecfe3efcfefe3ce3fe3e3ee3ef3e3e3ec3e3e3ee3cefe34343be3ff3ffcff3e3e3e3ffcff3fcfe3e3e3cc3cff3cf3fc3ef3cf3e3c3c3e3ee343e3e347c3e3f3e33ef3fee3fff3f3c3cfffcfc3fc3c3c67e3ee3ec3e3e3ef3ec3c3fc3fc3cfefcffcffcf3ccc3f3cc3cf33ccce3b7c3e7e3ecfe7e7ee3fe3effffff3ffe3ef3fff3ffffffcc3fffcf3fcffffc3fffff3fffffc
    fffffcffcffffcff3ffffef3fcfffecfe3ffff3e3cc3fe3f3ee3eeeeee3e3cc3e3ef3e3ee7e3e3eef3fcff3cfe3e3ecfff3fcf3c3cc3fe3ef3cfc3fc3fe3cc3cfe3fcfe343e3e7e3e37e7c3e3e3e3c3fc33e3cffce3e3e3fc3ccfcc3c6ec7e3e3efe3ee3eef3ee7c3ce3fefc3c3c3fcf3fff3e7cff7c3fcff3e3ee7e7e3e3e3e3c3e77e3ccfcffcffef3ec3ffeffefffff3fffcf3ffcffcfcffffffcffffcfff
    f3fcfc3fff3cffffffffffcfcfecf3ffeefefee3fe3efccec3ec343e3e3ef3ee3e3ee3e73e34e53e3ffffffcf3ce3e3ffcfe7effcf3e3e3e3e3fffcfcf3fc3e3c3e3e3fe3e3e3e3e3e3e3e3e3c3e3e3e3ee3e3fc3e3e3ee3cfc3c3c6cc7c3e3ec3e3e3ee3cfc3fc7ec3bf3cccecfef3fcfcfcc7ffffee3fe3efe7cf3e3e7e3fe3e3ee3ef3f3cfffffc3fc3eff3ffff3fffff3ffcffcffcff3fffcffffcffffff
    cfff3efffcffff3cf3ff3f3ff3fefeefffcf3e3fcfe3e3e3ee3eeeeee3e3ee3e3ec3e3eee5e7e34ccfcf3fcf3ff3e3fffe7e3e73cfcfc3e3cfe3f3f3ffe3fe3ffcfc3f3e3e3c3e3e3e3e3e3e3c3e3e3e3e73ee3e3e3ef3e7e3bc3ccc3c3cc3efcfcfcf3fe3ecf3ffc7be7ce7c3ec3cfcffcffc7cfc3c7ecfcf7cc3fe3e3e3ee3ee7e7c3cfeff3ff3fcffccffcffcffcffffcff3f3cf3cf3fffcff3fffffffcff
    3c3ffc3fffc3fcffccc3fcfcffe3fffef3fcfecff3efee3eccfc3ee3ee3ef3e3e3e3ec3e734343e3cfffff3fcfe3ecfec3c343ee3cf3fcf3e3cfcffcf3fcf3cc3f3e3efc3e3fe3e3e3e3e3e3e3e3c3e3e3e3e3e3e3e3ef3e347ecc3c3cf3efe3fc3cfefefc3ebbb7ce7bcc3c3c3fccffc3c3e3cc3cfc3e3f3e7e3c3cc3e3e3e3e3e73cffcfffeffff3ff3c3fffffffffffff3ffffcfcffcfffffcffcffcfffff
    fecfe3ecffffffff3c3eccf3cf3fec3cceffe3fefc3e3efe3eceeecee3efe3ee3ecc3ee74eee3ee3ef3cffcf3cff3e3c3e3e3e3ee3fcf3ec3e3cffffcff3ffffcfcfcf3cf3cf7c3e3e3ce3e3fcffcfe3e3e3e3e3e3e3e3ee3c3e3e7ec3cfe3cfefef3e3fcfcf3ffc7bc7c3c3ccf7f3e3efe3fef3fe3fefefec3cfef3e3ee3e3e3e3ee3fcff3fcffffcffcfcffffeffffff3ffcfcffffcfffcffffcfffffff8ff
    c3c3fef3ffce7c3ffec3c3ffcfefcfefccfecccf3fc3efcfee3eefecefe3e3e3e3e3e343e7343e3effffff3ffc3efe3fefc3ee3e3e3fff3fe3e3f3f3fcffc3cf3f3e3cf3ec3f3e343eff343e3c3c3f3e3fe3e7ce3ecc3e3ee343e7e3efc3efe3cf3cfcfe3fecc7c3c3bc3ccfc3efee3e3e3ec3ee3efe3f3c7c3e3c3fee3e3efe3e3e3fcfffffffffff3fc3ffcff3fcfffffcff3fff3ffffff3fcffcffcf3ffff
    3ffcf3ecff3ceceeff3ffcff3ffc3efe3cff3fcfcffe3ffcfeeeefececce3e3e3e3eee343ee3eccf3fcf3fcfeff3cfcf3ffe3eeee7fcfcfe3e3e3fcfff3ffff3efe3c3eff3ce3e3e3e3ec7e3e3ef3ef3e3c3e3c3e3fe3ee3e3ee3e3e7e3efe3fcffcfc3fcf3c3cbb7ccccc3ffe3e7cc3fefffff3fe3e3efe7cfc3ecf3e3e3e3e3ee3efff3fffc3ffcfcc3effffebe3ffff3ffcfcffeffcfffcffc3fffffffffc
    fc3fce3cffcf3eee3ffcffcfefeffc3fefcfe3ef3c3fef3cfeeeee3efef3eeccce3e35e3e3ee3c3efffffcf3f3ecf3ffc3fceee34ef3ffe747eecff3fcfffcffc3fcfc3cfcf3fe3ee343e3fee3e3cf3ffefc3e3efc3cf3e3ee7e3ee347fc3cfefcfc3fee3cffcfffcc3c3cc3cfc3f3cc3f3e3efcfff3fe7fe3e3e3cc3e3ec3fe3e3e3effffcffcfff3cfe3eff3fe7bef3ffcffff3cffffffffcfffcfcfcffcff
    ffc3f3e3cffee43efcffcf3f3f3cfccff3f3fe3eefcf3efe3e34feefefee3e3e3ee7e34343e3ec3c3ffcfffcfcf3ffcf3cf3feeee7fcfe7eee73f3fffffcff3cfff3cf3f3f3cf3e3e7c3ee33e7ee3fefc3f3efe3e3efef3e3e3ee3e3e3ecccf3fcffecf3fef3fcf3fffccf3e3e3eccf3eeef3fe3feffc3e3ef3fce3ce3ef3ef3ee3ec3fcfff3ffffcff3cfcfffff7e7cffffff3fcfffcff3ffff3fff3fffffff
    fffec3ef3fcf3eeeffcf3cffcfcf3ecfefce3efe3e3ef3cfeeeceefeeeeee3e3e3e3ee3eee3e3e3eff3ff3ff3cffcf3ffcfe3fe3eeefe7ee3ee3ffcff3ff3ffcf3ff3cffcfef3e3e3c3e3efe3e3e3ff3ffef3c3fef3c3cfccfe3fe3ecf3c3efef3fcffcfe3ccc3cccc3f3ecfe3cf3e3e3e3ec3cc3f3cfec3c3ee3fef3efc3e3e3e3e3eff3cccfc3c3ecfe3c3fcfcf77bffcf3fcfffcfffffffc3cffcffcffffc
    fff3fc3efffcfeeeff3fffc3f3fefe3cf3fcfe3eee3cfe3effffefefefc3fe7ee3ef3ee3e3e43ec3cffffcf3ef3fffcfc3cfc3eeeee3e4e3f3efcff3fffffcfffcfcffcf3f3ccfc3fef3e3c3c343ee3cff3ccfc3fcfffcf3f3cfefcf3efefe3ffcff3f3cfffffffff3eccfe3ce3fc3cfe3b3cfffeccf3e3efcf3ef3ef3cfefe3ee3ecef3fcff3ebe7b3fffcffffff7e7cfffffcffffffffcc3effcfffff8ffff
    fcfcfcc3fffffeeffcffcf3ccf3cfefc3fe3ffe3cfcf3fefefce3efeeecfee343e3ef3ee3e3ee3ec3fcfff3ffcffcf3fcc3eeceeefeee3eecf3fffcfcffcfff3ff3fcf3fcfc3f3cfe3fe3cce3e3e3ffc3fff3fce3fe3cfcfefc3f3fcfcf3cffcffcfcfffe3cfcfc3cff3e3c7f3effee3cc3e3fcff3fec3c3f3efc3c3cf3c3c3e3ee3feffcfffef3cc3eec3fe3ff3fce3cf3ffcfffcff3fc3efffffffcffffcff
    ffff3fcefffcfefcfeee3fffccfce3cfffcfe3ecf3c3ef3fcffeefefefcf3efece3efefeeee7e3ece3ff3fcfcffffcf3fecefeee4eeeee3f3fcf3fffffffffffcffff3ffc3cfeff3fe3ec3c3ee3ee3ffe3fecf3fef3ff3fcf3fefcff3fefc3fcf3fffcfcfcf3ff3ce3ec3e3cefe3c3cc3fecfcf3fff3e3efffc3ceffccffcfccf3cff7ffffff3ff3fec3ffcfeffcffe3fcffcfff3fffce3ef3fffcfffcfffff8
    f3fcff3cfffcfffeeecccffcf3cfcffcfcfcfeffccfcfcfcf3efcefeeeeefc3c3ee3fc3c3c3eee3eeeeffff3fc3f3fccfc3fcfeeecfe3fecee3fffcff3fff3ffffcffcffff3c3fcfcfc3cfcf3e3e3ec3fefff3fe3cfcfcffcfcf3fcfef3fcfcffcfffcf3fffc3cfff7c3efef3c3cfc3fef3f3ffffcfe3fe3cffe3c3ff3cc3cf3cfeffcffff3fcffcfffecff3c3ffff3ef3fffffffffe3ef3fcfcfcf3ffffffff
    fcff3ffc3fcffcf3c3fffff3cff3efc3fcff3c3e3fe3f3c3efc3ccfeffc3efefe3fee3fefce3e3ef3e3ffcffc3ecff3f3fefcf3eecefeeee74bfcfffffcfcfcf3ff3fffcfcffeff3ffff3cfcfee7f3cfcf3fcfcfc3fcff3f3cfcfcf3fecffff3fffcffcfc3ffce3cfffef3fcfcfcffe3ffcfefcfff3cffcf3cf3e3ecfcffefffcffffeff3ffffffff3f3c3ffefcfffc3fcfffffcf3e3efcfeccc7cfcf8ff8fff
    f3cfffcfcffcffffffffffffffcfcfcfcf3feee3e3e3efffe3e3efefeee474c3fec3cfef3e343eeceeef3fffeeff3fcfcffcfcff3eeee3ecfe7efff3fff3ffffcffffcf3ff3fc3ffcf3fef3fe33eec3e3fcfff3ffeff3cfcffff3fcff3fc3fcfcffff3fffcff3fec7c3fcc3f3f3fc3fcfff3fefffffcffcfcfcfef3eff3ff3ffffff3cfffffffffcfcfefeff3e3ffffe3fcff3fffc3ff3ce3c3cc3cc3ffffffc
    fcf3fff3fffc3ffcffcfffffcf3cfffffcccf3ce3e3e3e3effcc3efefe5e47eecffcfc3ccc3eec3ef7eecff3c3fcfcfcfcfffccffee5efffffeeffffffcfc3cff3fff3ffffcffcfff3fcfff3fee3f3efffff3ffc3c3fffffcf3ffcfcfffffffffcf3ffcf3fcfff3fc3cfffffccfcfffff3ffc3ff3fffff3cf3cf7e3c3fcffffcffcfc3ffeffcffffffe3e3fcfcfefffcffffffff3ffefcf3ccc3cfcfccffffff
    f3fcfffcffcfffffcfcfcfcffffcfcf3cfffec3cc3eccfcfcf3cfeefe47e3ef3ffe3feff3ee343ece3e3ffcfeffffcffffe34eceefeee3ffff3e3ffcff3ffff3fffcffcfcff3ff3fcfff3fcfc3fcccff3fcffcf3fffcfcf3fcfcfff3fc3cfcf3ffcffffcff3cecfcfcf3cfcff3cf3cf3fffcfcffffcfffffcff3fe3ecf3efcfffffffefcfcfffcfcf3cfcfcfc3ef3fff3c3fcfffcfff3ffcf3ffff3fffcfff8f
    cfc3fffffffcffcffffffffff3fcfffcffcfffc3ef3e3c3ffffe3c3e7eeefeeecfcfef3ce3ee3ee3eeefff3e7c3c3e3ee3eecf3fceceecfcecfcffffffcfcfcfcfffffff3fcffcfff3fcfffcfcf3f3fffcff3cfefcfff3cfff3fcfffffff3fffcffcfff3fcff3c3c3ffcff3cfffcffffcfffeffffffff3ffffffc3fcfe3bffffffcfcffff3fcffffcfe3fffffe3effffefffffffffcfffcfcfffcfffffcfffff
    3f3ffffcff3fcfcc3eeff3ffffffffcffffff3ffcfefefc3fcf3ec3ecefeeee7fcfccffffc34e3efe3ee7fc3e3efece3ece3effeffe3efeee74cfff3fffff3ffff3fcf3fff3fff3fcfffcf3f3ffcfffcf3fffff3f3fcffc3cfcff3fcf3fcffcff3fffcfffcfcffc3fcff3fcfc3ffcfcfffffcffcfff3cfcffcfffec3e7ec3fcffffff3fcffffffff3cfef3cfcfcfcfff3cfcffffcfffcff3fffffcf8fffcf8ff
    ccffcffffffcff3fef3cfffccfcffcffcffffcff3c3c3f3effef3cc3efefee3eeff3eecfceec3efeee7eee3fffcfe3eefecfcfcffcfeeef3ee343ffcff3ffffcffffffffcffcffffff3ffffcfffffcfffcffcffcfcff3ffffff3fcffcfcffff3fcfcfffcf3fecfffcfcffcffffeffffffffffffffffecfffff3ff3ee7c3efffffcfffeffcfcfefffcf3fffff3e3ff3fffcffffcfffcfffffffffffffcfffcfff
    3e3fffff3ffffefeffcfefffcfffcff3fcffff3eccfefeffcffcff3e3efeeeeef3ccf3c3c3cfece3e3e7ee4eefc3fece3eeeffffffefcfefffeeefffffffcfff3fcf3fcff3ff3fcf3ffcf3ffcf3cf3f3f3fff3fff3ffcfcf3fcfffff3fffcffcfffff3ffffff3ccffffcff3cfff3fcffffcf3fff3fc3fcff3ffc3b3c3e3f3ff3fffcf3fffffcfffffcfefe3feffecffcf3fcfffff3fff3fcff8ffc3ffcfffcfc
    f3cffcfffffcffcfffecffe3fcffffffcf3ffcfc3e3c3e3e3fff3cfcfc3e343eefcecffefffe3eecceee343e3efeeccfefefe3cfcfffffffcffe3fffffcfff3fffffffffffcfffffcfffffcfffcffcfccfcffcffcfef3ffcfffffcfcffcff3fffcf3ffffcf3ffcfc3f3ffcffcfcfffff3ffffffcc3cfcfffffe3ee3eeeefefffffffcffffcffffffc3cfffcfc3efffffffcf3ff3ffffffffffffcffcfff8ffff
    ccfcfffffcfffcffffcfeffcfffcffcffcffffe3efe3fe3cf3cfffc3e3ece7ee7cfcfcefcfe3ef3e3e34e3cfc3ee3ee3ecc3ee3feefcfcffffcefffcffffffffcff3fcf3ffffcf3fffcf3ff3fcf3ffff3f3ffffffffcfcf3fcf3ff3ffcf3ffcff3fffffffffffffffcfcffff3ffffcffffcce3e7cfcf3ffcfe7fce3f3c3cfffcfffffcfff3fe3fcfffcf3ffffcf3ffcfff3fffcfffffcfcfffcffcff3ffff3ff
    3c3ffcfffffffffffffffcffc3fffcfcf3ffffe3c3cce3cfef3fcffcfcf3ee3d43cf3cff3e3eeeccece34e3fcfe3ee3efcce3eceeffff3ff3ffcfcff7fff3fcff3fffffcfcf3fffcf3fffcfff3ffcf3fccfcffcff3f3fffcf3fcfcfff3ffcffcffcfcffc3ec7c3ffffff3cfcffcfffff7e3e7cce3ffcfff7f7cf3eecfcfe3ffffcffff3ffffcfffcffffcfc3cfcffffcffcfcfffffffffffcffcf3fffffcffcf
    f3fcfffffffcffff3fcffff3ffcffff3ffffcf3fefe3fcf3cffef3ff3fe3c3e4ccefeffccce3e3cc3e3e3efcf3efcfefefeceeeeee3eff3ffffffffccffffffffffcfcffffffcf3ffffcfffcffcffffcf3fffff3fcffcf3fcfffcfffffcffcffcffffc7bd7bcccc3cf3fffffffff3fc3cbc3bf3efc3cfce3ce3cfe33efe3fefffffffcfffcffcfffff3ffffff3ffcfff3ff3ffcffcf3fcfffff3ffcff8ffffff
    ccff3fcfffffffcfccfc3fffefffccfcfcffcfffe3eff3ef3e3e3fcfcf3c3ee3cf3cfffe3fee3eece34ee3efcfe3eeccc3feeee3fcef3ffcfff3fffefffcfff3fcfff3f3f3fcfcfcfcff3ff3ffffcfcffcf3cfffffcfffcff3fcff3ffffff3fcf3fcfcfffcc3ffffffffcfc3cf3fffbec3bfe3cf3ffe3c3fcffcf3efe3cfcfffcffcfffcffffffcffffcffcffcffff3ffffcffffffffff3ff8ffcffffffcffcf
    3f3ffcf3fcffffffff3cfccffffcfffffffefffccf3eec3fefcfee3ffffce3cf3feffc3efe34ce3eee3e34c3e7ee3e3effe3e5ecfffcfcfffccfffc3ffffffffffffcffcfcff3ffffffcffcffcf3fff3ffcfffcfcff3ff3ffcffffffcf3cfcffcffffffffffcc3cffcfffffffffcfc7c3ee3cffcfc3fcefc3ef3fcfc3fffcfffffffffffffcfcfffcffffffffffffffffcfcff3f3fcfcffffffffffffcf8ffff
    cffcffcffffcf3fcfffffffcfcffffcf3fcffff3ffcf7bbe3c3e3cfcf3cf3e3ecfff3fecfecf3fe3e34eee3efef3eecfefcceeecceff3f3fcf3bffefffcff3ffcff3ffcfffcffcf3fcfff3fcf3ffcffcf3ffffff3cffcffcfff3ffff3cfcfffffcfff3fff3ffffffff3fcfcffcff7fecfc3fffff3fecf3cfcffcffcfefffffeffcffffcfffcfffcffcffcffcffcffcffffff3ffcfffffcfffffcff8ffffcfff3
    cfffff3cff3fffffffffffff3fffffffcffffffffffcf7e7cecee3e3ee3ecfc3c3ecfcfff7cfeeecce3e3e43c3cffcfe3cffe3efcfcfcff3fffeefcfffffffcfffffcff3cf3fcfcff3fffcf3cfcfffffffcf3fcfff3ff3fcf3fffcfcfcf3cf3fff3ffffffffcfc3cfcffffff3fffbfc3fcfffcfccf3cfcffcfcfcf3cffcfcf3fffffff3ffffff3ffff3ffcffffffffffcffffffffcf3ffcf8ffffffcf8ffcfff
    3cfffffffffcfcfffffffffffcffffcffffffcfcfcf3fccb7c3c3cfc3e7cf3fffcff3ffcfefe3e3e3ee3ee3eeecccfcfff3ceeccce3fc3fefcfeef3fff3fcffffcfff3ffffcfff3cfcfc3fcfcff3fcf3fffffff3ffcfcffffffcfff3cfcffcfcfffcffcfebc3fffffffcf3fffffce3fcfffcff3c3cfffcfeff3f3efcfffffcffffcffffcffcffcfffcfe3cf3ff3fffffffc3fcfcffffcfffcffffcffffcff3ff
    cf3ffffcffffffffffcffcffffffcfffc3ccffffffffc3fce7cfcf3ee7c7ece3cf3ffc3fecfecce3ecee3ee3e3e3ecfcfcfffefc34ee7e43e3efbffccffffffffff3ffcffcfffcffcf3fcf3cf3cfffffcf3fcfffcffff3fcfcfffcfcf3fcffcffcfffcc7c3ffcfcfcf3fffcfcf7fcffffff3fecfcfefff3fcffffcffffcffffcffffffcffffffffffffccfcfcffcffffc3ffffffffcffffffcffff8ffcf3fcff
    cffffffffcff8fffcffcfc3cffcffffccc3fff3c3cfffe3cfcfe3cf3e3e3c3fcf3cfcffcfe3e3efe3e3ee34cfc3efe3fffcfefcfc347e3eecfcceee3feffcff3ffffcffffffcff3ffcfcfeffcfcfcf3fffcfff3ffff3fcfffffff3cf3fcf3fff3fffe7eccecc3cffffffcfffffcfffff3fcfc3ffeff3ffefefcfffcf3fffcfcccfcffffffcffcfffcfff3cfc3ccfff3ffcfcfcffffffcfffffcffffffffcffcf
    3cffffffffffffffffcf3ccfc3fffcf3cffffcffcfc3fcf3e3f3cfcc3efeec3efcfc3ccf3fecff3ece3e3e3e3ce3fefcf3fcf3eef3e3e3ee3fffceeec3cf77cfe3c3fffcf3ff3fcfcf3fcf3cf3ffffcfcfff3ffffcfffffffffffffcfcffcffcffffffffffffffc3fcfcfffcf3cff3fffffffcf3cfffcfffcfffff3ffffcf3fffc3ecfeff3fffcffffcfff3ffcfc3fccfffcffcffff3f8ff8fffcffcff8ff8ff
    cfffcffcfffffffcffffffc3cfcfcfcffffcffffcffcffcc3ecffcf3e3e33ee7ff3fff3ceeffcccf3ee7ecefcf3ecf3fcfffcfc3effcfcfeeffcfee3efe3ec3e3ee7fff3ffcfffff3fcffcffcfcf3ffff3ffffcffffffffcff3fc3fcff3ffcffffcffffff3cecfffcffff3fffff3fffffffcf3fcffcffffcffcffffcfcffcffcfffffc3cfefcfffff3fffcffffffcfcf3cf3ff3cffffcfffffffffffffcccfcf
    f3ffffffff8ffffffcfcf3fcf3ff3fffcfffffffff3ffffffc3cffcfcfcec3c3efcfe3cf3cfcf3eee3e3e3f3e3cf3efff3e3fe3ec3f3ffe3eeefefee7e3e3ef3ff3ee3fecfffcfcffcfcf3fcf3ffffcffffcffffffcffcffffcfffcf3fcfcfffcffffcffce3f3fe3fff3cffc3fcfffffffcf3fcfffffffffcf3ffcffffcffffffffffffccfffffcfffccfffffcffffcfffcfcfffffcff3fcfcf8fffcfff3cc3f
    cfffc3cfffffffffff3fffffcfcfcffff3ff3cff3ffcffffefcf3ff3e33f3e3e3c3fcf3ee3cfec3e3e3ee3ef3ffcc3eece3ec7e7cffcfcee43e3efe3ee3ec3ecc3e3fcc3ffcffffcfffffcffcfefcff3fcffffffcffffffffcfffcfffffcf3fffff3fffc3fffecfffcffffcffcfffffffffcfcfffc3ffcffffffffffcff3cfcffcffcffffe3cffffcff3fcfcfffffffcfcfffcffffffffffffffc8cfc3fff8fc
    fffcfff3ffffcfcf8fffcfcf3cf3fffcffffb3fcfcffff3f3ffccfffcfec3ec3ec3f3cc3e3ef3ecfcff3fffcfcf3ec3c3e3c3e3e77e3c3e3ee3fe3ee3ec3e3f3ecfcf3ce3cfffffffcf3fff3fcfff3fffffffcffffffcffffffcff3fcf3fcff3fffffcc3ffccffffffcfcffcfc3fffffcf3ffcffffffffff3fcfffcffffffeffffffffcfffcffcff3cffcffff3ffffff3ffcf3fc3fcfcfcf8fcfc3c3cc8ffcff
    ffff3fcffcffffffffcfffffcfcfcfffffffefcfff3fcffffcfffcfffcf3f3ec3eecff3ece3ecf3ff3fefcf3ffcf3fef3cc3e3e3cc3eee3eccccfefe3efe3eecf3efcf3ee7ffc3fcfffffcfcf3c3fffcfffcffffffcffffcff3f3ffffcfffcfffcffcffffc3ff3fcf3fff3ff3cfffffffffcffcfffcfffffffffffffffffffcffcfc3ff3fffcff3cfffcff3cffffcfffffffcfffcffff8ffffc3fcfc8fcc3f8f
    cffcfcfcfff3fcf3fff3ff3cff3ffcffffcff3ffcfcf3cffffffffffff3ccf3e3e3c3ef33ec3fcfcfcfcf3fcf3fcfc3cf3fecfc3efe3e7ee3e3efc3fe3effc3fe3ef3cf73cf3ecff3cfcffffcffcfcfffcfffffcffffffffffcffcfcfffcff3fffffffffcfffffcfffcffcffeffffffffcff3f3cfffffffffffcffffcffcff3fc3fcc3cfffffcfffcffffffffcffffffffcfffcf3f3fffffffc8f8fc3c3cffff
    fff3fcf3ffcff3cffcffcfffffcfcffcffffffef3ffcffcfffffffcfffffc3ecfc3ecfccf3cef3ffcf3fcfff3feff3ffcfcf3cfc3e7e7e7ecffc3feeffe3efc3e7e3ffee3fce3fe3e3ffffc3fcffcffffffffffffffffcfffcfffffff3f3fcfcfffffffc3fffecfffcff3ffcc3fffcffffcfffffef3fcffcfffffffff3ffffffffc3cfcfcffffcfffffcffffffcfffffcff3ff3ffffcfcf3f8f3cf3fc8fc8ffc
    ffffffffcffcfffcffffffcffff3fcf3ffcfff3ffcf3fcf3ffcfff3ffffffcf3e3e3e3cffe3cccf3cfcf3fcfffc3fcff3f3ffc3ee7cc3e3f3f3feee3c3cff3fe7e3fc3f3eff3e7c3ffffcfffcf3fffcffff3fcfff3fffffffffcfcfffcffffffcffcffcfffccffff3ffcffe3cfffffffcff3fcff3cffffffffffffc3cffffcfffffc3ec3ffffffcfefcffcffcfffcffffffffcffccfff3cffffcf8ffcfcffcff
    fffcf3cfff3fcfff3cffcfff3ffcff3fcf3fccffffffcf3fcf3c3cfc3fcfffcc3cfc3e3c3fc3efcfcf3cfc3fcf3fffffeceec7e37c7eceeecfcfc3ffcfcf3efcf3effcfc3ecfcfefeffffffcffcfcfff3fcffffffffcfff8ffff3ff3fffcf3fcf3fffcfffc3ffffcffffcfccffffffffffcffffcfcffcfffffffffffccffffffcfffc3ecfcffcfffffffffcfffffffffffffffffffc3fcfcfffffcfff383cfff
    ffffcfcfffcf3c3fffffff3fffff3ffffcfc3fcfcfcffcfcfc3cffffcfffcff3ef3ec3efcfcf3c3f3cfcf3eff3efc3e7c3e7c3bbe3cf3f73e3fcecfcff3cfcf3ee3ef3fccf3f3c3c3cf3fcf3ffcff3ffffffffcffcffcfffcf3ffffffcfffcfffffff3ffccffff3fffcff3c3ffffcfffcffffcc3cfcf3fffffcffffffe3effffffc3ffc3cffffffcff3fcffffffffcfffffcfcfc3fcfcfcffffff3fcfcfcfcf3
    fff8f3ffcf3ffcffffcffffcffffcfcff3fff3ff3ff3f3fc3cfe3c3fffffffffccc3ec3e3f3ec3fef3cfcfcf3ce7ee3ec3e3e3e3be3fcfce3fff3fcf3fffcfecf3fecfcff3fefffce3eecffffcf3ffcffcffcffffffff3fffffcffcffffffff3fcfffffc3ffffcfffcf3fecffcfffffff3fcfeffff3cfffffffffff3fc7c7ffffffcfcfccfffcfff3ffffffffffffff3fffffffffcf3cf3ffffcffff8ff83f8f
    fffcfff3fffcffcfcffffffffffffcf3fcc3cffcfcffcfc3fc3cfffcffcfffcff3fe3cc3efc3cef3ce3e3c3ecc3e7cc3c7ec7e7ec3ffff3eefcceffffcff3f3fecc3ef3fcffc3cf3fc33e3fcffffcffffffffffffffcffcffcfffffff3fcf3fcffffcfc3ffffc3fcffffc3cfffffffcfcfff7fffcffcffffcffff3fec3b7cffff3ffcf3c3fcf3cc3ffcffcffffcff3ffffcf3f3fffcfcfffffffffcfffffcfff
    ffcffcfcfcfffcff3ffffcfffcff3fcffffffcfff3cffffcf3cfc3ec3cffffffffcff3ec3efc3e3fe3fec3ec3ecc37ec3e37ccc3cffecff3e3ff3cfcffcfeffcf3ef3fcff3cfffcfcffc3ecff3fffffcfcfff8ff8fffcfffffffffcffffffcffffffffffffffcffff3ffcf3ffffffffffffcffcff3fcfcfffff3ffe3ee7cf3fcfffffcffeffcfffcbcfcffffffffffcfffffffcfcc3c3ffffffffffffcff83fc
    fffff3ffffc3ff3fcfffffffff3ffcfffc3cf3fcfffc3fcfcff3ccffff3ff8fffffcfcf3ecffc3ecfe3e3fe3e3c3ec3ecc7cc3cffeffe3fe3ffeff3fcf3fc3efcf3fefcffffcff3f3fffcf7fffcfcffffffcfffffff3fffcff3fcfffcffcfffffcf3ffffffccfcffcfffcfcffcfff3ffffcfcffffcffcff3ffcfcfcf37c7ffceffffffc3cfffffffc7c3cfc3cfffffffcfffcffff3fcfffffffcfffcff3ffcff
    ffffcfc3fffcfcfffffcffcffffffcffffcffcf3ff3fcf3f3fcf3f3fc3cfffffcffff3ec3e3cfc3e3cffc3cfc3fffc3f3cf3fe3effcfefffcfcfcfffcfc3fff3fcccf3f3cff3ffccfcff3cffcfffffcf3fffffffffcffcffffffff3ffffffffcfffffcffffc3fff3fffcf3fffffffffffcfffff3fffff3fffff3f3c3ec7cff3cfffcfffcfffffff3fc7cf3fcc7cffffffcffffcfffffffffffffcffffffcffff
    fff8f3fcfcff3c3fcfffffffffcfff3ff3fcf3fcffcffcccc3fefcccfcfcffffffffffcfe3ef3fc3cfffffcfffc3cfccc3fefcffe3ff3ccffecfcfcfcffcfcffcff3effcf3fcffffffcffcffff3fcf3fffffff3fcfffffff3fffcfffff3fff3ffffcfffffc3fcffcfcfcfcffcffffcffcfe3ffcfffcffcfcf3cfcfe3e3effcf3f3efffffc3ffffffffccefcffcc7ffffcf3ffff3fcffffffcfcfff8ffcffffcf
    fffffccfff3cfccfffff8f3fffff3fffffcf3cfffcf3c3f3cc3cf3f3c3f3fccfcfcffff3ec3efcfeffcfcfff3cffcf3fffcfffcffcffcfffe3ee3fff3fcfff3ff3ffc3ffcfcffcf3fcf3fff3ffffffffffcffcffffffcfffffcffffcffffcffffcffffffccffffcfff3cfffffffcffffc3feffffffff3fc3cff3e3e3e7cc3ceebccf3ff3cffffcfcff3f3c3cf3cccffffffcf3ffcffffcffffffffffffffffff
    ffffc3fc3ffc3c7cff8ffffffcffffcfffffcfc3f3cffcfc3fc3efcfffcfcfffffffcfffc3e3cf3c3ffffffcffc3cfcfffffcffffff3ffc3eeefcfcfccf3fffcffcfcfcff3ffffcffffcfcfbfc7cffcffffffffffcfffffcfffffffffffffffffffffffc3fffffc3fcfffffffcffffcfffecffffcffcffffc3ef3c3eccffffff77ccfffffcfffffffffccfcfcf3c3cff3cffcffffc3fffffffcf3fffcfff8fff
    f8ffccc3cfffc3ccfffffcfffffcffffffff3fffcffcff3ffe3cc3fcf3cff3ff3fffffcffc3c3fffeffff3ffff3fffffffcffffcf3cfcffeecf3cffffffffcffcff3fc3ffcfcf3ffcf3ff3cf3e3cffff8fff8fcffff3ffffffff8ff3ffcfffcfff3ffcf3cffffefcffcffcffffff3ffffff3fcffff3fe3efff3ee3e73ffffffffb7c7cfffcffffffffff3f3cf3ccfc3cfffffcffffffffffffffffffffffffff
    """))

def on_button_pressed6(selection, selectedIndex):
    global statusbar, tilemap_1, col, load_p, row, myMenu2
    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
    if selectedIndex == 0:
        statusbar = statusbars.create(120, 5, StatusBarKind.health)
        statusbar.value = 0
        pause(100)
        tilemap_1 = tilemap("""
            level4
            """)
        tiles.set_current_tilemap(tilemap_1)
        scene.set_background_image(img("""
            666a666666a66666a66666a66666a6666a66666a6666a6666a6666a6666a6666b666a666b6666a666b666b66966b669666b6696a6696a6966b66966b66966b6966b6966b6966b6966b6966b696b696b6966b6966b6966b696b6966b6966b6966b696b696b696b6966b6966b66966b66966b6696a6696a66966b666b666b666b666b6666a66666a66666a6666a6666666a66666a66666a6666666a66666a6666a
            6a666a6a6a66a6a666a6a666a6a696a6966a9a669a6966a9669a6966a9669a6a66a966b66a9a696a989a669a6a669a6a9a69a6696a6696a6a96a6a96a98a96a6a96a6a96a6a96a6a96a6a96a6a698b66a9a698b69a6a96a6a698b69a6a96a6a96a666a6a66a66a6a96a6a96a98a96a98a96a6a696a6696a6a66a9a66b66a966a98989a696a9a696a9a696a9669a6a9a669a6a666a6a666a6a6a666a6a666a666
            666a666666666698966696a966986a66a66666a666a6a66a6a66a6a96a6a66966966a66a96666a6666669a6669a66666666a66a696a98969666966a69696a696669696a696669696a9696a96969a69a96669a69a6696a69696a96a6696a9696a969a96969a969696a6966696a96696a966a9696a69a6a6969a96669a69a66a666a6a666a66666a66666a666a68966666a66696a96696a6966698966669a66a6a
            6a669a6a9a6a98a6a6a6a666a6a666666a6a6669a666696666696666666698a6a6a696966a6a969a9a9a666a6669a9d9a966969a66989a6a6a9a69698a6966a9a6a6a696a9a6a6a966a6966a6a6698989a669a669a696989a666969a6966a6966a666a6a666a6a696989a98966a6a666a9666a69666966a6666a6a666669669a69669a669a6a696a6a666a66986a6a6666a6a666a68666a6a6a6a6a6a6666669
            666a666666666666666666a66666a9a69669a6a666a98a6a9a6a6a6a6a98a9669666a6a669666a6666666a969a69d1dd19b6a666b6a989669666a6a696a6b966969696a966969666a966a969696a96a9669a669a696a6a98969a6a696a696a6a969a96969a96969a6a966a989a96969a669a966a69a6a969a696969a6b6a6a666a6a669866966a66969a696a6a96669a696666a6669a66666666666666a6a6a6
            a6666a6a66a6a6a9a6a9a666a69a666a6a666666a966696666669669666966a66a96666a6a69a696a9a6966a69d1d9111d696b9a6966a6b6a9a96969a96986a989a6a966a989a9a9669a96a6a9698966a9a69a696a696969a6a9696a969a69696a696a69a696a98966a9696a966a6a696a666a96989698989a6a6a6696a6966b696698a9a6a666986a666a669689a666a6a66966a666a9a6a69a6a6a98966666
            66a666666a669666666666a966a6666666a6a9a666a6a6a6a9a6a6a6a9a6a696a66a9a9696a666a66669a696b91d11d969a6b6669a6969a96666a9a666a9696a966966a9669a6696a966696966a9a69a9696696a969a6a669696a96989896a98969a696a966a96a9a966a696a699919a696b966a6b6a69a66696696a6696a696a6a6a9666966b6a966696698a66a66a66669a89896a6666698666696898a6a6a
            669a6a9a6698a6a6a6a6a966a666a9a6b6966669a669669666696696666696a69696666a66969696b9a66a66111191119a696a9a669a6666a9a96669a966a96989a6b9669a6969a696a9a6a9a9669a696a69a6966a96969a9a696a6a9a96969a9a696a9669a9696696a969a6119bdd919b66a9696969a669a6a96a696a6698a69696666a66a96666a9a6a6a966966966a98666a6a669a6a66a6a98a66a666966
            6a6666666a666669669666a669a666666a6a69a6698a6a66a986a66a96a98966a6a6a9696a6a6a6a666969a9d1911d1d191a96696a69a9a96696a9a696a96a9a969a669a696a9896a969696696b9696a969a96a9966a9a9669a6969696a9a6a9696a9669a696a69a999b6a999d11911d11996a6a6a6696a69698966a969a6966a66a9a969a66a9a666669666a6a6a6a966a9a69669866698966666698966a66a
            666a6a6a669a69a6a66a66698669a6b696698666a696969a669a9696a666a6a9696966a66969696969a6a661911d19119d999a9a969669669a6969698969a966a9696b69a969a96969a6b6b9a69a6a969a69696a6b96966a969a9a9a69669696a69669a969a999a6939d199dd9d1d91916bb9696969a6969a6a989a66a669a6969a6666a66966669a9a6a6a966966666a66666a6a6a9a66a6a6a9a6a66a666a6
            9a6966966a666a6666a69a6a69a6666a6a66b6a966a6a6669a666a6696b69666a66a696a9a6a6a6a6a9999d11d1111d119d9b9966b6a9a9a69a6a96a9a966696989a96b69a696a9a96969a969a69696a969a6a9969a6a996a9669669a9a9a9a969a9a96a9691d19911d191d11191d1d1d996a9a6a969a6a69669a696969a669a66969a696a6a9a69669669666a6a9a6966b6a96669666a69669686666a69a666
            666a66a66989a666a96666698666a969669a6966a96696a9896a969a6a96a9a969a96a9666969696966b19d191d91d191d99b9a969a9666969696a9696a9a9a9a966a96b69a69696a9a696a9696a9a969a69969a96996a969a9a69a966969669a9696a969a191d1d9d91d1919d191919d9d999699a989696a9a696a9a6696a669a6a696a6969696a9a69a66a966666a6a98966a6a66a6986a6a69a69a66666b6
            a666a669a66a669a66a9a6a69a696a6a6a666a6966a9896a66966a6696669896a666966a9a6a96a96a96d9d111111911d9b9a696a9669a9a6a9a969a696966966b9a969a969a9a69669a9696a969696b696a9a69a6a969a96969a969a9a9a9a966a9696b619d9b9b9d191d1d1d1d9dd9dd1dd9d9b969a9a96696a96669a6969a66966a696a66a69669a66a966a96a96666a6a696698966a9666666a6669a66a6
            69a696a666a698669666696a66a66966969a966a696a6a696a6a969a6a9a698969a98b966969896a966b6b91d91d11d1116a96a9669a966996966969a9a69a9a96696b696a96969a9a969a9a96b9a9a96b969696996b969a9a9696a969669696b969a9a999d6b696a96b99b99d9d9d919d99d9dd9b9b6666b6a966a9a69a6a696a6b9698969a96a6b669666a966a669a969696a6a698a966a69a6966a666a696
            a666a666a9666b6a6a9a6a696969a6a6a6666a96a696969896966a6969669a6a966696a9a69a9a9669b969d111d9191196969696b9a96b9a6b6b9a69669a96969a9a969a969a9a96969a96969a9696969a96b9a9a69a6b6969a9a969a9a9a9a96b9a9696a9b969a969a96a96a969a9b9a9b9dd99d999a9a96966b9696966969a999a69a989898969a69a9a966a969866a6a66a6966a966a666a66a669a669866
            66a9669a66a96a969666966a6a66696969a969896a6a6a69a6a9696a6a9a696989a9a69669a66669a99a9a11911111d91d9a9a69a969a96969a969a9a9696a9a96969a969a96969a9a969a9a969a9a9a969a96969a9969a9a96996b969696969a96969a9696a9a96b96a969a96a96966969a96d9d9b99969a9b96a989a9a6b666a696a66b6b69a669a96d989666a69a96696a966a966a6696966989a666a69a6
            a966a666966a666a66a6a96969a9a6a6a66a6a969696969a696a6a9696696a69a69669a69b969b9a9696911d1d191d11dd1199b969a9619a9696a96969a969696a9a969a969a9a96969a96969a9696969a996b6b969a969699ddd19a9a9a9a9696b6b969a9a96969a96969a96996b6b9a9696a9a9b9a6b9a969a9669a66969a9696a96969a6989a661919d9a9a9698989a66666966a6966a6a6a6a666a96a666
            98989a9a6a969a969a9666a6a66669696969698a6a69a6696a969699a116a96696a9a696d9a99a966ba9d1911911d1911191d119a969d911b6a996b6b96b9a9a99696b969a96969a9a969a9a969a9a9a969b99b9a969a9a9a19191d1996969a9a99a96a96969a9a969a9a969a9a99a969a9a969696a996a69a696a9a969a966b9a996a9a696a9669d9ddd196666a69a669a9a9a6a696a6966969696a966666a6
            a6a96666966a666a6669a96969a9a6a6a6a9a69969a69a9a696a96a9111119a9a96969a99b9d9699a96d111d111d111d91d9d9d9d99d9dd9119b69a96b96b9696a9a96b9a969a9696969b96969a9696969d939199a969696191d1d91d19b9b9696969b9b9a996969a96969a9696a969a96969a9a9696a996969a96966b6989a99d6d96696a966a99dd19d9b9a9696a69a666666966a698a9a6a6a6666a6a9696
            9666a69a6a69696969a666a6a66696969696698a969669896a96696a919191199939d119b969b939999d191191d19191191d19d19dd9d91111119b99a969a96b9969b9a969a99b9a9b9a969a9b969a9b9bdd1dd9d9b9a9b99d191d191dd999a9b9a9a96969a9a9b9969a9b969a9969a969a96969a9a969a9a9696a9a969a9696d9a96b9a9669a9b9d9d19166989a6966969a9a6a9696a966669669a96696a6a6
            a69a96a6966a6a6a6a69a96969a96a69a6a9a696a989a96a969a9a9696d1d1d11d1d191d11dd9d9b9b11d1d9d1911111dd9919d119d9d9dd19d1119b96b969a96a9696969b969a9969a969a9969a9969a919d9d9d969b96bd1d191d1919d9a969a9969a9a969969a9a9969a9b969a969a969a9a96969a9669a9a96969a96b9b9d99b966669a96919d19dd9a9a9896a9a6a6669666a66989a9a6a666a6a669666
            96a66696a6969696969669a6966a969a69669a9696a96a969a69666a9a96d19d11911d11911dd16d9b91191d9d91d1d191d1d9d919d9b9a9699b9d969a9a969b99a9a9b9a969a969a9969b9b9a99b9a999d9d9dd9a9a9699a9191d91dd9d99b9696b9b999b9a9a9699a9a9969a969b969b9a96969a96969a96696a9a9669a9d9a9b6a9a99d69dd91d9d919966d9b96696969a69a969a698989696a96969a6a98
            a969a6a696a989a6a989a696a9696a6969a9669a696a969a9696a996969a99d91d11911d1d19119d911d1d9119d9199119d91d9dd9d99a969a969a9a9969b9a9699b969a99a9969b969b9a9699a9699b9b99b199b9699a9b99d1d1d1919d9b99a99a99a69a99699a969969a969b9a9a9a96969a9a96b9a969a9a96969a96969a9696969a99a191d9dd1d9361d91d919a6a9896a69a696a966a66a96a6a666669
            66a69696a966a96966b696a96a9a969a696a9a69a96969a969a969a9a6966a91d1911d1911911d1dd1d1911d919d9d9a99d19d91d99a969b969a9969b9a9969b9a969a99699b9b99a9b9b99a9b969a9dd91d9d9a99a999b961919191d9d9d9d99b99a999b969b9a99b9a9b99a969969969a9b969969a969a96969a9a969a9a969a96a969a99d9d919d9d91d9dd9ddd9d969a6969896a6989a9696669669a9a6a
            9696a6a966a966a69a96a96696669a69a696969699b9a969a696a9669a9a9969911d191119d191d1191119111d9d9d9d9b9b19d9b9b969a96b99a9b96996b9a969b9b9b9b9a969a99b969a9969b9b911d1d1dd99b99dd9ddd1d1d1d1d9dd19dd99a996b969b9a9969a99b9699b9a9b9a99969a9a9a996b969a9b96969a96969a69699b996d9d1dddd91dd9dd91d919d99a696a96a9696a9666a6a9a66a666966
            a6a969669a969a96a9696a9a9a9a696969a9a6a9d1d99b9696a969a969696a9a69d1111d19d9d9911d99d1d9119dd99b9999a969a969a99699b96969a9a99a99b969a969a99b9b969a9b9969b9a99dd919191d119dd91d9191919d1919d9d19dd99b99a9b9a9969b99b969a9a9969a996a9a9969b96b99a9b969a96b969a9a969a9a9da99dd9d9191d919191d9d19ddd996a96a966a6966a96969669a969a6a9
            6966a9a9669a696969a6969669696b6a96969999d1ddd9da999a969a9a9a9699a99d91d19d9d9dd999dd91d1d1d99b99a9a969a996b99b9bdd91ddd9969b99699a9999a99699a99a9999a9b9b999b11d1d1d919dd91d1d1d1d1d191d9d91d19d9d9b9b99b9969b9a9a96b99b96b9b96999b96b9b969a96969a96969a9a96969a9696999dd91d919d9dd9ddd9d9d9d99d9d969696a969a696a9a6a9a666a69666
            a9a966989a696a9a989a9a69a9a9a9969a9a6a9d1d191119d169a969696969a969a9d1919d9d9a99ba99b999d9d9d9a969b9b996b99a969d911d191dd9b969a9b9b6b99b9b9a9699b9a99b999a9d1919191d1dd91d19191919d191d19d1d9d9d9d9999a99a9b9b9999b99a99a99a99bbb969b9a969d9b9a9b969a9b96969a9696b6ba9a91d9d1ddd191d9191d9dd9dd9d9db6a9696a969a966969669a96989a9
            66969a69a96a9696a96969a9696966a9a9696961d9111d1119d969a9a9a9a969a96969b9d9d999b96969a9b999b9a969b96969a99a969a111d191d1919b9a99b9699b9a99a999b9b9b9699a99d91d1d1d191919d9d91dd1d1d191d9d9d911d9d9dd9399b999b99a9b99a99b99d99b9996b9a999b9391999b96b99a969a9a96b9a99969619d19d99d9d91d9d9dd919d9d9d99a96a6966a6669a6a69a6696a9666
            9a6a69a966969a6969a9a969a9a69b9696a9a9a9111d191919da9696969696b969a9a99a9b9a9a969a9b969a9a969b9a99a9b99a99b999d91d11d91dd99b9b99a9b9a99699b9b9b9969b9b9d9d1d91919d1d19d9d9d91919d91d1d19d9dd91d9d9d9d9d9b9a9b99b9a99b99a99d99b9a99b9b969b91ddd99b99a969a969969a969a69a9d9d9dd1d91d9d9d1d919dd9d9d9b96699a9a9969a969698969a6989a9
            a96969669a9a969a969696a96969a96b6996969d11911111dd999a9a9b9a99a9a9969a96996969b9a9969a9699b9b969b999a99d996b9d1119191119d9b999a999b99b9b9b99699a9b9b99d9d1911d1d1919dd9d9d9d1dd11d19191d19d91d9d9d9d9d9d99999a9999b99b99b9a9d9b9b99b9a9b19d9193d1d99b9969b9a9b969a99b9191dd9199d9d9dd9d9d9d9d9d9d9a69a696696a9a96a9a96a9669a6966
            69a9a69a96969a96a9a9a969a9a969a99a9a9a99d11d19d191d9b99696969a96969a9969a9a9b969969a999b9a969a996b699b9ddd19b19d11d1d1d19d9b9a99b99a999a99a9b9b999b9b9d1d1d19191d1d191d1d19d9191919d1dd91d1d9119d9d9d9d9b9a9b9b9a99a99d9a999a9999b1999b91d1dd9d9d91d9b9a969969a9696a99dd9d91ddd9d9d9dd9d9dd9d9d9d999a96a9a9696669669896a9a696a6b
            966969a96a9a96969696969a9696b969a96996d99d191111d1119d9d9a9a9699b9b969b99b969a9b9a99b9a9699a99b99b9a9911911d1d11d191191d99b9b969b9a99a99b999b99b9a999d1d9191d1d919ddd19191d1d1dd1d1d911d919d19dd9dd9dd9d999b999b9b99b9a999b99b9a99b1dd919d919d191d9d99b99a9bd969a999d9d91d9d99dd9b99d9d9d9d9d9d9d93999d9696a9a9a9a96b969696a969a
            6b9a9a969696a9a9a9a9a9a969a969a969a9b9dd1d111d911919d9d9d999b9a969a9b9a969a99969b9b9699b9b99b96b99b99d1d11d19119111d119d199a999b999b99b99b9b9b9b99b9a91d1d19191d1d9b91dd1919d919191d19d1d1d9dd91d9d9d9d9db99a9b999a9999b19b9d99b9b999d1dd19dd9d19d9d9b9699b99d9d9b9d9d1d9d9ddd91d9a969b99d9dd9d9d9d9dd9d9a969699999a96a9a6966a96
            9a69696a9a99696969696969a969a969a9699d91191d911d1d19d9d9d9b9699a9b96969b9b96b9a9969a9b969a969b9939dd1d1191911d1d919191d9d9b99b9b9a99b99b99a999a99b999d19191dd1d91d9bd9d91dd11d1dd191d1919d119d919d9d919d9d9b999b9b99b9b9b99b9dd999b9b19d9d19d19dd9d9d9a9a969a9d9d99b9d9d9d9999d99b96b9a9a969a9b9d9b9d9d9d99d9d9b9b96a9669a69a96a
            969a9a9696a9a9a9a9a9a9b969a9969a99a9a91d1111111911d9dd9d9d9b9a99699a99a99699b99b9a9996b9b99b99a911191d91111d19191dd119d9d99b9b99b99b9b99a999a999b9db9d1d1d191911d9bdbd91d19d919191d91d19d99d9d9dd9d9d9d9d9d9b9b999b9d9999a99dd1dd9d9d91d19d19d9d9d9d99969b9a99d9d9b9d9d99b9b9a9a969b969696a9696b9a9d9b9d9d9d9d9dd9a969a969a96696
            9a96969a996969696996969a9696b9a969999111d91d1911d1919d9dd9d99b969a99b996b9a99a9699b9a99b9b99a99d9d911911d91191d19d99dd9d9d99b9a99b999a999b9b99b9999b91919191d1d9ddb9dbb91911d1d1d91d19d1d19d9dd9d919d9dd9d9d999b9a99b1ddd9b999d91dd9dd91919d91d9d9d9db9b99a999d99b999b9a99a9b9699a96b9a9a9969a96969a969a9b9b9d9b9696b696a969a9a6
            969a9a969a9a9a9b9a9a9b969b9b9699b9a1d1d9111911d1911d9d9d9d9d99b9b9b96b99b99a99b9a9999b9969a99b9d9d91dd9d11d1191d191d9d91d939999b99a999b9b999b99bdb9d1d1d1d1d91d19b9b9b9bb1d919191d191d1919d9d9d9d9d9dd9d9d9ddd9b99b99b919d9ddd91d9d191dddd1dd91d9d9d999a9699b9a9a9b9a969b96969a969a9696996b9a99a9a996b9696a96a96a9a969a969a69696
            b9696969a9699696969969a9b9a969a9696919111d11d1111191d919d9d9399b9969b9a99a99699b9b9a99a9b99b999d9d9d9d9d9119119d19d9d9d9d99b9a99b99b9b999b9d1dd999b191919191d19dbddb9db9c6d1d1dd191d9d91dd9d9d919d9d9d9d9d9d99d9b99b99ddd9d9d1d91d9d191919d91d9d9d9ddd999b9a9699969a99b969a9a996b9969a9a9a969696996a99a9a996969a9696b969a9696a9a
            9a9a9a9b969a9b9a9b9a9b969699a999a9b9d1d191191191d1d9d9dd9d9d9d99a9b9b99b9969b9a99969b9999b99a9d9d9dd9d911d11d1d1919d19d9ddd999b99b99b9b9b9dd919d9391d1d1dd1d911d9b9db9db8c89d9191dd19dd9d9d9d9d9d9dd9d919d9d9d9d9d9d9b9911d19d91d91ddd9dd91d91d19dd99ddd9b9969b9a99969a9a996969b96b9a9969969a9a9a9969a9696b9a9a969a96a9696b69696
            969696969a9969a99a96969a9b9a9b99999b19111d11d1d1919d911d9d9d9d9d99a99a969a99b99b9a999a9a99dd99d9dd919d9d19191d11d11d91d9d99db99b99a999b99dd11d1d1d11919d9191dd9bdb9bdb9d66c6b9d1d9191d9d9d9dd9dd9d9d919d9dd9dd9d9dd9d1ddd91d191dd19191d1919d19d9d9d9d999b9b9b9a99a9a996996b9b9a9b9a9969a9a9b996969a96969a9696969b96999a9a969a9a9
            a9a9b9a9b96b9a969969b9b99a9969a9393919d191d19119119dd19191d99d9b9b96999b99b99a9999b9b999b111d9d9d9d91d19111d19191d11d919d19d9b9d9b9db99bdd9191919191dd11d1d191b9b9db9db9bbd6cb6d1d1d19d9d9d9d9d9d9d9d9d9d9d919d9d9d9dd9119d91dd919ddd919dd19dd91d9d9d9399b969b969969b9a9b99a996969969a9969969a9b9a99a9b969a9a9b969a9a6969a9a9696
            9696969b69b9699b9a9b9a969969b99b99dd19d111911d19dd9d91d9d9d9319a999b9a99a99a99b9a99a99b99d191dd19d9d91d11d9111d119191d9d9d1d99d9d9d99b99d11d1d1d1d19d99d9d9d19dbdb9db9bdb9b6b6b689d911d9d19d919d9d9d9d9d9d9d9d9dd9d9191d91d19d19d1d91d91d9dd91d9d9d9d9d9b9b9a99b9a99a9969a9969a9b9a9b969b9a969969969969a99b9969a9a9699a969696b6b
            9a9b9a99a99a9b9699b9699b9a9b9a99a999dd9d1d11919d9d919d919d9d99b9b9a999b99b99b99b9b99b9b91d1d19111d919d19111d91191d1d91d9d919d9b9d9d9d939d9191919191d9dd9d919dd9b9db9bd9b9bb6b6b6cb119d19d9d9d9d9dd19d9dd9d9d9dd919ddd191dd91d91d191d91d91d91d9d19d9d9d99b9999b9699b9969b9969a999a9969b9a969b9a9a9a9a9a99696b9a96969a969a9a9a99a9
            699a99a99699b9a9a969b9a999b969b969a961d91191d9d919dd19ddd9d9d999699b9a9b99b99a9999b999b1d19111d911d9d11d19111d1d1919d9d9dd9dd99d9d9b199d11d1d1d1d1d91d911d19db9db9db9bdbd9b6b6b6b69d191d9d9d9d9d99d9dd9d9dd9d9d1d9d91dd911d91d919d91d91d91d91d9dddd9d9b99a9a99a9b969a9b9a9b99b69969a99699a9969969969996b9a96969b9a996b9696969696
            9a9696969a9a96999b9a9996a99a999a99b9d9d1d1d19d9d9d919d9919d99a9b9b99b999a99a99b9a99a9b99d11d9111d911191911d91919119d1d9d9d9d9d9d9b99b1dd1919191919d1911d91919bdb9bd9bd9b9b6b6b6b6c9d1d191dd9dd9dd9dd9d9d9d9d9d9d91d9191d9d91d1ddd1d91d9dd91d9d19191ddd9b99b96999a9b999a9969a99a9a999a9b9a969a9a9b9b9a99a99b9a9b96969a969a9b9a9a9
            b99a9b9a99b999a969b96b999b99b969b999dd1911919dd9d9d1d9ddd99399b9b9a99b9b99b99b999b9999a99d911d9111d1d11d1d11119dd19d9d919d9d9dd9d9dd9d91d1d1d1d1d19d1d911dd1b9b9db9bd9bd7d6b6b6b8c9d9191d19119d9d9d919d9d9d9d9d91d1d91d191d19d919d9d9d191d9d19dd9d9d999b9b99b9a9999a96969b9969999a96996999b99b9969a969a969699969a9b99b9a99696969
            6b9969b9b996a99b9a999b9a99a99a999b939111d11d19d91d9d91991d99b99b999b99a99b9b99b9b9b9a99b9911d111919191d19191d9d9d9d9d9d9d9d9d9d9dd191d1919191919191d91d91919bddb9dbd9bd9bd6c6b6b6c9d1d1d91d191d91d9d9d9d9d919d9d19d91d9d19d91d9d191dd9dd9d19dd919d9d9d9a99a99b9b9a99b9b9b9b9a9a969b9a9b9a99a996b9b99b9969a9b939a996b69696b9a9a9a
            99a9b9969a999b9699b9a999a99699b9a999d1919191191d9d9d9ddd9dd9b9a9b9b9b999b999b99b999b99b99d9d91911d111d91111d19d9d9dd919dd9dd9d19d9d1d191d1d1d1d1dd91d1d1d1db9b9db9b9bdb9b9c6c6cb6bb919d1d91dd91d191d9dd9d9d9d9d9d191d191d1d191d91d919191d9dd91d9dd9d9d9d999b999999b9699a99699969b99b99699a996b99a969a9b9b9d9d9996b99a9b99a969969
            b9699a9b99a9b9a9b99b9b9b99b9b99b99b9d1d11d1d1d19d9d9191919d99b999b999a9b9b9b9b99b9b99d9b9d99d11d191d11119d1919dd9d9d9dd9d9d9d9d19d9191d191919d19d91d191919d9dbd9bddb9d9bdb6b6b6c6b6dd19191d911d91dd1d19d919dd9d19d1d9d19d9d9dd91d9dddd19d191d9d19d19dd9dd9b9dd939b9939b969b9a9b99a996b9a9969b9a999a9969b9d9d9d9a99a999a9699a9a96
            9b9a999a99969999b9a999a969b99a99b99dd19111911919d9d9d9d9d9d9b9b9b9b9b99999b9993d999399b99b9391d19119191d1191d191d9d19d9d9d9d9d9dd91d1d191d1d191d11d91d91d1bdb9bd9b9dbbd79bb6b6b6c6c9191d191d9d1d91919d119dd9d9d9d191d91d191d191d919d919d9dd9d19dd9dd9dd9dd9d9d9d9d9d9999b9b99b9a996b99b9b9b99b969b99b9b99dd9d9d9b996b969a9b9699a
            99b96b99b69b9a9b999d9999b99a99b99a999d1d911d11d9d91d9d9d9d9d999999b99b9b9d9b9d91db99d9939d99d1911d1d119191d11d1d9191d9d9d9d919d19d91d91d19191d19d91d911d9d9b9db9bdb9d9b9d6b6b6c6b6bb9d19dd191d91d9d1d9d9d9d9d9d9ddd91d9d91d9d19d1d9d9dd1d91d9d9d919dd919191d9dd9d9d9bd9399a96999b999a99969b9a99b99a9969d9d9d9b969a99a99b9969b9a9
            699a99a999b9b9969b11ddd99a99b99a99ddd9111d191d1d1d9d9dd9dd9ddddd939b99b99399dd19d9d9dd99d9d9d11d191191d1d11919111d19d9d9d919dd99dd1911d91d1dd91d1d911d911b9db9bd9b9bb9dbb6b6b6b6cb66d91d191d191d91d911d1d19d9d9d191d91d1d91d9d19d9d919d91d91d9d9d9d9d19ddd9dd9d9dd9d9d99d999b9a99b9a99a9b9969b99a9969bd9d9d9d99b99a996d9a9a9699b
            9a99b99b9d9a9b9b91d111dd99b99b99b999d1d91911191919d9d919d919d99d99d9b911d9bd911d9d9d9dd9d9d9d99d11d1d1d191d1d1d9191d9d1919d9d9d9d91dd911d91911d911d9191d9db9bd9bdb7d9bd9c6b6b6cb66b6dd919d19d191d919d9d99d9d9dd91d91d9191d91d9dd9dd9d19d9dd9d9d9d9d9d9d9d9d919d9d9d9d9dd939b9b99b999b99b9a9b99a9969b99d9d9d9939b9b99b99b999b9a96
            99b99a99b99999b9d1919119d99b99a99b93191d9d9d911d1d19d9d9d9d9dd9ddd9111d1d9911d19d9d9d9d9d9d9d9d99d919191d9d91d11d1d91d1dd9d9d9d9d919d9d91d1d191d9191d19db9bd9bdb9d9bdb9c6b6c6b66bcb6b91d19d19d19d9dd919dd9d9d91d91d91d9d91d91d91d91d9ddd91919d9d9d9d9d9dd9dd9dd9d9d9d9d99d99b9b99b9a9b99999b969b9b9b939d9d9399d999a99a999b99b99a
            9b9a99b99b9b9a999d11d1d19d9b9b99b9d1d19d9dd91d19199d9dd9dd9119199d19d191d1d1d911d19d9d9d9dd9d9dd91d11d1911119191d911d919d9d9d9d91d9d9d9d91919d1d19d9dd9d9bdbd9b9bbdb96b6b6c6b6cb66b6bd91d191d19d9d9d19d919d9d191d91d91d1d91d91d91d91d919dd9ddd9dd9d9d9d9d9d9d9d9d9d9d9d939d99b9b9a9999a9b9b9b999d9d99d9dd9d9dd939b9699b69d9d69a9
            9999b99a99b199b9b1d19191dd99b9b99b991d9d919d9d111dd919d9d91d1d9dd9d91d1191d111d19d9d9d9d9d9d9d9d91191911d9d1d1d111d911d191d919d19d9d919d9dd9d919d9dd91d9bd9db9db9b9d6cb6c6c6cb66bc6b6dd919d19d1d19d9d91d9d9d1dd91d91d919d19dd91d91d9dd9d91d9d919dddd9d9d9d919d9d9d9d9d9d99b9b99999b9a9999b999a9b9d9a9dd9d9d9d9d999d9b99b9a9d999b
            9a9b9b99b99b9b99991d111111d9999b99b911d9d9d9d19d19d9d9d9191d9d9d9d1d99d1d191919d19d9d9d9d9dd19dd1d1dd1d91d9191919111d9191d1dd9dd19d91d9dd91d19d19d9d19dd9bd9bdb9b6bbb6b6b6c66c6c6b6a6b91d1d91d919d9d9d9dd9d19d91d91d91dd9dd91d9dd9d191d9d9dd9ddd919dd9d9d9d9d9d9d9d9d9d9d9b9d9a9a9999b9a99dd9d99d9d919d9dd9d9ddd9399b9a9999d9b99
            b999969b9a99d9b9b9d191d919d9bb99b99b9d111d9d19d9119d91d9d1d9d9d9d919dd99d111d119d9d9d9d9d9d9d1191919191d9d91d11d19d911d119191d9d19ddd9d9d191dd91d9d9d1b9bdb9b9db6c66b66b6c6cb8b6b8b6b819d91d91dd19d9d9d9b19d191d91d91d91d91d91d91d9d9d91dd919d919d9d91dd9d9d9d9d9d9d9b9d9b9d9d999b9b99b9b96d9d9b9dd9dd919dd9d9d9d9b9d99d9b99b9d9
            9a9a9b9999b9a9dddd11d111dd9d99b9b9b9999d9119d9d19d9dd9d91d11919d9d9d9d9d99d919119d9d9d9d9d9d99d11d191d99d9d919d19111d919d1d1d9d99d919d919d191d1919d9d9db9b9bdb9c6f8c6c6cb6b66c6b6c6c6c61d191d919d9d9d9db9b19dd91d91d9dd91d91d91d9d191dd9d9d91d9dd919d9d91d9d9d9d99399d9d99d9d99b999d9d999b99d9dd9d9d9dd9d9d9dd9d9d9d9b9939a99b9b
            9999b9b9a99911191191191919d9b99b99b9b939d91d9d9d91d9d9d911911d1d919d9191dd91d19d9d9dd9d9d9d9d9d99d9dd19d9d9d91d1d19d11d1d919119dd1d91dd1d19d191d9d9d9db9dbd9b9b6c6c6c6c66b6cc6c6c6c6b8c99dd91dd9d9d9d9b9dbd191d91d9dd91d91d9dd919d9d9d9191dd9dd91d9ddd9d9d9d9d9d939d9d9dd9a99399b9a9d99b9d9b9d9d9dd9d9dd9d9d99d9b9d9d9b9999b99d9
            b9b99b9b9b931911d1d191d1d9d9d9b9b9d9d99d9d9d9d9dd9d9d9dd1d1d1911d1d19d9d91d91d1d9d9d9d919d9d9d9d9d9d9d9d9dd9dd9191d19199d9d1d91991d1d919191dd1919d9d9b9bd9bddb78c8c66b8bc6c6c6c6c6c6c6c6d91d919d9d9d939bd9b9d91d9d19d9d919dd919dd91dd9ddd99dd919d9d9191d9dd9d9d9d99d9d9d9b9d99b9b9999bd99d9d9bd9d9dd9d919d9dd9d9d99b9d9b9b9b9a99
            9b9b99b999d11d191911d119d9d99b9d99b9939d9d9d9d9d9d91d9d9191911d91d91d91d9d9d9d91d9d919d9dd919d9d9d9d9d91d919d91d1919d1d1919d1ddd191911d91dd919dd9d9db9db9b9b9d6c8ccc6c66b6b68c8c6c6b8c8c9d9d9d19d9d9dbd9bdb9dd91d9d9d91dd9191d9d19d91d919dd919dd9dd9dd9d9d9dd9d9d939939d9d99399b9bd9399b939d9d9dd9d9d9d9d9d9dd9d9dd9d9d9d9b999d9
            bd99a99b9b19191111d9119d9d9d9d9939d9d99b9dd9dd919d9d1111d111d111911d9d9d9d919d1911d9d9dd919dd9d9d9d919d1d9d19d9d9d9d9d9dd1d9d9191dd19d1d911d91d19d9d8c6bdbd9bd6c6f6c6c6c6c6cc6c8c8c6c6f66d91d9dd9d9b9b9b9b9bd9d91d9d9d9d9ddd9d19dd9d9d9dd919dd9d9d919d9d9d9d9d939d9d9d9d9d999b99b99b9d99d9d9d9d9d919dd9d9dd9d9dd9d9d9d99b99b9a99
            d9dd9b99b111d11d9111d19dd91d9b9d99d9dd9dd9d9d9d9d9d9d9191d919191dd919d9dd9ddd9d1d919d9d9d9d191d9d9d9d9d91d9d9d1d19d9d9d99d1911d1919d19d1d9d1d919dd9b8c66b6db9bb6c6c8c6cc6c6c6f6c6c8cc68c6b9d9d9d9ddbd9bdbdd9bdb199d9dd19191919d9d91d91d9d9d9d9d91d9dd9d9d9d9dd9d9d9dd9d9dddd9d9b9b9999399d9dd9dd9dd9d9d9d9d9dd9d9d9d9939d9d9b9b9
            9d9999b99d9119111d9191d9d9d9d9b9d9d9ddd9119d919d9d91d91d11d1d1d1911dd1919d99d99d11d9d9d9d9d91d9d9d9dd9d919d9d991d9d9d9d9d191d919d1d91d91919191dd9b18c8c6b9b6db6c8cc6f6c8c6c6c8c8f6f6cc6c6c8c99d9d9b9bd9b9b9b9b6b9d9d9d9ddd9dd9d19d9dd9d91d9d9d9d9dd9d9d9ddd9d9d9dd9d9d9d999d939d99b9b9d939d9d9d919dd9d9bd9dd9d9dd9d9399d9d9d999b
            9dd9b9b9b11d1d191d1d19d9d9d9d99d9d9dd91191d9d9d9d1d91d919919191d19d919d1d9d19dd9d91d91d91d91d9d9d9d91d9d9d9d9d9d9191d9d9d9d191d1d91d91d1d1d91d9bd88c6f6bbb9bd9b6c6f6c8c6f6c666c6c68c6f8c6c6c8cb99c9b9bdb9dbdb9b6b9d9d91919dd919ddd19d9dd9dd9d9d9d9d9d9dd99dd9dd9d9d9d9dddd9d99d9d9b9b9d99d9d9d9dd9d9d9b9bd9d9dd9d9d9939d9d99b9a9
            999dd99b9191911d1919d9d9d9d9d939d9d9111d1d11d9d9d91d11d1d1d1d9d9d911d9d919d1d9d991d11d191d19dd9d9d9d919d9d9d9d9d9d9d19d9dd191d9d1d91d19d9d91d1b9db6f68c66db9bdb6f68c6f6c6c6cc6c8cc6f6c6c86b8c88d6cc9bd9bd9b9d6b6b6d9dd9d9d91d9d9d9d9d9d9d9d91d9d9d9d9d9ddd9d9d9d9d9d9d9d9939b9d9d9d9d9dd9d9dd9d9d9d9d9bd9b9d99d91d9dd99d9bd9b99b
            9a99dd99d1111d919d9d19d91119d99d9dd1d191919119d911d191919199d9d9d9d9d9d9d919119dd19191d191d191119d9d9d19d919d9b9d9d9d9d99d91dd19191d9191d1d91b9bb8c6c8cc8d9bd9b6c8cc6c8f68c66c6c6c6c8cc6c6c6c6c6c86c6bd9bdb9b6b8c8c99d9d9dd9d9dd919d9d9d919d9d9dd9d9d9d99d9d9d919d9d9d9d9d99d9d9b9d9d9d9d9399d9d9d9d9b9bb9b939dd9d9d9dd9d99b9b99
            b9b9d9d9dd91d11d19d9d9dd9d1d1dd9d9d191d111d19dd1d191d1dd1d9d9d919d9d919dddd1d1d191d1d91d191d19d1d9d9d9dd9ddd6b8d9d9d9d9dd91d9191dd91d91d91919db9b6c8c6f6f9bd9b9b6c6f6c6c6c6cc6c8ccc6f6ccc6c66cc86c8c6bb9b9dbd8c6c68cc9d9d9d9d9d9d9dd9d9dd9d9d9d9d9d9d9dd9d9d9d9d9d9d9dd9d939d9d9d9d9d9d9d9d9d9d9d9d9bdb9db9bd9d9d9d9d9d9d9b9a69b
            999b9d9d911d1919d9d9d9d9d9d9191d9d191d191d91199191d191999d9d9d1d9d9dd9d19999191d19191d191d91d1919d9d9d9d1968bb6b9d9d9d9d919d19dd91d91d919d1db9bb8cc6f66c9bd9bdbd8c6c8f68f6c66c6f66f68c6cc6c6c66f6f6c66dbdb9b6c6c8c8c6c9d9d9d9d9d9d9d9dd9d9dd9dd9d9dd9d99d9d9d9d9d9b9d9d9d9d9d9b9d99b9d9dd9d9d939d9db9b9b9bd9bb9b9d9dd9dd9b966b69
            b9b99bd1d1d911d9d9dd9d9d9d91d1919d9d191d1119d9d1d191d9dd9dd9d9d1d119d9d9d9dd9d191d1d191d91191d1d9d9d9d99b8cc8b6c99d9d9d9ddd91d19191d91dd19d9bd66c6f6c8f6bd9bd979c6f6c6c6c6c6c66c6c8c6f66cc876c6c86c8cb9b9db6c8c6c6f68c88b99d9d9dd919d9d9d9d9d9d99d99d9d9d9d9d9d9d9d9d9d9d9d9d9d9d939dd9d9d9d9d99a69b9bdb9b9b9c6c6d9d9d99b9ba66a6
            9b9b999d1911191d9d9d19d9d9d99dd9d91d9d919d19dd1d191d19d9d9d9d9d919dd1d9d9d9d9d1919191d911dd1919d9d9d99dd8c6866b6b9d9d9d9d91d9191dd91d9d9dd9d9b6c8c68c6c6b9bd7bdb66c6c8f6c6c6c8c6f6c6f66c6cc8c6c6cc8c66db9b6b8c6f686c86cc6c6d9d9d9dd9d9d9dd9d9d9d9d939d9d9d9d9d9d99d9d9dd9d9d9d9d9d6d9d9d9d9d9b9b9bb9b9b9bdb9c6c6a6b9d9399d96b96a
            999d9b99d1191d111d9d9119d9d9d9d9dd91d1d1191d9191d1191d19d9d9d9d191d91919d19d91d1d1d191d19191d9d9d99dd9bb68ccc6bbb9d9d9d9d191b6b9d919d9d999bdbd8cc6f6f687bd9b9d9ddd8cc6c6c686c6c6c8c86c6c6686c6c68f6cc6bdb9bd6c66cc6ccc6c8c88b9d9d9dd9dd9d9d99d9d9b999d9b9d9d9d9b939d9d9d9dd9d9d9b9a6d9d9d9d9d9d9b9db9b9b9b9c8c866b6a6d9b9b9b6a69
            b9b9b9b9dd1d119191191d19d9d9d9d9d9d99199d1d1d1d191d1d911d9d9d99dd91d91d9d91d191919d91d91dd191d9d9d9d939b8c6f6b6b6b9d9d9d91d99b6a91d9d99ddd9b9c86f68c6cc6b9bdb9b9bb6c6f6c6cc6c6c66c6f6c66cc6c6c6c6c6c6c6d9d9b66cc6c6c66c6c6c8c6b9d9d9d9d99d9d9d9d9d939d9d99399b9d999d9b9d99d9dd9d99b69d9d9d9b9b9b9b9bdb9bd9b86c8c8c6b6a99b99996b6
            9b99b99d9191d1d11d11d9d19d19dd19d9dd91dd91919191d91911d919d19dd9191d19191d191d1dd11d191d919dd99d9d9bdb9b6c866bb6b69d9d1d19d9d999d99d9d9d9bb9b6c8c6c8c8c6cb9b9bdb96cc86f8c686c86c6f6c6c6c66cc66c6c6f6f6b9bbd9bb78c8c6c6c6f6c6c6bb6b9d9d9d9d9939d9d99d9b9d9399399d939b9d9d939d9d9b9b9b9d9d9d9d9d9b9bd9b9b9bb8c86c6c6c6b6b99bdba69a
            99b9939d9d11919191919d91d919d91d9d9d919d9d1d1d19d9d1d911d99d99d19dd91d9d9dd1919d99d91d191d1919d9bdb9b9bb8c6fc666bb69dd919d9b9bb69d9d9d99b9db6c8c6f6f6c6f6db9db9bd8c6f66c6c6c6c6c68c8c6c6c6c6cc66c68c68bb9d7b9bb68c6f6c86c6c8c6b6bbb9d9dd993999d9b9399d99b99d9d9d99d9d99d99d9d9d9b99a69d9d939b9b9b9b9b9bd96c6c6c8666c66bb99969a66
            9b93999d9d91d11d1d1d19d91dd1919119d9dd9dd9d9191d19d9d1d91d9dd9d9d91d9d9dd9191d19d91d9191d91d9d9b9b9bdb96c6f66cbb86bb919db6b9d9a6b9d99dbdbd9b6c6f6c68c6f66b9bd9b9b6f6c8c6c6c6c6c6f6c6c6c86c68c6c6c6c6c6b9b9b9d96c6c6c86c6c6c6c6b6b6b9d9d9d99d9399d99b9d939d99b9d9b9d9939939d9d9b9db69a9d9d99b9b9bdb9b9b9bb66c8c6c6cb6b66cb9ba669a
            9999bd9dd9d191d91191d1dd9191dd1dd1119d919d919d191d919191d9d9d9d1dd9d19d91d1dd9d9d9d91ddd91d9d9bdd9bd9bb6c86c86b6bb6b61d9b69b9b696d9399b9db9db8c68cc6f68cb9bdb9bd6c8c6c66c66c6cc6c86c68c6c6cc8c6c6c68c87bbd9bbb6c66c6cc6c6c6f6c6b9b6b9d9d9dd9d9b9d9b9b9999d9399b9d99399399d9d9d9b99b66b9b939b9bd9b9bb9bd9bb86c6c6b66b6a6b6b99b6b6
            9bd99dd9d1d1d11191d19191d91d1991919d1d9d9d9dd191d1d1dd1d19d91d9191191d1d9191919d9d9dd9191d91939b9bd9b68c8cc8c6b6b6b6cb999a6a996a699939db9bb9c68cc6f68c6c9bd9bd9bc6c6f6c66c6c66c68cc678cc6c86f6c66c6c6f66db9d9bd8c6c6666c6c66c6b6b6b6b9b9d9d99d9d9b9b9bd93999d9d99399399b9d939b99bb9b96a696b9b9bb9b9bd9bb96c68c6c6b6b6b66a6b99a96
            d9b9b9d191919191d191d1d111d9d9d91d191d191d9d91dd919191919d9199d1d91d9191d19dd9d9d9d91d1d919d9bdbd9bb6c8c6c6f6c6b6b6b6b9b96966a96ba9d9b9b9d9b8c6f6c6cc6f87d9b9bd6ccc6c66bc6b6c6c6b76b6c6c66c86c6c6c6c86c6d9bbd9b7b6b6bcb66c6c66b66b6a69b6b9d9399b99b99a699bd9b9d939b99b9b9d9b99bb996a6969a9b9b9b9b9b9bb9b6bb86f68c66c66b66b6b966a
            999b99d1d11d1d1d1d1d1919d91919d9d91d191d191d1911d1dd191d19d9319d19d1d91d9d9d91d99d99d99d19d9d9b9bb9c8c6cc6f6c6b6b6bb6b99bd9396b696d9db9bdb9b6c86f68cc86c9bbdb9b666c8c6c6b6c6b6c6d9db6c8c6c8c6c66c6c6c8cb9bd9bb9d9c6c6b6b6b6c8c6bb6b86c69a69d9b9d9b9b96ba999b9d999b9b6a96a99b6a969a969a96b9b9bb9b9b9b9b9bb96c68c68b6cb6a6b66a6b96
            9b9d9bd9191d919191911d11119dd9d9d1d91d91d1d91d91919191d9d19d91d91d9191d9119d99d9d9d9d1d99d99d9b9d9c86c86f6868c6b6b6b66ab99b69a96a969b939bb6c8cc68cc6ccc6bd9b9b7b6b8c6c66c6b6c6c9bb9b6c6f6c66c6c6c686c666b9bb9db9b6c6c686b6b66c6b6b6b6cb69a999d9b99b9b969639d9939b999b9696a69b96a96b96b6d9b9b9b9bb9bdb9b9b68c86c6c6666b686a666a6b
            1dd9b9111d1111d11d191919dd19d1dd9d1d9119d91d191d191ddd1d91d1d91191d1d91d99d9ddd9dd9d99d9d9d9b9bdb9c8c6f6c8cc6f66b6b9b6b6b8b9a6969a9b9bdb9c8c6f6f68cc6c6f9b9bd9dbb876c6cb6b6c66bb9db9c6c686c6c6c68c6c6f6bbd9b9b9b6c8c8c6c8c6b6c66b9b6b66a696399b9b9d9a6b6a99939b99ba96a9a99b69696b96a9b9bb9bb9bd9b9b9b9b98c68c6c86c6b6a6c66c8b666
            1191d19d1919d919191d1dd191919d91919119d91d9191d91dd919191d9191d91d9d91d9d9d9999d9d99d9d99d9d939b9c8c6f686c6f66b6b6b6b8c66b66c6ba696db9b9b68c686c8c6f6f6cdbd9bb99bb6b6b96b6c6c6db9b9b66c6c6c6c68c66c6c6c6bb9bdb9b6c686cc6c686b6b6a66b6b696a69b99b9a6969a969a69b9a696b9696b69a9a69a969b9b9b9b9b9b9b9b9b9bb68c66f6c6c6c66b6c6c686a6
            1d1d91d191d111d1d1d19191d1dd11d1d1d91d19d91d1d1d9191d19d191dd91d91d1d9d99d9d939d9d9d9d9d9b99d9b9bb6c68ccc6c6c8c6b6b6b66cc6b6b6969a9b9db9b6c6f6c8c6f686c669bd9dbd9bdb9bdb6b6b6b9bdbdb6c6c6c6c6c66c6c668c66db9b9bd66c6c6c8ccc6b6b6b6b6a6b6b9b69b99b9b9a6969a9b69b99b99a9a969a969b969a8b9b9b9b9b9bb9bb9b666c66c8668c686a66b6b68c6c6
            1911d191d1919d1919191d1d91919d919191d9d9d9d999d91d19191d91d91d91d9191d9d9d9d9d9d9d9d99399d939b9bd9b6c6c6cc8c8c6c6c6c6bb686c6a68b66bb9b9bdc8c6c8c6f6c6c8cc6b9b79bd9b9b9b9c6b6bdb9b99b66c6c686c6c6c66cc68c6b9b9b9bb6b6c8c6c686c6b6b6b6b6b6a69a69b999b99b9a9699b99b99b96969a969b69a68666b9b9bb9bb9b9b9b9bc86c86c8c68c6c6c66a66c68c6
            d1d911d191d1d191d1d1d911d1d1d191dd1911d9d9d9b9b9d91d9dd91d9191d91d9d9d9d9d9d9d9dd9d9399d9d999bd9bb9b8c6f68c6f66c6b6b6b6c6c6b6c68b8c6dbd9b66c8c6f66c8c6f686cb9b9b9b9bdb9db9bb9b9b9bb9c6c68c6c686c6c686c8c6db9bdb9b9c6c6c6f6c6c66c6b6b6b6b6b69b9b9b99b9696b9b6a9b9b99b9b9b969a99668c8cb6bb9b6d9b9b9b9bb66c86c86c6c6c8686c66b66c686
            1d119191dd9191d1919d119d919191d19191d91d19b9d98b6b191d1d91ddd91d91d19d919d9d9d9199d99d9939d9d9bb9db6c6c6c6f66c6c66c66c68c6c6b6c8c68db9b9b8c6f6c6c86cc68c6b66cdb9bdb9b9bdb9b9b9bdb9bd6c6c6c6c6c6c68c6c86c6b9b9d9b9b666c8c68c66b6b6a66a66b669a99b9b9b9b9a9698b66699b9b99b96b96b88c66c686868b6b9b9b9bb966c68c6c6c68c6c6c66c86a66c6c
            9191d1d1911d1d91d91d9d11d191d9191ddd919d9d9d9bb666a919d919d91d9dd9d919dd9d99d9d9dd9d993999b9db9db96c8f68f66c8c66cb6b68c6b86b6b6c6c879bdb9bc68c6f6cc6f6c6fb6c6b9b9b9bd79b9bdb9bd9bd9b6c66c86c6c66c6c8c6c6b9bdb9b7b9cb6c6c6c6f6b6a6b6b6b66a6c96a999b99b99b6c866a6a9b99a99b99a686c6c86c6c6c689b9bb9b9b9b8686c6868c6c68c6c86c6c6b68c
            11d19191d1919119db9d191919d1d1dd9191dd1d19b9b96ba966b91d1d9d9b9d91d9d9d9d939d9dd9d9d9399399d9b9b9b8c66c6c8c6f6c666a6cc8dbdb6b6b68c6bd9b9b78c6f68c6f68c6c68c66db9bdb9b9bdb9b9b9b9b9bb66c66c86c68c6c66c6c6db9b9b9b9b66c68cc6c66c66b6b6b6a66c66b99b99a99a9986c8b6b686b99b998c86c6868c6868c68c6b9b9b9b98c6cc68c6c6c68c686c6c686c6c66
            191d1d1d91dd19d999d9b1ddd1919d91d1d91919d99d9d9666a6b669b9d9b6a9191dd9d9d99d9d9d19dd9d9d9d999bb9b6c6f68c6c6c68c6bc6b66c9b9b9b6b6c66db9bd6b68c6c6c68c6c8c8c6fd9bd9b9db9d9b9bd9bdb9b9b6c6c86c686c66c6c86c9b9b9bdb9bdd66c686f68c6b66b66b66b66a66b9b9b9b99b8c86c6b6b6c86b98c686c86c6c68c6c686c66b9b6b9b9b68686c6868c66c6c6666c86b6b6
            1d19191d19191d93b9b9969d91dd1919d91d91d9b9b9b9b9a696a6a69b9b999d9d9d9d9d9d9d9dd9dd9d9dd9993939bd9c86c8c6f6c8c6c66b66b8b9b9bd9c6b6cb9b9b6b8c6c8c6f6c6f6c6c6c66b9bb9b9bdb9bd9bb9b9bdb66c68c68c6c6c6866c8c79b9b979b9b9b6c6c86c86c6a68c6a66a6c6b6869b999b9886c8666b6b6868868c6c686c8686c686c68c89b9b9bb9b9c6c68c6c66c86c68c6c66c668b
            91d1d191d1d1d9d99d9bda6619191d1d9191d9d9d9b9d9b99a6b696b69d9b6a61d19199d9d993919d91919d93999b9b9b8c86c6c68c6f68c6c6b8c9bdb9b9b6b68b9bd6c686f6c6c8c6c68cc6f6c6cd9b9b79b9b9bb9db9b9b9b86c6c8c6c6c6c6c6c68b9bdb9bdb9bb6b6c6c86c66c6b6666b66b66a6b886b9a88c6c6c6b6a666b6c6c68686c686c6c68c68c666b9b9b96b9b6b686c68c68c68c6686a686a66
            1d919d191919d9b9b9b996b6a19d91919d99dd9d9b9d9b9d6b696a69a69b9b96d9d9dd9d99399d9d9d9dd9d99d9d9b9b6c6cc6f6c8c68c6c6b6c66b9b9b9b6b6b8db9b68c6c68cc6c6f68c6f68c8d88b7d6c6dbb9b9b9b9bd9b6c8c86c6c6686c6c68c79b9b9b9b9b9b9c666c6c6c66c6cc6c6a6b6a66c6c88866c686866a66bb8b68c6c6c6c86c68c686c6686cb9b9b9b9b9b668c686c6c66c66c6c66c6c66a
            91d1d91dd1919b9d9b9b9a696b191d9dd9d99d9b99b9b9b996a6b698b6b966a661919dd9d99dd9dd19d9d9d9d9b9bb9d8c6c6c86c6f6c6c86c68cb9bdb9bb6b6b66db9c86f68c6c6f68c6f66c68c7d8b9b86c9b9b97b9bd9bb6c686c86f68c6c686c66b9bdb9b9bb9b9b6b6c6c68c6b6686c86b66a66b686c6cc68c6c6c86b666b6866868c686c6c686c66b6c86b9b6b9b9b69b866c6c686c86c8686c6866a66
            d9d91d1919d9b9d9b9d966b6a69d9dd9d9d9d9b9b9d99d9b9a966a696a6a96b9a9d9d9d9dd9d9d99d9dd9d9d99d9b9bb68c8c6c8c66c8c6c8c8c6bb9b9b9b66b6b6b9c8c68c6f68c68c686c8c8c69b6b6b6c86b66b6bd9b79b66c6c6f68c6c66c6c6c6bb9b9b9b96bb6b66c668c66c6a6c66c66a66b86c6c6868c668c86c6b6b66a6c6c6c68c68686c68c6b9b9b9b9b9b6b9b98b6c686c686c686c6c86c6c68c
            6b91191d91b9d9b99b9ba69696a6d99d9d9d9b9d9b9b9b99b66a96b6b969a9666b6dd91d9d9d9ddd9d9d919939b9bd96c86c6f6c6f686f686c686b9b9bd76b6b6c66c6c6f6c68c6c8c6f6c86c66bd9b9bb66c86cc6c6bb9b66c6c68c6c6c68c686c66b86b9b9bdbb69b6b6a6b6c8c666c6c68c66b66b68c68c6c68c66c6866b6a6666a686c66c6c6c68b9b96b9b6b9b9b9b9b9b6866c686c686c6c66c6868666
            b6b9d191d99d9b9b99b9b6a6a696a9d99d99b9d9b99b99b9b696b69a66a69bb9a96a9d9d9d9d9d99d9a9b9d99b9b9bb6c6c6c686c6c8c6c6f6c6c9b9b9b9c6b6b6b6b66c68c8c6f66c68c6cc6f6db9b6b6c68c68c86c9b9b6c668c66c686c68c6c68b6d6c9bb9b9b6c66866b86c686c66a66c6c6b6a6c6686c686c68c68c66a66a6a666c686868686c9b6b9b9b9b96b96b9b6b9bb6b866c68c6868c686c6c6c8
            69869b19d9b9b99d9bdb996b69a696d9d9d9d9b99b9d9b9b9a69a6969a96d9b96b6969b919dd99d9b96b6b9b99b9b9b66c8c6c8c68c6c68c68c6b7db9b9b66a66a6c6c6c86c6c68c8c6c6f68c66b9bd668c6c6c68c6866bb66cc66c66c6c8c6c66c6db9b6b9b9b9b66c6bc66b68c6c86b86c68686b666b8c686c68c686c6c66b6666b6c68c6c6c6c6b69b9b6b96b9b9a9b9b9b969b96b66c66c6c6686c666a66
            a6b6a6b9b9b99b9bb9b9bb69a66b6b9b99db9b9b9d9b9b99b9a696a6b66db9bb9b6a9a69b999b9b99b9969a9a9b9b9db66c68c6f6c6c8c6c6c6c9b9b9bd9c6b6b6b6b6b6c6c6c8c6c6f686c6c86cb96cc68c8c8c6c8cc686c668c66c86c6c686c86b9b69b9b9b9b9b6b8b9b66b686c6c6c686c6c86a6a666c6c86c66c6868c66a6a66a6666c686c6b9b9b69b9b9b96b9b96b96b9a6bb6b6868686c6c686c8686
            b69a9666a99bd9b9b9b9b9c669a96a66ba99b99b9b99b9d9b696b96969b9b9b9b969696b6ba9b99b99ba96696b9bdb9bdb9c6c668c86c6f68c6bb9b9b9bb6c6b6b66b6b68c8c6c6c6c6c8c6c6c6876c68c686c6c6c668c6c6a6c6c66c6686cc86c68b9cb9b9b9b9b9b96b6b6a6c6c86866b8c686c6666b6c686c686c86c666a6666b668b8686c6869b969b9b69a9b9b96b9a9b9b9666b6a6c6c668686c686c6c
            6b666b9a99b9b9b9b9b9bb6a866b696b969b9b99b9b99b9b9b9a6a9a6b9b9b9b9b6a9a9696969b9b9b996b9a9b9b9b9b9b9bb6bc66cc6c68c66b9b9bdb9b66b66a6b6b66c6c6f68c6c86c6c8c6c6d86c68c6f68c6f6c6c866c668c8c6c6c86c6c8bb666b9bb9c6b6b9bb9d9a66686c6c6c666c6c68b6a6b68c686c686c68c666b6a68b66b86c686b9b6b9b69b96b9a96b9b969a9bb9866686686c6c6c66c6866
            a96b9869b99b8b9bdb9b986b6b69a696a6999b9b99b9b9b999b96969b9b9b9bb9b96b69ab9a6b9b9b9b9a96b69b9b9b9b9b9b9b9b86c68c6c6d9b9b9b9b9b66a6b66a6b6686c68c6f66c6f686f6bb6c8c6f66c6c68c6f6c6c66c66c6886c686f6b99bb9b9b6b686c6d9b9b69b6c6c686c68b86c68b666b6b66c6c686c6866c6a666b66a66b668bb9b9b9a9b9a9b969b9a96b9a969b98a66a6c6c686866a68b86
            66a96b9a9b9d9b9b9b9cb6b66a6a69a69b9b9d99b99b999b9a96b6b69b9bb9b9b6b969a9669b9a999b996b96b9bb9b9b9bb9b9b6b6c6f66c6bb9bb9b9b9bb6b6b6b6b66a6c66c6c66c6c86c6c689b686c66c86c8c686c6866c6a6c86c6c6c8c669bb9bb9b9868c66c9b9c9bb6b868c6c66c68686b66a6668686868c66c6c6666a6b6a66b66a66896b69b96b96b9a9b69b69a96b9a6b6686686866c66c686686c
            9b66a98699b9b9b9b9c868c6b66b66b69a9b9b9b9b99bd9b996b969a9bb9b9bb6b6a96969a96996b99b9b9a9b9b9b9bb9b96b966c68c6c86c9b9b9b9b9b9b6b66a66b6a6b6c68c6c8db6c68c6c6b6c6c8c86c86c6c6c86c6c6c686c6c686866c6c9b9b9b9c8c66c86c9b9b6666c6c6866a66c6c66a66a6a6c6c6c66c8666b8b666666b66a66b6bb69a96b9b9b969b69a9b9b69b696686a6c66c686a6866c6c68
            b69a969b6a9bb9bb9b86c68c6b6b6b6a669b99b99b9b9b99b9a96a9b9b9b9b98b9b6bb6b96b9a69a9b99a969bb9b9b9b96c66cc86c6868c66b9b9b9bb9b9b6b6b6b6a66b6b8c68c6b9668c6c8c6b66c86c6c6c6c6f68c6c66c66c6686c6c6c86c666b9b6b866c86c8686b9a6a68686c6c6866c68b6666686868668666c6a666a6a6a66a96b66a99a96b9b69a69a69b96b969b9b9b6a66686a66a6686c6a686c6
            9a696a69a9b9b9b9b86c8c6866b6b6b6b6a69b9a99b99b9b99b969b9b9b9b9c666b69a96a96969b969a969a9b9b6b9b9c8c6c86c68c6c6c8b9bb9bb9b9bb9c96c66b6b66b666c66b9b6c68c6c6b9c68c68c6c8c686c6c68c66c68c6c86c66c6c86bd9b666c686c866c6c96b66b6c6c6866c6a6868b6a6b6c6c6c6c6c8666b66666b6966b96b996b69b9a9b69b9b9b6b96b9a96b9a668a666868686c66866c668
            b69a69b69b9b9b9b9c686c6c8b6a66b698b6a66b6d9b99b9b96b9a9b9b9bb98c8b6a66b6b9a9a96b9a96b96b9b9b9b96c68686c68c68c6c67b9b9b9b9b9b98c66a666b6a66b86c66bb68c6c686b9c6c6c6c686c6c6868c66c68b68c6c66c6868c6d686b6c68c686c868c6b9b66a6686c6c686c6c666b6686868686866c6a6a6a6a66a69a9a9b6b9b9a96969a96b69a9a9a96b9a966a668a66a66c66a66a686a6
            6969b69a9b9bb9b9b9b6c686c666b66a66b66b6a6b9b9b99b9b9b9b6b9b9b986c66b9b6b669b969a969b9686b69b9b6c86c6c68c68c66c6c9b9b9b9b9b97b66c66ba66b6b6b6c6c66b6c686cc6b9c686686f6c6c8c6c6c6c66c6c6686c66c6c66d86c68c86c6c6c6c6c68b96a666c6c68686c666a6a66a6b6c6a6c6a68666666666a9b696969a969696bb9a969b9b96969b9696b66668666866a66868668b686
            ba969a69b9b9b9bb9b9c86c86c6b6a66b6b6b6b6b699a9a68b9a9b9b9bb9b6cb68686b69ab69a9b969b9a6c6bb6b9b866c868c686c6c8686b9b9b9b79bb9b68c8c66b66a66a66b6c66c68c6c6b9b68c6c6c686c6c6c86c66c66a68c6c66c668cb66c6c6686868686868666b66b6868686c6c66a6666a666a6668666866a6a6a6a69696b9a9bb96bb9a969a96b9a696b9a69a9a998a68b6a66a6686a66a668668
            96b6b969bb9b9b9b9bb66c6c686b69a6b6a66a696a6a666c686b6b9b9b9b989b9b8c68b669a6969b9a96686868b9b86c86c6c6c6c686c6cb9b9b6b9b9b9b98c6688c6a66b66b6666c86c68c687b66c66c66b6c68686c686c6a66866c6bb68b6b66c6868c6c6c6c6c6c6c8c6d68b6b6c6c6898668b6a66a666a6c6a6c6c6666696b9a9a96b966b99a96a6866b969b6b969b696b6b66cc66686686a66686c6ccc6
            b969a9b9b9b9b9b9b99b6686c686a66b669a666a6666b6b86c6b69b9b9b66bb9b66c68b6a66cbb8666868c6bb69b6686c68686868c6c6c6b9b6d9b9b9b9bb68c6c6666b66a66a6a66c68c66c6b9c66c66c6866c6c6c6c6c666c6c6c66686a69b6686c6c686c68686868666a98b6868686a6b6a66866666b6a66c66866868a68b9a96b969b69cc66686666a668a66a66a66a669a966cf686a66a6668b6668cf66
            6b9a969b9b6b9bb9bbb6c6c86c686b66a666b66b6ba68686c686a9b69b9b89b98c86c66b66b6696a86c6c689b9b98c6c68c6c6c6c686866b9b9b9b9b6b9b66c686c6a66a668c6b6a66c68c686b9b6c6c66c6c66b66c68c68c6866c68c6a69b686c6c686c6868c6c6c6c6c68b666a6c6b686866a66b6a6a6666bf6cc6a66666b969b96b9a9a6fc6a6b6a6666a666666a6666a6866a6cc66a666668b686a66cc6c
            9a969bb9b9b9b96b9996c86c68c66b6b6b6b6a66a666c6c686c68b9bb9b9b9bb666868c6b66a6a666c686c6b9b6b9c686c6868c686c6c86b9b9b9b6d9b9b9868c6866c6b6c686666c686c68c6bb6b668c68c6c86c66c6686c6c8686c686b9c6c68686c686c666c6866868666a66668686b66a668b666666a666cc6f668a6a69a9a69a96986ccf666666a6a6666a6a6668a6666a668ffc666a6a668c668ccffcc
            6969a9b9b9b9bb9bbb6c66c686c6c6b698b6b6b66b6b686c686c6b9b9b69bb99b8c6c66b6b6b6b6b686c68d9b9b9b9bb686c6c68c686c6b9b69b69b9b9b9b8c66c6c66a666c6c6a66a6c686c69b96bb66a6686c68b66c8c6866c6c686c6d8686c6c686c6c68c686c6c6c6c666a6a6a66a686686b689a6c868acff6e8666c9b6969b66ba666cfc66a6a666668a6666686666a66686cccf6b98666a6c6acf6cfcf
            9b9b9b9b6b9b9b9b99b68686c68686b6a69896a686a66b686c686b96b9b9b96b96868686b6a966b6a6c68b9b69b9b9b9b9b686c66c6c68b9b9b9b9b9b6b9b66c8686c666a68686c66666c6c6b9b6b69b666c6c686c68666c6c8686c6c6986c68686a6c6866c66c66868668a666666686686a66a668b86fc666cfcffe6b6c69a9b69f9966a6fefc668666a66666a686ac6a666a6666cf7c66986a66f66fcfef7f
            96b9b9b9b9b9b9b9b69c8c6c68c6c66a6b6b6a66b666a6b6a66c69b9b9b69b9bb6c6c6c6a966a6966b866b9b9a9b6b9b9b6b6868686866b69b9bb9b69b9b68686c6c66a66c6c6c6a6ca66866b9b99b69a6b666c6c68c6c8686c6c6866b8c686c6c668686a686a686a6c6a668a6a68b6a6c96c6686666afc66cfcf7fc6b6cc966a6cfc8f66ccf7f666a6668a6a666a66c6666666a6fcffc6b6a666cfc6fef7ffc
            b9b9b6b9b9b69b69b9b86686c668686696a6669a686a666668b6b9bb969a9b69b986c68666a666a6b668a96b9b69b96b969a6c6c6c6c6c9bb9b96b9b9b9b9c6c68686a66c68686668686c6cb9b6bb9b866a6a6686866c68c6c66b86a6666c6c6868c66a6686686c6666866c6666866866868686a18b8cff66cf7ff7fc9ccf6b666fcccc66ccffc6a666a6666668c666cc68a6a666cf7fc6986668cfccfcff7ff
            9b9b9b9b9b9bb9b9bb66c6c686c6c6a6a66b6a66b6666a6a6b9b9a96b9b6b9b9b9c686a6a6b6a66b6866bb9b69b9b9b9a9b686868686c669b69b9b9b9b69c686c6c666c668b6a6c6a6c66c69b6996b66c8666a6c6c6c8666868b6666a6a66a66a666a668c6c6c668a6a6c686a6a6a66a66a66a666666cf7c6cff7fcfc6f7f666a6cffcf6e4747f6666666a66a6cf66cfc6666668ccfcfec666a66cf7fcf7fcf7
            b9b69b9b69b9b9b9b98b66b86c6868666b66a96b6a6a666686b69b69b9b96b9a69b66866666b6866a6a8969b9b9a9a96b9b66c6c6c6c68b69bb9b69b69b686c6868c6a66a6666c66668c68686a6c98a686c866c666866c8c6c66bb9c666a66686c686c8666866a66686686a666666866866c666a68afcffcf6fcfcf7f6efc6a668cf7fc47eeee4c66a6a666666cc66cfcc66a6666c6fcff66666afcfcf7f7fcf
            9b9b9bb9b9a96b9a9b9b9b9b8686c6c868b6686666668c6a686b96db9a9a9b69b9b6a6c86a666a668666b9b9a96b96b9b96868668668666c89b69b9b9b98b86c6c66666a66a6a68a6b668b6c6686a668c66c686a6a6c68666686b66a6b666a6b686c6c6c6a6a6686a6f66c6686a66a66a666a66866c6f7ff7fef7fcfcf7fcc666cfcfc7e4e74eee669696c6a6cffc6fcf66666a6cfef7f7ccbbecf7f7ffcfefc
            79b9b969b9b9b9b69b69b969b6c6686c666a66a6a6a66686c66a9a69696b969b9a998666c66a66b86b86bb696b9b69b96b8b86c6c6c6c866c9b9b9a9b6b68668668c6a6686666b66b9a668686c6c68c66c686c68666b86c6a6c686a666a6666866ac6f66866686a666cc6fc66a6866a668a6686c6afccfcfccf7ff7f7fcf7f66acff7fe7edb7e7fb6a96ac9668ccf6ec7f6a6666cfcffcffce47b7fffcf7cf7f
            9b6b9bb9a96b9b9b9b9b9a9b69b86c66a6a66686666a6a666a66b66abb9b9a9b698c68c68666b666a66b69a6b969b9a9b9666c6866866a66b69b69b69b6a6c6c6c66866a6c6b9b9b966c6c6c6868666c686a6686c6a666a68686a666a66a6a6b866fcf6c66a666686cfcfcc66666a6686666a66c6ccf7f7ff7ffcffcfcf7fc666f7ffffddb9bdce6696a6f69ccf7fc7ffc666a66ccf7f7fcf94bbdf7ef7f7ffc
            79b9b9b96b9b69a96b96b9b9bb66a6868666a66a8686668c686866b68696b96b9a66666a6a686a6666a68666a9a9a96b9b6a66a6a66a6b9b9b9a9b9b9a66686686a6c6666a6b9a96b6a666a66a6c6c866a668c6a686b68666c6668686666b666a66cfec66868a68b6cfcfcf68a666866a6a666cfbcf7fff74e7f7f7f7f6fcfc66fcfcef9ddb9b7fc6b9cfcc6ccffcf7fcf666666cf7ffe7efd9b9be47eef7cfc
            6b9b69b69bb9b96b9b9b96b696a6686c6b666a666c6c6c666a66a66668b69a66686c8a66686b66a6a6666a686b696b9b698686686866b96b69a696b9696a66a6c6866a8c666b96b9b686a6686866866a686c66666c66a66c686a66a66a6a66a66ccfefc66cc666686fcf7fc6666a66a66666b9fccf7fcf7e4e4eefcffcf7f7f6ccfef7fdd9b79cf76c8f7fc6f6f7f7f7f7fb6a6ccffcfdbfcdd97d7b47ef7f7f
            9b9b9b9b866b6b9b96b9a9b9a66866a6686a666a686686a6866c686a666a698a6666668686b66866686a6686666b9b69b98b6a666a689b9b9a96a96a9b66b686686c66668a69a9b96a668686c6c6a6866c668b6a68666a686a6686686666966a6cfcf7f666cc6a66ccfcffec66866a66a69a96cfcffcf74e47e47eef7fcfcfc6cfcfffc7dd9bb7fc6fcfcff6ccffcf7fcfc6666cc77e77b77d9bbb9bbb7c7e7f
            9b96b9a66a686a96b9a96b986866a6686a666a666a6a66866a6866a686a68966a6a68b6a6b98b6a6866686b6a6a6969a9868668c666b6b6969b66866b9a66a66a66868a666b969b6a6686c6a668666c6868668666a6a666a6686a6c6a6a6a6666cf7fcfe68cf668b8f7fcf7f66a686669cc66cfef7f7ffb4e47be7fcf7e7f7fc7ef7f7f19db9bcfe6fe7f7c7f77777e77777e7777efffcfce7bb9b77cc777777
            b9b9b666a66669b9a96b96b6b6a6686c66868686866686a66866a66668666c6b66866866b96a6966a6a66a686669a9b69c66a666a68b99a9a6986c6a969b66986c6a6668c69a9b96686a666686a6866a66a6a6a666866a6666a6666666666a6acffcf7fc66fc6666cffcf7fc666cc69a6fc66cfcfcff7f797b9b7df7e4eeefcc7befffcdd9bb977e7777777777e7e777e7e77e7ef7c7c777c7c777e7777e7c7e
            6b9b9b9a668a6a6b669b9a99b966c666a66a66a66a66a666a66a6686a66a68969a6b6a696a966a66666a66866a9a969a66a66868666b6b969b6b6668b9a9b6b668668b866a69b6a66a6686a66666a6866c666668a66a666a66686a86a6a66696cf7fcf7f6ccfe6a6fef7ffcfc66cf966ccf6cfef7f7fcfddddb9bbff7b7df7fc7d65e77bddb9b7e7e7e7ee7e7e77e7e77e7e77ccfef7f7e77e77c77c7e77e77c
            9b6986896b6666866a6b69b69a9b68a66866a666668666a6686686a668666a6a969669ab96b666a6a66666a666b69a6966686a66a689b69a9b96a9b696969a98b6a6666a669b98668666a668a6866c6a66868a666b668666a66a6666866a6a68fcff7fcfccf7f666f6f7fcf7f66fcf6afcfef6cffcfcfcdd9b9b9b7c7db9ec7f7cf7be7d9b97db777e7e77c7e7c77c7c777c7ef7c777777e77f7e7e77c7f7fff
            9b9c6c6866a686a66699a96b96b666686a66686a86a6a6866a66a666a66a6666b9a9a96969a6a69669a6a666a696b9b98a66a66666a69a96b6a9969a9ab9a66686686a668b9a66a66a6666a666a6866686a6668b66b66a6b686668a66a66666ccf7ffcf7f7ffc68bc6efcf7fc6bcfc66cf7fcf7f7f774fd9ddbdb777bd9b7774747dbb7dddbb6ffe77e7c7e77c7e77e7e7c77c7ff7f7ec7c7e777c7e77effcfe
            6986866a6866a668b9a69b9a969a98b6666a66666666666a6666668666a668a696b96b9a6969866a666666a6686a669a666a66a6a69896b9696b6b96b96b66a66a66a68666b96666a66a6866a666a6a66a66c6689a96a6666a6a6666666a66a6ffcf7fcfcfcf7c6cfef7f7ffc6fcfc6cfcffefcfff4ed77dd9b96b4b7ddbe74be749db7e79bcfecf7e777e7c77e7c77c7c7ef7f777e777e7f77c7e77c7fffcfc
            76c66a66c668668b89b96b69a9b9686a6866a6a6a6a68a6686a6a6a6a666a669a96a66969a96a666a6a6a666a6666a666a66666666b6b96b9a99a9a9696966686686666a68686a686666a666686a66686666c86a69b696a686666a6a6a6669fcf7ffcf7f7f7ffc6cf7f7ffcfe6fef66cf7fcf7c7777db7b7cfffef74bd7e7e74eeedb947c77fcf777e7c77c7e77f7e7e77e7fc7ce7c7f7c77e7e7c7f7efcff7f
            666a68686a66a6698b69a9b96b698b668b86666668666666a6666666668666866a966a6a96b666a9666666a6698a666a668686a689a96b9a696b9696a9a6a86a6a6a6866a66a666a66a666a6a6666a66a6a6f669b69a69866a66866666c86a6fefcf7fcfcf6cf7c6fccf7feffef6fefc7f77777477b77e77cf7fc7e747474b4e47e49b77e7e7777e7c7e7f77f7e77c7f7ff7f7e7f77e7e7f77f7e77e7fff7fff
            6a6866c66686686b69b9696a969a6686666a6a686a6a66a66686a686a66a66a666986666a969a66689a66696a6666a6666a66a96a6969a969a96b6b96b66666666666a6666666a666a66866666a6666a666ccc9a969b66a6666a66a686cf66cffcf7ff7f7fcf7fcfef7f7f7f7fc77777747747e77e7e77e7ef77e7e7d47d7474e47eb9e77e77ec7e77e777e77e7c7f77f7c77e777ec7f777e7cff7f7ffcfffcf
            6666c66a68b6a6a66a96a9b96b966a6a6a66666a66666a6686a666a66666a666a66a6a6696a9866a6666a6a666a66666a669896969a9696b96b969a96986a6a6a66a666a6a6a666a6686a6a6a6686a6666afcf96b9a98666a6666a66a6fc66cf7fcf7eeff7fccf7fc7f7fcf7e77e7e7477e77e774777e77e77e77ecf7c74b7bd7bd9b77c7e7c77e7c7f7ec7f7c7f77fec7f7f7f7f77f7ec7f7fcfffffffcfcfc
            c6c86a6666866666b969b696b6b98666666a68666a66a666a666a666a6a6668666a6666a69696a666a6666666666a668666a66a6a96b6a96a96a9696a98666666866866866666a666666666666a6666a666cfc696b6698a666a6666668cfc6feff7e4e74fcf7fcfcfcf7c7e77e77e77e777e77e77e7e77e7777ecf7fef77e7edb9bb9b7e7c77e7f7e77e77e7e777ef7f77e7e7c7e7f77c7f7fffffcfcff7ffff
            7f666686a66a689a96a969a969a66a66a6666a6a6666666a66986666666686a6a66698666a6a6666666a6a6a6a9666a66a666666669a969a9696b6a966a6a66a66a66a66a68a6666a6a6a66a6666a6666acf7fb696986666a666a66a6ccfccfc7ffd74b9f7cfcf77777f7e7c77e77e77e7e7e77e7ec7e77e7ee7f7f777e7e77ddb9bd6e7c7e7f777c7f7f7c7f7fef7c7ef7c7f7e7f7e7f77ecffcffff7fffcff
            666a66a668666a69696b9a69a9696666998a666666a66a66986a66a6a66a6666666a96b666666a6a6a666696666a6666666a6a66a6696b696a969a969a6666666666a666666666a6666666666a666a6866cffc69a9a6a6a6666866666cf7f6fffcfd9db7cfc7777e7e747e77e77e77e77e777e7ef77e7e77e7fc7f7f7e7e7e7c7bcc7e7c77f77ec7f77e7e7f7e7f7c7f77c7f7c7f7c7f7ec7ffff7ffffffff7f
            66c66866a6a6669a9a96a9696b6a9a68a66666a6666a66968966666666666a66a66669a9a66a66666666a6869a666a6a6a66666669a69a9696b6969a6666a6a6a6a666a6a6a6a6668a66a6a6666a666a66cf7fc6966666686a6c6a6a6cffcf7f7fcddb9b7e7e7e77e77777e77e77c77e77e7eec7e7e7f7fefc7fcf7e7c77c7e7e7fff77e7e7e7c7e7e7c7f77fcf7c7f7e7f77e7f7c7f7c7f7ff7fffcffcf7fff
            6668b6686666a6b696b969a69a96966666a6a666a6666a66a6a6a9898a66666666a6b6969666666a66a66698666a966666666a6a669a966a9a9a9a696a666666666666666666666a66666666a6666a6668cffcf9b69a66ac668c66668fc7fcfcfe7e7cf7ec7f77e7747ee77e7e7e7e77e7ec7f77c77c7f7c7fc7f777e7e7e77c7fc7f7c7f7c7f7e7f7f7e7fc7f77f77c7f7cf7f7c7f7ef7c7ffffffff7ffffff
            6a6668a66a66669a696a969a6969a6a6a696668666a66666666666a6666a6a6a66666a66a9a66a6666666a66a66666a666a666669a6969a96696696a666a66a686a6a66a66a66a6666a6a68666a66666a6fef7f69a66a6cf66cfc66a6ccff7f77777777e7f7e7e747e777e77e777e7e7ec7f77e77e7fcefcf7f77e7e7c7f7c7e77e77e7f77e77e7f77e7f7f7f7c7ecef7c7e7f7c7f7c77f7ffffcfcffffffcfc
            666a666666a6a669b6969a6969a6966666866a66a666a6a6a96a6666a98666666a66669a96666666a66a666666a66666a666a66a6696a6969a69a69966666666a66666666666666a666666a6a666a6666cf7ffcc699698cf66cfc666cf7777747ee7e7fe7e77777e77e7e7e77e7e777f7f77e7c7e7fc7f77e77e7c7c77e77e7f7f7c7f77ec7f7f77ce7f7fcf7c7f7f77f7f7f7c7f7ef7f7fcfcfffff7ffcffff
            6666a9a6a66666a69a9a6969a696a69a66a666666666666968666a96666a666a666a6a6666a6a6a6666666a6a666a6a66666666966a696a9696696a6a6a6a6666666a6a6a66a6a666a66a666666666a6ccffcf7696a666fcc6fcf69677e7e7e7e7f7fe7777e7e7e7e77e777e7cf7f7fc77e7c77eff77e7f77c7c7e77f77f7c77e77f77ec7f7c7ec7f7fcf7f7cef7c7f7c7f7c7f7cf7c7fcfffffcf7ffffff7ff
            cc698966666a669a69696b6b96a966666666a66a9a6a66a666a9666a66666a6696666666666666666a69a66666696666989a6a686666a966a69a9696966666a66a6666666666666666666666a6a6a6666cf7fcfc6b96acfcfcc77e7e7477747ef7f7777e7e77e7777e77e7e7f7c7fc7e7c7e7ef7c7ffc77e7e7e7f7e7c7e7e7f7c7e7f7f77e7f7f77f7f7fc7f77f7e7f7f7cf7cf7e7f7f7ef7fffffffcfcffff
            ffffc69a6a6689696a96a986c9698a6a6a66666666666666a6666a666a6696668a66a66a6a66989a6666666a698a666a66666696a98666969a6989a98989a66666a66a66a68a66a6a6a6a6a6666666a6ccffcf76c9698cf7777e7747e77e7ef7c77e7e7e77e77ee7e7e7c7cf7fef77e7f7e7f7ff7fc77f7c77f777c7f7e7f7c7e7f7c7e7cf7f77efcfcfc7f7c7f7f7f7c7f7ef7ef7f7fcfcfffcf7ffffffffcf
            cfcffff66666a9a696a9696cc6a96666666a6a6a66a66a66666a6666666a66a696666966696a666666a66a666a666a666a66a66a696a96a9696a9669a698966a6666666666c66666666666666a6a66c66fc7fffcf9a66e77e7e77e777e7eef777e77e777e7e7e77e77c7ef7fec77e7f7ef7f7f7fc7e7f7e7f77ec7f77c7c77f7f77c7f7f77e7cf7f7f7f7f7f7f7c7f7cf7cf77f7c7fcf7ffcffffffcfcf7ffff
            ffffcfcf66a69696a9696a6cc696a96a666666696666666a666986a66a66666686a66a66a6666a66a966666989666669898966696866696a66966b66986b6a666a6a6a6a6af6a66a666a6c6a66c666c6bfff7fcfc67b777e777e77e7e777777e7e7e7e7e77e77c77c7ef7f7f77f77c7f7f7fcfc7f7f777c77e7c7e7c7e7f7e7e7cef7e7c7f7f7f7fcf7f7c7ec7f7f7c7f7f7fc7f7f7f7f7ff7ff7ffffffffcf7
            ff7fffff6a666a69696a966cc6b696966a698986a66a6a666a666c696666a6a696666666666a6666666a698666a66a66669a69a66a96a9696a9a96b6a9696666696666666ccc66666a666c666cf69cfc6c7ffc77e77e7e77e7e7e77e77e7e7e77e777e77e77fe7e7ef7f7fc7e77e7fef7fc7f7e77e7c7c7f7c7f7f7e7f77f7f7f777f7f7f7cef7f7f7f7f7f7f7f7ef7f7ce7cf7f7f7ffcfffffcff7fcf7fffff
            ffffcfcfc669a96a98966a6ccc698a6a666a66a66666696666a6ac68a6a66966a66a989a66666c6a66666a6a6666696a6a69666666696a669666696966a69a9a6866a9666cfc66a66c6c6cf69cfc6cfc6ffc77e77e7777e77e777e77e7e77e7e77e7e7e7c7fcf7f7f7f7f77e7c7fc7f7f7fc7c7f77c7e7c7e7f777c7f7c7c7c7c7fc7c7e7f7f7fcfec7cec7f7cef7cf7f7fc7f7cf7ffcffcf7ffcfffffffcf7f
            cffffffffe6696966a6a96ccfc6c9c6698966666ac6a686a6cc6ccc69669866666666a666a96ac696a66666966a986669666a9a969a6969a6b9a98a9a969666669a6666acfcf6666ac6fcfc6cfcf6cfcc777ee7e77e7e77e77e7e7e77e7e777c7e7c77c7fef7f7fc7fce7e7c7f7ff7fc7f77e777e7f7f77c7f7ece7f7e7f7f7f7f7ef7f7fcfcfcf7f7f7f7f7f7f7f7cecf7f7f7f7fcffcfffffcffcf7fffffff
            fcf7ff7ffc6b6a6c6cc669fc7feccfb666a66a66ccc69c66ccc6c7c666c6a66a6a666666666a6cc6666a96a666666a66a9666666a696a66966666966696a69a668666a66cf7f66966fcfccf6ccfcfc7e77e7f7e7e77e7e77e77e777e777e7e77e777e77f7c7f7f7fc777c7e7f7f7fc7fc7e77e7f7c7e7ce7f77c7f77c7f7e7c7f7c77f7fcf7f7f7f7f7c7f7cce7f7f7f7c7f7fc7f7ffff7fcfff7fffffcf7fcf
            fffffffff76c666cccccc6ccf7cf7ccc666a66ccc7e66cc6c7f7fcc66ac6c666696a96a6989ccfc66a968666a66a669666a96a9696a969a69a96a969a6696a9669a66666cffcc689cfcf7fccf7f7e777e7fe7f777e77e7e7e7e7e7e7ee77c7e7c7f7efef7fcf7fec7f7e7ef7fef7fef77e7c7677e7f7e7f77ce7f7cf7f7c7f7f7ef7fcf7f7fcf7f7c7f7f7f7f7f7cc7f7f7fc7fceffcffffff7fff7ffffffff7
            ff7ffcffcfccec6cccf7c7c7ec7cc7e7cc6cccc7eb16bcd6eccce7fe6cccc6c6a6666666a68cc7f6666696a6696696a669669896a9666696666966a696a69666a6666a6cf7fffc6bfcf7fcf7fc777e7e7f7fc77e7e7e777e777e77e777f7e7c77e77f7f7f7f7fc77e7e7f7f7f7fc7c7e7f7e7e7c7c7c7f7ce7f77f77c7f7f7cef7cf7fcfcf7f7fcf7f7f7fcef7fc7f7f7fc7f7c7f7fffcff7fffcfffcf7ff7ff
            cfffffffff77fcfef7f7c7e77f777b7eccf7f7e77bd7b77e777777f6cf77c7c666a66a6669ccfcccc66a6669c6a68696a66a66666669a66a9a989a96696986a6666a966cfcf7f766cfcfcf7e77e7e7efcf7c7e7e77e77e77e7e7e77f7e77e77f7e7fc7fcfcef7e7f7c7c7f7fc7f7e7f7c7e7c76e7f7f77c7f7c7f7cef7e7cef7ff7ff7f7f7fcf7c7f7fce7f7cc7fcf7fc7f7fcf7fffcffffffffffcfffffffff
            7fcff7ff7f7e77c7f7fcf7f7e7e7e7e777fccf77e7b7b7e7e77e77ef7fcf777e777b7bcb686e6f7fc6986986c66c96a696969a9a96a6969666698966a66a96666a6666cfc7fcfc6b6fef7777e77e7f7f7777e777f77f7e7f777c7f77e7e77f77efcf7f7f7f7f7c77e7f7fcf77e7c7f77f7f7f7f7f77e7f7f7c7f7c7f7c7f7f7f7fcf7fcfcf7c7f7f7ce7f7cf7f7f7cf7ce7f7f7f7fcf7fcffcffcfff7ffcffcf
            fcf7fffffff77e7f7f7f7f7f77f77f7c7e77f7fc77e7e77ed7e77e77f7f7f777e7e7777777777ecc5c6c6a66cc6c6a666a66666669666a69a96a966969666a69669866cff7f7fc6cf7777e7e7e77f7f77e7e7f7e77e777e77e77777e777c77e7f7f7fcf7fc77e7f7c77f7c7ec7f7e7c7e77c7c7e7ce7f7c7c7f7c7f7c7f7fcfcf7f7fcf7f7f7f7f7f7f7fc7f7f7f7f7f7fccf7fffffffffffffff7ffffffffff
            7ffcffcffff7e777cf7fccf7fc7e77e7f7e7cf7f7e7e7e77e777e777ef7fccf77e7e7e7e7e7e77777ccc669cccccc6c6969a69a96c6b9666666989a6a69cc668986a6cccf7fcff777e7e77e777fcf777e77c7777e77e7c77e7f7e7e7c7e7e7cf7f7fc7fc77f7c77e7f7fe7f77f77f7e7f7f7f7f7f7f7c7f7f7c7f7c7f7cf7f7fcfcfcf7f7ccf7ccf7fcc7f7f7fc7f7f7f7f7fffcfcf7ffcf7fcfffffcfcf7fff
            f7ff7fffcffc7f7e77f7f7fc7ff7f7c777f77cf7c77f77e77e7e77e777cc7f7fe777e7e77e77e7e7eb7ccccf7ccf7ccff6669866cc9869a96a98989696acf966a6c66cf7fef777e7e7e7e77f7fe7e7e7e7e77ee7c7e7e7e7c777e77c7e7c7f7fecf7ff7e7e7e7f7f7cf7c77f77ec7c7f7c7e7c7c7c7f7f7e7f7f7f7f7f7fcfcf7f7f7f7fc7f7f7f7c7f7f7fcc7fccecc7f7ffffff7fffffffff7ffcfffffffcf
            cfcfffcfffff77e7f7cf7f7fc7fc7f7ef77e777e7f77fcffc777e77e7fefffccfef77e7e77e77e7e77e7f7f7f777fffcfc6a696cccc9666696698966a66cf66666cfcfcf7f7e7e7e77c77f77fcf77c777c7e77c77e7c77f77e7c7f77e7f7f7f7f7fcf77c7f77c77ef7f7ef7e7f7c7f77f7f7f7f7f7e7f7c7f7c7ec7f7cf7f7f7fcf7f7f7f7f7ce7fef7fcc7f7f7f7f7fcfcfcfcfcffcf7ffcfffffff7ffcffff
            7ff7fcff7ffff77e77e7f6f7fc7fcf7f7e7f7f7f77e7777f7fe77e7e7ff7ff7f7c7fe7e7e7e7e7e7f7e77f7c7f7ffcffcf696cccccf69a6a66a69896966ccc6a98ef6cf7777e77c7c77e77fec77c7e7c77e7f77e7f77f77e7f77e7e7f77f7fec7f7f77e7f7e7f7fcf7e777c7f7c7f7c7c7c7c7e7cf7f7c7f7cf7f7f7fefcffcf7fcf7fc7f7cf7fc7f7f7f7f7fcc7f7f7f7fffff7ffcfffffff7ffcffffff7fff
            fcfcf7ffffcffef7f7f7cecf7fc7f7f77f7c7f7ec7f7fe77f77f7f7fffffff77fcf7f7f7f7e7f7f7ef7e77e7effcffcffcf6ccccf7c666989696a6a66cfefc668cf7f77e7e7e7e77e7f7efcf7f7e77c77c777e77e7777e77e7e77c7c7fefce7f7e77e7f77e7c7fe77f7f7f7e7c7f7e7f7f7f7fcf77c7f7f7c7c7fcfcf7f7f7fcf7f7f7cf7f7f7f7f7f7f7fcf7f7fcf7f7fcf7ffffcfcfcf7ffffff7ffcffffcf
            7fcf7fcffff7f77f7c7f7f7f7f7f7f7fc7f7f7c7f7ce7cf7ecf7e7fffcffcfe777fcf7c77f7f7e7f7ff7fc7ff7ffcff7ffc7e7c7cfcc6c6c6a669698bcf77ffe6f7e7e77e7c7c7f7e77f7f7f77e7f77e7e7e77c77e7e7e7f77c7ff7f7f7f77c77f7c7c7e7c7fcf7f7e7c7e7f7f7e7f76e7cec77c7f7f7ec7fcf7fc7fcfcfcf7fcf7f7f7cf7f7f7fcccf7f7c7f7f7f7f7f7ffff7ffff7ffffffcfcfffff7fffff
            fcffff7f7fffff7c7f7c77f7f6fcf7fcfc7f7f7f7f7f77ef7f7fcfcffffcfff7f77f7ffcf7e7f7fcffcfffc7ffcff7ffcfff7f7f77efcc6cc696a66c6fcfccff77e77e7e7e77e777e7fcfc77e77e7e7f77f7e7e7e7c7e7c7e7f7f7fce7f7c7f7e7c7f7e7f7f7f77c7f7c7f7c7e7f7c7cf7f7f7f7f7f7cf7f77ff7ff7f7f7f7fcf7f7ccf7cecccf7f7f7fcf7fcf7f7fcccf7ffcffcfffcf7fffffffcfcfffcf7f
            cf7f7fffcfffcffef7f7fe7c7f7c7fc7f7fcc7f7ce7fcf7ffffcfff7fcff7fffcf7ecc7f7fcf7fffcffcffff7ffcffcff7fffff7cf77f7fec6c669cfcf7e7f77e7c7e7e7c7f77f7e7fc7f7e7c7f777e7e777e77e777e7f77c7fcfc7f77c7f77c7f77c7f7cf7f7ce7f7c7f7e7f7f7cef77c7f7f7f7cec7c7fcf7fcfcfcfcfcfcf7f7fc7f7f7f7f7f7f7f7c7f7f7fcc7f7f7ffffcff7ffffffcf7fffffffcfffff
            f7ffcf7ff7fffffffc7f7fcf7fcfc7fc7f7f7fcf7fc7f7ffcf7ff7fffffffffffffcfffcf7f7fcf7fcff7f7fffcfcff7fffcf7fffffc7fc7f7cc66fc7fcf77e7c7e7c77f777e7e7ffcff7e7f7e7e7f77c7e7c7e7f7e777e7ff7f7e77c7f77e7f77c7e7c77f7c7f7f7e7f7cf7c7ce7f7cf7f7c7cef7f7f7f7fcfcf7f7f7f7f7f7f7ccf7fcf7f7f7fccf7fcfcf7f7fcf7f7fcfcff7ffcf7fcfffffcf7fffff7ffc
            ffcffcfcff7fcf7fffffc7f7f7c7fc7fffccf7f7f7f7ffffffffffffcf7ffcf7fffff7ffff7f7fffff7fffffcff7fcfffcfcffcfcfcffcfcf7fcfecfcf77e7c7e7e7f7e7e7f7c7fc7f7c77c77e7c77e7e7f77f77777f7cfcf7f7e7f7e7e7c7f7e7c76f7fe7c7e7c7c7f7c7e7f7f7f7c7e7cef7f7c7f7f7ff7f7f7ffcffcfcf7f7fc7f7f7f7fccf7f7fc7f7f7fcc7f7fcf7fff7fffffffff7ffcfffff7fcfffff
            7ff7ff7f7ffcffffffcfff7f7ffff7f7ffff7fccf7fcffcf7fcfcfcffffffffffcf7fffcfcfffcfcffffcfcff7ffff7fcff7fffcf7ffcff7f7fefcf777e7f7e7f77f77e7c77e7fcff7f7e7f7e7f7e7c7f77e7e7f7f77e7f7f7e7c77c7f7c7f7e7f7c7e77f7f7f7f7f7c7f7f7f7c7c7f7f7f77f7f7f7ccf7ffcfcfc7f7f7f7fcfc7fcf7f7fc7f7f7f7f7fc7fc7f7fcf7f7fcfffffcf7fcffffff7ffcffffffcff
            fcffcffffcf7f7ff7fff7ffcffcffffffcfffff7fc7fffffffffffff7ffcf7ffffffffff7ffcffff7ffffff7fffcfffff7fffcffffcff7ff7fcf7f7e7f7e7c7f7e77e7f77c7ffc7f7c77f77e777c7f777e7f7c7e7e7ffcf7c7c7f7f7e7f7e7e7c7c7f7f7c7e7c7e7c7f7c7f7cef7f7c7f7cf7fc7f7f7fcfc7f7f7ffcfcf7f7f7fc7f7fcc7fcf7fccf7fcf7f7fcf7f7f7fcf7ffcffffff7fcf7fffffffcfcfffc
            f7fcf7f7fcffcfcfffcfffff7ff7fffcfff7fcff7fcfcf7ffcf7f7fffffffffcfcffcfcffcff7fcfffcf7ffffcff7fcfcffcf7f7fff7ffcfc7fc77c7f77e77e77f7e7c7c7f7f7ffcf7e77e7c7f7e77ee7f77e7e7c7fcef7c7f7e7e7c7c7e7f7f7f7e7c7c7f7f7f7f7f7fe7ce7f7f7f7f7f7cf7fcceff7f7ffcffcf7f7f7fcc7f7fcf7f7ff7f7f7f7fcf7fcfcf7f7fccfcf7fffff7ffcffffffffcfcfffff7fff
            fff7ffffcf7ff7fcfff7fcffffcffcfffcffff7ffffffffff7ffffffcfcffcfffffffff7ff7fffffcfffffcfff7ffff7fcffffffcfcffcffcf77f7f77e7f7f7c77ef7e7f7fcfcf7f77ce7f7e7e7f7e7f77e7c7f7ffcf77c7e7c7f7c7f7f7f7c7c7f7f7f7f7c7ec7ec7e7f7f7f7c7f7f7cef7fcf7f7fcfcfcf7f7fcfcfcf7f7fcf7f7f7f7fccfcf7f7f7f7f7f7fcf7f7f7ffffcfffffffcf7ffcffff7ff7fffcf
            7fffcf7ffcfcffcf7ffffffcfffcfff7fffcfffffcf7ffcffffcffcffff7fff7ff7ff7fffffcfcfff7fcfff7ffffcfcfff7fcfcff7fcff7f77f7e7e7f7c77e7ef777f7f7fcf7f7c7e7f77e7f7c77e777c7c7f77f7f7f7f7f7f77c7f77e7c7c7f7e7c7e7f7ef7f7f7f7f7f7cf7f7f7cec7f7c7f7fff7f7f7f7ffcf7f7f7f7fcf7f7fcfcfc7f7f7fcfcf7fc7f7f7f7fcfffcffffcfcf7fffffffffcfffffffffff
            fcf7ffcf7ff7fcf7fc7ffcfff7fff7ffffff7fcffffffff7fcffcff7fffffcfffffffffcf7ffff7fffff7ffffcfcfffcfffff7fcffff7fffc7e7f7f7e7f7f7777fe7cf7ff7ff7c7f7e7c7f77e7f7c7f7e7f77fcfcfc7c7e777f7e77f7f7f7e7c7f7f7f7c7c7f7c7f7c7f7f7c7f7fcf7f7f7f7ffc7ffcffcffcf7fcf7f7fcc7f7fc7f7f7fcf7fc7f7f7f7ffcfcf7fff7f7ffcffffffff7ffcff7fff7ffcffcff7
            ffcfcffcfcfff7fffffcf7ffffcfffffcf7ffffcf7ffcfffffcff7fffcfffffcffcfcfcfffcf7fffcf7fffcfffff7f7ffcf7ffff7fcfffcf7f7f7e7c7f7e7ef7e7f7fcfcfcf7e7f77f7e77c7f77e7f7e7f7ef7f7f7e7f7c7f7e7f7f7e7c7f7f7f7c7c7f7f7f7c7f7cf7ce7f7f7ce7f7f7cf7f7fcfcf7f7f7f7ff7f7fcf7f7fcf7ff7f7f7f7fcfcf7fcfc7f7f7fcfcfffffff7fcf7fffffff7ffffffffffff7ff
            fcff7f7ff7f7ffcf7f7fff7f7ffcffcffffffcfffffff7ffcff7ffffff7fcfff7ffffff7ffffffcffffffffcf7fffffffffffcfcfff7fcffc7e7c7f7e7e7f77fcfcfcf7f7f7c7e7e77c7f7f77ec7f77c77ef7fef7f7c7e7f7e7f7c7c7f7e7c7f7e7f7f7ec7ef7f7f7ef7f7f7cf7f7cc7f7f7cfcf7f7ffcffcf7f7fc7f7fcf7f7f7fcfcfcfcf7f7f6f7f7fcf7f7f7ffcfcfcfffffffcffcfffffcfcffcf7fffff
            cf7ffffcffffcf7ffcfc7ffcfcf7ffff7ffcfff7ffcffffff7fffcfcfffff7ffffcf7ffffcf7fcff7ffcfcfffffcffcf7fcfcf7ff7ffffcff7f7f7ef7f7f7cef7f7f7ffcf77e777c7e77e7e7f7e77ec7fcf7fcf7c7e7f7f7cc7c7f7f7ec7f7f7c7f7cec7f7f7c7f7c7f7cf7f7ec7f7fcf7cfcf7ffcfcf7f7fcfcf7ff7fc7fcfcfcf7f7f7f7fcf7f7fcfcf7fcffcffcffffffcfcfcff7ff7ffcfffff7fffffcf7
            fffcfcff7fcf7ffcff7ffcf7ffffc7fffffff7fffff7ffcffffcfffff7fffffcffffffcfffffffcfffffff7ffcff7ffffffffffcfffcf7fcf7c7ce77f7c7f7f7fffcf7f77f77f7e77f7f7c7f7e7f7f7ef7fcf7c7f7f7c7c7f7f7f7e7f7f7c7e7f7cf7f7f7f7f7f7ef7cf7c7cf7f7fc7f7f7f7ff7f7f7ffcfc7f7fc7fcf7fc7f7f7f7fcffcf7f7fcf7f7f7fcf7f7fff7fcf7ffffff7fffffffffcf7fffffcf7ff
            cfcff7fcff7ffcff7ffcf7ffc7f7ff7f7cc7ffcf7f7fcf7f7f7f7f7f7fcf7f7f7f7fcff7ff7ffcffcf7f7fffff7fffcfcf7fcf7ffcffffffcf7f7f7f7ef7efcfc7f7ff7f7ece7c7e7777e7f7e6f7c7f7fcf7f7f7e7c7f7f7e7c7ecf7c7c7f7f7cf7e7f7cf7c7f7f7cf7c7fc7f7f7cf7f7fcff7ffcfff7f7ff7fc7ff7f7fcfcf7fcfcf7f7f7fcf7f7fcfcfcf7ffff7fffffffcf7ffffffcfcfcffffffcff7ff7f
            f7fcffff7ffcff7ffcf7ffcfffffcffcffff7f7fcffcf7fcfcfcf7fcfc7fcfcfcf7f7c7f7ffcff7ffffffffcfffffffffffffffcff7fcf7ff7f7c7f7c7e7f7f7ffff7c7ce7f7f77f7e7e7f7c7e7f7fcfcf7f7c7f7f7f7e7c7f7f77c7f7f7ce7f7e7f7cf7f7fe7f7f7c7fc7f7f7cf7f7f7fcf7fcf7f7fcff7fcf7fc7fcf7f7f7fc7f7ffcfcf7f7fcf7f7f7fcfcf7ffffcfcffffffcffcffffff7ffcffff7fccf7
            ffff7fcffcff7ffcf7ffcfc7f7fcf7f7f7f7ffcf7f7f7fcf7f7f7fc7ffc7f7f7f7fcff7fcc7f7fc7f7fffcfff7ffcf7fcfcf7fff7fffcffcfc7f7f7ef7fffcffc7f7f7f7f7c7f7f7c7f7c7e7ff7fcf7f7ff7ce7e7c7e7f7f7c7fef7f7cef7f7cf7f7fcf7ce7fc7fecf7f7f7fef7f7fcefc7ffcf7ffcfcf7f7f7fcff7fcf7fcf7ffcf7f7f7ffcf7fcfcfff7f7fffffcffff7fcf7ffffff7ff7ffffffcf7fcf7fc
            fcfffff7ff7ffcff7ffcf7ffffffcffcfcffcf7ffcfcfcf7fcfcfcff7f7fcf7f7fc7f7fcf7fcf7ff7f7c7fcfffffffffffffffcfffcff7fff7f7e7f7c7f7ffcfff7cec7f7f7f7e7f7f7c7f7f7ffcf7ffcf7c7f7f7f7f7c7cef77c7f7f77c7f7f7f7fc7f7f7f7f7c7f7f7fcc7f7f7f7fcfff7fcffcf7f7fcfcfcf7f7f7f7fcf7fc7ffcffcf7f7fcf7f7f7ffcfcffcfff7fffffffff7fffffffffcf7f7fcf7ff7f
            ff7fcf7ffcffcf7fccf7ffcfcf7ff7ff7f7f7ff7f7f7f7ff7f7f7f7f7ff7f7fcf7ff7fc7fcf7f7f7fcff7f767c7cffcf7fcfcfffcff7fffcfc7f7f7f7ffcfff7fcf7f7f7c7f7f7f7e7f7f7cfcf7f7fcf7c7f7c7f7c7c7f7f77f7f7c7ef7f7c7c7fcf7f7c7f7f7fcf7f7f7f7f7fcccf7f7f7ff7f7fcffcf7f7f7fcf7fcff7f7fcff7f7f7f7fcf7f7fcfcfcf7f7ffff7fffcfcfcfcfffcffcffcffffcf7f7f7fcf
            7fff7fffcfcffcfff6f6fcf7fffcffcffcffcfcffcffff7fcfcff7fcf7fcff7fcf7fcf7fc7f7fcfcf7cf7fcccf767f7ffffff7fff7fffcff7fc7f7fefcff7fffff7c7f7fef7cec7fcc7f7ff7fcfcfcf7f7f7f7f7c7f7f7e7f7c7ce7f7c7f7f7ffc7f7cf7f7f7cc7f7cccf7fcf7f7fcffcffcffcf7f7f7f7fcf7f7fcf7f7fcfcf7ffcf7fcfcf7fcfcf7f7fcfff7fcfffffffffffffcfff7fffff7f7fcfcfcfcf7
            ffcfffcfff7f7fcf7ffeffcfcf7fcff7ff7fcf7fcf7f7ffcf7f7ffcf7fcf7fcf7fcf7ff7ffcf7f7f7f7fcf7f7fcfc7f7c77cfffcfffcff7fff7f7ccf7f7fffcfcff7f7f7c7f7f7f7f7fefcfcf7f7f7fc7f7e7f7ef7ec7f7c7cf7f7f7f7f7cffc7f7cf7cf7fccf7f7f7f7f7f7cf7ff7f7f7f7f7fffcfcf7fc7fcfcf7fcfcf7f7ff7f7ffcf7f7fcf7f7ffcf7f7ffffffcfcf7f7fcffff7fffcf7fcf7f7f7f7f7ff
            cffcfcfcfcffffcffcff7ff7fcff7fffcfff7fff7ffcfcf7fffcfcf7fcf7fcf7fc7fc7ff7f7fcfcfcfcf7f7f67c7ff7ffff7f7c7f7ff7fffcfffff7ffffffff7ffffcf7fcf7f7f7f7fcf7f7fcffcff7f7cef7c7f7f7f7c7fc7c7f7c7f7cfef7f7f7f7f7ce7f7f7fcf7fc7fcf7fcfcffcffcffcf7f7f7ffcff7f7f7fcf7f7fffcfcfcf7f7fcfcfffffcf7ffcffcfcfffffffffff7fcffffff7f7f7ffcfcffcf7f
            f7ff7ff7ffcf7ff7ff7ffcff7c6ffcf7fcfcfcfcfcf7f7ffccf7ff7fff7fcf7fcff7ff7fcfcf7f7f7f7fcfcefffc7fc7c7f7f7fcf7f7ffcff7fcfffcfffcfcffffcf7cf7e7f7fcecf7fcfcf7f7f7f7f7f7f7cf7e7c7cef7c7f7f7f7f7f7f7f7f7ce7f7f7fc7f7f7c7f7fcf7f7ff7f7fcf7f7f7ffcfcf7f7f7fcfcf7f7fcfc7f7f7f7fffffff7fcf7ffffcf7fffff7ff7ffcffcfffffcfcf7ffcfcf7f7f7cf7fc
            ffcfffcff7fffcffcffcf7fcff7ffcffff7fff7fffffffcff7ffcffcfcff7ffcf7fcf7fcf7f7fcfcf7f7f7f7f7cfcf7ff7fcfc7f7fcf7c7fcfffcfcfcfffffffcff7f7f7fcf7f7f7ffcf7ffcffcf7cce7f7c7ef7f7f7f7c7f7f7cec7fcff7f7cf7fc7f7f7fc7fcf7fcf7f7fcf7ffcfcf7ffcffcf7f7fcfcfcf7f7ffcf7fcffcfcfcf7fcf7fffffffcf7fffffcf7ffffffff7ffffcfff7f7fc7f7f7fcf6c6cfcf
            cffcfcfcffcfcf7c6cf7ffcfcffcf7fcfcfcfcfcf7fccf7fffcff7ff7fcffcf7fcf7fcf7fcfcf7f7ffcfcf7fcf7f7fcf7fc7f7fcf7f7fcf7f7cff7fff7ff7fff7fff7fcf7f7fcfcfcf7ff7f7f7f7f7f7f7f7f7c7f7f7c7f7f7cef7ffcf7cc7f7ce7f7fecf7fc7f7fc7fcf7f7ffcf7f7ffcf7fcf7fcf7f7f7f7fff7f7ffcf7f7f7f7fffcffcf7f7fffffcfcfffffffcff7ffffcfff7f7fcf7ffcfcfcf7fcf7f7f
            f7ff7fff7fff7fffcf7ffcf7f7fcfff7ff7fcf7f6fcffcfcf7fcffcfff7fcfcff7ff7fcf7f7f7fcf7f7f7ff7f7fcf7f7fef7fcf7f7fc7f7f7f7c7ffcffffffcfffcfc7f7f7fcf7f7f7fcfcfcf7f7f7f7ce7f7f7f7cef7f7f7cf77f7f7f7f7fcef7f7f7c7f7f7fcf7fcf7fcffcf7ffcfcf7ffcf7fcf7fcf6fcfc7fcff7f7fcffcfcf7fff7ffffffcf7fffff7ffcfffffffffcfff7ff7fcf7fc7f7f7f7fcf7ffcf
            cfcffcfffcfffcfc7fcfcf6fcff7f7ff7fff7f6c7c7f7ff7fff7fcf7fcff7ff7ffcff7fcfcfcf7fcfcfffcffffc7fcfcf7fcf7f7fc7fcf7fcf7fc7f7ffcfffff7ffffcf7fcf7ffcfffcf7f7f7f7f7ccf7f7f7cf7f7f7c7f7c7cfcfcff7f7f7c7f7fccf7f7fcf7f7fc7f7f7f7fcf7ff7fcfcf7fcf7ff7f7fcf7ffcf7ffcfcf7f7f7fff7ffcf7fcffffcf7fffffff7ff7ffcfff7ff7fcf7ff7ffcfcfcfcf7fcf7f
            fff7ff7fff7fff7ffcfcf7ffcfcfffcffcfcfcfcfcfffcffcfcfcf7fcf7ffcffcf7fcf7f7f7fcf7f7f7cf7f7f7ff7f7f7f7f7fcf7ff7f7f7f7f7fc7f7cff7fcfffcff7fcf7ffcf7f7f7f7f7f7fccf7f7f7f7f7ec7f7f7f7fef7f7f7f7f7ccf7f7f7f7f7fc7f7fcf7ff7fcfcf7ffcf7ff7f7ff7f7f7fcff7f7fc7f7fcf7f7fcfcff7cfffffffff7fcfffffcfcf7fffffffff7ffccf7fcf7ffcf7ff7f7fcfcf7fc
            f7fffcfcfcfcfcffcf7fffcf7ff7fcf7ff7ff7ff7fcf7f7ff7fcf7ff7ffcf7f7fffcfffcfcf7fcfcfcf7ffcfffcffcf7fcfcf7f7f7fcf7fcef7f7fcf7f7cffffcff7ffffffcf7ffcfcf7f7f7f7f7cf7cecccef7f7ce7f7c7c7fffcf7fccf7f7fc7f7f7f7ff7fc7fc7fcf7ffcfcf7ffcffcfcfcffcfcf7fcff7ffcfcf7fffcf7f7fffffcf7fcfcfff7f7fffffffffcffcf7ffc7f7fcf7ffcffcfcf6fc6f7fcff7
            ffcfcfff7fff7fcffffcf7fffcffcfffcff7ffcffcf7fffcffcf7fcffcf7ffcfcf7f7f7f7fcf7f7f7fcf7f7f7fcf7ffcf7f7fcfcfce7fcef7fcfc7f7f7f7c77fffffffcf7ff7fcf7f7fcfccf7f7f7f7f7f7f7c7fc7fc7fef7fc7f7fc7f7ef7c7fccf7fcf7fcf7fcff7fcf7f7f7ffcf7f7fcf7f7f7f7fcf7fcfcf7f7ffcf7f7fcf7cf7ffffff7ff7fffff7fcf7fffffffffcf7ffcf7ff7fcf7ff7fc7fcffcf7ff
            cfff7f7fff7ffff7f7ffffcf7fcf7f7fcfcfcf7f7fffccf7f7fffcf7f7ff7f7ff7ffcfcff7fcffcff7fcfcfcf7fff7fcfcfcf7f7f7ff7f7f7f7f7fcf7fcf7fc7cf7ffcfffffff7ff7f7f7f7fccf7f7fcf7f7f7f7f7f7f7cffcffc7c7f7f7cf7f7f7fc7f7fc7fcf7f7fcfcfffffcf7ffcff7fcfcfcfcf7ff7f7f7fffcf7ffcfcf7ffffffcfcffcfffcfcfffffffcfcf7f7f7ff7f7ff7fcf7ffcfffffc7f7ffcf7
            fcfcffffcfffcfcfffcf7ffcff7ffffcf7ff7ffffc7ff7ffffc7ff7fff7ffcfcffcff7f7ffcf7f7fcf7f7f7fcf7cffcf7f7f7fcf7fcf7fcfcf7fc7f7f7c7f7fc7f7ffffcf7fcff7fcfcf7f7f7f7fec7f7f7f7f7f7f7fef7f7f7cf7f7cc7f7fcf7fc7fcfcefcf7fcfcf7f7f7f7f7ff7ff7fcf7f7f7f7fcf7fcfcfc7f7ff7f7f7ffc7ffcffff7ffcfcfffcf7ffcffffffcf7fccfcf7fcf7ffcf7fcf7f6f6fcf7ff
            ff7fcfcff7fcfffcfcfffcf7fffcf7ffff7ffcf7fffcffcf7fffcffccffcf7f7f7fcffcfcf7fcff7fcffcff7fff7f7ffffffcf7ff7f7fcf7f7f7ff7fcf7fcf7f7fc7cfffffff7fcc7f7f7fcf7fc7fcf7f7fccf7fcef7cffcff7f7f7f7fc7f7f7f7fcf7f7f7f7fc7f7ffffcfcfffcff7ff7f7fcfcfcf7f7ff7f7fffcfcfcffcfcf7fffff7ffffcfff7ff7fffffcf7f7c7ffcf7fcfcf7ffcf7ffcf7fcc7ff7ffcf
            7ffff7fcffff7f7fff7f7fffcf7fffc7fcfcffcfcf7fcf7ffcf7f7ff7f7fcfffcfcf7ff7f7ff7fcf7f7f7fcf7fcfcf7f7f7f7ff7fcfcf7f7fcfc7fc7f7f7f7f7f7fc777fcf7ffcf7fcf7fc7fc7fcf7f7fc7f7cf7f7fcf7ff7cf7ccf7f7fcf7fccf7f7fcf7fffcff7fcf7fcf7f7f7fcfcfcffcf7f7fcfcfcfcff7f7fcf7f7f7f7ffcfcffffcfff7fffffffcf7ff7fcfff7f7ff7ff7ffcfcff7f7ffcfffcffcf7f
            ffcfffff7fcffffcfcfffcf7fffcf7ffffcf7ff7fffcfffcf7ffffcffcff7f7fcf7ff7ffcfcff7ffcffcfcf7fcf7fcfcfcfffcfcf7f7fcfcf7f7fcfcf7fcef7fcc7fffc7fffcf7ff7f7ffff7ff7f7f7f7fecf7ef7ff7ff7fc7f7f7cf7f7e7f7f7fcfcf7ffccf7fcff7ffcf7ffcffcf7f7f7f7ffcf7f7f7f7f7ffcfcf7fcfcfcf7f7fff7fff7fffffcf7fffffcfcf7f7fcfc7ff7ffcff7f7ffcfcf7f7f7fcf7fc
            fcf7fcfcfff7fcff7fcfcfffcf7fffcf7ffcfcffcf7f7f7fffcf7fc7ff7ffcff7ffcffcf7fc7ff7fcf7f7fcfcf7fcf7f7f7f7ff7ffcf7f7f7fcf7f7f7fcf7fc7f7f77c7f7cfffc7fcfffcffff7fcf7fcf7f7f7f7fcffcfc7f7fc7f7f7cfcf7fcf7f7f7fcf7fff7fcff7f7ffcfcf7fcfcfcfcf7f7ffcfcffcff7fcf7ffcf7f7fcffffcfffcfffcfcffffff7f7f7f7fcf7f7ff7fcfcf7ffcfcf7fcffcfffcf7fff
            cffff7ffcfffff7ffff7f7fcfffcfcfff7ff7fcf7ffffcfcf7fcfcff7ffcfcf7fcf7f7fcffff7ffcf7fff7fcf7ff7ffcfcfcf7ffcf7ffcf7fcf7fcf7fc7f7f7fcf7ff7fcf77ffff7fcf7fcfcfff7fcc7fcf7fcf7ff7f7f7fcf7fcf7fef7f7fc7fcf7ff7fff7fcfcf7ffcfcf7f7ffcf7f7f7fcfcf7f7fc7f7fcfcf7fc7ffffff7f7ffffcfffcffff7ffcf7fcfcf7fcf7fcf7ffcf7fffcf7f7ffcf7f7f7cfcfcf7
            fcf7fff7fcf7fffcf7ffffff7fcf7fcfcfcfff7ffcf7ffcfcffcf7fffcf7f7ffcfcffcf7f7fcfcf7ffc7ffcf7fcff7f7f7f7ffcf7ff7f7ffc7fcf7fcf7fcf7f7f7f7cf7f7fc77ffffffffffffcfff7ff7f7f7f7fcffcf7f7f7f7f7f7f7f7f7ff7f7fcff7fcf7f7fcfcf7f7ffffcf7ffcfcf7f7fcffcfffcfcf7fcfcffffcffffcffcffff7fff7ffff7f7fcf7f7ff7ffcf7fccf7fcf7fcfffc6f7fff6c6ff7fff
            ffcffcffffffcfcfffcfcf7ffcffff7ff7fcfcfcffcfcf7ff7f7ffccf7ffffcf7ff7f7fffcf7fcff7fffcf7ffcf7fcffcffcf7f7fcfcfcf7ff7fcf7f7fc7fcfcf7fcf7f7f7fcf77fcf7fcf7ffffcff7fccf7fcffcf7f7fcf7f7f7fccf7fcfc7fcfcf7fcfcf7fffcf7fffffcc7f7ff7f7f7ffcfcf7f7f7f7f7ffcf7f7fcfff7ffffff7fffffcfffc7fcfcf7fcff7fcf767fcf7ffcfcff7f7f6fcfcf7ff7fffcf7
            fcfcff7fcf7ff7fcfcfffcfcff7f7ffcfff7ff7fcf7ffff7ffffcff7ffcf7fcff7ffcfcf7fffcf7ff7f7fcf7fcfcf7f7f7f7fcffcf7f7fcf7fff7ffcf7ff7f7f7fc7f7fcec7f7fc7fcffffff7ffffffc7f7fcf7f7fcfc7f7fccfc7f7fcf7ffcf7f7ffcf7fffccf7ff7f7f7fffcfcfcffcfcf7f7ffcfcfcfffcf7ffcffff7fffcf7ffffcfcfff7fff7f7f7fcf7fcf7f676cf7fcf7f7fcfffcf7ff7ffcffcf7fff
            ff7fcffff7ffffff7fcf7fff7ffffcff7fffcfff7ffcf7ffcf7ff7ffcf7ffcf7ffcf7ff7fccf7ff7ffcff7ffcf7ffcffcfcfcf7f7ffffcf7fcfcfcf7fcf7fcf7f7fcf7f7f7f7f7f7f7cf7fcfff7fcffffffcf7f7f7f7fcf7f7f7fcfcf7fc7f7fcff7f7ff7f7ff7fcffcfcfc7ff7f7f7f7f7ffcf7f7f7f7f7f7ff7f7ff7ffffffffcffffff7f7f7cfcfcff7f7fcf7f7ccfcffcf7fffcf7fcfffcffcffcf7ffcf7
            fffff7fcfffcf7fffffcfcfcffcfcf7ffcf7fcfcfcf7ffcffcfcffcf7ffcf7ffcf7ffcffcf7ffcffcf7fcfcf7ff7fcf7fcf7fcfcf7f7ff7fff7ff7fff7fcf7fcfcf7fcef7fcf7ccf7f7fcffcfffff7fcf7ff7fcfcf7f7f7fcf7fc7f7fcf7fcf7f7ffffcffcfcffcf7fcf7fff7ffcfcffcff7f7ffcfcfcffcff7ffcffffffcfcf7fff7fc7fcfcff7f7f7f7ffcf7ffcffcf7f7fcfccf7fffcf7ff7ff7ffcfcffff
            cf7fffff7fcfffcf7fcfff7fcff7fffcffcff7ff7fffcff7fff7fcfffcffcfcf7ffcf7fcfff7f7f7fcff7fcff7ffcf7fcf7ff7f7ffcf7ffcfcfcffcf7fc7fc7f7f7f7f7fc7f7fc7f7f7c77fffcffffffffffff7f7fcfcfcf7fcf7fcf7f7ff7ffcfcc7fcf7fcf7f7ffcf7fcf7fcf7f7f7f7ffcfcf7f7f7f7fcfcf7f7fcfffffffffcffcff7f7f7fcfcfcff7f7f676f7f7ffcfcf7f7ffcf7fffcffcff7ff7fcf7f
            fffcf7fcfff7fcfffff7fffff7ffcfff7ffcffcffcf7fcffcf7fff7fcf7ff7fffcf7fff7f7ffffffcf7ffcf7ffcf7ffcf7fcffcfcf7ffcff7ff7fcfcfffcf7fcf7fcf7f7fcf7f7f7fcf7fc77f7ffcfcfcfcfcfffc7f7f7f7fc7ffcf7ffcf7fcf7ffffcf7ff7ffffcf7ffcf7ff7ffcfcfcfcf7f7ffcfffcfcf7fcffffff7ff7fcf7f7f7f7fcfcf7f7f7f7fcffc7c6fcc6cf7f7ffffcf7ffcf7fcf7fcfcffffcfc
            f7ffffffcfcfff7fcfcfcf7fffcff7fffcff7ff7ffcff7fcf7ffcfff7ffcffcf7fffcf7fffccf7f7fffcf7ffcf7ffcf7ffcf7f7f7ffcf7f7fcfff7ff7f7ffcf7fcf7fcfc7f7fcf7f7c7f7ff7fc77f7ffffffffc7ffcf7fcf7ff7f7ff7f7ffcf7fcf7f7ffcffc7f7ffcf7fcfcfcf7f7fcf7fcfff7fcf7fcf7ff7f7fcfcffffff7fcfcfcfcf7f7ffcfcfcf7f7ffc6fe67c7ffffc7f7fffcffcff7fffcff7f7ff7f
            ffcf7fcf7ffcfcffcfff7ffcfcfcffcf7fcffcffcff7fff7ffcfcf7ffcff7ffffcf7fffcf7ff7fffc7f7ffcf7ffcf7ffcf7ffcfffc76fcffcf7fffcffcfcf7fff7fc7f7ff7f7f7fcfefcf7cf7fcf7f7c7ff7ffff7f7fcf7ff7fcfcf7fcfcf7fff7ffcfcf7f7ffff7f7ff7fcf7f7ffcf7ff7fc7ffcf7ff7ff7ffcfffffff7f7fcf7f7f7f7ffcf7f7f7f7ffcfcffeff7c6fc7f7ffffcf7fcf7fcfcf7f7ffffcffc
            fcffffcffcff7ffcf7ffffcfff7fcffffff7ffcf7fcfcfcfcff7fffcff7ffcf7ff7fcf7fcfcffccfffffcf7ffcf7ffcf7ff76c76f7c67f7f7ffc7ff7ff7fffcfcfcfcf7f7fcf7fc7f7f7cf7f7f7f7fcf7c7ffcfffcf7f7fcfcf7f7ffcf7f7fcfcfcf7ff7fffcf7ffcfcff7f7ffcf7fcf7ffcffcf7ffcffcffcfffcf7f7fcfcf7ff7ffcfcf7fcfcffcff7fcf7f7fcf6cffffcffcfcf7ff7fffcf7ffffcf7fcf7f
            ff7fcff7ff7ffcffffcf7ff7fffff7f7fcffcffffff7fff7fcffcf7f7ffcff7fcffffcff7ff7ff7f7f7fcffcf7ffcf7ffcfc6c6effcf6cfffcfff7ff7ffcf7fcf7ff7fcfcf7fc7fcf7f7f7f7f7f7f7c7ffc7f7fcf7ffcfcf7fcfcf7f7ffcffcf7f7ffcffcf7fcfcf7f7fcfffcf7ff7fcfcf7f7fff7fc7f7f7f7f7fcfcf7f7f7f7ff7f7f7fcf7f7f7f7ffcffffff7fff7f7ffcf7ffffcffcf7fffcf7ffcff7ffc
            fcfff7fffcffcf7f7ffffcffcf7fffffff7ff7f7f7ffcf7fff7ff7fffcff7ffff7fcf7fffcff7ffffcff7f7fffcf7ffcf7ffefff7fcfef7f7f7f7fcfcfcfcff7ffcfff7f7fc7c67cf7fccf7fccfccf7f7cf7f7f7ffcf7f7fcf7f7ffcf7ff7f7ffffcf7f7fcff7fcffcf7f7f7f7fcff7f7f7fff7fcfcffffcfcfcf7f7f7fcfcfcfcfcfcff7f7fffcfcfcff7f7fcffcfcfffcffcfcf7ff7ffcfcf7fffcf7fffcff
            7fcfcffcffcffffffcf7ffcffffcf7fcfcfcffffffcffffcfcfcffcfcf7ffcf7fffcffcf7f7ffcf7ff7ffffc7f7ffcf7ff7ff7fcfcf7fcfcfcfcfcf7f7ff7fffcf7f7fffcf7fc6c76f7f76c7f7f7f7fcf7fcf7fc7f7f7ff7f7fff7fcff7ffffc7f7fffcff7fcff7f7fcfcfcfcfcf7ffcffcf7fcf7ff7f7f7f7f7ffcfcfcf7f7f7f7f7f7ffcfc7f7ffcf7ffcff7fcf7fcf7f7fff7ffcffcf7ffffc7ffcfcf7fcf
            fff7fcff7ff7fcf7ffffcff7f7ffffcf7fff7fcfcff7cfcfcff7fcf7fffcf7ffcf7fcf7ffffcffffcffcf7fffffcf7ffcff7ff7fcf7f6f7fcf7fcf7fff7ffcf7ffcffcf7ffcf7fccfcf7cccf7fcf7fc7fc7f7f7fc7f7fc7fcf7cfcf7fcfcc7fffff7f7fcffcf7ffcf7f7fcf7f7fcf7fc7f7ffcfcf7fcfcfcfcff7f7f7f7ffcfcfcfcfcf7fcfffcfcf7ffcff7fffffff7ffffc7ffcf7fcf7ff7f7ffcf7ffcff7f
            cfffff7ffcfff7fff7fcf7ffffcf7ffffcfffff7fcf6c7ff7fffffffcf7fffcffcff7ffcfcff7fcf7fcfcfcf7fcfffcf7fcfcffcf7fcc7cf7ffcf7fccfcfcf7fcf7f7fffcf7ffcf7f7fcf7f7fc7fcf7f7fcf7fcf7fcf7fcf7fcf7f7fcf7fffcf7fcfcff7f7ffcf7fcfff7fcffcf7ffcffcfcf7f7fcf7f7f7f7f7fcfcfcf7f7fcf7fcf7ffcf7f7fcf7fcff7ffcf7f7fcfcf7fffcf7fff7fffcfffcffcfcff7fff
            f7fcfcffcfcffffcffffffcfcffcfcf7ff7fcfcfffff7f6ffcf7f7fcfcfcf7fcf7fffcff7fcffcffff7ff7fffcf7f7fffcf7fcf7ffcfff6ff7f7ffcf7f7f7fffcf7ffccf7ffcf7fcf7c7cf7fcfc7f7fcf7f7fc7fcf7fcf7fc7f7fcf7f7fc7f7ff7ff7fcfff7f7ff7f7fcfcf7f7ff7f7f7f7f7ffcf7ff7ffcff7fcf7f7fcfcfcf7ff7ffcff7ffcf7fffcf7ffcfffcffcf7ffcf7fffcfcffcffcfcf7ff7f7ffcf7
            fff7ffcff7fcf7ffcf7fcff7fcff7fffcfffcff7f7fffffcffffffff7ff7fff7ffcf7fcfff7fcf7f7ffcffc7ffcfffcf7fffcf7fcf7f7fcf7fffcf7ffcfffccf7ff7f7fffcf7ffcf76c667cf7f767cf7fcfcf7fc7fcf7fc7ffcf7f7fcf7ffcf7fccfcf7f7ffcfcffcf7f7f7ffcf7fcfcfcfcf7cf7fcfcf7f7ffcf7ffcf7fcf7ff7ffcf7fffcf7ffc7f7ffcff7fcf7f7ffcf7ffcf7fcf7ff7ff7fffcffffcffcf
            fcffcff7ffffffcffcfff7ffff7ffcfcfcf7f7ffffcf7fcf7f7fcf7ffcf6ccffcffcff7fcfff7ffffcff7fffcf7fcf7ffcf7fffcfffcff7ffcf7fcfcf7f7f7f7fcfcff7f7fffcf7ffc67cf6fcfcccf7fc7f7fcff7f7fc7ff7f7fcfcf7ff7f7fcf7f7f7fcf7f7f7f7fcfcf76b7f7ff7f7f7f7f67cfcf7f7fcf7f7ffcf7ff7f7fcffcf7ff7f7fffcfffffcff7ffcfcfffcf7ffcf7fff7ffcffcffcfcf7fcff7ff7
            ffcff7fffcf7fcf7ff7fffcf7ffcff7ff7fffffcfcffffcfffffcf6cffcf76fcf7ff7fff7f7ffcfcff7ffcfcffff7fffcfcfcf7f7f7fcffcf7ffcf7fcfcfcfffcf7f7fcfcf7ffffc7ffcfcf7f7f7ffcf7fcf7f7fcfcf7fcfcfcf7f7fcf7fcf7f7fcfcfcf7fcfcfcf7f7f76b6fcfcfcffcfcfcf6f7f7ffcf7ffcfcf7ff7ffcfcf7f7ff7ffcfc7f7f7f7fcfcfcff7fcf7fffcffcfcfcfcff7ffcff7ffffcf7ffcf
            fcf7fffcffcfffffcffcfcfffcff7ffcfffcfcff7fcf7ffcfcf7ffc7fcff6c7fffcffcfcfffcff7f7ffcff7f7f7ffcfcf7ff7ffffffcf7f7ffcf7ff7fcf7fc7f7ffcfcf7f7fc7f7ff7fcf7fcf7ff7fffcf7fcfcf7f7ff7f7f7f7fcf7f7fcf7fcfcf7f7f7fcf7f7f7ffcffcfcf7f7f7f7f7fcf7feffcf7fffcf7f7ff7ffcf7ff7ffcfcfcfcffffcffcff7ff7f7ffcf7fcf7f7ff7fcf7fcffcff7ffcf7ffffcff7
            fffffcff7ff7f7fcfcff7fcfcf7fffcfcfcfcf7ffffffcff7fffcfff7f7fffc6f7fcf7ff7fcf7ffffcff7ffffffcff7fffcffcf7fcf7ffffcf7ffcffcf7ffffcfc7f7fcfcfcffcf7fcf7fcf7ff7fcf7ff7fcf7f7fcf7fcfcf7ff7fcfcfcf7fcf7f7fcfcfcf7ffcff7f7f7fcf7ffcffcf7676fcfcf7fcfc7f7ffcfcfcf7fcf7ffcf7f7fcf7f7f7fcf7fffcffffcf7fffcffffcfff7fffcf7fcffcffcfc7f6f7ff
            cf7fcf7ffcffffff7fcffff7ffffcff7ff7ffffcf7f7ff7ffcfcf7fffffcfcfffff7ffcffcfffcf7ff7ffcfcf7ff7ffcf7fcf7ffcfffcf7fcffcf7f7fffc7f7fcfffcf7f7f7f7fcfcfcff7ff7fcf7ffcfff7fcfcf7fcf7f7ff7fcf7f7f7ffcf7ffcf7f7f7ff7fc7fcffcfcf7fcf7f7f76bccf7f7ff7ffffcfcf7f7fcfcf7ffcf7ffcff7ffcfcff7ffcf7f7fcf7ffcf7fcf7ff7fcfcf7fffff7ff7ff7ffccffcf
            fffffffcf7fcfcfcfff7fcffcfcff7ffcffcf7ffffffcfffcf7fffcc6ffcff7fcfffcff7ff7fcfcfcffcf7fcffcffcfffff7ffcff7fcfcff7f7fffcfc7fffcfcf7f7fcfffcfcf7f7f7fcffcfcfcfcf7fcfcf7f7f7fcf7fcf7fcf7ff7ffcf7f7fcf7ffcfcf7f676cf7f7f7f7ff7ffcfcfcff7ffcfcffc7f7fcf7fffcf7fffcf7ffcf7fcfcf7ff7ffcffcfffcfcfcffcff7ffcffcff7ffcf7fffcffcffcfcf7ff7
            f7fcf7fcff6ff7ff7fffff7ff7fcffcff7ffffcf7fcff7fcfffcf7ff7c6f7fffc7fcf7ffcffcf7ff7fcffff7fcf7ff7f7fcffcf7fff7ff7ffffc7ff7ffc7fcf7ffcfcf7cf7ffcfcffff7fcf7ff7ffcff7ffffcfcfcf7fcf7fcfcf7ffc7f7fffcf7fcf7f7ffc7cf7cfcffcffcff7f7ff7fcffcf7ff7ffffff7ffccf7ff7f7fffcf7ffcf7fff7ffcff7ff7fcf7fff7ff7ffcf7fcf7ffcffffcf7fcf7fcf7fffcff
            fffcfff7fcfcffcffcf7fcffcfff7ffcffcf7ffcffcfcfff7fcfffcff6f7fcfcf6cfffcff7ffffcfff7f7fcff7ffcffffcfcf7ffcfcfcffcf7fffcffcfffcf7fcf7f7ff7ff7f7ff7c7fff7ffcffcf7fffc7fcf7f7f7ff7ffcf7fffc7ffcfc7f7ffcf7ffcf7ffcffcf7f7f7f7fcfcfcffcf7f7ffcff7f7f7ffcff7ff7ffcfcf7fff7ff7f67cfcf7fcf7f6c7ffc7ffcffcffffcfffcff7f7ffcff7fcf6ffcfcfcf
            cfcf7fcfcfcf7ffcffcfff7ffcfcffcf7ffffcff7ff7fcfcff7f7ff7ffccfcffff767ff7ffcf7ff7fcfffcf7ffcff7fcff7fffcff7ff7fcfcfcf7f7fc7f7fcff7ffff7ffcfcffcffffc7ffcff7ff7ff7fffcffffcff7ff7f7ff7f7ffcf7fffcfcf7ffcf7ffcff7f7ffffcffcf7ff7f7ff7fffcf7fcffcffcf7fcf7ffcfcf7ffc7ffcffc7c667fffcffccf6c6ffcf7fcf7f7ff7f7fcffffcff7fffcfcfff7fff7
            ff7fffffcffffcff7ffcfcffcf7fcffffcf7ff7ffcfff7ff7ffffcffcfff7fc7fcffccffcffcfcffff7fcfffcff7ffcf7ffcf7fcffcfff7ffcffffffffff7fcffc7fcfcf7ff7f7f7fcffcff7ffcffcffcf7f7f7ff7fcfcfcf7fcfcfcfffcf7ff7ffcf7ffcfcf7fffcf7ff7ff7fcffcf7ffcf7fffcf7ff7fcff7fffcf7ff7fcfffcf7f7fc6cc6fcf7fcf7fc7fcf7ffffffffcfffff7fcfcf7fffcfcf7f7fff7ff
            cfffcf7ff7f7ff7ffcf7ffcffffff7f7ffffcffcff7fffcffcf7c6fcf7fcffffffcfff7ff7ff7fcf7fffcf7ff7ffcffcfcf7fff7fcf7fcfcf7f7fccf7f7ffcf7fffcf7fcf7ffcfffcf7f7f7ffcf7ffcf7ffcfcfcffcf7f7fcfcf7fcf7f7fffcffcf7ffcff7fffcfcfcfcffcffcf7f7ffcf7ffc7f7ff7ffcf7ffc7fcff7fffcf7ff7fffcfffefcf7ff7ffcfff7ffcf7f7fcff7fcfcfff7fffcfcff7fffffcfcf6
            fcfcfffcffffcfffcfffcff7f7f7ffffcf7ff7ff7ffcf7fcfffcfcffffcfcf7f7ff7fffcffcffffcfcf7fffcffcff7ff7fffcfcff7ffcf7fffffcf7ffffcff7fcf7fff7ffcf7fc7ffcfffcfcf7ffcf7ffcf7ff7fcf7ffcff7f7ffcf7ffcf7f7fcfffcff7ffc7fcf7f7ff7ff7ff7fffcf7ffcfffffcffcf7ffcfffcf7ffcf7fffcffcf7fcf7ff7ffcffcff7fcfcffcfffcf7fffcff7fffcfcfff7ffcc6cfff6fc
            fff7fcff7fcf6f7ff7fff7ffffffcfcffcffcffffcffffff7fcf7f7f7ff7fffffcffcf7fcff7fcf7ffffcf7fcff7ffcffcf7fcf7ffcf7ffcf7fcfffcf7ff7fffcff7fcfcf7ffcff7f7fcff7fcfcffffcf7ffcfff7ffcf7fcfffcf7ffcf7ffcff7f7ff7ffcfffcf7fff7ffcff7ffccf7ffcf7f7f7f7fcf7fcf7f7f7ffcf7ffcf7fcffcf6fcfcf6ccf7ff7ffcff7fcfcfcfffcfcf7ffcfcff7f7fffcfcfcf7ffff
            7fffff7fffff7fcfffcf7ffcf7fff7fcff7ffcf7ffcf7fcfff7ffffffcffcf7fcf7c6ffff7fffcffcf7ffcff7fcfcff7ffcff7ffcffcfcf7ffcf7f7fffcffcf7f7ffcf7fffcf7fcfffcf7fff7ff7f7f7ffcf7f7ffcffff7fc7f7ffcf7ffcf7fcfcf7ffcf7f7f7ffc7ffcf7f7cf7ff7fcf7ffcfcfffcf7ffcffcfffcf7ffcffcfff7ff7c76f7c7c6cfcffcf7fcfff7ff7fcfff7ffcff7fcfffffcff7fffffcf7f
            fcf7fffcf7ffffccfcfffcffcfcfcfff7ffcffffcfffff7fcffcfcf7ff7ffcffcfcfcf7fcfcf7fcffcfcff7ffffcf7ffcf7fffcff7ff7fffcff7fffcf7fcf7ffffcf7ffc7f7ffcf7f7fcfcfcfcfcffffcf7ffcfcff7f7ffcffffcf7ff7f7ffcf7ffcf7fffcfffcfffcf7ffc6c6fcffcfcfcf7ff7fcf7ffcf7ff7fcf7ffcf7ff7fcfcf6cc6cfff6ff7fcf7ffff7fffcffff7fffcff7ffff7fcfcf7fff7fcffffc
            ffffcfcfffcfcfff7fcf7fcffff7ff7ffcff7f7ff7f7fffff7ff7fffcffcff7ff7ff7ffcfffcfff7fff7fffcf7ffcfcf7ffcf7fcff7ffcf7f7ffcfcfcff7fffcfcfffcfffffcf7ffcff7f7ff7ff7f7fcf7fcff7fcffcfcf7f7f7fff7ffcfcf7ff7ff7fcf7fcf7f7f7fcfcffffcf7fcf7ff7ffcffcf7fcf7ff7ffcf7ffcfffcfffcf7f7c6c7fcfcfcff7ffcf7ffcfcf7fcffcf7fcfffcfcfff7ffffcffff7f7ff
            7fcff7fcfcf7fcffff7ffff7f7ffcffcff7ffffcffffcf7fcfcffcf7fcff7ffcffcffcff7f7fcf7fcf7ff7ffcfcf7ffffcf7fff7fcfcffcfffcff7fff7ffcfcf7f7fcf7f7fcf7fcf7fcfff7ffcffcfcf7ffc7fff7f7ff7fffcffc7ffcff7fffcff7fff7ffcf7ffcffcf7f7f7f7ffcf7fcffcf7f7ffffcffcffcf7ffcff7fcf7fcffffcf7fff7ff7fcffcffcffcff7ffff7ffffff7fcf7fcfcffcfcfcf7ffffcf
            fff7ffff7fffff7f7fffcfcfffcffcff7fffcfcfcfcffffffff7fffffcf7ffcfcff7ff7fffffcffffcfcffcff7fffc7fcfffcfcffcff7ff7fcf7ffcf7ffcfcfffffcffcffcf7ffcffcf7fcfcff7ff7fffcfffccffcfcffc7ff7fffcff7ffc7f7fcfccffcf7ffcf7fcf7fffcfffcf7fff7f7fffcfc7fcf7ff7fcffcff7ffcffff7f7fcfffcfcfcffcf7ff7ffcf7fffcf7ffcf7fcfffcffff7fcf7f6ffcfcfcffc
            f7ffcf7fffcf7ffffcfcff7fcff7ff7fffcfcf7ff7fcf7fcf7fff7fcf7fffcff7fffcffcf7fcf7fcf7ffcff7ffcf7fff7f7ff7fcf7fcfcffcfffcff7ffcff7f7fcf7f7fcf7ffcf7fcf7ffcf7fcf7ffc7fcf7ff7f7fcf7fffcff7f7f7ffcfffffcf7ff7f7ffcf7fff7ffcf7fcf7fffcfcfffc7ff7fff7ffcffcf7ff7ffcf7f7fcfffcf7fcffff7ff7ffcffcf7ffcf7fffcff7ffcf7ff7fcfff7fcfcf7fff7fcf7
            ffcffffcfcfffcfcff7fcffff7ffcfffcff7fffcffff7fffcffcffcfffcfcf7ffcf7fcffcff7fff7ffcf7fcfcf7ffcfffffcfff7fff7ff7ff7fcf7fffcf7ffffcffffff7ffcf7fff7ffcf7ffcfcfcfffcf7fcffffcf7fcf7f7ffcfffcf7f7f7ff7fcffcfcf7ffcf7fcf7ffcf7fcf7f7fcf7ffcffcfcfcf7f7fff7ffcf7ffffcfcf7fffff7f7ffcfffcfcffffcf7ffcfcf7ffcff7ffcffcf7ffcfcfffcfffffff
            fcfcf7fff7fcff7fcffff7fcfffcfcf7fcffcf7fcf7fffcff7ffcff7fcff7ffffcfff7f7fcffcfcffcffff7ffffcff7fccf7fcffcfcfcffcffcf7ffcfcffcf7ff7f7fcffcf7ffcfcfcf7ffcf7ff7f7f7fffcf7f7f7fff7ffcfcfcf7fcffffffcfffcf7ff7ffcf7fffcffcf7fffcfffff7ffcff7ff7fffcfffc7ffcf7ffcf7ff7fffcf7fcfffcff7fcff7f7fcfffcff7fffcff7fffcfcf7ffcffcf7fcf7fcf7fc
            ff7fffcfcfff7ffff7fcffff7fcff7ffff7ffffffcffcff7ffcff7ffff7fffcf7fcfcfffff7ff7fcff7f7ffcf7ff7ffcfffff7fcf7fff7ff7ff7ffcf7fcffcfcffffcf7ffffcfcf7ffcfcf7ff7ffffcfc7f7ffffcfcfcfcf7ff7fcfcf7fccf7fcf7fff7ffcf7ffcf7fcf7ffcf7fcf7fcfcff7ffcffcf7fcf7ffcf7ffcf7ffcffcf7fffff7fcf7ffff7fffff7f7ff7ffcf7fcffcfcf7fffcffcf7fffffff7fff7
            """))
        col = 16
        load_p = 100 / 8
        row = 112
        world_gen()
        makeplayer()
    elif selectedIndex == 1:
        myMenu2 = miniMenu.create_menu(miniMenu.create_menu_item("4 sections"),
            miniMenu.create_menu_item("6 sections"),
            miniMenu.create_menu_item("8 sections"),
            miniMenu.create_menu_item("custom size"))
        
        def on_button_pressed7(selection5, selectedIndex5):
            global statusbar, secworld, world, tilemaps, col, row, load_p, secnum
            statusbar = statusbars.create(120, 5, StatusBarKind.health)
            statusbar.value = 0
            secworld = 1
            world = 0
            pause(100)
            scene.set_background_image(img("""
                666a666666a66666a66666a66666a6666a66666a6666a6666a6666a6666a6666b666a666b6666a666b666b66966b669666b6696a6696a6966b66966b66966b6966b6966b6966b6966b6966b696b696b6966b6966b6966b696b6966b6966b6966b696b696b696b6966b6966b66966b66966b6696a6696a66966b666b666b666b666b6666a66666a66666a6666a6666666a66666a66666a6666666a66666a6666a
                6a666a6a6a66a6a666a6a666a6a696a6966a9a669a6966a9669a6966a9669a6a66a966b66a9a696a989a669a6a669a6a9a69a6696a6696a6a96a6a96a98a96a6a96a6a96a6a96a6a96a6a96a6a698b66a9a698b69a6a96a6a698b69a6a96a6a96a666a6a66a66a6a96a6a96a98a96a98a96a6a696a6696a6a66a9a66b66a966a98989a696a9a696a9a696a9669a6a9a669a6a666a6a666a6a6a666a6a666a666
                666a666666666698966696a966986a66a66666a666a6a66a6a66a6a96a6a66966966a66a96666a6666669a6669a66666666a66a696a98969666966a69696a696669696a696669696a9696a96969a69a96669a69a6696a69696a96a6696a9696a969a96969a969696a6966696a96696a966a9696a69a6a6969a96669a69a66a666a6a666a66666a66666a666a68966666a66696a96696a6966698966669a66a6a
                6a669a6a9a6a98a6a6a6a666a6a666666a6a6669a666696666696666666698a6a6a696966a6a969a9a9a666a6669a9d9a966969a66989a6a6a9a69698a6966a9a6a6a696a9a6a6a966a6966a6a6698989a669a669a696989a666969a6966a6966a666a6a666a6a696989a98966a6a666a9666a69666966a6666a6a666669669a69669a669a6a696a6a666a66986a6a6666a6a666a68666a6a6a6a6a6a6666669
                666a666666666666666666a66666a9a69669a6a666a98a6a9a6a6a6a6a98a9669666a6a669666a6666666a969a69d1dd19b6a666b6a989669666a6a696a6b966969696a966969666a966a969696a96a9669a669a696a6a98969a6a696a696a6a969a96969a96969a6a966a989a96969a669a966a69a6a969a696969a6b6a6a666a6a669866966a66969a696a6a96669a696666a6669a66666666666666a6a6a6
                a6666a6a66a6a6a9a6a9a666a69a666a6a666666a966696666669669666966a66a96666a6a69a696a9a6966a69d1d9111d696b9a6966a6b6a9a96969a96986a989a6a966a989a9a9669a96a6a9698966a9a69a696a696969a6a9696a969a69696a696a69a696a98966a9696a966a6a696a666a96989698989a6a6a6696a6966b696698a9a6a666986a666a669689a666a6a66966a666a9a6a69a6a6a98966666
                66a666666a669666666666a966a6666666a6a9a666a6a6a6a9a6a6a6a9a6a696a66a9a9696a666a66669a696b91d11d969a6b6669a6969a96666a9a666a9696a966966a9669a6696a966696966a9a69a9696696a969a6a669696a96989896a98969a696a966a96a9a966a696a699919a696b966a6b6a69a66696696a6696a696a6a6a9666966b6a966696698a66a66a66669a89896a6666698666696898a6a6a
                669a6a9a6698a6a6a6a6a966a666a9a6b6966669a669669666696696666696a69696666a66969696b9a66a66111191119a696a9a669a6666a9a96669a966a96989a6b9669a6969a696a9a6a9a9669a696a69a6966a96969a9a696a6a9a96969a9a696a9669a9696696a969a6119bdd919b66a9696969a669a6a96a696a6698a69696666a66a96666a9a6a6a966966966a98666a6a669a6a66a6a98a66a666966
                6a6666666a666669669666a669a666666a6a69a6698a6a66a986a66a96a98966a6a6a9696a6a6a6a666969a9d1911d1d191a96696a69a9a96696a9a696a96a9a969a669a696a9896a969696696b9696a969a96a9966a9a9669a6969696a9a6a9696a9669a696a69a999b6a999d11911d11996a6a6a6696a69698966a969a6966a66a9a969a66a9a666669666a6a6a6a966a9a69669866698966666698966a66a
                666a6a6a669a69a6a66a66698669a6b696698666a696969a669a9696a666a6a9696966a66969696969a6a661911d19119d999a9a969669669a6969698969a966a9696b69a969a96969a6b6b9a69a6a969a69696a6b96966a969a9a9a69669696a69669a969a999a6939d199dd9d1d91916bb9696969a6969a6a989a66a669a6969a6666a66966669a9a6a6a966966666a66666a6a6a9a66a6a6a9a6a66a666a6
                9a6966966a666a6666a69a6a69a6666a6a66b6a966a6a6669a666a6696b69666a66a696a9a6a6a6a6a9999d11d1111d119d9b9966b6a9a9a69a6a96a9a966696989a96b69a696a9a96969a969a69696a969a6a9969a6a996a9669669a9a9a9a969a9a96a9691d19911d191d11191d1d1d996a9a6a969a6a69669a696969a669a66969a696a6a9a69669669666a6a9a6966b6a96669666a69669686666a69a666
                666a66a66989a666a96666698666a969669a6966a96696a9896a969a6a96a9a969a96a9666969696966b19d191d91d191d99b9a969a9666969696a9696a9a9a9a966a96b69a69696a9a696a9696a9a969a69969a96996a969a9a69a966969669a9696a969a191d1d9d91d1919d191919d9d999699a989696a9a696a9a6696a669a6a696a6969696a9a69a66a966666a6a98966a6a66a6986a6a69a69a66666b6
                a666a669a66a669a66a9a6a69a696a6a6a666a6966a9896a66966a6696669896a666966a9a6a96a96a96d9d111111911d9b9a696a9669a9a6a9a969a696966966b9a969a969a9a69669a9696a969696b696a9a69a6a969a96969a969a9a9a9a966a9696b619d9b9b9d191d1d1d1d9dd9dd1dd9d9b969a9a96696a96669a6969a66966a696a66a69669a66a966a96a96666a6a696698966a9666666a6669a66a6
                69a696a666a698669666696a66a66966969a966a696a6a696a6a969a6a9a698969a98b966969896a966b6b91d91d11d1116a96a9669a966996966969a9a69a9a96696b696a96969a9a969a9a96b9a9a96b969696996b969a9a9696a969669696b969a9a999d6b696a96b99b99d9d9d919d99d9dd9b9b6666b6a966a9a69a6a696a6b9698969a96a6b669666a966a669a969696a6a698a966a69a6966a666a696
                a666a666a9666b6a6a9a6a696969a6a6a6666a96a696969896966a6969669a6a966696a9a69a9a9669b969d111d9191196969696b9a96b9a6b6b9a69669a96969a9a969a969a9a96969a96969a9696969a96b9a9a69a6b6969a9a969a9a9a9a96b9a9696a9b969a969a96a96a969a9b9a9b9dd99d999a9a96966b9696966969a999a69a989898969a69a9a966a969866a6a66a6966a966a666a66a669a669866
                66a9669a66a96a969666966a6a66696969a969896a6a6a69a6a9696a6a9a696989a9a69669a66669a99a9a11911111d91d9a9a69a969a96969a969a9a9696a9a96969a969a96969a9a969a9a969a9a9a969a96969a9969a9a96996b969696969a96969a9696a9a96b96a969a96a96966969a96d9d9b99969a9b96a989a9a6b666a696a66b6b69a669a96d989666a69a96696a966a966a6696966989a666a69a6
                a966a666966a666a66a6a96969a9a6a6a66a6a969696969a696a6a9696696a69a69669a69b969b9a9696911d1d191d11dd1199b969a9619a9696a96969a969696a9a969a969a9a96969a96969a9696969a996b6b969a969699ddd19a9a9a9a9696b6b969a9a96969a96969a96996b6b9a9696a9a9b9a6b9a969a9669a66969a9696a96969a6989a661919d9a9a9698989a66666966a6966a6a6a6a666a96a666
                98989a9a6a969a969a9666a6a66669696969698a6a69a6696a969699a116a96696a9a696d9a99a966ba9d1911911d1911191d119a969d911b6a996b6b96b9a9a99696b969a96969a9a969a9a969a9a9a969b99b9a969a9a9a19191d1996969a9a99a96a96969a9a969a9a969a9a99a969a9a969696a996a69a696a9a969a966b9a996a9a696a9669d9ddd196666a69a669a9a9a6a696a6966969696a966666a6
                a6a96666966a666a6669a96969a9a6a6a6a9a69969a69a9a696a96a9111119a9a96969a99b9d9699a96d111d111d111d91d9d9d9d99d9dd9119b69a96b96b9696a9a96b9a969a9696969b96969a9696969d939199a969696191d1d91d19b9b9696969b9b9a996969a96969a9696a969a96969a9a9696a996969a96966b6989a99d6d96696a966a99dd19d9b9a9696a69a666666966a698a9a6a6a6666a6a9696
                9666a69a6a69696969a666a6a66696969696698a969669896a96696a919191199939d119b969b939999d191191d19191191d19d19dd9d91111119b99a969a96b9969b9a969a99b9a9b9a969a9b969a9b9bdd1dd9d9b9a9b99d191d191dd999a9b9a9a96969a9a9b9969a9b969a9969a969a96969a9a969a9a9696a9a969a9696d9a96b9a9669a9b9d9d19166989a6966969a9a6a9696a966669669a96696a6a6
                a69a96a6966a6a6a6a69a96969a96a69a6a9a696a989a96a969a9a9696d1d1d11d1d191d11dd9d9b9b11d1d9d1911111dd9919d119d9d9dd19d1119b96b969a96a9696969b969a9969a969a9969a9969a919d9d9d969b96bd1d191d1919d9a969a9969a9a969969a9a9969a9b969a969a969a9a96969a9669a9a96969a96b9b9d99b966669a96919d19dd9a9a9896a9a6a6669666a66989a9a6a666a6a669666
                96a66696a6969696969669a6966a969a69669a9696a96a969a69666a9a96d19d11911d11911dd16d9b91191d9d91d1d191d1d9d919d9b9a9699b9d969a9a969b99a9a9b9a969a969a9969b9b9a99b9a999d9d9dd9a9a9699a9191d91dd9d99b9696b9b999b9a9a9699a9a9969a969b969b9a96969a96969a96696a9a9669a9d9a9b6a9a99d69dd91d9d919966d9b96696969a69a969a698989696a96969a6a98
                a969a6a696a989a6a989a696a9696a6969a9669a696a969a9696a996969a99d91d11911d1d19119d911d1d9119d9199119d91d9dd9d99a969a969a9a9969b9a9699b969a99a9969b969b9a9699a9699b9b99b199b9699a9b99d1d1d1919d9b99a99a99a69a99699a969969a969b9a9a9a96969a9a96b9a969a9a96969a96969a9696969a99a191d9dd1d9361d91d919a6a9896a69a696a966a66a96a6a666669
                66a69696a966a96966b696a96a9a969a696a9a69a96969a969a969a9a6966a91d1911d1911911d1dd1d1911d919d9d9a99d19d91d99a969b969a9969b9a9969b9a969a99699b9b99a9b9b99a9b969a9dd91d9d9a99a999b961919191d9d9d9d99b99a999b969b9a99b9a9b99a969969969a9b969969a969a96969a9a969a9a969a96a969a99d9d919d9d91d9dd9ddd9d969a6969896a6989a9696669669a9a6a
                9696a6a966a966a69a96a96696669a69a696969699b9a969a696a9669a9a9969911d191119d191d1191119111d9d9d9d9b9b19d9b9b969a96b99a9b96996b9a969b9b9b9b9a969a99b969a9969b9b911d1d1dd99b99dd9ddd1d1d1d1d9dd19dd99a996b969b9a9969a99b9699b9a9b9a99969a9a9a996b969a9b96969a96969a69699b996d9d1dddd91dd9dd91d919d99a696a96a9696a9666a6a9a66a666966
                a6a969669a969a96a9696a9a9a9a696969a9a6a9d1d99b9696a969a969696a9a69d1111d19d9d9911d99d1d9119dd99b9999a969a969a99699b96969a9a99a99b969a969a99b9b969a9b9969b9a99dd919191d119dd91d9191919d1919d9d19dd99b99a9b9a9969b99b969a9a9969a996a9a9969b96b99a9b969a96b969a9a969a9a9da99dd9d9191d919191d9d19ddd996a96a966a6966a96969669a969a6a9
                6966a9a9669a696969a6969669696b6a96969999d1ddd9da999a969a9a9a9699a99d91d19d9d9dd999dd91d1d1d99b99a9a969a996b99b9bdd91ddd9969b99699a9999a99699a99a9999a9b9b999b11d1d1d919dd91d1d1d1d1d191d9d91d19d9d9b9b99b9969b9a9a96b99b96b9b96999b96b9b969a96969a96969a9a96969a9696999dd91d919d9dd9ddd9d9d9d99d9d969696a969a696a9a6a9a666a69666
                a9a966989a696a9a989a9a69a9a9a9969a9a6a9d1d191119d169a969696969a969a9d1919d9d9a99ba99b999d9d9d9a969b9b996b99a969d911d191dd9b969a9b9b6b99b9b9a9699b9a99b999a9d1919191d1dd91d19191919d191d19d1d9d9d9d9999a99a9b9b9999b99a99a99a99bbb969b9a969d9b9a9b969a9b96969a9696b6ba9a91d9d1ddd191d9191d9dd9dd9d9db6a9696a969a966969669a96989a9
                66969a69a96a9696a96969a9696966a9a9696961d9111d1119d969a9a9a9a969a96969b9d9d999b96969a9b999b9a969b96969a99a969a111d191d1919b9a99b9699b9a99a999b9b9b9699a99d91d1d1d191919d9d91dd1d1d191d9d9d911d9d9dd9399b999b99a9b99a99b99d99b9996b9a999b9391999b96b99a969a9a96b9a99969619d19d99d9d91d9d9dd919d9d9d99a96a6966a6669a6a69a6696a9666
                9a6a69a966969a6969a9a969a9a69b9696a9a9a9111d191919da9696969696b969a9a99a9b9a9a969a9b969a9a969b9a99a9b99a99b999d91d11d91dd99b9b99a9b9a99699b9b9b9969b9b9d9d1d91919d1d19d9d9d91919d91d1d19d9dd91d9d9d9d9d9b9a9b99b9a99b99a99d99b9a99b9b969b91ddd99b99a969a969969a969a69a9d9d9dd1d91d9d9d1d919dd9d9d9b96699a9a9969a969698969a6989a9
                a96969669a9a969a969696a96969a96b6996969d11911111dd999a9a9b9a99a9a9969a96996969b9a9969a9699b9b969b999a99d996b9d1119191119d9b999a999b99b9b9b99699a9b9b99d9d1911d1d1919dd9d9d9d1dd11d19191d19d91d9d9d9d9d9d99999a9999b99b99b9a9d9b9b99b9a9b19d9193d1d99b9969b9a9b969a99b9191dd9199d9d9dd9d9d9d9d9d9d9a69a696696a9a96a9a96a9669a6966
                69a9a69a96969a96a9a9a969a9a969a99a9a9a99d11d19d191d9b99696969a96969a9969a9a9b969969a999b9a969a996b699b9ddd19b19d11d1d1d19d9b9a99b99a999a99a9b9b999b9b9d1d1d19191d1d191d1d19d9191919d1dd91d1d9119d9d9d9d9b9a9b9b9a99a99d9a999a9999b1999b91d1dd9d9d91d9b9a969969a9696a99dd9d91ddd9d9d9dd9d9dd9d9d9d999a96a9a9696669669896a9a696a6b
                966969a96a9a96969696969a9696b969a96996d99d191111d1119d9d9a9a9699b9b969b99b969a9b9a99b9a9699a99b99b9a9911911d1d11d191191d99b9b969b9a99a99b999b99b9a999d1d9191d1d919ddd19191d1d1dd1d1d911d919d19dd9dd9dd9d999b999b9b99b9a999b99b9a99b1dd919d919d191d9d99b99a9bd969a999d9d91d9d99dd9b99d9d9d9d9d9d9d93999d9696a9a9a9a96b969696a969a
                6b9a9a969696a9a9a9a9a9a969a969a969a9b9dd1d111d911919d9d9d999b9a969a9b9a969a99969b9b9699b9b99b96b99b99d1d11d19119111d119d199a999b999b99b99b9b9b9b99b9a91d1d19191d1d9b91dd1919d919191d19d1d1d9dd91d9d9d9d9db99a9b999a9999b19b9d99b9b999d1dd19dd9d19d9d9b9699b99d9d9b9d9d1d9d9ddd91d9a969b99d9dd9d9d9d9dd9d9a969699999a96a9a6966a96
                9a69696a9a99696969696969a969a969a9699d91191d911d1d19d9d9d9b9699a9b96969b9b96b9a9969a9b969a969b9939dd1d1191911d1d919191d9d9b99b9b9a99b99b99a999a99b999d19191dd1d91d9bd9d91dd11d1dd191d1919d119d919d9d919d9d9b999b9b99b9b9b99b9dd999b9b19d9d19d19dd9d9d9a9a969a9d9d99b9d9d9d9999d99b96b9a9a969a9b9d9b9d9d9d99d9d9b9b96a9669a69a96a
                969a9a9696a9a9a9a9a9a9b969a9969a99a9a91d1111111911d9dd9d9d9b9a99699a99a99699b99b9a9996b9b99b99a911191d91111d19191dd119d9d99b9b99b99b9b99a999a999b9db9d1d1d191911d9bdbd91d19d919191d91d19d99d9d9dd9d9d9d9d9d9b9b999b9d9999a99dd1dd9d9d91d19d19d9d9d9d99969b9a99d9d9b9d9d99b9b9a9a969b969696a9696b9a9d9b9d9d9d9d9dd9a969a969a96696
                9a96969a996969696996969a9696b9a969999111d91d1911d1919d9dd9d99b969a99b996b9a99a9699b9a99b9b99a99d9d911911d91191d19d99dd9d9d99b9a99b999a999b9b99b9999b91919191d1d9ddb9dbb91911d1d1d91d19d1d19d9dd9d919d9dd9d9d999b9a99b1ddd9b999d91dd9dd91919d91d9d9d9db9b99a999d99b999b9a99a9b9699a96b9a9a9969a96969a969a9b9b9d9b9696b696a969a9a6
                969a9a969a9a9a9b9a9a9b969b9b9699b9a1d1d9111911d1911d9d9d9d9d99b9b9b96b99b99a99b9a9999b9969a99b9d9d91dd9d11d1191d191d9d91d939999b99a999b9b999b99bdb9d1d1d1d1d91d19b9b9b9bb1d919191d191d1919d9d9d9d9d9dd9d9d9ddd9b99b99b919d9ddd91d9d191dddd1dd91d9d9d999a9699b9a9a9b9a969b96969a969a9696996b9a99a9a996b9696a96a96a9a969a969a69696
                b9696969a9699696969969a9b9a969a9696919111d11d1111191d919d9d9399b9969b9a99a99699b9b9a99a9b99b999d9d9d9d9d9119119d19d9d9d9d99b9a99b99b9b999b9d1dd999b191919191d19dbddb9db9c6d1d1dd191d9d91dd9d9d919d9d9d9d9d9d99d9b99b99ddd9d9d1d91d9d191919d91d9d9d9ddd999b9a9699969a99b969a9a996b9969a9a9a969696996a99a9a996969a9696b969a9696a9a
                9a9a9a9b969a9b9a9b9a9b969699a999a9b9d1d191191191d1d9d9dd9d9d9d99a9b9b99b9969b9a99969b9999b99a9d9d9dd9d911d11d1d1919d19d9ddd999b99b99b9b9b9dd919d9391d1d1dd1d911d9b9db9db8c89d9191dd19dd9d9d9d9d9d9dd9d919d9d9d9d9d9d9b9911d19d91d91ddd9dd91d91d19dd99ddd9b9969b9a99969a9a996969b96b9a9969969a9a9a9969a9696b9a9a969a96a9696b69696
                969696969a9969a99a96969a9b9a9b99999b19111d11d1d1919d911d9d9d9d9d99a99a969a99b99b9a999a9a99dd99d9dd919d9d19191d11d11d91d9d99db99b99a999b99dd11d1d1d11919d9191dd9bdb9bdb9d66c6b9d1d9191d9d9d9dd9dd9d9d919d9dd9dd9d9dd9d1ddd91d191dd19191d1919d19d9d9d9d999b9b9b9a99a9a996996b9b9a9b9a9969a9a9b996969a96969a9696969b96999a9a969a9a9
                a9a9b9a9b96b9a969969b9b99a9969a9393919d191d19119119dd19191d99d9b9b96999b99b99a9999b9b999b111d9d9d9d91d19111d19191d11d919d19d9b9d9b9db99bdd9191919191dd11d1d191b9b9db9db9bbd6cb6d1d1d19d9d9d9d9d9d9d9d9d9d9d919d9d9d9dd9119d91dd919ddd919dd19dd91d9d9d9399b969b969969b9a9b99a996969969a9969969a9b9a99a9b969a9a9b969a9a6969a9a9696
                9696969b69b9699b9a9b9a969969b99b99dd19d111911d19dd9d91d9d9d9319a999b9a99a99a99b9a99a99b99d191dd19d9d91d11d9111d119191d9d9d1d99d9d9d99b99d11d1d1d1d19d99d9d9d19dbdb9db9bdb9b6b6b689d911d9d19d919d9d9d9d9d9d9d9d9dd9d9191d91d19d19d1d91d91d9dd91d9d9d9d9d9b9b9a99b9a99a9969a9969a9b9a9b969b9a969969969969a99b9969a9a9699a969696b6b
                9a9b9a99a99a9b9699b9699b9a9b9a99a999dd9d1d11919d9d919d919d9d99b9b9a999b99b99b99b9b99b9b91d1d19111d919d19111d91191d1d91d9d919d9b9d9d9d939d9191919191d9dd9d919dd9b9db9bd9b9bb6b6b6cb119d19d9d9d9d9dd19d9dd9d9d9dd919ddd191dd91d91d191d91d91d91d9d19d9d9d99b9999b9699b9969b9969a999a9969b9a969b9a9a9a9a9a99696b9a96969a969a9a9a99a9
                699a99a99699b9a9a969b9a999b969b969a961d91191d9d919dd19ddd9d9d999699b9a9b99b99a9999b999b1d19111d911d9d11d19111d1d1919d9d9dd9dd99d9d9b199d11d1d1d1d1d91d911d19db9db9db9bdbd9b6b6b6b69d191d9d9d9d9d99d9dd9d9dd9d9d1d9d91dd911d91d919d91d91d91d91d9dddd9d9b99a9a99a9b969a9b9a9b99b69969a99699a9969969969996b9a96969b9a996b9696969696
                9a9696969a9a96999b9a9996a99a999a99b9d9d1d1d19d9d9d919d9919d99a9b9b99b999a99a99b9a99a9b99d11d9111d911191911d91919119d1d9d9d9d9d9d9b99b1dd1919191919d1911d91919bdb9bd9bd9b9b6b6b6b6c9d1d191dd9dd9dd9dd9d9d9d9d9d9d91d9191d9d91d1ddd1d91d9dd91d9d19191ddd9b99b96999a9b999a9969a99a9a999a9b9a969a9a9b9b9a99a99b9a9b96969a969a9b9a9a9
                b99a9b9a99b999a969b96b999b99b969b999dd1911919dd9d9d1d9ddd99399b9b9a99b9b99b99b999b9999a99d911d9111d1d11d1d11119dd19d9d919d9d9dd9d9dd9d91d1d1d1d1d19d1d911dd1b9b9db9bd9bd7d6b6b6b8c9d9191d19119d9d9d919d9d9d9d9d91d1d91d191d19d919d9d9d191d9d19dd9d9d999b9b99b9a9999a96969b9969999a96996999b99b9969a969a969699969a9b99b9a99696969
                6b9969b9b996a99b9a999b9a99a99a999b939111d11d19d91d9d91991d99b99b999b99a99b9b99b9b9b9a99b9911d111919191d19191d9d9d9d9d9d9d9d9d9d9dd191d1919191919191d91d91919bddb9dbd9bd9bd6c6b6b6c9d1d1d91d191d91d9d9d9d9d919d9d19d91d9d19d91d9d191dd9dd9d19dd919d9d9d9a99a99b9b9a99b9b9b9b9a9a969b9a9b9a99a996b9b99b9969a9b939a996b69696b9a9a9a
                99a9b9969a999b9699b9a999a99699b9a999d1919191191d9d9d9ddd9dd9b9a9b9b9b999b999b99b999b99b99d9d91911d111d91111d19d9d9dd919dd9dd9d19d9d1d191d1d1d1d1dd91d1d1d1db9b9db9b9bdb9b9c6c6cb6bb919d1d91dd91d191d9dd9d9d9d9d9d191d191d1d191d91d919191d9dd91d9dd9d9d9d999b999999b9699a99699969b99b99699a996b99a969a9b9b9d9d9996b99a9b99a969969
                b9699a9b99a9b9a9b99b9b9b99b9b99b99b9d1d11d1d1d19d9d9191919d99b999b999a9b9b9b9b99b9b99d9b9d99d11d191d11119d1919dd9d9d9dd9d9d9d9d19d9191d191919d19d91d191919d9dbd9bddb9d9bdb6b6b6c6b6dd19191d911d91dd1d19d919dd9d19d1d9d19d9d9dd91d9dddd19d191d9d19d19dd9dd9b9dd939b9939b969b9a9b99a996b9a9969b9a999a9969b9d9d9d9a99a999a9699a9a96
                9b9a999a99969999b9a999a969b99a99b99dd19111911919d9d9d9d9d9d9b9b9b9b9b99999b9993d999399b99b9391d19119191d1191d191d9d19d9d9d9d9d9dd91d1d191d1d191d11d91d91d1bdb9bd9b9dbbd79bb6b6b6c6c9191d191d9d1d91919d119dd9d9d9d191d91d191d191d919d919d9dd9d19dd9dd9dd9dd9d9d9d9d9d9999b9b99b9a996b99b9b9b99b969b99b9b99dd9d9d9b996b969a9b9699a
                99b96b99b69b9a9b999d9999b99a99b99a999d1d911d11d9d91d9d9d9d9d999999b99b9b9d9b9d91db99d9939d99d1911d1d119191d11d1d9191d9d9d9d919d19d91d91d19191d19d91d911d9d9b9db9bdb9d9b9d6b6b6c6b6bb9d19dd191d91d9d1d9d9d9d9d9d9ddd91d9d91d9d19d1d9d9dd1d91d9d9d919dd919191d9dd9d9d9bd9399a96999b999a99969b9a99b99a9969d9d9d9b969a99a99b9969b9a9
                699a99a999b9b9969b11ddd99a99b99a99ddd9111d191d1d1d9d9dd9dd9ddddd939b99b99399dd19d9d9dd99d9d9d11d191191d1d11919111d19d9d9d919dd99dd1911d91d1dd91d1d911d911b9db9bd9b9bb9dbb6b6b6b6cb66d91d191d191d91d911d1d19d9d9d191d91d1d91d9d19d9d919d91d91d9d9d9d9d19ddd9dd9d9dd9d9d99d999b9a99b9a99a9b9969b99a9969bd9d9d9d99b99a996d9a9a9699b
                9a99b99b9d9a9b9b91d111dd99b99b99b999d1d91911191919d9d919d919d99d99d9b911d9bd911d9d9d9dd9d9d9d99d11d1d1d191d1d1d9191d9d1919d9d9d9d91dd911d91911d911d9191d9db9bd9bdb7d9bd9c6b6b6cb66b6dd919d19d191d919d9d99d9d9dd91d91d9191d91d9dd9dd9d19d9dd9d9d9d9d9d9d9d9d919d9d9d9d9dd939b9b99b999b99b9a9b99a9969b99d9d9d9939b9b99b99b999b9a96
                99b99a99b99999b9d1919119d99b99a99b93191d9d9d911d1d19d9d9d9d9dd9ddd9111d1d9911d19d9d9d9d9d9d9d9d99d919191d9d91d11d1d91d1dd9d9d9d9d919d9d91d1d191d9191d19db9bd9bdb9d9bdb9c6b6c6b66bcb6b91d19d19d19d9dd919dd9d9d91d91d91d9d91d91d91d91d9ddd91919d9d9d9d9d9dd9dd9dd9d9d9d9d99d99b9b99b9a9b99999b969b9b9b939d9d9399d999a99a999b99b99a
                9b9a99b99b9b9a999d11d1d19d9b9b99b9d1d19d9dd91d19199d9dd9dd9119199d19d191d1d1d911d19d9d9d9dd9d9dd91d11d1911119191d911d919d9d9d9d91d9d9d9d91919d1d19d9dd9d9bdbd9b9bbdb96b6b6c6b6cb66b6bd91d191d19d9d9d19d919d9d191d91d91d1d91d91d91d91d919dd9ddd9dd9d9d9d9d9d9d9d9d9d9d9d939d99b9b9a9999a9b9b9b999d9d99d9dd9d9dd939b9699b69d9d69a9
                9999b99a99b199b9b1d19191dd99b9b99b991d9d919d9d111dd919d9d91d1d9dd9d91d1191d111d19d9d9d9d9d9d9d9d91191911d9d1d1d111d911d191d919d19d9d919d9dd9d919d9dd91d9bd9db9db9b9d6cb6c6c6cb66bc6b6dd919d19d1d19d9d91d9d9d1dd91d91d919d19dd91d91d9dd9d91d9d919dddd9d9d9d919d9d9d9d9d9d99b9b99999b9a9999b999a9b9d9a9dd9d9d9d9d999d9b99b9a9d999b
                9a9b9b99b99b9b99991d111111d9999b99b911d9d9d9d19d19d9d9d9191d9d9d9d1d99d1d191919d19d9d9d9d9dd19dd1d1dd1d91d9191919111d9191d1dd9dd19d91d9dd91d19d19d9d19dd9bd9bdb9b6bbb6b6b6c66c6c6b6a6b91d1d91d919d9d9d9dd9d19d91d91d91dd9dd91d9dd9d191d9d9dd9ddd919dd9d9d9d9d9d9d9d9d9d9d9b9d9a9a9999b9a99dd9d99d9d919d9dd9d9ddd9399b9a9999d9b99
                b999969b9a99d9b9b9d191d919d9bb99b99b9d111d9d19d9119d91d9d1d9d9d9d919dd99d111d119d9d9d9d9d9d9d1191919191d9d91d11d19d911d119191d9d19ddd9d9d191dd91d9d9d1b9bdb9b9db6c66b66b6c6cb8b6b8b6b819d91d91dd19d9d9d9b19d191d91d91d91d91d91d91d9d9d91dd919d919d9d91dd9d9d9d9d9d9d9b9d9b9d9d999b9b99b9b96d9d9b9dd9dd919dd9d9d9d9b9d99d9b99b9d9
                9a9a9b9999b9a9dddd11d111dd9d99b9b9b9999d9119d9d19d9dd9d91d11919d9d9d9d9d99d919119d9d9d9d9d9d99d11d191d99d9d919d19111d919d1d1d9d99d919d919d191d1919d9d9db9b9bdb9c6f8c6c6cb6b66c6b6c6c6c61d191d919d9d9d9db9b19dd91d91d9dd91d91d91d9d191dd9d9d91d9dd919d9d91d9d9d9d99399d9d99d9d99b999d9d999b99d9dd9d9d9dd9d9d9dd9d9d9d9b9939a99b9b
                9999b9b9a99911191191191919d9b99b99b9b939d91d9d9d91d9d9d911911d1d919d9191dd91d19d9d9dd9d9d9d9d9d99d9dd19d9d9d91d1d19d11d1d919119dd1d91dd1d19d191d9d9d9db9dbd9b9b6c6c6c6c66b6cc6c6c6c6b8c99dd91dd9d9d9d9b9dbd191d91d9dd91d91d9dd919d9d9d9191dd9dd91d9ddd9d9d9d9d9d939d9d9dd9a99399b9a9d99b9d9b9d9d9dd9d9dd9d9d99d9b9d9d9b9999b99d9
                b9b99b9b9b931911d1d191d1d9d9d9b9b9d9d99d9d9d9d9dd9d9d9dd1d1d1911d1d19d9d91d91d1d9d9d9d919d9d9d9d9d9d9d9d9dd9dd9191d19199d9d1d91991d1d919191dd1919d9d9b9bd9bddb78c8c66b8bc6c6c6c6c6c6c6c6d91d919d9d9d939bd9b9d91d9d19d9d919dd919dd91dd9ddd99dd919d9d9191d9dd9d9d9d99d9d9d9b9d99b9b9999bd99d9d9bd9d9dd9d919d9dd9d9d99b9d9b9b9b9a99
                9b9b99b999d11d191911d119d9d99b9d99b9939d9d9d9d9d9d91d9d9191911d91d91d91d9d9d9d91d9d919d9dd919d9d9d9d9d91d919d91d1919d1d1919d1ddd191911d91dd919dd9d9db9db9b9b9d6c8ccc6c66b6b68c8c6c6b8c8c9d9d9d19d9d9dbd9bdb9dd91d9d9d91dd9191d9d19d91d919dd919dd9dd9dd9d9d9dd9d9d939939d9d99399b9bd9399b939d9d9dd9d9d9d9d9d9dd9d9dd9d9d9d9b999d9
                bd99a99b9b19191111d9119d9d9d9d9939d9d99b9dd9dd919d9d1111d111d111911d9d9d9d919d1911d9d9dd919dd9d9d9d919d1d9d19d9d9d9d9d9dd1d9d9191dd19d1d911d91d19d9d8c6bdbd9bd6c6f6c6c6c6c6cc6c8c8c6c6f66d91d9dd9d9b9b9b9b9bd9d91d9d9d9d9ddd9d19dd9d9d9dd919dd9d9d919d9d9d9d9d939d9d9d9d9d999b99b99b9d99d9d9d9d9d919dd9d9dd9d9dd9d9d9d99b99b9a99
                d9dd9b99b111d11d9111d19dd91d9b9d99d9dd9dd9d9d9d9d9d9d9191d919191dd919d9dd9ddd9d1d919d9d9d9d191d9d9d9d9d91d9d9d1d19d9d9d99d1911d1919d19d1d9d1d919dd9b8c66b6db9bb6c6c8c6cc6c6c6f6c6c8cc68c6b9d9d9d9ddbd9bdbdd9bdb199d9dd19191919d9d91d91d9d9d9d9d91d9dd9d9d9d9dd9d9d9dd9d9dddd9d9b9b9999399d9dd9dd9dd9d9d9d9d9dd9d9d9d9939d9d9b9b9
                9d9999b99d9119111d9191d9d9d9d9b9d9d9ddd9119d919d9d91d91d11d1d1d1911dd1919d99d99d11d9d9d9d9d91d9d9d9dd9d919d9d991d9d9d9d9d191d919d1d91d91919191dd9b18c8c6b9b6db6c8cc6f6c8c6c6c8c8f6f6cc6c6c8c99d9d9b9bd9b9b9b9b6b9d9d9d9ddd9dd9d19d9dd9d91d9d9d9d9dd9d9d9ddd9d9d9dd9d9d9d999d939d99b9b9d939d9d9d919dd9d9bd9dd9d9dd9d9399d9d9d999b
                9dd9b9b9b11d1d191d1d19d9d9d9d99d9d9dd91191d9d9d9d1d91d919919191d19d919d1d9d19dd9d91d91d91d91d9d9d9d91d9d9d9d9d9d9191d9d9d9d191d1d91d91d1d1d91d9bd88c6f6bbb9bd9b6c6f6c8c6f6c666c6c68c6f8c6c6c8cb99c9b9bdb9dbdb9b6b9d9d91919dd919ddd19d9dd9dd9d9d9d9d9d9dd99dd9dd9d9d9d9dddd9d99d9d9b9b9d99d9d9d9dd9d9d9b9bd9d9dd9d9d9939d9d99b9a9
                999dd99b9191911d1919d9d9d9d9d939d9d9111d1d11d9d9d91d11d1d1d1d9d9d911d9d919d1d9d991d11d191d19dd9d9d9d919d9d9d9d9d9d9d19d9dd191d9d1d91d19d9d91d1b9db6f68c66db9bdb6f68c6f6c6c6cc6c8cc6f6c6c86b8c88d6cc9bd9bd9b9d6b6b6d9dd9d9d91d9d9d9d9d9d9d9d91d9d9d9d9d9ddd9d9d9d9d9d9d9d9939b9d9d9d9d9dd9d9dd9d9d9d9d9bd9b9d99d91d9dd99d9bd9b99b
                9a99dd99d1111d919d9d19d91119d99d9dd1d191919119d911d191919199d9d9d9d9d9d9d919119dd19191d191d191119d9d9d19d919d9b9d9d9d9d99d91dd19191d9191d1d91b9bb8c6c8cc8d9bd9b6c8cc6c8f68c66c6c6c6c8cc6c6c6c6c6c86c6bd9bdb9b6b8c8c99d9d9dd9d9dd919d9d9d919d9d9dd9d9d9d99d9d9d919d9d9d9d9d99d9d9b9d9d9d9d9399d9d9d9d9b9bb9b939dd9d9d9dd9d99b9b99
                b9b9d9d9dd91d11d19d9d9dd9d1d1dd9d9d191d111d19dd1d191d1dd1d9d9d919d9d919dddd1d1d191d1d91d191d19d1d9d9d9dd9ddd6b8d9d9d9d9dd91d9191dd91d91d91919db9b6c8c6f6f9bd9b9b6c6f6c6c6c6cc6c8ccc6f6ccc6c66cc86c8c6bb9b9dbd8c6c68cc9d9d9d9d9d9d9dd9d9dd9d9d9d9d9d9d9dd9d9d9d9d9d9d9dd9d939d9d9d9d9d9d9d9d9d9d9d9d9bdb9db9bd9d9d9d9d9d9d9b9a69b
                999b9d9d911d1919d9d9d9d9d9d9191d9d191d191d91199191d191999d9d9d1d9d9dd9d19999191d19191d191d91d1919d9d9d9d1968bb6b9d9d9d9d919d19dd91d91d919d1db9bb8cc6f66c9bd9bdbd8c6c8f68f6c66c6f66f68c6cc6c6c66f6f6c66dbdb9b6c6c8c8c6c9d9d9d9d9d9d9d9dd9d9dd9dd9d9dd9d99d9d9d9d9d9b9d9d9d9d9d9b9d99b9d9dd9d9d939d9db9b9b9bd9bb9b9d9dd9dd9b966b69
                b9b99bd1d1d911d9d9dd9d9d9d91d1919d9d191d1119d9d1d191d9dd9dd9d9d1d119d9d9d9dd9d191d1d191d91191d1d9d9d9d99b8cc8b6c99d9d9d9ddd91d19191d91dd19d9bd66c6f6c8f6bd9bd979c6f6c6c6c6c6c66c6c8c6f66cc876c6c86c8cb9b9db6c8c6c6f68c88b99d9d9dd919d9d9d9d9d9d99d99d9d9d9d9d9d9d9d9d9d9d9d9d9d9d939dd9d9d9d9d99a69b9bdb9b9b9c6c6d9d9d99b9ba66a6
                9b9b999d1911191d9d9d19d9d9d99dd9d91d9d919d19dd1d191d19d9d9d9d9d919dd1d9d9d9d9d1919191d911dd1919d9d9d99dd8c6866b6b9d9d9d9d91d9191dd91d9d9dd9d9b6c8c68c6c6b9bd7bdb66c6c8f6c6c6c8c6f6c6f66c6cc8c6c6cc8c66db9b6b8c6f686c86cc6c6d9d9d9dd9d9d9dd9d9d9d9d939d9d9d9d9d9d99d9d9dd9d9d9d9d9d6d9d9d9d9d9b9b9bb9b9b9bdb9c6c6a6b9d9399d96b96a
                999d9b99d1191d111d9d9119d9d9d9d9dd91d1d1191d9191d1191d19d9d9d9d191d91919d19d91d1d1d191d19191d9d9d99dd9bb68ccc6bbb9d9d9d9d191b6b9d919d9d999bdbd8cc6f6f687bd9b9d9ddd8cc6c6c686c6c6c8c86c6c6686c6c68f6cc6bdb9bd6c66cc6ccc6c8c88b9d9d9dd9dd9d9d99d9d9b999d9b9d9d9d9b939d9d9d9dd9d9d9b9a6d9d9d9d9d9d9b9db9b9b9b9c8c866b6a6d9b9b9b6a69
                b9b9b9b9dd1d119191191d19d9d9d9d9d9d99199d1d1d1d191d1d911d9d9d99dd91d91d9d91d191919d91d91dd191d9d9d9d939b8c6f6b6b6b9d9d9d91d99b6a91d9d99ddd9b9c86f68c6cc6b9bdb9b9bb6c6f6c6cc6c6c66c6f6c66cc6c6c6c6c6c6c6d9d9b66cc6c6c66c6c6c8c6b9d9d9d9d99d9d9d9d9d939d9d99399b9d999d9b9d99d9dd9d99b69d9d9d9b9b9b9b9bdb9bd9b86c8c8c6b6a99b99996b6
                9b99b99d9191d1d11d11d9d19d19dd19d9dd91dd91919191d91911d919d19dd9191d19191d191d1dd11d191d919dd99d9d9bdb9b6c866bb6b69d9d1d19d9d999d99d9d9d9bb9b6c8c6c8c8c6cb9b9bdb96cc86f8c686c86c6f6c6c6c66cc66c6c6f6f6b9bbd9bb78c8c6c6c6f6c6c6bb6b9d9d9d9d9939d9d99d9b9d9399399d939b9d9d939d9d9b9b9b9d9d9d9d9d9b9bd9b9b9bb8c86c6c6c6b6b99bdba69a
                99b9939d9d11919191919d91d919d91d9d9d919d9d1d1d19d9d1d911d99d99d19dd91d9d9dd1919d99d91d191d1919d9bdb9b9bb8c6fc666bb69dd919d9b9bb69d9d9d99b9db6c8c6f6f6c6f6db9db9bd8c6f66c6c6c6c6c68c8c6c6c6c6cc66c68c68bb9d7b9bb68c6f6c86c6c8c6b6bbb9d9dd993999d9b9399d99b99d9d9d99d9d99d99d9d9d9b99a69d9d939b9b9b9b9b9bd96c6c6c8666c66bb99969a66
                9b93999d9d91d11d1d1d19d91dd1919119d9dd9dd9d9191d19d9d1d91d9dd9d9d91d9d9dd9191d19d91d9191d91d9d9b9b9bdb96c6f66cbb86bb919db6b9d9a6b9d99dbdbd9b6c6f6c68c6f66b9bd9b9b6f6c8c6c6c6c6c6f6c6c6c86c68c6c6c6c6c6b9b9b9d96c6c6c86c6c6c6c6b6b6b9d9d9d99d9399d99b9d939d99b9d9b9d9939939d9d9b9db69a9d9d99b9b9bdb9b9b9bb66c8c6c6cb6b66cb9ba669a
                9999bd9dd9d191d91191d1dd9191dd1dd1119d919d919d191d919191d9d9d9d1dd9d19d91d1dd9d9d9d91ddd91d9d9bdd9bd9bb6c86c86b6bb6b61d9b69b9b696d9399b9db9db8c68cc6f68cb9bdb9bd6c8c6c66c66c6cc6c86c68c6c6cc8c6c6c68c87bbd9bbb6c66c6cc6c6c6f6c6b9b6b9d9d9dd9d9b9d9b9b9999d9399b9d99399399d9d9d9b99b66b9b939b9bd9b9bb9bd9bb86c6c6b66b6a6b6b99b6b6
                9bd99dd9d1d1d11191d19191d91d1991919d1d9d9d9dd191d1d1dd1d19d91d9191191d1d9191919d9d9dd9191d91939b9bd9b68c8cc8c6b6b6b6cb999a6a996a699939db9bb9c68cc6f68c6c9bd9bd9bc6c6f6c66c6c66c68cc678cc6c86f6c66c6c6f66db9d9bd8c6c6666c6c66c6b6b6b6b9b9d9d99d9d9b9b9bd93999d9d99399399b9d939b99bb9b96a696b9b9bb9b9bd9bb96c68c6c6b6b6b66a6b99a96
                d9b9b9d191919191d191d1d111d9d9d91d191d191d9d91dd919191919d9199d1d91d9191d19dd9d9d9d91d1d919d9bdbd9bb6c8c6c6f6c6b6b6b6b9b96966a96ba9d9b9b9d9b8c6f6c6cc6f87d9b9bd6ccc6c66bc6b6c6c6b76b6c6c66c86c6c6c6c86c6d9bbd9b7b6b6bcb66c6c66b66b6a69b6b9d9399b99b99a699bd9b9d939b99b9b9d9b99bb996a6969a9b9b9b9b9b9bb9b6bb86f68c66c66b66b6b966a
                999b99d1d11d1d1d1d1d1919d91919d9d91d191d191d1911d1dd191d19d9319d19d1d91d9d9d91d99d99d99d19d9d9b9bb9c8c6cc6f6c6b6b6bb6b99bd9396b696d9db9bdb9b6c86f68cc86c9bbdb9b666c8c6c6b6c6b6c6d9db6c8c6c8c6c66c6c6c8cb9bd9bb9d9c6c6b6b6b6c8c6bb6b86c69a69d9b9d9b9b96ba999b9d999b9b6a96a99b6a969a969a96b9b9bb9b9b9b9b9bb96c68c68b6cb6a6b66a6b96
                9b9d9bd9191d919191911d11119dd9d9d1d91d91d1d91d91919191d9d19d91d91d9191d9119d99d9d9d9d1d99d99d9b9d9c86c86f6868c6b6b6b66ab99b69a96a969b939bb6c8cc68cc6ccc6bd9b9b7b6b8c6c66c6b6c6c9bb9b6c6f6c66c6c6c686c666b9bb9db9b6c6c686b6b66c6b6b6b6cb69a999d9b99b9b969639d9939b999b9696a69b96a96b96b6d9b9b9b9bb9bdb9b9b68c86c6c6666b686a666a6b
                1dd9b9111d1111d11d191919dd19d1dd9d1d9119d91d191d191ddd1d91d1d91191d1d91d99d9ddd9dd9d99d9d9d9b9bdb9c8c6f6c8cc6f66b6b9b6b6b8b9a6969a9b9bdb9c8c6f6f68cc6c6f9b9bd9dbb876c6cb6b6c66bb9db9c6c686c6c6c68c6c6f6bbd9b9b9b6c8c8c6c8c6b6c66b9b6b66a696399b9b9d9a6b6a99939b99ba96a9a99b69696b96a9b9bb9bb9bd9b9b9b9b98c68c6c86c6b6a6c66c8b666
                1191d19d1919d919191d1dd191919d91919119d91d9191d91dd919191d9191d91d9d91d9d9d9999d9d99d9d99d9d939b9c8c6f686c6f66b6b6b6b8c66b66c6ba696db9b9b68c686c8c6f6f6cdbd9bb99bb6b6b96b6c6c6db9b9b66c6c6c6c68c66c6c6c6bb9bdb9b6c686cc6c686b6b6a66b6b696a69b99b9a6969a969a69b9a696b9696b69a9a69a969b9b9b9b9b9b9b9b9b9bb68c66f6c6c6c66b6c6c686a6
                1d1d91d191d111d1d1d19191d1dd11d1d1d91d19d91d1d1d9191d19d191dd91d91d1d9d99d9d939d9d9d9d9d9b99d9b9bb6c68ccc6c6c8c6b6b6b66cc6b6b6969a9b9db9b6c6f6c8c6f686c669bd9dbd9bdb9bdb6b6b6b9bdbdb6c6c6c6c6c66c6c668c66db9b9bd66c6c6c8ccc6b6b6b6b6a6b6b9b69b99b9b9a6969a9b69b99b99a9a969a969b969a8b9b9b9b9b9bb9bb9b666c66c8668c686a66b6b68c6c6
                1911d191d1919d1919191d1d91919d919191d9d9d9d999d91d19191d91d91d91d9191d9d9d9d9d9d9d9d99399d939b9bd9b6c6c6cc8c8c6c6c6c6bb686c6a68b66bb9b9bdc8c6c8c6f6c6c8cc6b9b79bd9b9b9b9c6b6bdb9b99b66c6c686c6c6c66cc68c6b9b9b9bb6b6c8c6c686c6b6b6b6b6b6a69a69b999b99b9a9699b99b99b96969a969b69a68666b9b9bb9bb9b9b9b9bc86c86c8c68c6c6c66a66c68c6
                d1d911d191d1d191d1d1d911d1d1d191dd1911d9d9d9b9b9d91d9dd91d9191d91d9d9d9d9d9d9d9dd9d9399d9d999bd9bb9b8c6f68c6f66c6b6b6b6c6c6b6c68b8c6dbd9b66c8c6f66c8c6f686cb9b9b9b9bdb9db9bb9b9b9bb9c6c68c6c686c6c686c8c6db9bdb9b9c6c6c6f6c6c66c6b6b6b6b6b69b9b9b99b9696b9b6a9b9b99b9b9b969a99668c8cb6bb9b6d9b9b9b9bb66c86c86c6c6c8686c66b66c686
                1d119191dd9191d1919d119d919191d19191d91d19b9d98b6b191d1d91ddd91d91d19d919d9d9d9199d99d9939d9d9bb9db6c6c6c6f66c6c66c66c68c6c6b6c8c68db9b9b8c6f6c6c86cc68c6b66cdb9bdb9b9bdb9b9b9bdb9bd6c6c6c6c6c6c68c6c86c6b9b9d9b9b666c8c68c66b6b6a66a66b669a99b9b9b9b9a9698b66699b9b99b96b96b88c66c686868b6b9b9b9bb966c68c6c6c68c6c6c66c86a66c6c
                9191d1d1911d1d91d91d9d11d191d9191ddd919d9d9d9bb666a919d919d91d9dd9d919dd9d99d9d9dd9d993999b9db9db96c8f68f66c8c66cb6b68c6b86b6b6c6c879bdb9bc68c6f6cc6f6c6fb6c6b9b9b9bd79b9bdb9bd9bd9b6c66c86c6c66c6c8c6c6b9bdb9b7b9cb6c6c6c6f6b6a6b6b6b66a6c96a999b99b99b6c866a6a9b99a99b99a686c6c86c6c6c689b9bb9b9b9b8686c6868c6c68c6c86c6c6b68c
                11d19191d1919119db9d191919d1d1dd9191dd1d19b9b96ba966b91d1d9d9b9d91d9d9d9d939d9dd9d9d9399399d9b9b9b8c66c6c8c6f6c666a6cc8dbdb6b6b68c6bd9b9b78c6f68c6f68c6c68c66db9bdb9b9bdb9b9b9b9b9bb66c66c86c68c6c66c6c6db9b9b9b9b66c68cc6c66c66b6b6b6a66c66b99b99a99a9986c8b6b686b99b998c86c6868c6868c68c6b9b9b9b98c6cc68c6c6c68c686c6c686c6c66
                191d1d1d91dd19d999d9b1ddd1919d91d1d91919d99d9d9666a6b669b9d9b6a9191dd9d9d99d9d9d19dd9d9d9d999bb9b6c6f68c6c6c68c6bc6b66c9b9b9b6b6c66db9bd6b68c6c6c68c6c8c8c6fd9bd9b9db9d9b9bd9bdb9b9b6c6c86c686c66c6c86c9b9b9bdb9bdd66c686f68c6b66b66b66b66a66b9b9b9b99b8c86c6b6b6c86b98c686c86c6c68c6c686c66b9b6b9b9b68686c6868c66c6c6666c86b6b6
                1d19191d19191d93b9b9969d91dd1919d91d91d9b9b9b9b9a696a6a69b9b999d9d9d9d9d9d9d9dd9dd9d9dd9993939bd9c86c8c6f6c8c6c66b66b8b9b9bd9c6b6cb9b9b6b8c6c8c6f6c6f6c6c6c66b9bb9b9bdb9bd9bb9b9bdb66c68c68c6c6c6866c8c79b9b979b9b9b6c6c86c86c6a68c6a66a6c6b6869b999b9886c8666b6b6868868c6c686c8686c686c68c89b9b9bb9b9c6c68c6c66c86c68c6c66c668b
                91d1d191d1d1d9d99d9bda6619191d1d9191d9d9d9b9d9b99a6b696b69d9b6a61d19199d9d993919d91919d93999b9b9b8c86c6c68c6f68c6c6b8c9bdb9b9b6b68b9bd6c686f6c6c8c6c68cc6f6c6cd9b9b79b9b9bb9db9b9b9b86c6c8c6c6c6c6c6c68b9bdb9bdb9bb6b6c6c86c66c6b6666b66b66a6b886b9a88c6c6c6b6a666b6c6c68686c686c6c68c68c666b9b9b96b9b6b686c68c68c68c6686a686a66
                1d919d191919d9b9b9b996b6a19d91919d99dd9d9b9d9b9d6b696a69a69b9b96d9d9dd9d99399d9d9d9dd9d99d9d9b9b6c6cc6f6c8c68c6c6b6c66b9b9b9b6b6b8db9b68c6c68cc6c6f68c6f68c8d88b7d6c6dbb9b9b9b9bd9b6c8c86c6c6686c6c68c79b9b9b9b9b9b9c666c6c6c66c6cc6c6a6b6a66c6c88866c686866a66bb8b68c6c6c6c86c68c686c6686cb9b9b9b9b9b668c686c6c66c66c6c66c6c66a
                91d1d91dd1919b9d9b9b9a696b191d9dd9d99d9b99b9b9b996a6b698b6b966a661919dd9d99dd9dd19d9d9d9d9b9bb9d8c6c6c86c6f6c6c86c68cb9bdb9bb6b6b66db9c86f68c6c6f68c6f66c68c7d8b9b86c9b9b97b9bd9bb6c686c86f68c6c686c66b9bdb9b9bb9b9b6b6c6c68c6b6686c86b66a66b686c6cc68c6c6c86b666b6866868c686c6c686c66b6c86b9b6b9b9b69b866c6c686c86c8686c6866a66
                d9d91d1919d9b9d9b9d966b6a69d9dd9d9d9d9b9b9d99d9b9a966a696a6a96b9a9d9d9d9dd9d9d99d9dd9d9d99d9b9bb68c8c6c8c66c8c6c8c8c6bb9b9b9b66b6b6b9c8c68c6f68c68c686c8c8c69b6b6b6c86b66b6bd9b79b66c6c6f68c6c66c6c6c6bb9b9b9b96bb6b66c668c66c6a6c66c66a66b86c6c6868c668c86c6b6b66a6c6c6c68c68686c68c6b9b9b9b9b9b6b9b98b6c686c686c686c6c86c6c68c
                6b91191d91b9d9b99b9ba69696a6d99d9d9d9b9d9b9b9b99b66a96b6b969a9666b6dd91d9d9d9ddd9d9d919939b9bd96c86c6f6c6f686f686c686b9b9bd76b6b6c66c6c6f6c68c6c8c6f6c86c66bd9b9bb66c86cc6c6bb9b66c6c68c6c6c68c686c66b86b9b9bdbb69b6b6a6b6c8c666c6c68c66b66b68c68c6c68c66c6866b6a6666a686c66c6c6c68b9b96b9b6b9b9b9b9b9b6866c686c686c6c66c6868666
                b6b9d191d99d9b9b99b9b6a6a696a9d99d99b9d9b99b99b9b696b69a66a69bb9a96a9d9d9d9d9d99d9a9b9d99b9b9bb6c6c6c686c6c8c6c6f6c6c9b9b9b9c6b6b6b6b66c68c8c6f66c68c6cc6f6db9b6b6c68c68c86c9b9b6c668c66c686c68c6c68b6d6c9bb9b9b6c66866b86c686c66a66c6c6b6a6c6686c686c68c68c66a66a6a666c686868686c9b6b9b9b9b96b96b9b6b9bb6b866c68c6868c686c6c6c8
                69869b19d9b9b99d9bdb996b69a696d9d9d9d9b99b9d9b9b9a69a6969a96d9b96b6969b919dd99d9b96b6b9b99b9b9b66c8c6c8c68c6c68c68c6b7db9b9b66a66a6c6c6c86c6c68c8c6c6f68c66b9bd668c6c6c68c6866bb66cc66c66c6c8c6c66c6db9b6b9b9b9b66c6bc66b68c6c86b86c68686b666b8c686c68c686c6c66b6666b6c68c6c6c6c6b69b9b6b96b9b9a9b9b9b969b96b66c66c6c6686c666a66
                a6b6a6b9b9b99b9bb9b9bb69a66b6b9b99db9b9b9d9b9b99b9a696a6b66db9bb9b6a9a69b999b9b99b9969a9a9b9b9db66c68c6f6c6c8c6c6c6c9b9b9bd9c6b6b6b6b6b6c6c6c8c6c6f686c6c86cb96cc68c8c8c6c8cc686c668c66c86c6c686c86b9b69b9b9b9b9b6b8b9b66b686c6c6c686c6c86a6a666c6c86c66c6868c66a6a66a6666c686c6b9b9b69b9b9b96b9b96b96b9a6bb6b6868686c6c686c8686
                b69a9666a99bd9b9b9b9b9c669a96a66ba99b99b9b99b9d9b696b96969b9b9b9b969696b6ba9b99b99ba96696b9bdb9bdb9c6c668c86c6f68c6bb9b9b9bb6c6b6b66b6b68c8c6c6c6c6c8c6c6c6876c68c686c6c6c668c6c6a6c6c66c6686cc86c68b9cb9b9b9b9b9b96b6b6a6c6c86866b8c686c6666b6c686c686c86c666a6666b668b8686c6869b969b9b69a9b9b96b9a9b9b9666b6a6c6c668686c686c6c
                6b666b9a99b9b9b9b9b9bb6a866b696b969b9b99b9b99b9b9b9a6a9a6b9b9b9b9b6a9a9696969b9b9b996b9a9b9b9b9b9b9bb6bc66cc6c68c66b9b9bdb9b66b66a6b6b66c6c6f68c6c86c6c8c6c6d86c68c6f68c6f6c6c866c668c8c6c6c86c6c8bb666b9bb9c6b6b9bb9d9a66686c6c6c666c6c68b6a6b68c686c686c68c666b6a68b66b86c686b9b6b9b69b96b9a96b9b969a9bb9866686686c6c6c66c6866
                a96b9869b99b8b9bdb9b986b6b69a696a6999b9b99b9b9b999b96969b9b9b9bb9b96b69ab9a6b9b9b9b9a96b69b9b9b9b9b9b9b9b86c68c6c6d9b9b9b9b9b66a6b66a6b6686c68c6f66c6f686f6bb6c8c6f66c6c68c6f6c6c66c66c6886c686f6b99bb9b9b6b686c6d9b9b69b6c6c686c68b86c68b666b6b66c6c686c6866c6a666b66a66b668bb9b9b9a9b9a9b969b9a96b9a969b98a66a6c6c686866a68b86
                66a96b9a9b9d9b9b9b9cb6b66a6a69a69b9b9d99b99b999b9a96b6b69b9bb9b9b6b969a9669b9a999b996b96b9bb9b9b9bb9b9b6b6c6f66c6bb9bb9b9b9bb6b6b6b6b66a6c66c6c66c6c86c6c689b686c66c86c8c686c6866c6a6c86c6c6c8c669bb9bb9b9868c66c9b9c9bb6b868c6c66c68686b66a6668686868c66c6c6666a6b6a66b66a66896b69b96b96b9a9b69b69a96b9a6b6686686866c66c686686c
                9b66a98699b9b9b9b9c868c6b66b66b69a9b9b9b9b99bd9b996b969a9bb9b9bb6b6a96969a96996b99b9b9a9b9b9b9bb9b96b966c68c6c86c9b9b9b9b9b9b6b66a66b6a6b6c68c6c8db6c68c6c6b6c6c8c86c86c6c6c86c6c6c686c6c686866c6c9b9b9b9c8c66c86c9b9b6666c6c6866a66c6c66a66a6a6c6c6c66c8666b8b666666b66a66b6bb69a96b9b9b969b69a9b9b69b696686a6c66c686a6866c6c68
                b69a969b6a9bb9bb9b86c68c6b6b6b6a669b99b99b9b9b99b9a96a9b9b9b9b98b9b6bb6b96b9a69a9b99a969bb9b9b9b96c66cc86c6868c66b9b9b9bb9b9b6b6b6b6a66b6b8c68c6b9668c6c8c6b66c86c6c6c6c6f68c6c66c66c6686c6c6c86c666b9b6b866c86c8686b9a6a68686c6c6866c68b6666686868668666c6a666a6a6a66a96b66a99a96b9b69a69a69b96b969b9b9b6a66686a66a6686c6a686c6
                9a696a69a9b9b9b9b86c8c6866b6b6b6b6a69b9a99b99b9b99b969b9b9b9b9c666b69a96a96969b969a969a9b9b6b9b9c8c6c86c68c6c6c8b9bb9bb9b9bb9c96c66b6b66b666c66b9b6c68c6c6b9c68c68c6c8c686c6c68c66c68c6c86c66c6c86bd9b666c686c866c6c96b66b6c6c6866c6a6868b6a6b6c6c6c6c6c8666b66666b6966b96b996b69b9a9b69b9b9b6b96b9a96b9a668a666868686c66866c668
                b69a69b69b9b9b9b9c686c6c8b6a66b698b6a66b6d9b99b9b96b9a9b9b9bb98c8b6a66b6b9a9a96b9a96b96b9b9b9b96c68686c68c68c6c67b9b9b9b9b9b98c66a666b6a66b86c66bb68c6c686b9c6c6c6c686c6c6868c66c68b68c6c66c6868c6d686b6c68c686c868c6b9b66a6686c6c686c6c666b6686868686866c6a6a6a6a66a69a9a9b6b9b9a96969a96b69a9a9a96b9a966a668a66a66c66a66a686a6
                6969b69a9b9bb9b9b9b6c686c666b66a66b66b6a6b9b9b99b9b9b9b6b9b9b986c66b9b6b669b969a969b9686b69b9b6c86c6c68c68c66c6c9b9b9b9b9b97b66c66ba66b6b6b6c6c66b6c686cc6b9c686686f6c6c8c6c6c6c66c6c6686c66c6c66d86c68c86c6c6c6c6c68b96a666c6c68686c666a6a66a6b6c6a6c6a68666666666a9b696969a969696bb9a969b9b96969b9696b66668666866a66868668b686
                ba969a69b9b9b9bb9b9c86c86c6b6a66b6b6b6b6b699a9a68b9a9b9b9bb9b6cb68686b69ab69a9b969b9a6c6bb6b9b866c868c686c6c8686b9b9b9b79bb9b68c8c66b66a66a66b6c66c68c6c6b9b68c6c6c686c6c6c86c66c66a68c6c66c668cb66c6c6686868686868666b66b6868686c6c66a6666a666a6668666866a6a6a6a69696b9a9bb96bb9a969a96b9a696b9a69a9a998a68b6a66a6686a66a668668
                96b6b969bb9b9b9b9bb66c6c686b69a6b6a66a696a6a666c686b6b9b9b9b989b9b8c68b669a6969b9a96686868b9b86c86c6c6c6c686c6cb9b9b6b9b9b9b98c6688c6a66b66b6666c86c68c687b66c66c66b6c68686c686c6a66866c6bb68b6b66c6868c6c6c6c6c6c6c8c6d68b6b6c6c6898668b6a66a666a6c6a6c6c6666696b9a9a96b966b99a96a6866b969b6b969b696b6b66cc66686686a66686c6ccc6
                b969a9b9b9b9b9b9b99b6686c686a66b669a666a6666b6b86c6b69b9b9b66bb9b66c68b6a66cbb8666868c6bb69b6686c68686868c6c6c6b9b6d9b9b9b9bb68c6c6666b66a66a6a66c68c66c6b9c66c66c6866c6c6c6c6c666c6c6c66686a69b6686c6c686c68686868666a98b6868686a6b6a66866666b6a66c66866868a68b9a96b969b69cc66686666a668a66a66a66a669a966cf686a66a6668b6668cf66
                6b9a969b9b6b9bb9bbb6c6c86c686b66a666b66b6ba68686c686a9b69b9b89b98c86c66b66b6696a86c6c689b9b98c6c68c6c6c6c686866b9b9b9b9b6b9b66c686c6a66a668c6b6a66c68c686b9b6c6c66c6c66b66c68c68c6866c68c6a69b686c6c686c6868c6c6c6c6c68b666a6c6b686866a66b6a6a6666bf6cc6a66666b969b96b9a9a6fc6a6b6a6666a666666a6666a6866a6cc66a666668b686a66cc6c
                9a969bb9b9b9b96b9996c86c68c66b6b6b6b6a66a666c6c686c68b9bb9b9b9bb666868c6b66a6a666c686c6b9b6b9c686c6868c686c6c86b9b9b9b6d9b9b9868c6866c6b6c686666c686c68c6bb6b668c68c6c86c66c6686c6c8686c686b9c6c68686c686c666c6866868666a66668686b66a668b666666a666cc6f668a6a69a9a69a96986ccf666666a6a6666a6a6668a6666a668ffc666a6a668c668ccffcc
                6969a9b9b9b9bb9bbb6c66c686c6c6b698b6b6b66b6b686c686c6b9b9b69bb99b8c6c66b6b6b6b6b686c68d9b9b9b9bb686c6c68c686c6b9b69b69b9b9b9b8c66c6c66a666c6c6a66a6c686c69b96bb66a6686c68b66c8c6866c6c686c6d8686c6c686c6c68c686c6c6c6c666a6a6a66a686686b689a6c868acff6e8666c9b6969b66ba666cfc66a6a666668a6666686666a66686cccf6b98666a6c6acf6cfcf
                9b9b9b9b6b9b9b9b99b68686c68686b6a69896a686a66b686c686b96b9b9b96b96868686b6a966b6a6c68b9b69b9b9b9b9b686c66c6c68b9b9b9b9b9b6b9b66c8686c666a68686c66666c6c6b9b6b69b666c6c686c68666c6c8686c6c6986c68686a6c6866c66c66868668a666666686686a66a668b86fc666cfcffe6b6c69a9b69f9966a6fefc668666a66666a686ac6a666a6666cf7c66986a66f66fcfef7f
                96b9b9b9b9b9b9b9b69c8c6c68c6c66a6b6b6a66b666a6b6a66c69b9b9b69b9bb6c6c6c6a966a6966b866b9b9a9b6b9b9b6b6868686866b69b9bb9b69b9b68686c6c66a66c6c6c6a6ca66866b9b99b69a6b666c6c68c6c8686c6c6866b8c686c6c668686a686a686a6c6a668a6a68b6a6c96c6686666afc66cfcf7fc6b6cc966a6cfc8f66ccf7f666a6668a6a666a66c6666666a6fcffc6b6a666cfc6fef7ffc
                b9b9b6b9b9b69b69b9b86686c668686696a6669a686a666668b6b9bb969a9b69b986c68666a666a6b668a96b9b69b96b969a6c6c6c6c6c9bb9b96b9b9b9b9c6c68686a66c68686668686c6cb9b6bb9b866a6a6686866c68c6c66b86a6666c6c6868c66a6686686c6666866c6666866866868686a18b8cff66cf7ff7fc9ccf6b666fcccc66ccffc6a666a6666668c666cc68a6a666cf7fc6986668cfccfcff7ff
                9b9b9b9b9b9bb9b9bb66c6c686c6c6a6a66b6a66b6666a6a6b9b9a96b9b6b9b9b9c686a6a6b6a66b6866bb9b69b9b9b9a9b686868686c669b69b9b9b9b69c686c6c666c668b6a6c6a6c66c69b6996b66c8666a6c6c6c8666868b6666a6a66a66a666a668c6c6c668a6a6c686a6a6a66a66a66a666666cf7c6cff7fcfc6f7f666a6cffcf6e4747f6666666a66a6cf66cfc6666668ccfcfec666a66cf7fcf7fcf7
                b9b69b9b69b9b9b9b98b66b86c6868666b66a96b6a6a666686b69b69b9b96b9a69b66866666b6866a6a8969b9b9a9a96b9b66c6c6c6c68b69bb9b69b69b686c6868c6a66a6666c66668c68686a6c98a686c866c666866c8c6c66bb9c666a66686c686c8666866a66686686a666666866866c666a68afcffcf6fcfcf7f6efc6a668cf7fc47eeee4c66a6a666666cc66cfcc66a6666c6fcff66666afcfcf7f7fcf
                9b9b9bb9b9a96b9a9b9b9b9b8686c6c868b6686666668c6a686b96db9a9a9b69b9b6a6c86a666a668666b9b9a96b96b9b96868668668666c89b69b9b9b98b86c6c66666a66a6a68a6b668b6c6686a668c66c686a6a6c68666686b66a6b666a6b686c6c6c6a6a6686a6f66c6686a66a66a666a66866c6f7ff7fef7fcfcf7fcc666cfcfc7e4e74eee669696c6a6cffc6fcf66666a6cfef7f7ccbbecf7f7ffcfefc
                79b9b969b9b9b9b69b69b969b6c6686c666a66a6a6a66686c66a9a69696b969b9a998666c66a66b86b86bb696b9b69b96b8b86c6c6c6c866c9b9b9a9b6b68668668c6a6686666b66b9a668686c6c68c66c686c68666b86c6a6c686a666a6666866ac6f66866686a666cc6fc66a6866a668a6686c6afccfcfccf7ff7f7fcf7f66acff7fe7edb7e7fb6a96ac9668ccf6ec7f6a6666cfcffcffce47b7fffcf7cf7f
                9b6b9bb9a96b9b9b9b9b9a9b69b86c66a6a66686666a6a666a66b66abb9b9a9b698c68c68666b666a66b69a6b969b9a9b9666c6866866a66b69b69b69b6a6c6c6c66866a6c6b9b9b966c6c6c6868666c686a6686c6a666a68686a666a66a6a6b866fcf6c66a666686cfcfcc66666a6686666a66c6ccf7f7ff7ffcffcfcf7fc666f7ffffddb9bdce6696a6f69ccf7fc7ffc666a66ccf7f7fcf94bbdf7ef7f7ffc
                79b9b9b96b9b69a96b96b9b9bb66a6868666a66a8686668c686866b68696b96b9a66666a6a686a6666a68666a9a9a96b9b6a66a6a66a6b9b9b9a9b9b9a66686686a6c6666a6b9a96b6a666a66a6c6c866a668c6a686b68666c6668686666b666a66cfec66868a68b6cfcfcf68a666866a6a666cfbcf7fff74e7f7f7f7f6fcfc66fcfcef9ddb9b7fc6b9cfcc6ccffcf7fcf666666cf7ffe7efd9b9be47eef7cfc
                6b9b69b69bb9b96b9b9b96b696a6686c6b666a666c6c6c666a66a66668b69a66686c8a66686b66a6a6666a686b696b9b698686686866b96b69a696b9696a66a6c6866a8c666b96b9b686a6686866866a686c66666c66a66c686a66a66a6a66a66ccfefc66cc666686fcf7fc6666a66a66666b9fccf7fcf7e4e4eefcffcf7f7f6ccfef7fdd9b79cf76c8f7fc6f6f7f7f7f7fb6a6ccffcfdbfcdd97d7b47ef7f7f
                9b9b9b9b866b6b9b96b9a9b9a66866a6686a666a686686a6866c686a666a698a6666668686b66866686a6686666b9b69b98b6a666a689b9b9a96a96a9b66b686686c66668a69a9b96a668686c6c6a6866c668b6a68666a686a6686686666966a6cfcf7f666cc6a66ccfcffec66866a66a69a96cfcffcf74e47e47eef7fcfcfc6cfcfffc7dd9bb7fc6fcfcff6ccffcf7fcfc6666cc77e77b77d9bbb9bbb7c7e7f
                9b96b9a66a686a96b9a96b986866a6686a666a666a6a66866a6866a686a68966a6a68b6a6b98b6a6866686b6a6a6969a9868668c666b6b6969b66866b9a66a66a66868a666b969b6a6686c6a668666c6868668666a6a666a6686a6c6a6a6a6666cf7fcfe68cf668b8f7fcf7f66a686669cc66cfef7f7ffb4e47be7fcf7e7f7fc7ef7f7f19db9bcfe6fe7f7c7f77777e77777e7777efffcfce7bb9b77cc777777
                b9b9b666a66669b9a96b96b6b6a6686c66868686866686a66866a66668666c6b66866866b96a6966a6a66a686669a9b69c66a666a68b99a9a6986c6a969b66986c6a6668c69a9b96686a666686a6866a66a6a6a666866a6666a6666666666a6acffcf7fc66fc6666cffcf7fc666cc69a6fc66cfcfcff7f797b9b7df7e4eeefcc7befffcdd9bb977e7777777777e7e777e7e77e7ef7c7c777c7c777e7777e7c7e
                6b9b9b9a668a6a6b669b9a99b966c666a66a66a66a66a666a66a6686a66a68969a6b6a696a966a66666a66866a9a969a66a66868666b6b969b6b6668b9a9b6b668668b866a69b6a66a6686a66666a6866c666668a66a666a66686a86a6a66696cf7fcf7f6ccfe6a6fef7ffcfc66cf966ccf6cfef7f7fcfddddb9bbff7b7df7fc7d65e77bddb9b7e7e7e7ee7e7e77e7e77e7e77ccfef7f7e77e77c77c7e77e77c
                9b6986896b6666866a6b69b69a9b68a66866a666668666a6686686a668666a6a969669ab96b666a6a66666a666b69a6966686a66a689b69a9b96a9b696969a98b6a6666a669b98668666a668a6866c6a66868a666b668666a66a6666866a6a68fcff7fcfccf7f666f6f7fcf7f66fcf6afcfef6cffcfcfcdd9b9b9b7c7db9ec7f7cf7be7d9b97db777e7e77c7e7c77c7c777c7ef7c777777e77f7e7e77c7f7fff
                9b9c6c6866a686a66699a96b96b666686a66686a86a6a6866a66a666a66a6666b9a9a96969a6a69669a6a666a696b9b98a66a66666a69a96b6a9969a9ab9a66686686a668b9a66a66a6666a666a6866686a6668b66b66a6b686668a66a66666ccf7ffcf7f7ffc68bc6efcf7fc6bcfc66cf7fcf7f7f774fd9ddbdb777bd9b7774747dbb7dddbb6ffe77e7c7e77c7e77e7e7c77c7ff7f7ec7c7e777c7e77effcfe
                6986866a6866a668b9a69b9a969a98b6666a66666666666a6666668666a668a696b96b9a6969866a666666a6686a669a666a66a6a69896b9696b6b96b96b66a66a66a68666b96666a66a6866a666a6a66a66c6689a96a6666a6a6666666a66a6ffcf7fcfcfcf7c6cfef7f7ffc6fcfc6cfcffefcfff4ed77dd9b96b4b7ddbe74be749db7e79bcfecf7e777e7c77e7c77c7c7ef7f777e777e7f77c7e77c7fffcfc
                76c66a66c668668b89b96b69a9b9686a6866a6a6a6a68a6686a6a6a6a666a669a96a66969a96a666a6a6a666a6666a666a66666666b6b96b9a99a9a9696966686686666a68686a686666a666686a66686666c86a69b696a686666a6a6a6669fcf7ffcf7f7f7ffc6cf7f7ffcfe6fef66cf7fcf7c7777db7b7cfffef74bd7e7e74eeedb947c77fcf777e7c77c7e77f7e7e77e7fc7ce7c7f7c77e7e7c7f7efcff7f
                666a68686a66a6698b69a9b96b698b668b86666668666666a6666666668666866a966a6a96b666a9666666a6698a666a668686a689a96b9a696b9696a9a6a86a6a6a6866a66a666a66a666a6a6666a66a6a6f669b69a69866a66866666c86a6fefcf7fcfcf6cf7c6fccf7feffef6fefc7f77777477b77e77cf7fc7e747474b4e47e49b77e7e7777e7c7e7f77f7e77c7f7ff7f7e7f77e7e7f77f7e77e7fff7fff
                6a6866c66686686b69b9696a969a6686666a6a686a6a66a66686a686a66a66a666986666a969a66689a66696a6666a6666a66a96a6969a969a96b6b96b66666666666a6666666a666a66866666a6666a666ccc9a969b66a6666a66a686cf66cffcf7ff7f7fcf7fcfef7f7f7f7fc77777747747e77e7e77e7ef77e7e7d47d7474e47eb9e77e77ec7e77e777e77e7c7f77f7c77e777ec7f777e7cff7f7ffcfffcf
                6666c66a68b6a6a66a96a9b96b966a6a6a66666a66666a6686a666a66666a666a66a6a6696a9866a6666a6a666a66666a669896969a9696b96b969a96986a6a6a66a666a6a6a666a6686a6a6a6686a6666afcf96b9a98666a6666a66a6fc66cf7fcf7eeff7fccf7fc7f7fcf7e77e7e7477e77e774777e77e77e77ecf7c74b7bd7bd9b77c7e7c77e7c7f7ec7f7c7f77fec7f7f7f7f77f7ec7f7fcfffffffcfcfc
                c6c86a6666866666b969b696b6b98666666a68666a66a666a666a666a6a6668666a6666a69696a666a6666666666a668666a66a6a96b6a96a96a9696a98666666866866866666a666666666666a6666a666cfc696b6698a666a6666668cfc6feff7e4e74fcf7fcfcfcf7c7e77e77e77e777e77e77e7e77e7777ecf7fef77e7edb9bb9b7e7c77e7f7e77e77e7e777ef7f77e7e7c7e7f77c7f7fffffcfcff7ffff
                7f666686a66a689a96a969a969a66a66a6666a6a6666666a66986666666686a6a66698666a6a6666666a6a6a6a9666a66a666666669a969a9696b6a966a6a66a66a66a66a68a6666a6a6a66a6666a6666acf7fb696986666a666a66a6ccfccfc7ffd74b9f7cfcf77777f7e7c77e77e77e7e7e77e7ec7e77e7ee7f7f777e7e77ddb9bd6e7c7e7f777c7f7f7c7f7fef7c7ef7c7f7e7f7e7f77ecffcffff7fffcff
                666a66a668666a69696b9a69a9696666998a666666a66a66986a66a6a66a6666666a96b666666a6a6a666696666a6666666a6a66a6696b696a969a969a6666666666a666666666a6666666666a666a6866cffc69a9a6a6a6666866666cf7f6fffcfd9db7cfc7777e7e747e77e77e77e77e777e7ef77e7e77e7fc7f7f7e7e7e7c7bcc7e7c77f77ec7f77e7e7f7e7f7c7f77c7f7c7f7c7f7ec7ffff7ffffffff7f
                66c66866a6a6669a9a96a9696b6a9a68a66666a6666a66968966666666666a66a66669a9a66a66666666a6869a666a6a6a66666669a69a9696b6969a6666a6a6a6a666a6a6a6a6668a66a6a6666a666a66cf7fc6966666686a6c6a6a6cffcf7f7fcddb9b7e7e7e77e77777e77e77c77e77e7eec7e7e7f7fefc7fcf7e7c77c7e7e7fff77e7e7e7c7e7e7c7f77fcf7c7f7e7f77e7f7c7f7c7f7ff7fffcffcf7fff
                6668b6686666a6b696b969a69a96966666a6a666a6666a66a6a6a9898a66666666a6b6969666666a66a66698666a966666666a6a669a966a9a9a9a696a666666666666666666666a66666666a6666a6668cffcf9b69a66ac668c66668fc7fcfcfe7e7cf7ec7f77e7747ee77e7e7e7e77e7ec7f77c77c7f7c7fc7f777e7e7e77c7fc7f7c7f7c7f7e7f7f7e7fc7f77f77c7f7cf7f7c7f7ef7c7ffffffff7ffffff
                6a6668a66a66669a696a969a6969a6a6a696668666a66666666666a6666a6a6a66666a66a9a66a6666666a66a66666a666a666669a6969a96696696a666a66a686a6a66a66a66a6666a6a68666a66666a6fef7f69a66a6cf66cfc66a6ccff7f77777777e7f7e7e747e777e77e777e7e7ec7f77e77e7fcefcf7f77e7e7c7f7c7e77e77e7f77e77e7f77e7f7f7f7c7ecef7c7e7f7c7f7c77f7ffffcfcffffffcfc
                666a666666a6a669b6969a6969a6966666866a66a666a6a6a96a6666a98666666a66669a96666666a66a666666a66666a666a66a6696a6969a69a69966666666a66666666666666a666666a6a666a6666cf7ffcc699698cf66cfc666cf7777747ee7e7fe7e77777e77e7e7e77e7e777f7f77e7c7e7fc7f77e77e7c7c77e77e7f7f7c7f77ec7f7f77ce7f7fcf7c7f7f77f7f7f7c7f7ef7f7fcfcfffff7ffcffff
                6666a9a6a66666a69a9a6969a696a69a66a666666666666968666a96666a666a666a6a6666a6a6a6666666a6a666a6a66666666966a696a9696696a6a6a6a6666666a6a6a66a6a666a66a666666666a6ccffcf7696a666fcc6fcf69677e7e7e7e7f7fe7777e7e7e7e77e777e7cf7f7fc77e7c77eff77e7f77c7c7e77f77f7c77e77f77ec7f7c7ec7f7fcf7f7cef7c7f7c7f7c7f7cf7c7fcfffffcf7ffffff7ff
                cc698966666a669a69696b6b96a966666666a66a9a6a66a666a9666a66666a6696666666666666666a69a66666696666989a6a686666a966a69a9696966666a66a6666666666666666666666a6a6a6666cf7fcfc6b96acfcfcc77e7e7477747ef7f7777e7e77e7777e77e7e7f7c7fc7e7c7e7ef7c7ffc77e7e7e7f7e7c7e7e7f7c7e7f7f77e7f7f77f7f7fc7f77f7e7f7f7cf7cf7e7f7f7ef7fffffffcfcffff
                ffffc69a6a6689696a96a986c9698a6a6a66666666666666a6666a666a6696668a66a66a6a66989a6666666a698a666a66666696a98666969a6989a98989a66666a66a66a68a66a6a6a6a6a6666666a6ccffcf76c9698cf7777e7747e77e7ef7c77e7e7e77e77ee7e7e7c7cf7fef77e7f7e7f7ff7fc77f7c77f777c7f7e7f7c7e7f7c7e7cf7f77efcfcfc7f7c7f7f7f7c7f7ef7ef7f7fcfcfffcf7ffffffffcf
                cfcffff66666a9a696a9696cc6a96666666a6a6a66a66a66666a6666666a66a696666966696a666666a66a666a666a666a66a66a696a96a9696a9669a698966a6666666666c66666666666666a6a66c66fc7fffcf9a66e77e7e77e777e7eef777e77e777e7e7e77e77c7ef7fec77e7f7ef7f7f7fc7e7f7e7f77ec7f77c7c77f7f77c7f7f77e7cf7f7f7f7f7f7f7c7f7cf7cf77f7c7fcf7ffcffffffcfcf7ffff
                ffffcfcf66a69696a9696a6cc696a96a666666696666666a666986a66a66666686a66a66a6666a66a966666989666669898966696866696a66966b66986b6a666a6a6a6a6af6a66a666a6c6a66c666c6bfff7fcfc67b777e777e77e7e777777e7e7e7e7e77e77c77c7ef7f7f77f77c7f7f7fcfc7f7f777c77e7c7e7c7e7f7e7e7cef7e7c7f7f7f7fcf7f7c7ec7f7f7c7f7f7fc7f7f7f7f7ff7ff7ffffffffcf7
                ff7fffff6a666a69696a966cc6b696966a698986a66a6a666a666c696666a6a696666666666a6666666a698666a66a66669a69a66a96a9696a9a96b6a9696666696666666ccc66666a666c666cf69cfc6c7ffc77e77e7e77e7e7e77e77e7e7e77e777e77e77fe7e7ef7f7fc7e77e7fef7fc7f7e77e7c7c7f7c7f7f7e7f77f7f7f777f7f7f7cef7f7f7f7f7f7f7f7ef7f7ce7cf7f7f7ffcfffffcff7fcf7fffff
                ffffcfcfc669a96a98966a6ccc698a6a666a66a66666696666a6ac68a6a66966a66a989a66666c6a66666a6a6666696a6a69666666696a669666696966a69a9a6866a9666cfc66a66c6c6cf69cfc6cfc6ffc77e77e7777e77e777e77e7e77e7e77e7e7e7c7fcf7f7f7f7f77e7c7fc7f7f7fc7c7f77c7e7c7e7f777c7f7c7c7c7c7fc7c7e7f7f7fcfec7cec7f7cef7cf7f7fc7f7cf7ffcffcf7ffcfffffffcf7f
                cffffffffe6696966a6a96ccfc6c9c6698966666ac6a686a6cc6ccc69669866666666a666a96ac696a66666966a986669666a9a969a6969a6b9a98a9a969666669a6666acfcf6666ac6fcfc6cfcf6cfcc777ee7e77e7e77e77e7e7e77e7e777c7e7c77c7fef7f7fc7fce7e7c7f7ff7fc7f77e777e7f7f77c7f7ece7f7e7f7f7f7f7ef7f7fcfcfcf7f7f7f7f7f7f7f7cecf7f7f7f7fcffcfffffcffcf7fffffff
                fcf7ff7ffc6b6a6c6cc669fc7feccfb666a66a66ccc69c66ccc6c7c666c6a66a6a666666666a6cc6666a96a666666a66a9666666a696a66966666966696a69a668666a66cf7f66966fcfccf6ccfcfc7e77e7f7e7e77e7e77e77e777e777e7e77e777e77f7c7f7f7fc777c7e7f7f7fc7fc7e77e7f7c7e7ce7f77c7f77c7f7e7c7f7c77f7fcf7f7f7f7f7c7f7cce7f7f7f7c7f7fc7f7ffff7fcfff7fffffcf7fcf
                fffffffff76c666cccccc6ccf7cf7ccc666a66ccc7e66cc6c7f7fcc66ac6c666696a96a6989ccfc66a968666a66a669666a96a9696a969a69a96a969a6696a9669a66666cffcc689cfcf7fccf7f7e777e7fe7f777e77e7e7e7e7e7e7ee77c7e7c7f7efef7fcf7fec7f7e7ef7fef7fef77e7c7677e7f7e7f77ce7f7cf7f7c7f7f7ef7fcf7f7fcf7f7c7f7f7f7f7f7cc7f7f7fc7fceffcffffff7fff7ffffffff7
                ff7ffcffcfccec6cccf7c7c7ec7cc7e7cc6cccc7eb16bcd6eccce7fe6cccc6c6a6666666a68cc7f6666696a6696696a669669896a9666696666966a696a69666a6666a6cf7fffc6bfcf7fcf7fc777e7e7f7fc77e7e7e777e777e77e777f7e7c77e77f7f7f7f7fc77e7e7f7f7f7fc7c7e7f7e7e7c7c7c7f7ce7f77f77c7f7f7cef7cf7fcfcf7f7fcf7f7f7fcef7fc7f7f7fc7f7c7f7fffcff7fffcfffcf7ff7ff
                cfffffffff77fcfef7f7c7e77f777b7eccf7f7e77bd7b77e777777f6cf77c7c666a66a6669ccfcccc66a6669c6a68696a66a66666669a66a9a989a96696986a6666a966cfcf7f766cfcfcf7e77e7e7efcf7c7e7e77e77e77e7e7e77f7e77e77f7e7fc7fcfcef7e7f7c7c7f7fc7f7e7f7c7e7c76e7f7f77c7f7c7f7cef7e7cef7ff7ff7f7f7fcf7c7f7fce7f7cc7fcf7fc7f7fcf7fffcffffffffffcfffffffff
                7fcff7ff7f7e77c7f7fcf7f7e7e7e7e777fccf77e7b7b7e7e77e77ef7fcf777e777b7bcb686e6f7fc6986986c66c96a696969a9a96a6969666698966a66a96666a6666cfc7fcfc6b6fef7777e77e7f7f7777e777f77f7e7f777c7f77e7e77f77efcf7f7f7f7f7c77e7f7fcf77e7c7f77f7f7f7f7f77e7f7f7c7f7c7f7c7f7f7f7fcf7fcfcf7c7f7f7ce7f7cf7f7f7cf7ce7f7f7f7fcf7fcffcffcfff7ffcffcf
                fcf7fffffff77e7f7f7f7f7f77f77f7c7e77f7fc77e7e77ed7e77e77f7f7f777e7e7777777777ecc5c6c6a66cc6c6a666a66666669666a69a96a966969666a69669866cff7f7fc6cf7777e7e7e77f7f77e7e7f7e77e777e77e77777e777c77e7f7f7fcf7fc77e7f7c77f7c7ec7f7e7c7e77c7c7e7ce7f7c7c7f7c7f7c7f7fcfcf7f7fcf7f7f7f7f7f7f7fc7f7f7f7f7f7fccf7fffffffffffffff7ffffffffff
                7ffcffcffff7e777cf7fccf7fc7e77e7f7e7cf7f7e7e7e77e777e777ef7fccf77e7e7e7e7e7e77777ccc669cccccc6c6969a69a96c6b9666666989a6a69cc668986a6cccf7fcff777e7e77e777fcf777e77c7777e77e7c77e7f7e7e7c7e7e7cf7f7fc7fc77f7c77e7f7fe7f77f77f7e7f7f7f7f7f7f7c7f7f7c7f7c7f7cf7f7fcfcfcf7f7ccf7ccf7fcc7f7f7fc7f7f7f7f7fffcfcf7ffcf7fcfffffcfcf7fff
                f7ff7fffcffc7f7e77f7f7fc7ff7f7c777f77cf7c77f77e77e7e77e777cc7f7fe777e7e77e77e7e7eb7ccccf7ccf7ccff6669866cc9869a96a98989696acf966a6c66cf7fef777e7e7e7e77f7fe7e7e7e7e77ee7c7e7e7e7c777e77c7e7c7f7fecf7ff7e7e7e7f7f7cf7c77f77ec7c7f7c7e7c7c7c7f7f7e7f7f7f7f7f7fcfcf7f7f7f7fc7f7f7f7c7f7f7fcc7fccecc7f7ffffff7fffffffff7ffcfffffffcf
                cfcfffcfffff77e7f7cf7f7fc7fc7f7ef77e777e7f77fcffc777e77e7fefffccfef77e7e77e77e7e77e7f7f7f777fffcfc6a696cccc9666696698966a66cf66666cfcfcf7f7e7e7e77c77f77fcf77c777c7e77c77e7c77f77e7c7f77e7f7f7f7f7fcf77c7f77c77ef7f7ef7e7f7c7f77f7f7f7f7f7e7f7c7f7c7ec7f7cf7f7f7fcf7f7f7f7f7ce7fef7fcc7f7f7f7f7fcfcfcfcfcffcf7ffcfffffff7ffcffff
                7ff7fcff7ffff77e77e7f6f7fc7fcf7f7e7f7f7f77e7777f7fe77e7e7ff7ff7f7c7fe7e7e7e7e7e7f7e77f7c7f7ffcffcf696cccccf69a6a66a69896966ccc6a98ef6cf7777e77c7c77e77fec77c7e7c77e7f77e7f77f77e7f77e7e7f77f7fec7f7f77e7f7e7f7fcf7e777c7f7c7f7c7c7c7c7e7cf7f7c7f7cf7f7f7fefcffcf7fcf7fc7f7cf7fc7f7f7f7f7fcc7f7f7f7fffff7ffcfffffff7ffcffffff7fff
                fcfcf7ffffcffef7f7f7cecf7fc7f7f77f7c7f7ec7f7fe77f77f7f7fffffff77fcf7f7f7f7e7f7f7ef7e77e7effcffcffcf6ccccf7c666989696a6a66cfefc668cf7f77e7e7e7e77e7f7efcf7f7e77c77c777e77e7777e77e7e77c7c7fefce7f7e77e7f77e7c7fe77f7f7f7e7c7f7e7f7f7f7fcf77c7f7f7c7c7fcfcf7f7f7fcf7f7f7cf7f7f7f7f7f7f7fcf7f7fcf7f7fcf7ffffcfcfcf7ffffff7ffcffffcf
                7fcf7fcffff7f77f7c7f7f7f7f7f7f7fc7f7f7c7f7ce7cf7ecf7e7fffcffcfe777fcf7c77f7f7e7f7ff7fc7ff7ffcff7ffc7e7c7cfcc6c6c6a669698bcf77ffe6f7e7e77e7c7c7f7e77f7f7f77e7f77e7e7e77c77e7e7e7f77c7ff7f7f7f77c77f7c7c7e7c7fcf7f7e7c7e7f7f7e7f76e7cec77c7f7f7ec7fcf7fc7fcfcfcf7fcf7f7f7cf7f7f7fcccf7f7c7f7f7f7f7f7ffff7ffff7ffffffcfcfffff7fffff
                fcffff7f7fffff7c7f7c77f7f6fcf7fcfc7f7f7f7f7f77ef7f7fcfcffffcfff7f77f7ffcf7e7f7fcffcfffc7ffcff7ffcfff7f7f77efcc6cc696a66c6fcfccff77e77e7e7e77e777e7fcfc77e77e7e7f77f7e7e7e7c7e7c7e7f7f7fce7f7c7f7e7c7f7e7f7f7f77c7f7c7f7c7e7f7c7cf7f7f7f7f7f7cf7f77ff7ff7f7f7f7fcf7f7ccf7cecccf7f7f7fcf7fcf7f7fcccf7ffcffcfffcf7fffffffcfcfffcf7f
                cf7f7fffcfffcffef7f7fe7c7f7c7fc7f7fcc7f7ce7fcf7ffffcfff7fcff7fffcf7ecc7f7fcf7fffcffcffff7ffcffcff7fffff7cf77f7fec6c669cfcf7e7f77e7c7e7e7c7f77f7e7fc7f7e7c7f777e7e777e77e777e7f77c7fcfc7f77c7f77c7f77c7f7cf7f7ce7f7c7f7e7f7f7cef77c7f7f7f7cec7c7fcf7fcfcfcfcfcfcf7f7fc7f7f7f7f7f7f7f7c7f7f7fcc7f7f7ffffcff7ffffffcf7fffffffcfffff
                f7ffcf7ff7fffffffc7f7fcf7fcfc7fc7f7f7fcf7fc7f7ffcf7ff7fffffffffffffcfffcf7f7fcf7fcff7f7fffcfcff7fffcf7fffffc7fc7f7cc66fc7fcf77e7c7e7c77f777e7e7ffcff7e7f7e7e7f77c7e7c7e7f7e777e7ff7f7e77c7f77e7f77c7e7c77f7c7f7f7e7f7cf7c7ce7f7cf7f7c7cef7f7f7f7fcfcf7f7f7f7f7f7f7ccf7fcf7f7f7fccf7fcfcf7f7fcf7f7fcfcff7ffcf7fcfffffcf7fffff7ffc
                ffcffcfcff7fcf7fffffc7f7f7c7fc7fffccf7f7f7f7ffffffffffffcf7ffcf7fffff7ffff7f7fffff7fffffcff7fcfffcfcffcfcfcffcfcf7fcfecfcf77e7c7e7e7f7e7e7f7c7fc7f7c77c77e7c77e7e7f77f77777f7cfcf7f7e7f7e7e7c7f7e7c76f7fe7c7e7c7c7f7c7e7f7f7f7c7e7cef7f7c7f7f7ff7f7f7ffcffcfcf7f7fc7f7f7f7fccf7f7fc7f7f7fcc7f7fcf7fff7fffffffff7ffcfffff7fcfffff
                7ff7ff7f7ffcffffffcfff7f7ffff7f7ffff7fccf7fcffcf7fcfcfcffffffffffcf7fffcfcfffcfcffffcfcff7ffff7fcff7fffcf7ffcff7f7fefcf777e7f7e7f77f77e7c77e7fcff7f7e7f7e7f7e7c7f77e7e7f7f77e7f7f7e7c77c7f7c7f7e7f7c7e77f7f7f7f7f7c7f7f7f7c7c7f7f7f77f7f7f7ccf7ffcfcfc7f7f7f7fcfc7fcf7f7fc7f7f7f7f7fc7fc7f7fcf7f7fcfffffcf7fcffffff7ffcffffffcff
                fcffcffffcf7f7ff7fff7ffcffcffffffcfffff7fc7fffffffffffff7ffcf7ffffffffff7ffcffff7ffffff7fffcfffff7fffcffffcff7ff7fcf7f7e7f7e7c7f7e77e7f77c7ffc7f7c77f77e777c7f777e7f7c7e7e7ffcf7c7c7f7f7e7f7e7e7c7c7f7f7c7e7c7e7c7f7c7f7cef7f7c7f7cf7fc7f7f7fcfc7f7f7ffcfcf7f7f7fc7f7fcc7fcf7fccf7fcf7f7fcf7f7f7fcf7ffcffffff7fcf7fffffffcfcfffc
                f7fcf7f7fcffcfcfffcfffff7ff7fffcfff7fcff7fcfcf7ffcf7f7fffffffffcfcffcfcffcff7fcfffcf7ffffcff7fcfcffcf7f7fff7ffcfc7fc77c7f77e77e77f7e7c7c7f7f7ffcf7e77e7c7f7e77ee7f77e7e7c7fcef7c7f7e7e7c7c7e7f7f7f7e7c7c7f7f7f7f7f7fe7ce7f7f7f7f7f7cf7fcceff7f7ffcffcf7f7f7fcc7f7fcf7f7ff7f7f7f7fcf7fcfcf7f7fccfcf7fffff7ffcffffffffcfcfffff7fff
                fff7ffffcf7ff7fcfff7fcffffcffcfffcffff7ffffffffff7ffffffcfcffcfffffffff7ff7fffffcfffffcfff7ffff7fcffffffcfcffcffcf77f7f77e7f7f7c77ef7e7f7fcfcf7f77ce7f7e7e7f7e7f77e7c7f7ffcf77c7e7c7f7c7f7f7f7c7c7f7f7f7f7c7ec7ec7e7f7f7f7c7f7f7cef7fcf7f7fcfcfcf7f7fcfcfcf7f7fcf7f7f7f7fccfcf7f7f7f7f7f7fcf7f7f7ffffcfffffffcf7ffcffff7ff7fffcf
                7fffcf7ffcfcffcf7ffffffcfffcfff7fffcfffffcf7ffcffffcffcffff7fff7ff7ff7fffffcfcfff7fcfff7ffffcfcfff7fcfcff7fcff7f77f7e7e7f7c77e7ef777f7f7fcf7f7c7e7f77e7f7c77e777c7c7f77f7f7f7f7f7f77c7f77e7c7c7f7e7c7e7f7ef7f7f7f7f7f7cf7f7f7cec7f7c7f7fff7f7f7f7ffcf7f7f7f7fcf7f7fcfcfc7f7f7fcfcf7fc7f7f7f7fcfffcffffcfcf7fffffffffcfffffffffff
                fcf7ffcf7ff7fcf7fc7ffcfff7fff7ffffff7fcffffffff7fcffcff7fffffcfffffffffcf7ffff7fffff7ffffcfcfffcfffff7fcffff7fffc7e7f7f7e7f7f7777fe7cf7ff7ff7c7f7e7c7f77e7f7c7f7e7f77fcfcfc7c7e777f7e77f7f7f7e7c7f7f7f7c7c7f7c7f7c7f7f7c7f7fcf7f7f7f7ffc7ffcffcffcf7fcf7f7fcc7f7fc7f7f7fcf7fc7f7f7f7ffcfcf7fff7f7ffcffffffff7ffcff7fff7ffcffcff7
                ffcfcffcfcfff7fffffcf7ffffcfffffcf7ffffcf7ffcfffffcff7fffcfffffcffcfcfcfffcf7fffcf7fffcfffff7f7ffcf7ffff7fcfffcf7f7f7e7c7f7e7ef7e7f7fcfcfcf7e7f77f7e77c7f77e7f7e7f7ef7f7f7e7f7c7f7e7f7f7e7c7f7f7f7c7c7f7f7f7c7f7cf7ce7f7f7ce7f7f7cf7f7fcfcf7f7f7f7ff7f7fcf7f7fcf7ff7f7f7f7fcfcf7fcfc7f7f7fcfcfffffff7fcf7fffffff7ffffffffffff7ff
                fcff7f7ff7f7ffcf7f7fff7f7ffcffcffffffcfffffff7ffcff7ffffff7fcfff7ffffff7ffffffcffffffffcf7fffffffffffcfcfff7fcffc7e7c7f7e7e7f77fcfcfcf7f7f7c7e7e77c7f7f77ec7f77c77ef7fef7f7c7e7f7e7f7c7c7f7e7c7f7e7f7f7ec7ef7f7f7ef7f7f7cf7f7cc7f7f7cfcf7f7ffcffcf7f7fc7f7fcf7f7f7fcfcfcfcf7f7f6f7f7fcf7f7f7ffcfcfcfffffffcffcfffffcfcffcf7fffff
                cf7ffffcffffcf7ffcfc7ffcfcf7ffff7ffcfff7ffcffffff7fffcfcfffff7ffffcf7ffffcf7fcff7ffcfcfffffcffcf7fcfcf7ff7ffffcff7f7f7ef7f7f7cef7f7f7ffcf77e777c7e77e7e7f7e77ec7fcf7fcf7c7e7f7f7cc7c7f7f7ec7f7f7c7f7cec7f7f7c7f7c7f7cf7f7ec7f7fcf7cfcf7ffcfcf7f7fcfcf7ff7fc7fcfcfcf7f7f7f7fcf7f7fcfcf7fcffcffcffffffcfcfcff7ff7ffcfffff7fffffcf7
                fffcfcff7fcf7ffcff7ffcf7ffffc7fffffff7fffff7ffcffffcfffff7fffffcffffffcfffffffcfffffff7ffcff7ffffffffffcfffcf7fcf7c7ce77f7c7f7f7fffcf7f77f77f7e77f7f7c7f7e7f7f7ef7fcf7c7f7f7c7c7f7f7f7e7f7f7c7e7f7cf7f7f7f7f7f7ef7cf7c7cf7f7fc7f7f7f7ff7f7f7ffcfc7f7fc7fcf7fc7f7f7f7fcffcf7f7fcf7f7f7fcf7f7fff7fcf7ffffff7fffffffffcf7fffffcf7ff
                cfcff7fcff7ffcff7ffcf7ffc7f7ff7f7cc7ffcf7f7fcf7f7f7f7f7f7fcf7f7f7f7fcff7ff7ffcffcf7f7fffff7fffcfcf7fcf7ffcffffffcf7f7f7f7ef7efcfc7f7ff7f7ece7c7e7777e7f7e6f7c7f7fcf7f7f7e7c7f7f7e7c7ecf7c7c7f7f7cf7e7f7cf7c7f7f7cf7c7fc7f7f7cf7f7fcff7ffcfff7f7ff7fc7ff7f7fcfcf7fcfcf7f7f7fcf7f7fcfcfcf7ffff7fffffffcf7ffffffcfcfcffffffcff7ff7f
                f7fcffff7ffcff7ffcf7ffcfffffcffcffff7f7fcffcf7fcfcfcf7fcfc7fcfcfcf7f7c7f7ffcff7ffffffffcfffffffffffffffcff7fcf7ff7f7c7f7c7e7f7f7ffff7c7ce7f7f77f7e7e7f7c7e7f7fcfcf7f7c7f7f7f7e7c7f7f77c7f7f7ce7f7e7f7cf7f7fe7f7f7c7fc7f7f7cf7f7f7fcf7fcf7f7fcff7fcf7fc7fcf7f7f7fc7f7ffcfcf7f7fcf7f7f7fcfcf7ffffcfcffffffcffcffffff7ffcffff7fccf7
                ffff7fcffcff7ffcf7ffcfc7f7fcf7f7f7f7ffcf7f7f7fcf7f7f7fc7ffc7f7f7f7fcff7fcc7f7fc7f7fffcfff7ffcf7fcfcf7fff7fffcffcfc7f7f7ef7fffcffc7f7f7f7f7c7f7f7c7f7c7e7ff7fcf7f7ff7ce7e7c7e7f7f7c7fef7f7cef7f7cf7f7fcf7ce7fc7fecf7f7f7fef7f7fcefc7ffcf7ffcfcf7f7f7fcff7fcf7fcf7ffcf7f7f7ffcf7fcfcfff7f7fffffcffff7fcf7ffffff7ff7ffffffcf7fcf7fc
                fcfffff7ff7ffcff7ffcf7ffffffcffcfcffcf7ffcfcfcf7fcfcfcff7f7fcf7f7fc7f7fcf7fcf7ff7f7c7fcfffffffffffffffcfffcff7fff7f7e7f7c7f7ffcfff7cec7f7f7f7e7f7f7c7f7f7ffcf7ffcf7c7f7f7f7f7c7cef77c7f7f77c7f7f7f7fc7f7f7f7f7c7f7f7fcc7f7f7f7fcfff7fcffcf7f7fcfcfcf7f7f7f7fcf7fc7ffcffcf7f7fcf7f7f7ffcfcffcfff7fffffffff7fffffffffcf7f7fcf7ff7f
                ff7fcf7ffcffcf7fccf7ffcfcf7ff7ff7f7f7ff7f7f7f7ff7f7f7f7f7ff7f7fcf7ff7fc7fcf7f7f7fcff7f767c7cffcf7fcfcfffcff7fffcfc7f7f7f7ffcfff7fcf7f7f7c7f7f7f7e7f7f7cfcf7f7fcf7c7f7c7f7c7c7f7f77f7f7c7ef7f7c7c7fcf7f7c7f7f7fcf7f7f7f7f7fcccf7f7f7ff7f7fcffcf7f7f7fcf7fcff7f7fcff7f7f7f7fcf7f7fcfcfcf7f7ffff7fffcfcfcfcfffcffcffcffffcf7f7f7fcf
                7fff7fffcfcffcfff6f6fcf7fffcffcffcffcfcffcffff7fcfcff7fcf7fcff7fcf7fcf7fc7f7fcfcf7cf7fcccf767f7ffffff7fff7fffcff7fc7f7fefcff7fffff7c7f7fef7cec7fcc7f7ff7fcfcfcf7f7f7f7f7c7f7f7e7f7c7ce7f7c7f7f7ffc7f7cf7f7f7cc7f7cccf7fcf7f7fcffcffcffcf7f7f7f7fcf7f7fcf7f7fcfcf7ffcf7fcfcf7fcfcf7f7fcfff7fcfffffffffffffcfff7fffff7f7fcfcfcfcf7
                ffcfffcfff7f7fcf7ffeffcfcf7fcff7ff7fcf7fcf7f7ffcf7f7ffcf7fcf7fcf7fcf7ff7ffcf7f7f7f7fcf7f7fcfc7f7c77cfffcfffcff7fff7f7ccf7f7fffcfcff7f7f7c7f7f7f7f7fefcfcf7f7f7fc7f7e7f7ef7ec7f7c7cf7f7f7f7f7cffc7f7cf7cf7fccf7f7f7f7f7f7cf7ff7f7f7f7f7fffcfcf7fc7fcfcf7fcfcf7f7ff7f7ffcf7f7fcf7f7ffcf7f7ffffffcfcf7f7fcffff7fffcf7fcf7f7f7f7f7ff
                cffcfcfcfcffffcffcff7ff7fcff7fffcfff7fff7ffcfcf7fffcfcf7fcf7fcf7fc7fc7ff7f7fcfcfcfcf7f7f67c7ff7ffff7f7c7f7ff7fffcfffff7ffffffff7ffffcf7fcf7f7f7f7fcf7f7fcffcff7f7cef7c7f7f7f7c7fc7c7f7c7f7cfef7f7f7f7f7ce7f7f7fcf7fc7fcf7fcfcffcffcffcf7f7f7ffcff7f7f7fcf7f7fffcfcfcf7f7fcfcfffffcf7ffcffcfcfffffffffff7fcffffff7f7f7ffcfcffcf7f
                f7ff7ff7ffcf7ff7ff7ffcff7c6ffcf7fcfcfcfcfcf7f7ffccf7ff7fff7fcf7fcff7ff7fcfcf7f7f7f7fcfcefffc7fc7c7f7f7fcf7f7ffcff7fcfffcfffcfcffffcf7cf7e7f7fcecf7fcfcf7f7f7f7f7f7f7cf7e7c7cef7c7f7f7f7f7f7f7f7f7ce7f7f7fc7f7f7c7f7fcf7f7ff7f7fcf7f7f7ffcfcf7f7f7fcfcf7f7fcfc7f7f7f7fffffff7fcf7ffffcf7fffff7ff7ffcffcfffffcfcf7ffcfcf7f7f7cf7fc
                ffcfffcff7fffcffcffcf7fcff7ffcffff7fff7fffffffcff7ffcffcfcff7ffcf7fcf7fcf7f7fcfcf7f7f7f7f7cfcf7ff7fcfc7f7fcf7c7fcfffcfcfcfffffffcff7f7f7fcf7f7f7ffcf7ffcffcf7cce7f7c7ef7f7f7f7c7f7f7cec7fcff7f7cf7fc7f7f7fc7fcf7fcf7f7fcf7ffcfcf7ffcffcf7f7fcfcfcf7f7ffcf7fcffcfcfcf7fcf7fffffffcf7fffffcf7ffffffff7ffffcfff7f7fc7f7f7fcf6c6cfcf
                cffcfcfcffcfcf7c6cf7ffcfcffcf7fcfcfcfcfcf7fccf7fffcff7ff7fcffcf7fcf7fcf7fcfcf7f7ffcfcf7fcf7f7fcf7fc7f7fcf7f7fcf7f7cff7fff7ff7fff7fff7fcf7f7fcfcfcf7ff7f7f7f7f7f7f7f7f7c7f7f7c7f7f7cef7ffcf7cc7f7ce7f7fecf7fc7f7fc7fcf7f7ffcf7f7ffcf7fcf7fcf7f7f7f7fff7f7ffcf7f7f7f7fffcffcf7f7fffffcfcfffffffcff7ffffcfff7f7fcf7ffcfcfcf7fcf7f7f
                f7ff7fff7fff7fffcf7ffcf7f7fcfff7ff7fcf7f6fcffcfcf7fcffcfff7fcfcff7ff7fcf7f7f7fcf7f7f7ff7f7fcf7f7fef7fcf7f7fc7f7f7f7c7ffcffffffcfffcfc7f7f7fcf7f7f7fcfcfcf7f7f7f7ce7f7f7f7cef7f7f7cf77f7f7f7f7fcef7f7f7c7f7f7fcf7fcf7fcffcf7ffcfcf7ffcf7fcf7fcf6fcfc7fcff7f7fcffcfcf7fff7ffffffcf7fffff7ffcfffffffffcfff7ff7fcf7fc7f7f7f7fcf7ffcf
                cfcffcfffcfffcfc7fcfcf6fcff7f7ff7fff7f6c7c7f7ff7fff7fcf7fcff7ff7ffcff7fcfcfcf7fcfcfffcffffc7fcfcf7fcf7f7fc7fcf7fcf7fc7f7ffcfffff7ffffcf7fcf7ffcfffcf7f7f7f7f7ccf7f7f7cf7f7f7c7f7c7cfcfcff7f7f7c7f7fccf7f7fcf7f7fc7f7f7f7fcf7ff7fcfcf7fcf7ff7f7fcf7ffcf7ffcfcf7f7f7fff7ffcf7fcffffcf7fffffff7ff7ffcfff7ff7fcf7ff7ffcfcfcfcf7fcf7f
                fff7ff7fff7fff7ffcfcf7ffcfcfffcffcfcfcfcfcfffcffcfcfcf7fcf7ffcffcf7fcf7f7f7fcf7f7f7cf7f7f7ff7f7f7f7f7fcf7ff7f7f7f7f7fc7f7cff7fcfffcff7fcf7ffcf7f7f7f7f7f7fccf7f7f7f7f7ec7f7f7f7fef7f7f7f7f7ccf7f7f7f7f7fc7f7fcf7ff7fcfcf7ffcf7ff7f7ff7f7f7fcff7f7fc7f7fcf7f7fcfcff7cfffffffff7fcfffffcfcf7fffffffff7ffccf7fcf7ffcf7ff7f7fcfcf7fc
                f7fffcfcfcfcfcffcf7fffcf7ff7fcf7ff7ff7ff7fcf7f7ff7fcf7ff7ffcf7f7fffcfffcfcf7fcfcfcf7ffcfffcffcf7fcfcf7f7f7fcf7fcef7f7fcf7f7cffffcff7ffffffcf7ffcfcf7f7f7f7f7cf7cecccef7f7ce7f7c7c7fffcf7fccf7f7fc7f7f7f7ff7fc7fc7fcf7ffcfcf7ffcffcfcfcffcfcf7fcff7ffcfcf7fffcf7f7fffffcf7fcfcfff7f7fffffffffcffcf7ffc7f7fcf7ffcffcfcf6fc6f7fcff7
                ffcfcfff7fff7fcffffcf7fffcffcfffcff7ffcffcf7fffcffcf7fcffcf7ffcfcf7f7f7f7fcf7f7f7fcf7f7f7fcf7ffcf7f7fcfcfce7fcef7fcfc7f7f7f7c77fffffffcf7ff7fcf7f7fcfccf7f7f7f7f7f7f7c7fc7fc7fef7fc7f7fc7f7ef7c7fccf7fcf7fcf7fcff7fcf7f7f7ffcf7f7fcf7f7f7f7fcf7fcfcf7f7ffcf7f7fcf7cf7ffffff7ff7fffff7fcf7fffffffffcf7ffcf7ff7fcf7ff7fc7fcffcf7ff
                cfff7f7fff7ffff7f7ffffcf7fcf7f7fcfcfcf7f7fffccf7f7fffcf7f7ff7f7ff7ffcfcff7fcffcff7fcfcfcf7fff7fcfcfcf7f7f7ff7f7f7f7f7fcf7fcf7fc7cf7ffcfffffff7ff7f7f7f7fccf7f7fcf7f7f7f7f7f7f7cffcffc7c7f7f7cf7f7f7fc7f7fc7fcf7f7fcfcfffffcf7ffcff7fcfcfcfcf7ff7f7f7fffcf7ffcfcf7ffffffcfcffcfffcfcfffffffcfcf7f7f7ff7f7ff7fcf7ffcfffffc7f7ffcf7
                fcfcffffcfffcfcfffcf7ffcff7ffffcf7ff7ffffc7ff7ffffc7ff7fff7ffcfcffcff7f7ffcf7f7fcf7f7f7fcf7cffcf7f7f7fcf7fcf7fcfcf7fc7f7f7c7f7fc7f7ffffcf7fcff7fcfcf7f7f7f7fec7f7f7f7f7f7f7fef7f7f7cf7f7cc7f7fcf7fc7fcfcefcf7fcfcf7f7f7f7f7ff7ff7fcf7f7f7f7fcf7fcfcfc7f7ff7f7f7ffc7ffcffff7ffcfcfffcf7ffcffffffcf7fccfcf7fcf7ffcf7fcf7f6f6fcf7ff
                ff7fcfcff7fcfffcfcfffcf7fffcf7ffff7ffcf7fffcffcf7fffcffccffcf7f7f7fcffcfcf7fcff7fcffcff7fff7f7ffffffcf7ff7f7fcf7f7f7ff7fcf7fcf7f7fc7cfffffff7fcc7f7f7fcf7fc7fcf7f7fccf7fcef7cffcff7f7f7f7fc7f7f7f7fcf7f7f7f7fc7f7ffffcfcfffcff7ff7f7fcfcfcf7f7ff7f7fffcfcfcffcfcf7fffff7ffffcfff7ff7fffffcf7f7c7ffcf7fcfcf7ffcf7ffcf7fcc7ff7ffcf
                7ffff7fcffff7f7fff7f7fffcf7fffc7fcfcffcfcf7fcf7ffcf7f7ff7f7fcfffcfcf7ff7f7ff7fcf7f7f7fcf7fcfcf7f7f7f7ff7fcfcf7f7fcfc7fc7f7f7f7f7f7fc777fcf7ffcf7fcf7fc7fc7fcf7f7fc7f7cf7f7fcf7ff7cf7ccf7f7fcf7fccf7f7fcf7fffcff7fcf7fcf7f7f7fcfcfcffcf7f7fcfcfcfcff7f7fcf7f7f7f7ffcfcffffcfff7fffffffcf7ff7fcfff7f7ff7ff7ffcfcff7f7ffcfffcffcf7f
                ffcfffff7fcffffcfcfffcf7fffcf7ffffcf7ff7fffcfffcf7ffffcffcff7f7fcf7ff7ffcfcff7ffcffcfcf7fcf7fcfcfcfffcfcf7f7fcfcf7f7fcfcf7fcef7fcc7fffc7fffcf7ff7f7ffff7ff7f7f7f7fecf7ef7ff7ff7fc7f7f7cf7f7e7f7f7fcfcf7ffccf7fcff7ffcf7ffcffcf7f7f7f7ffcf7f7f7f7f7ffcfcf7fcfcfcf7f7fff7fff7fffffcf7fffffcfcf7f7fcfc7ff7ffcff7f7ffcfcf7f7f7fcf7fc
                fcf7fcfcfff7fcff7fcfcfffcf7fffcf7ffcfcffcf7f7f7fffcf7fc7ff7ffcff7ffcffcf7fc7ff7fcf7f7fcfcf7fcf7f7f7f7ff7ffcf7f7f7fcf7f7f7fcf7fc7f7f77c7f7cfffc7fcfffcffff7fcf7fcf7f7f7f7fcffcfc7f7fc7f7f7cfcf7fcf7f7f7fcf7fff7fcff7f7ffcfcf7fcfcfcfcf7f7ffcfcffcff7fcf7ffcf7f7fcffffcfffcfffcfcffffff7f7f7f7fcf7f7ff7fcfcf7ffcfcf7fcffcfffcf7fff
                cffff7ffcfffff7ffff7f7fcfffcfcfff7ff7fcf7ffffcfcf7fcfcff7ffcfcf7fcf7f7fcffff7ffcf7fff7fcf7ff7ffcfcfcf7ffcf7ffcf7fcf7fcf7fc7f7f7fcf7ff7fcf77ffff7fcf7fcfcfff7fcc7fcf7fcf7ff7f7f7fcf7fcf7fef7f7fc7fcf7ff7fff7fcfcf7ffcfcf7f7ffcf7f7f7fcfcf7f7fc7f7fcfcf7fc7ffffff7f7ffffcfffcffff7ffcf7fcfcf7fcf7fcf7ffcf7fffcf7f7ffcf7f7f7cfcfcf7
                fcf7fff7fcf7fffcf7ffffff7fcf7fcfcfcfff7ffcf7ffcfcffcf7fffcf7f7ffcfcffcf7f7fcfcf7ffc7ffcf7fcff7f7f7f7ffcf7ff7f7ffc7fcf7fcf7fcf7f7f7f7cf7f7fc77ffffffffffffcfff7ff7f7f7f7fcffcf7f7f7f7f7f7f7f7f7ff7f7fcff7fcf7f7fcfcf7f7ffffcf7ffcfcf7f7fcffcfffcfcf7fcfcffffcffffcffcffff7fff7ffff7f7fcf7f7ff7ffcf7fccf7fcf7fcfffc6f7fff6c6ff7fff
                ffcffcffffffcfcfffcfcf7ffcffff7ff7fcfcfcffcfcf7ff7f7ffccf7ffffcf7ff7f7fffcf7fcff7fffcf7ffcf7fcffcffcf7f7fcfcfcf7ff7fcf7f7fc7fcfcf7fcf7f7f7fcf77fcf7fcf7ffffcff7fccf7fcffcf7f7fcf7f7f7fccf7fcfc7fcfcf7fcfcf7fffcf7fffffcc7f7ff7f7f7ffcfcf7f7f7f7f7ffcf7f7fcfff7ffffff7fffffcfffc7fcfcf7fcff7fcf767fcf7ffcfcff7f7f6fcfcf7ff7fffcf7
                fcfcff7fcf7ff7fcfcfffcfcff7f7ffcfff7ff7fcf7ffff7ffffcff7ffcf7fcff7ffcfcf7fffcf7ff7f7fcf7fcfcf7f7f7f7fcffcf7f7fcf7fff7ffcf7ff7f7f7fc7f7fcec7f7fc7fcffffff7ffffffc7f7fcf7f7fcfc7f7fccfc7f7fcf7ffcf7f7ffcf7fffccf7ff7f7f7fffcfcfcffcfcf7f7ffcfcfcfffcf7ffcffff7fffcf7ffffcfcfff7fff7f7f7fcf7fcf7f676cf7fcf7f7fcfffcf7ff7ffcffcf7fff
                ff7fcffff7ffffff7fcf7fff7ffffcff7fffcfff7ffcf7ffcf7ff7ffcf7ffcf7ffcf7ff7fccf7ff7ffcff7ffcf7ffcffcfcfcf7f7ffffcf7fcfcfcf7fcf7fcf7f7fcf7f7f7f7f7f7f7cf7fcfff7fcffffffcf7f7f7f7fcf7f7f7fcfcf7fc7f7fcff7f7ff7f7ff7fcffcfcfc7ff7f7f7f7f7ffcf7f7f7f7f7f7ff7f7ff7ffffffffcffffff7f7f7cfcfcff7f7fcf7f7ccfcffcf7fffcf7fcfffcffcffcf7ffcf7
                fffff7fcfffcf7fffffcfcfcffcfcf7ffcf7fcfcfcf7ffcffcfcffcf7ffcf7ffcf7ffcffcf7ffcffcf7fcfcf7ff7fcf7fcf7fcfcf7f7ff7fff7ff7fff7fcf7fcfcf7fcef7fcf7ccf7f7fcffcfffff7fcf7ff7fcfcf7f7f7fcf7fc7f7fcf7fcf7f7ffffcffcfcffcf7fcf7fff7ffcfcffcff7f7ffcfcfcffcff7ffcffffffcfcf7fff7fc7fcfcff7f7f7f7ffcf7ffcffcf7f7fcfccf7fffcf7ff7ff7ffcfcffff
                cf7fffff7fcfffcf7fcfff7fcff7fffcffcff7ff7fffcff7fff7fcfffcffcfcf7ffcf7fcfff7f7f7fcff7fcff7ffcf7fcf7ff7f7ffcf7ffcfcfcffcf7fc7fc7f7f7f7f7fc7f7fc7f7f7c77fffcffffffffffff7f7fcfcfcf7fcf7fcf7f7ff7ffcfcc7fcf7fcf7f7ffcf7fcf7fcf7f7f7f7ffcfcf7f7f7f7fcfcf7f7fcfffffffffcffcff7f7f7fcfcfcff7f7f676f7f7ffcfcf7f7ffcf7fffcffcff7ff7fcf7f
                fffcf7fcfff7fcfffff7fffff7ffcfff7ffcffcffcf7fcffcf7fff7fcf7ff7fffcf7fff7f7ffffffcf7ffcf7ffcf7ffcf7fcffcfcf7ffcff7ff7fcfcfffcf7fcf7fcf7f7fcf7f7f7fcf7fc77f7ffcfcfcfcfcfffc7f7f7f7fc7ffcf7ffcf7fcf7ffffcf7ff7ffffcf7ffcf7ff7ffcfcfcfcf7f7ffcfffcfcf7fcffffff7ff7fcf7f7f7f7fcfcf7f7f7f7fcffc7c6fcc6cf7f7ffffcf7ffcf7fcf7fcfcffffcfc
                f7ffffffcfcfff7fcfcfcf7fffcff7fffcff7ff7ffcff7fcf7ffcfff7ffcffcf7fffcf7fffccf7f7fffcf7ffcf7ffcf7ffcf7f7f7ffcf7f7fcfff7ff7f7ffcf7fcf7fcfc7f7fcf7f7c7f7ff7fc77f7ffffffffc7ffcf7fcf7ff7f7ff7f7ffcf7fcf7f7ffcffc7f7ffcf7fcfcfcf7f7fcf7fcfff7fcf7fcf7ff7f7fcfcffffff7fcfcfcfcf7f7ffcfcfcf7f7ffc6fe67c7ffffc7f7fffcffcff7fffcff7f7ff7f
                ffcf7fcf7ffcfcffcfff7ffcfcfcffcf7fcffcffcff7fff7ffcfcf7ffcff7ffffcf7fffcf7ff7fffc7f7ffcf7ffcf7ffcf7ffcfffc76fcffcf7fffcffcfcf7fff7fc7f7ff7f7f7fcfefcf7cf7fcf7f7c7ff7ffff7f7fcf7ff7fcfcf7fcfcf7fff7ffcfcf7f7ffff7f7ff7fcf7f7ffcf7ff7fc7ffcf7ff7ff7ffcfffffff7f7fcf7f7f7f7ffcf7f7f7f7ffcfcffeff7c6fc7f7ffffcf7fcf7fcfcf7f7ffffcffc
                fcffffcffcff7ffcf7ffffcfff7fcffffff7ffcf7fcfcfcfcff7fffcff7ffcf7ff7fcf7fcfcffccfffffcf7ffcf7ffcf7ff76c76f7c67f7f7ffc7ff7ff7fffcfcfcfcf7f7fcf7fc7f7f7cf7f7f7f7fcf7c7ffcfffcf7f7fcfcf7f7ffcf7f7fcfcfcf7ff7fffcf7ffcfcff7f7ffcf7fcf7ffcffcf7ffcffcffcfffcf7f7fcfcf7ff7ffcfcf7fcfcffcff7fcf7f7fcf6cffffcffcfcf7ff7fffcf7ffffcf7fcf7f
                ff7fcff7ff7ffcffffcf7ff7fffff7f7fcffcffffff7fff7fcffcf7f7ffcff7fcffffcff7ff7ff7f7f7fcffcf7ffcf7ffcfc6c6effcf6cfffcfff7ff7ffcf7fcf7ff7fcfcf7fc7fcf7f7f7f7f7f7f7c7ffc7f7fcf7ffcfcf7fcfcf7f7ffcffcf7f7ffcffcf7fcfcf7f7fcfffcf7ff7fcfcf7f7fff7fc7f7f7f7f7fcfcf7f7f7f7ff7f7f7fcf7f7f7f7ffcffffff7fff7f7ffcf7ffffcffcf7fffcf7ffcff7ffc
                fcfff7fffcffcf7f7ffffcffcf7fffffff7ff7f7f7ffcf7fff7ff7fffcff7ffff7fcf7fffcff7ffffcff7f7fffcf7ffcf7ffefff7fcfef7f7f7f7fcfcfcfcff7ffcfff7f7fc7c67cf7fccf7fccfccf7f7cf7f7f7ffcf7f7fcf7f7ffcf7ff7f7ffffcf7f7fcff7fcffcf7f7f7f7fcff7f7f7fff7fcfcffffcfcfcf7f7f7fcfcfcfcfcfcff7f7fffcfcfcff7f7fcffcfcfffcffcfcf7ff7ffcfcf7fffcf7fffcff
                7fcfcffcffcffffffcf7ffcffffcf7fcfcfcffffffcffffcfcfcffcfcf7ffcf7fffcffcf7f7ffcf7ff7ffffc7f7ffcf7ff7ff7fcfcf7fcfcfcfcfcf7f7ff7fffcf7f7fffcf7fc6c76f7f76c7f7f7f7fcf7fcf7fc7f7f7ff7f7fff7fcff7ffffc7f7fffcff7fcff7f7fcfcfcfcfcf7ffcffcf7fcf7ff7f7f7f7f7ffcfcfcf7f7f7f7f7f7ffcfc7f7ffcf7ffcff7fcf7fcf7f7fff7ffcffcf7ffffc7ffcfcf7fcf
                fff7fcff7ff7fcf7ffffcff7f7ffffcf7fff7fcfcff7cfcfcff7fcf7fffcf7ffcf7fcf7ffffcffffcffcf7fffffcf7ffcff7ff7fcf7f6f7fcf7fcf7fff7ffcf7ffcffcf7ffcf7fccfcf7cccf7fcf7fc7fc7f7f7fc7f7fc7fcf7cfcf7fcfcc7fffff7f7fcffcf7ffcf7f7fcf7f7fcf7fc7f7ffcfcf7fcfcfcfcff7f7f7f7ffcfcfcfcfcf7fcfffcfcf7ffcff7fffffff7ffffc7ffcf7fcf7ff7f7ffcf7ffcff7f
                cfffff7ffcfff7fff7fcf7ffffcf7ffffcfffff7fcf6c7ff7fffffffcf7fffcffcff7ffcfcff7fcf7fcfcfcf7fcfffcf7fcfcffcf7fcc7cf7ffcf7fccfcfcf7fcf7f7fffcf7ffcf7f7fcf7f7fc7fcf7f7fcf7fcf7fcf7fcf7fcf7f7fcf7fffcf7fcfcff7f7ffcf7fcfff7fcffcf7ffcffcfcf7f7fcf7f7f7f7f7fcfcfcf7f7fcf7fcf7ffcf7f7fcf7fcff7ffcf7f7fcfcf7fffcf7fff7fffcfffcffcfcff7fff
                f7fcfcffcfcffffcffffffcfcffcfcf7ff7fcfcfffff7f6ffcf7f7fcfcfcf7fcf7fffcff7fcffcffff7ff7fffcf7f7fffcf7fcf7ffcfff6ff7f7ffcf7f7f7fffcf7ffccf7ffcf7fcf7c7cf7fcfc7f7fcf7f7fc7fcf7fcf7fc7f7fcf7f7fc7f7ff7ff7fcfff7f7ff7f7fcfcf7f7ff7f7f7f7f7ffcf7ff7ffcff7fcf7f7fcfcfcf7ff7ffcff7ffcf7fffcf7ffcfffcffcf7ffcf7fffcfcffcffcfcf7ff7f7ffcf7
                fff7ffcff7fcf7ffcf7fcff7fcff7fffcfffcff7f7fffffcffffffff7ff7fff7ffcf7fcfff7fcf7f7ffcffc7ffcfffcf7fffcf7fcf7f7fcf7fffcf7ffcfffccf7ff7f7fffcf7ffcf76c667cf7f767cf7fcfcf7fc7fcf7fc7ffcf7f7fcf7ffcf7fccfcf7f7ffcfcffcf7f7f7ffcf7fcfcfcfcf7cf7fcfcf7f7ffcf7ffcf7fcf7ff7ffcf7fffcf7ffc7f7ffcff7fcf7f7ffcf7ffcf7fcf7ff7ff7fffcffffcffcf
                fcffcff7ffffffcffcfff7ffff7ffcfcfcf7f7ffffcf7fcf7f7fcf7ffcf6ccffcffcff7fcfff7ffffcff7fffcf7fcf7ffcf7fffcfffcff7ffcf7fcfcf7f7f7f7fcfcff7f7fffcf7ffc67cf6fcfcccf7fc7f7fcff7f7fc7ff7f7fcfcf7ff7f7fcf7f7f7fcf7f7f7f7fcfcf76b7f7ff7f7f7f7f67cfcf7f7fcf7f7ffcf7ff7f7fcffcf7ff7f7fffcfffffcff7ffcfcfffcf7ffcf7fff7ffcffcffcfcf7fcff7ff7
                ffcff7fffcf7fcf7ff7fffcf7ffcff7ff7fffffcfcffffcfffffcf6cffcf76fcf7ff7fff7f7ffcfcff7ffcfcffff7fffcfcfcf7f7f7fcffcf7ffcf7fcfcfcfffcf7f7fcfcf7ffffc7ffcfcf7f7f7ffcf7fcf7f7fcfcf7fcfcfcf7f7fcf7fcf7f7fcfcfcf7fcfcfcf7f7f76b6fcfcfcffcfcfcf6f7f7ffcf7ffcfcf7ff7ffcfcf7f7ff7ffcfc7f7f7f7fcfcfcff7fcf7fffcffcfcfcfcff7ffcff7ffffcf7ffcf
                fcf7fffcffcfffffcffcfcfffcff7ffcfffcfcff7fcf7ffcfcf7ffc7fcff6c7fffcffcfcfffcff7f7ffcff7f7f7ffcfcf7ff7ffffffcf7f7ffcf7ff7fcf7fc7f7ffcfcf7f7fc7f7ff7fcf7fcf7ff7fffcf7fcfcf7f7ff7f7f7f7fcf7f7fcf7fcfcf7f7f7fcf7f7f7ffcffcfcf7f7f7f7f7fcf7feffcf7fffcf7f7ff7ffcf7ff7ffcfcfcfcffffcffcff7ff7f7ffcf7fcf7f7ff7fcf7fcffcff7ffcf7ffffcff7
                fffffcff7ff7f7fcfcff7fcfcf7fffcfcfcfcf7ffffffcff7fffcfff7f7fffc6f7fcf7ff7fcf7ffffcff7ffffffcff7fffcffcf7fcf7ffffcf7ffcffcf7ffffcfc7f7fcfcfcffcf7fcf7fcf7ff7fcf7ff7fcf7f7fcf7fcfcf7ff7fcfcfcf7fcf7f7fcfcfcf7ffcff7f7f7fcf7ffcffcf7676fcfcf7fcfc7f7ffcfcfcf7fcf7ffcf7f7fcf7f7f7fcf7fffcffffcf7fffcffffcfff7fffcf7fcffcffcfc7f6f7ff
                cf7fcf7ffcffffff7fcffff7ffffcff7ff7ffffcf7f7ff7ffcfcf7fffffcfcfffff7ffcffcfffcf7ff7ffcfcf7ff7ffcf7fcf7ffcfffcf7fcffcf7f7fffc7f7fcfffcf7f7f7f7fcfcfcff7ff7fcf7ffcfff7fcfcf7fcf7f7ff7fcf7f7f7ffcf7ffcf7f7f7ff7fc7fcffcfcf7fcf7f7f76bccf7f7ff7ffffcfcf7f7fcfcf7ffcf7ffcff7ffcfcff7ffcf7f7fcf7ffcf7fcf7ff7fcfcf7fffff7ff7ff7ffccffcf
                fffffffcf7fcfcfcfff7fcffcfcff7ffcffcf7ffffffcfffcf7fffcc6ffcff7fcfffcff7ff7fcfcfcffcf7fcffcffcfffff7ffcff7fcfcff7f7fffcfc7fffcfcf7f7fcfffcfcf7f7f7fcffcfcfcfcf7fcfcf7f7f7fcf7fcf7fcf7ff7ffcf7f7fcf7ffcfcf7f676cf7f7f7f7ff7ffcfcfcff7ffcfcffc7f7fcf7fffcf7fffcf7ffcf7fcfcf7ff7ffcffcfffcfcfcffcff7ffcffcff7ffcf7fffcffcffcfcf7ff7
                f7fcf7fcff6ff7ff7fffff7ff7fcffcff7ffffcf7fcff7fcfffcf7ff7c6f7fffc7fcf7ffcffcf7ff7fcffff7fcf7ff7f7fcffcf7fff7ff7ffffc7ff7ffc7fcf7ffcfcf7cf7ffcfcffff7fcf7ff7ffcff7ffffcfcfcf7fcf7fcfcf7ffc7f7fffcf7fcf7f7ffc7cf7cfcffcffcff7f7ff7fcffcf7ff7ffffff7ffccf7ff7f7fffcf7ffcf7fff7ffcff7ff7fcf7fff7ff7ffcf7fcf7ffcffffcf7fcf7fcf7fffcff
                fffcfff7fcfcffcffcf7fcffcfff7ffcffcf7ffcffcfcfff7fcfffcff6f7fcfcf6cfffcff7ffffcfff7f7fcff7ffcffffcfcf7ffcfcfcffcf7fffcffcfffcf7fcf7f7ff7ff7f7ff7c7fff7ffcffcf7fffc7fcf7f7f7ff7ffcf7fffc7ffcfc7f7ffcf7ffcf7ffcffcf7f7f7f7fcfcfcffcf7f7ffcff7f7f7ffcff7ff7ffcfcf7fff7ff7f67cfcf7fcf7f6c7ffc7ffcffcffffcfffcff7f7ffcff7fcf6ffcfcfcf
                cfcf7fcfcfcf7ffcffcfff7ffcfcffcf7ffffcff7ff7fcfcff7f7ff7ffccfcffff767ff7ffcf7ff7fcfffcf7ffcff7fcff7fffcff7ff7fcfcfcf7f7fc7f7fcff7ffff7ffcfcffcffffc7ffcff7ff7ff7fffcffffcff7ff7f7ff7f7ffcf7fffcfcf7ffcf7ffcff7f7ffffcffcf7ff7f7ff7fffcf7fcffcffcf7fcf7ffcfcf7ffc7ffcffc7c667fffcffccf6c6ffcf7fcf7f7ff7f7fcffffcff7fffcfcfff7fff7
                ff7fffffcffffcff7ffcfcffcf7fcffffcf7ff7ffcfff7ff7ffffcffcfff7fc7fcffccffcffcfcffff7fcfffcff7ffcf7ffcf7fcffcfff7ffcffffffffff7fcffc7fcfcf7ff7f7f7fcffcff7ffcffcffcf7f7f7ff7fcfcfcf7fcfcfcfffcf7ff7ffcf7ffcfcf7fffcf7ff7ff7fcffcf7ffcf7fffcf7ff7fcff7fffcf7ff7fcfffcf7f7fc6cc6fcf7fcf7fc7fcf7ffffffffcfffff7fcfcf7fffcfcf7f7fff7ff
                cfffcf7ff7f7ff7ffcf7ffcffffff7f7ffffcffcff7fffcffcf7c6fcf7fcffffffcfff7ff7ff7fcf7fffcf7ff7ffcffcfcf7fff7fcf7fcfcf7f7fccf7f7ffcf7fffcf7fcf7ffcfffcf7f7f7ffcf7ffcf7ffcfcfcffcf7f7fcfcf7fcf7f7fffcffcf7ffcff7fffcfcfcfcffcffcf7f7ffcf7ffc7f7ff7ffcf7ffc7fcff7fffcf7ff7fffcfffefcf7ff7ffcfff7ffcf7f7fcff7fcfcfff7fffcfcff7fffffcfcf6
                fcfcfffcffffcfffcfffcff7f7f7ffffcf7ff7ff7ffcf7fcfffcfcffffcfcf7f7ff7fffcffcffffcfcf7fffcffcff7ff7fffcfcff7ffcf7fffffcf7ffffcff7fcf7fff7ffcf7fc7ffcfffcfcf7ffcf7ffcf7ff7fcf7ffcff7f7ffcf7ffcf7f7fcfffcff7ffc7fcf7f7ff7ff7ff7fffcf7ffcfffffcffcf7ffcfffcf7ffcf7fffcffcf7fcf7ff7ffcffcff7fcfcffcfffcf7fffcff7fffcfcfff7ffcc6cfff6fc
                fff7fcff7fcf6f7ff7fff7ffffffcfcffcffcffffcffffff7fcf7f7f7ff7fffffcffcf7fcff7fcf7ffffcf7fcff7ffcffcf7fcf7ffcf7ffcf7fcfffcf7ff7fffcff7fcfcf7ffcff7f7fcff7fcfcffffcf7ffcfff7ffcf7fcfffcf7ffcf7ffcff7f7ff7ffcfffcf7fff7ffcff7ffccf7ffcf7f7f7f7fcf7fcf7f7f7ffcf7ffcf7fcffcf6fcfcf6ccf7ff7ffcff7fcfcfcfffcfcf7ffcfcff7f7fffcfcfcf7ffff
                7fffff7fffff7fcfffcf7ffcf7fff7fcff7ffcf7ffcf7fcfff7ffffffcffcf7fcf7c6ffff7fffcffcf7ffcff7fcfcff7ffcff7ffcffcfcf7ffcf7f7fffcffcf7f7ffcf7fffcf7fcfffcf7fff7ff7f7f7ffcf7f7ffcffff7fc7f7ffcf7ffcf7fcfcf7ffcf7f7f7ffc7ffcf7f7cf7ff7fcf7ffcfcfffcf7ffcffcfffcf7ffcffcfff7ff7c76f7c7c6cfcffcf7fcfff7ff7fcfff7ffcff7fcfffffcff7fffffcf7f
                fcf7fffcf7ffffccfcfffcffcfcfcfff7ffcffffcfffff7fcffcfcf7ff7ffcffcfcfcf7fcfcf7fcffcfcff7ffffcf7ffcf7fffcff7ff7fffcff7fffcf7fcf7ffffcf7ffc7f7ffcf7f7fcfcfcfcfcffffcf7ffcfcff7f7ffcffffcf7ff7f7ffcf7ffcf7fffcfffcfffcf7ffc6c6fcffcfcfcf7ff7fcf7ffcf7ff7fcf7ffcf7ff7fcfcf6cc6cfff6ff7fcf7ffff7fffcffff7fffcff7ffff7fcfcf7fff7fcffffc
                ffffcfcfffcfcfff7fcf7fcffff7ff7ffcff7f7ff7f7fffff7ff7fffcffcff7ff7ff7ffcfffcfff7fff7fffcf7ffcfcf7ffcf7fcff7ffcf7f7ffcfcfcff7fffcfcfffcfffffcf7ffcff7f7ff7ff7f7fcf7fcff7fcffcfcf7f7f7fff7ffcfcf7ff7ff7fcf7fcf7f7f7fcfcffffcf7fcf7ff7ffcffcf7fcf7ff7ffcf7ffcfffcfffcf7f7c6c7fcfcfcff7ffcf7ffcfcf7fcffcf7fcfffcfcfff7ffffcffff7f7ff
                7fcff7fcfcf7fcffff7ffff7f7ffcffcff7ffffcffffcf7fcfcffcf7fcff7ffcffcffcff7f7fcf7fcf7ff7ffcfcf7ffffcf7fff7fcfcffcfffcff7fff7ffcfcf7f7fcf7f7fcf7fcf7fcfff7ffcffcfcf7ffc7fff7f7ff7fffcffc7ffcff7fffcff7fff7ffcf7ffcffcf7f7f7f7ffcf7fcffcf7f7ffffcffcffcf7ffcff7fcf7fcffffcf7fff7ff7fcffcffcffcff7ffff7ffffff7fcf7fcfcffcfcfcf7ffffcf
                fff7ffff7fffff7f7fffcfcfffcffcff7fffcfcfcfcffffffff7fffffcf7ffcfcff7ff7fffffcffffcfcffcff7fffc7fcfffcfcffcff7ff7fcf7ffcf7ffcfcfffffcffcffcf7ffcffcf7fcfcff7ff7fffcfffccffcfcffc7ff7fffcff7ffc7f7fcfccffcf7ffcf7fcf7fffcfffcf7fff7f7fffcfc7fcf7ff7fcffcff7ffcffff7f7fcfffcfcfcffcf7ff7ffcf7fffcf7ffcf7fcfffcffff7fcf7f6ffcfcfcffc
                f7ffcf7fffcf7ffffcfcff7fcff7ff7fffcfcf7ff7fcf7fcf7fff7fcf7fffcff7fffcffcf7fcf7fcf7ffcff7ffcf7fff7f7ff7fcf7fcfcffcfffcff7ffcff7f7fcf7f7fcf7ffcf7fcf7ffcf7fcf7ffc7fcf7ff7f7fcf7fffcff7f7f7ffcfffffcf7ff7f7ffcf7fff7ffcf7fcf7fffcfcfffc7ff7fff7ffcffcf7ff7ffcf7f7fcfffcf7fcffff7ff7ffcffcf7ffcf7fffcff7ffcf7ff7fcfff7fcfcf7fff7fcf7
                ffcffffcfcfffcfcff7fcffff7ffcfffcff7fffcffff7fffcffcffcfffcfcf7ffcf7fcffcff7fff7ffcf7fcfcf7ffcfffffcfff7fff7ff7ff7fcf7fffcf7ffffcffffff7ffcf7fff7ffcf7ffcfcfcfffcf7fcffffcf7fcf7f7ffcfffcf7f7f7ff7fcffcfcf7ffcf7fcf7ffcf7fcf7f7fcf7ffcffcfcfcf7f7fff7ffcf7ffffcfcf7fffff7f7ffcfffcfcffffcf7ffcfcf7ffcff7ffcffcf7ffcfcfffcfffffff
                fcfcf7fff7fcff7fcffff7fcfffcfcf7fcffcf7fcf7fffcff7ffcff7fcff7ffffcfff7f7fcffcfcffcffff7ffffcff7fccf7fcffcfcfcffcffcf7ffcfcffcf7ff7f7fcffcf7ffcfcfcf7ffcf7ff7f7f7fffcf7f7f7fff7ffcfcfcf7fcffffffcfffcf7ff7ffcf7fffcffcf7fffcfffff7ffcff7ff7fffcfffc7ffcf7ffcf7ff7fffcf7fcfffcff7fcff7f7fcfffcff7fffcff7fffcfcf7ffcffcf7fcf7fcf7fc
                ff7fffcfcfff7ffff7fcffff7fcff7ffff7ffffffcffcff7ffcff7ffff7fffcf7fcfcfffff7ff7fcff7f7ffcf7ff7ffcfffff7fcf7fff7ff7ff7ffcf7fcffcfcffffcf7ffffcfcf7ffcfcf7ff7ffffcfc7f7ffffcfcfcfcf7ff7fcfcf7fccf7fcf7fff7ffcf7ffcf7fcf7ffcf7fcf7fcfcff7ffcffcf7fcf7ffcf7ffcf7ffcffcf7fffff7fcf7ffff7fffff7f7ff7ffcf7fcffcfcf7fffcffcf7fffffff7fff7
                """))
            tilemaps = [tilemap("""
                    level4
                    """),
                tilemap("""
                    level4
                    """),
                tilemap("""
                    level4
                    """),
                tilemap("""
                    level4
                    """)]
            col = 16
            row = 112
            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
            if selectedIndex5 == 0:
                load_p = 100 / 32
                for index43 in range(4):
                    tiles.set_current_tilemap(tilemaps[world])
                    world_gen()
                    world += 1
                makeplayer()
            elif selectedIndex5 == 1:
                load_p = 100 / 48
                for index44 in range(2):
                    tilemaps.append(tilemap("""
                        level4
                        """))
                for index45 in range(6):
                    tiles.set_current_tilemap(tilemaps[world])
                    world_gen()
                    world += 1
                makeplayer()
            elif selectedIndex5 == 2:
                load_p = 100 / 64
                for index46 in range(4):
                    tilemaps.append(tilemap("""
                        level4
                        """))
                for index47 in range(8):
                    tiles.set_current_tilemap(tilemaps[world])
                    world_gen()
                    world += 1
                makeplayer()
            elif selectedIndex5 == 3:
                secnum = game.ask_for_number("how many sections do you want", 2)
                if game.ask("you want " + ("" + str(secnum) + "sections")):
                    load_p = 100 / (8 * secnum)
                    tilemaps = []
                    for index48 in range(secnum):
                        tilemaps.append(tilemap("""
                            level4
                            """))
                    for index49 in range(secnum):
                        tiles.set_current_tilemap(tilemaps[world])
                        world_gen()
                        world += 1
                    makeplayer()
        myMenu2.on_button_pressed(controller.A, on_button_pressed7)
        
myMenu2.on_button_pressed(controller.A, on_button_pressed6)

@namespace
class userconfig:
    ARCADE_SCREEN_WIDTH = 320
    ARCADE_SCREEN_HEIGHT = 240

def on_update_interval():
    if world_gen_done == 1:
        if player1.y <= 2000:
            for value14 in tiles.get_tiles_by_type(assets.tile("""
                myTile32
                """)):
                if tiles.tile_at_location_equals(value14.get_neighboring_location(CollisionDirection.TOP),
                    assets.tile("""
                        transparency16
                        """)):
                    tiles.set_tile_at(value14.get_neighboring_location(CollisionDirection.TOP).get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            transparency16
                            """))
game.on_update_interval(2000, on_update_interval)

def on_forever():
    characterAnimations.loop_frames(player1,
        [img("""
                . . . . . . . c c . . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f b b b b b b f . . . .
                . . . e e f e e e e f . . . . .
                . . . e b b e b b 5 f . . . . .
                . . . e b b e 5 5 5 5 f . . . .
                . . . . e e 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f e e b b b b f . . . .
                . . . f e b b e e e f . . . . .
                . . . . e b b e b b 5 f . . . .
                . . . . f e e 5 5 5 5 c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . c c . . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f b b b b b b f . . . .
                . . . e e f e e e e f . . . . .
                . . . e b b e b b 5 f . . . . .
                . . . e b b e 5 5 5 5 f . . . .
                . . . . e e 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f b b b b b b f . . . .
                . . e b b e e e e e f . . . . .
                . . e b b e b b b 5 5 f . . . .
                . . . e e e 5 5 5 5 5 c . . . .
                . . . . . f f f f f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT))
    characterAnimations.loop_frames(player1,
        [img("""
                . . . . . . . c c c . . . . . .
                . . . . . . c b 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b b b f f . . .
                . . . e e f e e e e f e e . . .
                . . e b c b 5 b b 5 b f b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . c c . . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b e e e f . . .
                . . e b b f e e e e b b e . . .
                . . e e f 5 5 b b e b b e . . .
                . . . f 5 5 5 5 5 e e c . . . .
                . . . . f f f f f f f . . . . .
                """),
            img("""
                . . . . . . c c c . . . . . . .
                . . . . . . c 5 b c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b b b f f . . .
                . . . e e f e e e e f e e . . .
                . . e b f b 5 b b 5 b c b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f e e e b b b b f f . . .
                . . . e b b e e e e f b b e . .
                . . . e b b e b b 5 5 f e e . .
                . . . . c e e 5 5 5 5 5 f . . .
                . . . . . f f f f f f f . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_UP))
    characterAnimations.loop_frames(player1,
        [img("""
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b b b f f . . .
                . . . . . f e e e e f e e . . .
                . . . . . f 5 b b e b b e . . .
                . . . . f 5 5 5 5 e b b e . . .
                . . . . c b 5 5 5 5 e e . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c c 5 c . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b e e f f . . .
                . . . . . f e e e b b e f . . .
                . . . . f 5 b b e b b e . . . .
                . . . . c 5 5 5 5 e e f . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b b b f f . . .
                . . . . . f e e e e f e e . . .
                . . . . . f 5 b b e b b e . . .
                . . . . f 5 5 5 5 e b b e . . .
                . . . . c b 5 5 5 5 e e . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c c 5 c . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b b b f f . . .
                . . . . . f e e e e e b b e . .
                . . . . f 5 5 b b b e b b e . .
                . . . . c 5 5 5 5 5 e e e . . .
                . . . . . f f f f f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT))
forever(on_forever)

def on_forever2():
    if world_gen_done == 1:
        if player1.tilemap_location().y >= 1010:
            if lighting == 1:
                shadowcasting.set_anchor(player1)
                shadowcasting.set_shadow_enabled(True)
            elif lighting == 0:
                shadowcasting.set_shadow_enabled(False)
        else:
            shadowcasting.set_shadow_enabled(False)
forever(on_forever2)

def on_forever3():
    if world_gen_done == 1:
        player1.say_text(world)
forever(on_forever3)

def on_forever4():
    global nextspot
    if world_gen_done == 1:
        if controller.up.is_pressed():
            nextspot = player1.tilemap_location().get_neighboring_location(CollisionDirection.TOP)
            select.set_position(nextspot.x, nextspot.y)
        if controller.right.is_pressed():
            nextspot = player1.tilemap_location().get_neighboring_location(CollisionDirection.RIGHT)
            select.set_position(nextspot.x, nextspot.y)
        if controller.down.is_pressed():
            nextspot = player1.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM)
            select.set_position(nextspot.x, nextspot.y)
        if controller.left.is_pressed():
            nextspot = player1.tilemap_location().get_neighboring_location(CollisionDirection.LEFT)
            select.set_position(nextspot.x, nextspot.y)
forever(on_forever4)

def on_forever5():
    if world_gen_done == 1:
        if player1.y >= 2000:
            scene.set_background_image(img("""
                ffcfffcfffcfffcfffcfffcfffcffcffcffcffcffcffcfcffcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcc8cccfccfcfcfcfcfcfcfcfcfcfcfcfcfccfcfcfcfcfcffcffcffcffcfcfcfcfcfcfcfcfcffcffcffcffcfcffcfcfcffcfcffcffcffcffcfcfcffcffcfcffcffcffcfcfcffcfffffffffffffffffffffffffffffffffffffcfffcfffcfcffcfcffcffcffcffffffffffffffffffffffcffc
                fcffcffcfcffcffcfcffcffcfcffcfcffcffcffcffcffcfcfcffcffcfcfcf8fc8fc8fcfcfcfcffcffcffcffcffc8f8fcf8cf8cf8cf8cfcfcfcfcfcfcfc8fc8fcfcfcfcfcffcffcffcffcffcfcfcfcffcffcfffcffcfffcffcfffcfcffffcffffcffcffcffcfcffcfcffcffcfcffcffcffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfcfcfffcfffcffcfcfcffcffcffcffcfcfcfcfcfcfcfcfcfcfcfffcf
                ffcffcffffcffcffffcffcffffcffffcffcffcffcfcfcfffcfcfcfcfcf8fcfcfccfcfcfcfcffcfcfcfcfcfcfcfcfcc8c8cfccfcfccfcf8fcf8fcf8fc8fcffcfcf8fcf8ffcffcffcffcffcfcfcffcfcfcfcfcfcffcffcffcffcfcfffcfcffcfcffcffcffcffcfcfffcfcfcfffcfcfcffcffcffcfffcfffffffffffffffffffffffffffffffffffcffcfffcfcfcffcffcfcfcfcffffffffffffffcfffffcffcfff
                cffcffcfcffcffcfcffcffcfcffcfcfcfcfcfcfcfcffcfcffcffcfcf8fccf8cf8fcfcfcfcfcfcffcffcfcfcfcf8c8cfcfc8f8cf8fcfcfcfcfcf8fcfcfcfcfcfcfcfcfcfcfcffcffcffcfcfcfcfcfcfcfcfffcffcfcffcffcffcfcfcfcfcffcfcffcffcffcffffcfcffcffccffcfffcffcffcfcfcffcfcffcfcfcfcfcfcfcfcfcffcffcfeffcfffcffcfcffcfccfcfcffcffcfcfcffcffefcfcfffcfcfffffcfc
                ffcffcfffcffcffffcffcffffcffcffffffcffcfffcffcfcffcfcfcfcfcfcfcfcfccfcfcfcfcfcfcfcfcfcfcfcccf6c8cfccfc8fcf8cfccfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffcffcffcfcfcffcfffcfcfcfffcfcfcffcffcfcfffffcffffcffcffcffcfcfcfcfcfcfffcffcfcfcffcffcfffcfcffffffffffffffffffffffffeffffffffcfffffffcffcfcfcfcfcfcffcffffffefffffffcfffffcfcffff
                cffcffcfcffcffcfcffcffcfcfcffcfcfcffcffcfcfcffcfcfcfcfcfccf8cf8cf6f8fcfcffcffcfcfcfcffcfcf8c8cfcf6f8cfccfcfcf8fcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffcffcfcfcffcffcfcfcfffcfcfffffcffcffffcfcfcfcfcffcffcffcffcfffcffcffccfcfcfcfffcfcfcfcfcfffcfcfcfeffcfefcfefcfefcfffffcffcfffefcfcfffcfcfcffcfcffcfcffcfcfffffcfcffffcfcfffffcff
                fcffcffffcffcffcffcffcfffffcffcfcfcffcffcfcfcffcfcfcfcf8fcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf6cfc8c8cccf6cfc8cfcfcfcf8fcfcfcf8fcf8fcf8fcfcfcfcffcfcfcfcfcfcfcfcfcfcfcffcfcfffcfcfcfcffcfcffcfcfffffcfffcfcffcffcfcfcffcfffcfcfcfcfcfffcffcffcfcfcffffffcffffffffffffffcfffffffefffffffcfcffcffcfcffcffcfcfffffcfcfffffcfcffffcfcffcf
                cffcffcfcffcffcffcffcfcfcfcfcffffffcffcffcffcfcffcffcfcfcf6fcfcfcfcfcfcfcfffcffcfcfcfcf8cf8c8fcf8f8cf8cfcf6f6fccfcf8fccfcfcfcfccfcfcfcf8fcfcfcfffcfcfcfcfcfcfcffcfcfffcfcffcffffcffcfcffffcfcfcffcffffcffcffcffcfcfccfcffcfffcfcfcfcffcffffffcfcfffffcfcfcfcfcfcffffefcfefffcfcfcffffcfcfcffcfcfcffcffcfcffffffcffffffcfffffffff
                fcffcffcffcffcffcffcffffcffcfcfcfcffcffcffcffcfcfcfcfcfcfcfcfcf6fcccfcfcfcfcfcfcffcfcfcfc8cccc8cccf6fcf6fcfccf8fccfccf8fccfcf6fcfcfcffcfcf8fffcfcffcfcfcfcfcffcffcffcffcfcffcfcffcffffcfcffcfffcffcfcffcffcffcfcfcfffcfcfcfcfcffcffcfcfcfcfcffcfcfcffffffffffffffeffffffffcffffcffcfffcfffcffcfcfcffcfffffcffcfffcfcfffcfcfcfcfc
                ffcffcffcffcffcffcffcfcffcffffcffcfcfcfcfcfcfcffcfcfcf6fcfcfccfcf8ffcfcfffcffcffcfcfcf8c8cf8f6f6f6cfc8cf8ccf8cfcf8cf6fccfcf6fcf8fcfcfcfcfcfcfcfffcfcfcfcfcfcfcfcffcffcffffcffffcffcfcfcffcffcfcffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffffcffffffcfcfcfcfcfcfcfffcffcffffffcffcffefffcfcfcfcffcfcfffcfcfffeffcffffefffffffffff
                cffcffcffcffcffcffcffffcffcfcffcfffffcffcfcfcfcfcfcfcfcfcf8fcfccfcfcfcfcfcfcffcfcfcfcfccfc8ccc8ccf8ccfccfcfcfcf6fcfcfcfcf6fcfcfccfcfcfcfcfcfcfcfcffcfcfcfcfcfcfcfcfcffcfcffcfcffcffcfffcffcffcfcffcffcfcfcfcfcffcfcfcffcffcffcfcffcffcffcfcffcfcfcfffffffffffcfffcffffffcffcffcfffffcfcfffffcfcffcfcffffffcffffffcfffcfcfcfefcff
                cfcfcffcffcffcfffcffcfcfcffcfcffcfcfcfcffcfffcfcfcfcfcfcfcfcfcf8fcfcffcfffcfcfcfcfcf8cf68cf6f8fc8cf8f6f8cf8cf6fcf8cf6f8cfcfcf8cfcfcfcffcfcfcfffcfcfcfcfcfcfcfcffcfffcfcffcffffcffcffcfcfcffcffffcffcffcffcffcfcffcfcfcffcffcffcfcffcfcfcfffcffffffcfcfcfcfcfffcffffcfcfffffffffcfcfffffcfcfcfcfcffffcfcfcfffcfcfffcfffffffffffcf
                fcfffcffcffcffcfffcffcfffcfffcfcffcffcfcffccffcffcfcfcfcfcfcfcfcfcfcfcfcfcffcffcfcfcfc8fcc8cccccfc8ccfccfcfcfcc8cfcfccfcfcfcfcfcf6fcfcffcfcfcfcfffcfcfcfcfcfcfcfcfcfcffcffcfcffcffcffcfffcffcfcffcffcffcffcfcffcfcffcfcfcfcfcffcfcfcfcfcf6fffcfcfffffffffffcfcfcfcfffffefcfcfcffffcfcfcfcfffcffcf6ffffffffcfffffcffcfcfcfcfcffff
                cfcfcfcffcffcffcfcffcfcfcfcfcfffcffcffcfcfff6ffcfcfcfcfcfcfcfccfcfcfcffcffcffcfcfcfc8cf6f8fcccc8ccfcf6f8cccccfcfcf6f8fccf8fcfcf8fcfcfcfcfcfcfcfcfcfcfcfcfcffcfcffcfffcffcffcfcffcffcffcfcfcffcfcffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffcffcffffffcfcfcfcfcffffcfffffefffffffffcfcffffffcfcfcfcfcffcfcfcfcfffcfcfffffffffffffcfcf
                ffcffcfcffcfffcfffcffffcfffcfcfcfcff7ffcf6fcfcfcfcfcfcfcfcffcfcf6fcffcffcffcfcfcfcfcf8cc8cc8f8fccc8f6ccf8fcf8fccfcfccf8fcfcf6fccfcfcfcfcfcfcfffcfcfcfcffcfcfcff6ffcfcfcffcffcfcff7ffcffcfffcffcfcffcffcfcfcfcfcfcfcfcffcffcfcfcffcf6fcfcfcfcfcfcffffffcfffcfcffcfcffffcffcffeffcfcfcfcfffcffcfcfcfffffffffcfffffcfefcfcfefcffffc
                fcfcffffcffcfffcfffcfcffcfcfffcfff7ffcffcffcffcfcfcfcfcfcfcfcf6fcfcfcfcffcfcffcfcf6f6f8fcf6f6cc8f6fcf8fcccfcccf8cf8fccfccf6fcf8fccfcfcffcfcfcfcffcfcfcfcfcfcfcfcfcfffffcffcfcff7ffcffcffcfcf7ffcfcfcfcffcffcfcfcfcfcfcfcfcfcffcfcfcffcffcfcffffffcfcfffcfcfffcffffcfcfffffcfffffffffffcfcfcffcfffcfcfcfcfffcfcfffffffffffffcfcff
                ffffcfcffcffcfffcffcffcffcfcfcfcffffcfcffcffcfcfcfcfcfcfcfcfcfcfcfcffcfcfcffcfcf6fccccf6c8ccf8cc8cc8cc8f8f6fcfcfccf6f8cf8fcf8cfcfcfcfcfcfcfcfcfcff6fcfcfcfcfcfcfcfcfcfcfcffcfcffcffcffcff7fffcffcfcfcfcff6ffcfcfcfcfcfcfcfcfcfcfcffcfcf6fcfcfcfcffffcfffffcfffccfcffffcfcfffcfcfcfcfcffffcfcff6fcfffffffcfffffcfcfcfcfcfcffffffc
                fccffcfcffcffcfffcffcffcfffcffffcfcffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfffcfcf6fcf8f8f8fcfc8cfccf8cf8fc8ccf8ccccf8cfcfcfcfccfcf6fcfcfcfcfcfcffcfcfcfcfcfcffcfcfcfcfffcfffcfcffcffcffcff7fffcffcffcffcff6ffcfcffcfcffcffcffcffcffcfcfcfcffcffcffffcffffcfcffcfffcffcfffffffcffffcfffcffcfcfcfcffffcffcfcffcfcfffffffffffffcfcfcff
                cffcffffcffcffcfcfcffcffcfcfcf7ffffcfcfcffcfcfcfcfcfcfcfcffcfcfccfcfcffcfcfcfcfcfcccfccc8cfc8cc8cc8cc8cf6f6fcf8fcfccf8fccf8fcfcfcf8fcfcfcf6fcffcfcfcfcfcfcfcfcfcffcfcfcfcffcf6fcffcffcfffcffcfcfcfcff6ffcfcffcfcffcffcffcffcfcfcfcfcfcfcfcfcfcffffcfcffffcffcfcfcfffcfcffcffcfffcfcffcfffcfcfcfcffcfffffffffcfcfcfcfcfcfffffffff
                fcffcfcffcffcffffffcffcffcffffffcfcffcffcfcfcffcfcfcf6fffcfccf6fcfccfcfcfcff6fcc8f8f8cfcf8cfccfccf6f6f6cfcc8fcccccf8fccf6fcf6fc8fcfcfffcffcfcfcfcfcfcfcfcfcffcfcfcfcfffcfcffffffcffcffcfcfcffcffcfcfcfcfcffcfcffcfcf6fcfcfcfcfcffcfcffcfcfcfcfcfcfffffcffffffffffcfcffffffcffcffcfffcffcff6fffcfcfffcfcfcfcffffffffffffefcfcfcfc
                ffcffffcffcfffcfcfcffcfcffcf7fcffffcffcfcfcff6fcfcf6ffcfcffcf6fcfcfcfcfcfcfcf6fcfcccf8cfcf8ccc8f6c8cc8fc8cfc8f8fcfcccf6fcfcfcfcfcfcfcfcfcfccfcfcfcfcfcfcfcfcfcfcfcffcfcfff7fcfcffcffcffffffcffcffcfcffcffcfcff6fcfcffcfcfcfcffcfcfcfcfcffcffcfffffcfcfffcfcfcfcffffffcfcffffcffcfcfffcffcffcfcfffcffffffffffcfcfcfcfcfffffffffff
                cffcfcffcffcfcffcffcfffcfcfffffcfcffcfcffcfcfcfcfcfcfcfcfcf6fcfcf8fcf6ffcfcf6cf8ccf8cfc8ccf6f8ccfccf8cc8f8c8ccf6f6fcf6fcf8cf8cfccfcfcfcffcfcffcffcffcfcfcfcfcfcf6fcffcfcfcfffcfcffcffcfcfcfcfcfcfcff6ffcffcfcfcffcfcffcffcffcfcfcffcf6fcfcfcfcfcffffffcfffffffffcfcffffffcfffcfffcfcfffffcfcffcfffcfcfcfcfcffffffffffcffcffcffcf
                fcffcfcffcffffcffcffcfcfffcfcfcffcfcfffcfcfcffcf6fcfcfcffcfccfcfcfccfcfcfcf6cfcf8fcf6fcf8f6fccf8c8c8cf8cccfcf6cfc8cf6fcfcfcfcfcf8f6fcffcffcf6ffcffcfcffcffcfcfcfcffcffcfffcfffffcffcffcfcffcffcfcfcffcffcffcfcfcfcffcffcff6fcffcfcfcffcfcfcfcfcfcfcfcfffcfcffcfffffcfcfcffcfffcffcffcfcfcfff6ffcffffffffffffcfcfcfcfffcfffffcfff
                cfcffffcffcfcffcfffcfffcfcfcfcfcffcfcf7ffcfcf6fcfcfcfcfcffcf6f8cf6fcfcfcfcfc6f8cfc8cf8ccf6c8f8ccfcfc8ccf8c8c8f8c8fc8cf8c8f6fccfccfcfcfcfcfcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcffcfcffcffcffcfcffcfcffcfcffcffcffcffcff6fcfcf6ffcfcffcfcfcfcffcffcfcffffffcffffffffcfcfffffffffffcffcfcfffffffcfcfcffcfcfcfcfcfcffffffffcffffcfcfffcf
                fffcfcffcffcfcffcfffcfcfcffcffcfcffcfffcffcfcfcfcfcfcffcfccfcfcfcfcfcfcfcf6cfcfcfcfccf8f6fcfccc8c8cfc8c8cf6f6ccfcccfcccfcfcf8f6fcfcfcffffcfcfcfcfcffcfcfcfcffcfcfcffcfffffcffcfcfcfcfcffcfcfcffcfcfcfcfcff6ffcfcfcffcfcffcfffcfcffcfcff6fcfcfcf6fcfcffcfcfcfcfffffcfcfcfcfcfffffcfcfcfcfcfffcfcfffffffffffffcfcfcffffcffffffcfff
                cfcfffcffcffffcffcfcfffcfcffcffcfcffcfcfcf6fcfcfcfcfcfcffcc6fccc8cf6fccfcf6c8fccf8fc8ccfc8c8cf8fcf6ccfcf6cfccf8c8f6c8f8c8c8cfcfcfccfcfcfcfcfcfffffcfcffcfcfcf6fcfcfcfcfcfcfcfcfcffcfcfcffcfff6ffcf6fcfcfcffcfcffcfcffcfcfcfcffcfcffcfcffcfcffcffcfffcfffffffffcfcfffffffffffcfcfcf6ffffffcffcf6fcfcfcfcfcfcfffffffcfffcfcfffffcf
                fcfcfcfcffcfcffcffcfcfcfffcfcfcffcfcfcfcfcfcfcfcfcfcfcfcffcfcfcfccfcf8fcf6cfcf8fcfcfcf8cfcfc8cfcccf8c8c8c8c8c8cf6cf8cccccfcccf8fcfcfcffcff6fcfccfcfcfcfcfcfcffcfcfcfffcffcffcffcfcffcff6ffccffcffcfcf6ffcfcffcfcfcfcfcffcfcfcffcfcffcfcffcfcffcfcfcfffcfcffcffffffcfcfcfcfcffffff6ffcfcfffcffcfcfffffffffffcfcfcfffcffffffcfcfff
                cfffffffcffcfcffcffcfffcfcfffcfcffcfffcfcffcfcfcffcfcfcfcf6cccf6f8cfcfcf6c8fcfcf8fc8fccc8c8fcc8f6f6cf6cf8cf6fc8cc8cf8f8f68cc8cccccfcfcffcfcf8ffcfcfcfcfcfcf6fcfcfcfcfcfcffcffcff6fcff6ffcfffcffcffcfcfcffcfcffcffcfcffcfcffcfcffcfcffcfcfffcfcfcfcfcfcfffffffcfcffffffffffffcfcfcfcffffcfcfcfcffcfcf7fcfcffffffffcfffcfcffffffcf
                fcfcfcfcfcffffcff7ffcfcfffcfcfff7ffcfcffcfcfcfcfcfcffcffcfccf8cfcfc8cfcf6cfc8fcfccfccf8fcfc8f8fc8cf8c8c8c8c8c8cccf8ccc6ccf8fc8f6f8cfcfcfcfcfccffcffcffcfcfcfcfcfcffcffffcfcfcf6fffcfcfcffcfcfcff7ffcfffcffcfcff6ffcfcfcffcfcfcf6ffcfcfffcfcffcffcfcfcfcfcfcffffffcfcffcfcfcffffffcfcfcffcffffcfcfffcfffffcfcfcfcfffffffffcfcfffc
                ffffcfffffcfcffcffcffcfcfffffcfcffcffcfcfcffcffcffcfcfcf6f6fcfc8f6fcfcc8c8fcfcf8fcf8fcf6f8cc8ccfc8ccfcf6cc8c8cf68c8c8f8f8c68c8c8c8ccfcffcfc6fcfcfcffcfcfcfcfcfcfcfcfcfcfcfcfcffcfcffcffcfcffcfcffcffcfcfcffcfcffcfcfcfcf6fcffcffcffcfcfcfffcffcffcfcfffffffcfcfcfffffcfffffcfcfcffcfffcffcf7ffcffcffcfcffffffffffcfcffcfffffcfff
                cfcffcfcfcfffcffcffcffffcfcfcfffcffcff7fffcffcffcffcffcfcfc8f6fcfcccff6cfcfcf8fcf8cfcfcf6cf8fcc8fcf8cc8f8fccf68cc8ccc8cc8ccf8cc8ccf6ffcffcfccfcfcfcfcfcfcf6fccfcfcfcfcfcfcfcfcfcffcffcfcffcffcfcffcfcffcfcffcfcfcffcfcfffcfcffcfcfcffcffcfcfcffcffcf6fcfcffffffffcfcfffcfcffcfffcfcfcffcffffcffcffcfcfcfcfcfcfcfffffffffcfcfffcf
                fffcffcfffcfffcffcffcfcffffffcfffcffcffcfcfcfcfcfcffcfcfccfccfcfc8cf6c8ccfcfcfcfcfcf6f8cf8cccf8fcccf8fcfcccc8cf8cc8f6f6cf8c8cf8fc8cfcfcfcfccf6fcf6fcffcfcfcfcf6fcfcfffcfffcffcffcffcfcffcfcf7ffcfcfcfcffff7ffcffcfcffcfcfcff6fcffcfcff6ffcfffcff6ffcfcffffcfcfcfffffcfffffcffcfcfffcfcffcfcffcffcfffffffffffffffcffcffcfffffcfff
                cfcfcffcfcfcfcfcffcffffcfcf7ffcfcfcffcffffcfffcfcfcfcfcff6ffcff6cccf8c6f8fcfcfccfcfcfcf8ccf8f6ccf8f6fc8cf8ffc8c8c8c8cc8c8c8fc8ccfc8fcffcfcf6cfcf6cfcfcfcfcf6fcfcf6fccffcf7fcffcfcfcfff6ffcfffcffcfffcfcf7fffcfcffcfcfcfcffcffcfcffcf6ffcffcfcfcffcffcfcfcfffffffcfcffcfcfcffcfffcfcfffcff7fcffcffcfcfcfcffcffcffffffffffffcfffcf
                fffffcffffffffffcffcfcfffffffcfffffcffcfcffcfcffcfcffcf6ffcfcfc886f6c6fcfcf8fcf8fccf8fccf8cc8fcccfcccfccfcc8fcc8c8c8c8c8c8c6ccf6cfccfcfcffcf8cfcf8cfcfcf6fcfc8fccfcffcfcffffcffcfffcfcfcffcfcfcffcfcfffcffcfffcfcffcffcfcfcfcffcfcfffcffcffcfffcfcfcfcf6fcffcfcffffcffffffcffcfcfffcfcfcffffcffcffffffffffffcffcfcfcffcfffffffff
                cfcfcfcfcfcfcf7ffcffcfcfcfcfffcfcfcfcffcfcffcfcffcfcfcffcfcff6cc8c6c8fcfccfcfcfcf8fcfcf8cf8cc8f8f6f8f6f6ccfccf8cc6c8c8c8c6c8868c8c8fcfcfcfc6f8fc8c8fcfcfcf6fcfccfcf6fcffcfcffcffcfcfcffcfcfcfcfcfcffcfcfcfcfcffcfcfcf6fcfcfcfcffcfcfcfcffcffcfcffcffcfcfcfcffffcfcffcfcfcffffcffcfcf6fffcfcffcffcfcfcfcfcfcfffffffffffffcffcffcf
                fcfffffffffcfffcffcffffffffcfffcffffcfcfffcffcfcffcf6fcfcffcfc8cf68fcf8fcfcfcfcfcfcfccfcf6fccc8ccfcfcf8f8f6f8fcfcf8ccc8c8c8c8c8c8cc6fcfffcfc8ccfccfcfcf6fcc8c8f8cfcfcfcffcfcff7ffcfffcffcfcffcffcfcfcfcffcfcfcfcfcfcffcfcfcfcfcfcfcffcfcffcffcfcffcfffcfcfcfcfffffcffffffcfcffcffcfcfcfcffcfcfcfffffffffffffcfcffcffcfffffcfffff
                cfcfcfcfcfcfcfffcffcfcfcfcffcfcfcf7ffffcfcfcfffcf6fcfcfcfcfc6cc86cfcfcfcf8fcf8fcf8f8fcf6fc8cf6f8c8c8cccfc8ccccf6fcf8f6f6c8c86c8c86f8cfcfcf6c8fcf8c8fcffcf8fcfccfccfcfcfcffcfcffcffcf6fcfcff6ffcffcfcfcfcfcffcfcfcfcfcfcffcffcfcffcfcffcfcff6ffcfcff6fcff6fcffcfcfcffcfcfffffcffcffcfcfffcffffffcf7ffcfcffcffffffffffffcfcfffcffc
                fffffcfffffffcfcfcffffffffcffffffffcfcffffff7fcfffccfcffcfcfccfccffcffcfcfcfcfcfcfccf8fccfc8c8c8cc8cf8c8cf8f6f6cf8cc6c8c8c8c8c8cf8ccfcfcfcf6ccfcf6cffcfc8cc8cf6f8f6fcffcfcfcfcfcfcffffcff6ffcfcfcfffcfcfcfcfcfcffcfcfcfcf6fcffcf6ffcfcffcfcfcffcfcffcfcffcf6ffffcfcffffcfcfcffcfcff6fcf6fcfcfcfffffcfffcffffcffcffcfffffffffffff
                cfcfcfcfcfcfcfffffcfcf7fcffcfcfcfcffcfcf7fcffffcfc6ffcfcfcc6f8cf8fcfcfcffcfcfcfccf8fcfcf8cfccf6c8f6c8c8cc6c8c8c8cc8cf8c8fc8c8fc8ccc8fcffcf6c8fcf8c8fcfcfc8fc8cfccfc8fcffcfcfcfcfcfcfcfcfcfcfcffcfcf6fffcffcfcff6fcff6fcfcfcf6fcffcfcff6ffcfffcff6fcffffcfcfcfcfcfffcfcffffffcffff6ffcfcfffcfffcfcfffcffffcffffffffffcffcffcfffcf
                fffffffffffffcfcfcfffffffcffffcffcfcfffffffcfcff6cfccfcff6cccfcfcfcfcffcfcffcfcf8fcfccfcf8cf8c8f6c8c8cc8f8cccfc8ccc8c8cc8cf8c8cfcf8fcfcfcf8c8fcfc8cfcfc8cccfcc8cc8fcfcfcffcffcf6fcffcff6fcfcfcffcfcfcfcfcffcfcffcfcffcfcffcfcfcfcfcfcffcffcfcf6fffcfccffcf6ffcffcfcfffcfcf7fffcfcfcf6ffcfffcfcffcfcffcfcfffcffcfcfcfffffffffcfff
                cfcfcfcfcf7fcffcffcfcfcfffcfcffcffffcfcfcfcfffcfccffcff6c8fcf8fcfcfcfcfcfcfcfcfcfcfcf8fcfcf6fcc8c8c8c8c6c8c868c8c8f6c8c8c8c8cf6c8cf6fcfcf6c8fc8f8ccfcffccf6fcfcf8fc8cfcfcff6fcfcfcfcfcfcfcffcfcfcffcfcfcfcffcfcffcfcfcfcf6ffcfcfcfcfcfcfcfcfcffcfcfcffcffcfcfcf6fff6fcffcfffcffcfcfcfcffcfcfffcffffcffcfcfffffffffffcfcfcfffffcf
                fcffcffcfffffcffcffffffcfcfffcffcfcffcffcfffcfcc6f6ffcccfcf8fcfcfcffcffcfcfcfcfcfcf8fcf8fcfc8ffcfcf8c8c8c86cc8c8c6c8f8cf6c8f6c8fc8cc8f6fcc8ccfcf68fcfccf6cf6f6f6fccfcfcff6ffcfcfcfcffcfcfcf6fcfcf6fcfcfcfcf6fcfcfcff6fcfcfcffcfcfcfcfcfcffcffcfcfcffcfcf6fcfcfcfccffcf6fcfcffcfffcfcfcfcfffcfffcfcffcffcfcfcfcfcffcffffffffcfffc
                ffcffcffcfcfcfcffcfcfcffffcfcfcfffcfcfcffcfcfcf6fccf6f6f8fcfcffcffcffcfcffcfcfcfcfcfcfcfccfcfc8f8c8ccc8c8cf8cccf8c8c8c8c8fc8cfc8cf6fccffcf8c8cfc8cfcffcf8c8c8c8fc8f6fcf6ffcfcfcf6ffcffcf6fcffcfcfcfcf6fcf6ffcf6f6fccfcf6fcfcfcffcfcffcffcfcf6fcfcfcfcffcffcff6fcffcfcfcf6fcfcffcff6f6f6ffcffcfffcfcffcff6fffffffcffffcffcffffcff
                cffcffcffcfffcfcfffcffcfcffffffcfcfffffcfffff6c8cfcfc8fcfcfffcffcfcfcfcfcfcfcfcfcfcfcfcfcf8fcfcfcfcf8cccc8c8f8c8cc8cc8c8c8cf8c8f68c8c8fcf6cfcf6f68cfcffcf8cc8fcc8fcfcfcfcfcfcf6fcfcfcf6fcfcfcfcfcfcfcfcfcfcffcfcfcfcfcfcfcf6fcf6ffcf6fcfcffcffcffcfcfcffcfcfcfcf6ffffffcf6ffcfcffcffcfccffcfffcffffcffcffcfcfcffffcfffffffcfcffc
                fcffcffcffcfcfffcfcfcffffcfcfcffff6cf7ffcfcfcf6c8cfcfcf8fcfcfcfcfcfcffffcfcfcfcf8fcfcfcfcfcfcf8cf8ccf8f6f6f6c8f6f8fccfcfcf6c8cc8c8c8cfcf8c88c8f8ccfcfccc8cf8cc8cfc8cfcfcfcffcfcfccfcfcfcfcfcfcf6fcf6fccfcfcfcfffcffcffcfcfcfcf6fccfcffcff6ffcffcfcffcf6fcfcfcffcfcfcfcfffcfcfffcffcfffcfcfffcffcfcffcffcfcffffcfcfffcfcfcffffcff
                ffcffcff7ffcfcfcfffffcfcffffcfcfcffcffcffffefc8ccc8fc8fcfcfcffcffcffcfcffcfcfcfcfcfcfcfcfcfcfcfccff8fccf8c8cf6cf8cc8f6f8c8f8c8c8c8c8c8ccc8c8ccc868cfcffcfccf6c8c8cfccf6fcfcfcfccfcffcfcfcfcfcfcfcfcfcfcf6ffcfcfcfcffcffcfcfcfcfcf6f6fcf6ffcfcfcfcfcfcffcffcfcfcfffcfffcffcfcfcffffffcffcfcfffcffffcffcffcfcfcfffffcfffffffcfffcf
                cffcff7ffcffcfffcf7fcffcfcfcffffcf6fcffcfcff6f68cfcfcfcfcfcfcffcffcfcffcffcfcfcfcfcfcfcfcffcfcff8fcfcf8cfcf8cf8cfccfcfcfcc8cf6c8c6868ccf86c8c8f6c8fcfccc8f6cf8fcf6cf8fcffcffcf6fcfcfcf6fcfcfcfcfcfcfcfcffcffcfcfffcffcffffcffcffcfcfccfcccf6fcfcfcffcfcfcfcfcffcfcfcfcffcfcfcfcfcfcfffffcfcfffcfcffcff6ffcffffcfffffcffcffffcfff
                f7ffcffcffcffcfcfffffcffcfffcfcffccffcffffcff6c8fcf8fcfcfcffcfcfcfcffcffcfcffcffcffcfcfcfcfcffcfcfcfcfcfcfcfcfcf8cc8fcfcf8f6c88c88c8c88cf8686c8c8c8ffcfcc8f8cc8c8c8cfcf6fcfcfcfcfcfcf6cfcfcfcfcfcfcfcffcfcfcfffcfcfcffcf6ffcffcfcffcffcffcfcf6f6fcf6ffcffcfcf6fcffcfcfcffff6fcfcfcffcfcffcfcfffffcffcffcffcfcffffcfffffffcffffcf
                cffcfcffcfcfcfcfcfcfcfcffcfcfffcff6cffcfcffcfc6fcfccf8ffcfcffcfffcfcffcffcfcfcfcfcfcffcfcfcfcfcfcfccfcfcf8cf8cf6f8fc8fcfccc8c8c868686c8c8c8c86868cfcff8f6ccf8fcfcfc8cfccfcfcfccf8fcfc8cfcfcffcffcffcfcfcffcfcfcfcffcf6fcfcfcfcfcfcffcfcf6fcfcfcfcfcfcffcfcfcfcffcfcfcffcfcffcfcfcfcfffffffcfcfcfffcffcfcfcfffffcfffcfcfffffcffff
                fcffcfcfcfcffcfffcfcffcfcfffcfcf6fcfcffcfcff6fcfcf8fcfcfcffcffcfcfffcffcfffcf8fcffcfcfcffcfcfcfcf6fcfcfcfcfcfc8cfc8cc8cfcf8c8c8686a868c8cc6868a8c8cfcfcc88fccf8c8c8cf8f8fcfcf8fccfcfc8fcfcfcfcfcfcfcfcffcffcffcffcfcffcfffffcffcffcfcffcfffcfffcfcfcfcfcffcfcfcf6fcff6ffffcffcfffcfcfcfcfffcffffcfffcfcfcfcfcffffffffffcffffffcf
                cfcffcfcffcfcfcfcfffcffcfcfcfffffc6ffcffffcffc8f8fcfcfcffcfcfffcfcfcfcffcfcfcfcfcffcfcfcfcfcf6fcffcf8fcf6f8f6fcf8cc8ccf8fcf6c688c868a68cf868a686a68cfcf8c868fcfccfc8cfcccffccfcf8cfcc8fcf8fcfcfcfcfcfcfcfcffcffcf6ff6ffccf6ffcffcfcffcffcfcfcfcfffcffcff6ffcfcfcfcfcffcfcffcff6fcfcffffffcfffcfffcfffffffffffffcfcfcfcfffcffffff
                cffcffcfcffcfffcfcfcfcffffcfcfcfcfccfcfcfcfcffcfcf6fcffcf8ffcfcfffcfffcffcffcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcf8c8cf8c8c8fcc8c886a68a686a8c8c68a68686cf8f68cc8cf8c8ccf6fcf8fcf8cccfcff6cfccfcfcfcffcffcfcfcfcfcf6fcfcfcfcffcfcffcfcff6ffcfcffcfcfcfcfcff6ffcffcfffcfcfcfffffff6fffffcf6ffcfffcfffcfffcfcf6fcffcffffffffffffffcffcf
                f6fcfcffcfcfcfcffcffcfc6fcffffcff6fcffcfffffcffcfccf8fcfcfcffffcfcfcfcfcffcfccfcfcfcfcffcfcfcff8fcfcfcfcfc8fcfcf8ccf6cfcfcf6c868a68a868c8c68686a6a88fcf6c86cfcf6c8c8cf8cfcfcf8fcccfcc8fcfcfcfffcffcfcfcffcfcfcffcfcfcfcf6fcf6fcff6ffcfcffcffffffcfffcffcffcffcfcffcffcfcfcfcfcfcfffcfcfffffffcffffffffffffffffffcfffcfcffcfffffc
                ffcfcfcfcffcfffcffcffffcfcf6fffcfcf8fcfcfcfcfcffcf8cfcfcffcfcfcfffffcfffcfffcfcffcfcfcfcffcffcfcfcfcfcfcfcfc8cf6fc8c8c8f6fc8c8c88c868a68c88a8a86868cfcf88688cf88c8cf8cf6cfcf6cf8f8cf8cf8fcfcfcfcfcfcfcfcffcfcfcfcffcffcffcf6fcc6ffcfcffcffcf6fcffcfcfcffcff6ffcfcffcffcffffffcffcffffffcffcfffcffcfcfcfcffcfcfffffffffffffffffff
                cfcffcfcfcffcfcfcfcf6c6cf6ffcfcffcfcfcfcffcfffcf8cfcffcfcffcfffcf6fcfcfcfcf6fcfcfcf8fcf8fcfcfcffffcffcff8fcfcfcc8fcfcfccfcf6c8cc88c8888c8c8686888a68fcf6a8a8cfc68c8cccf8fcfc8fccfcfcccfcfcfcffcffcfcfcfcfcffcf6cf6fcf6fcfcffcfcfcfcffcffcfcffffcffffffcffcffcffffcfcfcffcf6fcfcffcfcfcffcfffffffffffffffffffffcffcffcfcfcffcffcf
                cffcfcffcfcffcffcfcfcfcfcfcffffcf6fcf8ffcffcfcfcfc8fcfcffcffcfcffcffcfcffcffcfcfcfcfcfcfcfcfcfcfcffcffcfcffcf6ffcf8f68f8cfc8cf8cf8c8c8c8c868a88c888ccfc88668c8c888c88fcf6fcfc8f8c8cf6f6f8fcfcffcfcff6fcfcfcffcfcfcccfcfcfcfcfcf6fcfcfcfcfffcfcffcfcf6fffcffcfcfcffffffcffcfffffcfffffffcffcffcf7ffffcfcfcffcffffffffffffffffffff
                f6fcffcffcfcff7ffcfcf6fcfcfcfcffcfcfcfcfcfcffcff6fcfcffccfcfcffcfcfcfcfcffcfcffcfcf8fcf8fcf8fcfcf6ffccfcfcf8cf8cfcfcfc8cfcf68c8c8c8c8c8c8c8c8c8c8c8cf8f6a8a68f86868cc8c8cf8c8c8fcfcf8cfcfcfcfcfcffcfcfcffffcfcfcfcf6fcf6fcfcf6fcc6ccffcfcfcfffcfffffffcffcffffffcfcfcffcffcfcfcfcf6ffffffffffffffffffffffffffcfffffffcfcffcffcfc
                ffcfcfcfcfff6ffcfcffcffcfcfcffcffcfcf8fcfcfcfcfcfccfcfcfcfcffcfcfcfcffcfcffcfcfcfcfcf8fcf8fcfcf8fcfcf8fcffcf8cff8f8c8fcccfc8fcf8fcf8c8c8c8c8c8c8c8c8cfc86888cfc8a8c88fcf6cffc8fc8f6c8c8cf8fcfcffcfcfc8ccfcfcf6ffcfcfcfcfcfcfcfcff86f6ffcfff6fffcfcfcfffffffcfcfcfffffcffcffcffff6ffcfcfcffcfcfcfcfffcffcfcfcfffcffcfffffffffffff
                cffcfcffcfcffcfcff6ffcfcfcffcffcf6f8fcfcffffcfcf6f8fcfcf8ffcffcfcfcfcfcffcff6ffcfcf8fcfcfcfcf8fccf8ffcfcfcfcfcfcfcfcf8f8f8f6cf8c8f8cf8f8c8f8c8c8cf8c8c8688a6cf86868c8cf8cfc8c8cf6c8f8cfcfccf8fcfcfcfcf8fcfcfcfcfcfcfcfcfcf8fcfcfc8c6fcff6fcfcfcffffffcfcfcffffffcfcfcfcffcffcfcfffcfffffffffffffffffffffffffffffffffffcfcfcffcff
                cfcfffcffcfcfcfcfcfcfcfcfcfcfcffcfcfcf6fcfcffcfcfcffcfcfccffcfcfcfcf8fcfcfcfcfcf8fcfcf6fcfcfcfcf8ffcfccf8ffc6f8f8fcfccccfcc6fccf8cf8cfc8f8c8fc888cf8f8c8a8888c8a8c8c8c8c8ffc8f8cf8c8cf8f8f6fccfcfcf6f6cfffcf6fcfcfcfcfcf8fcfcfcfcc8cfcfcfcfcfcfcfcfcfffffffcffcffffcfffcff6ffcfcfcffcfcffcfffcfcfcfffffcffcfcffffcffcfffffffffff
                cffcfcfcff6fcfcfcfcfcfcfcfcfcffcfcfccfcffcfcfcfcfcfcfcfcfcfffcfcf8fcfcfcffcfcf8fcfccfcf8fcfcfcfcfcffcf8fcfcf8cfcfcf8fcf8cffc8f8cc8cf8c8c8c8c8fc8c8c8c8f68c88cc8688c88cfcfc8f6c8f8cfc8cfccfc8f8cfcfcfc8c8cfcfc8f6fcfcfcfcfcfcfcf6fcf6fcffffcfcfcfcffffcfcfcfffffcf6ffcfffcffcfcffcffcfcfcfffffffffffcffffffffffcfffffffffcfcfcfcf
                fcfcffcf6ffcfcfcfcfcfcfcfcfcfcffcf6f8fcfcffcfcfcfcf8ffcfcfcfcfcfcfcfcfcfcff6fcfcf8fccfcfcf8fcf8c8cfcfccfcffc8cfcf8fcf8fcf6f8fcf8fc8c8c8f888cf8c868c8fc88a86868c88c8c888cf8f68c8cf8cf8c8f8fcfcf6ffcf6f8cffcf6fc8fcfcfcfcfcfcfcfcff6c8fcfcfcfffcf6fcfcffffcffcfcffffcffcfcffcf6fcff6ffffcffcfcffcfcfcffcffcffcffffffcfffcfffffffff
                cfff6ffcfcfcfcfcfcfcfcfcfcfcffcffcfcfcfcfcfcfcfcfcfcfcfcfcffcfcfcf8fccfcfcffcfcfcfcf8f8f8fcf8fcffcff8f8cfcf8cf8fcfcfcfccfcfccc8c8f8c8c8c8c88cf888c8c8cc86888a868a88f8c8cfcc8c8cf8cf8fc8ccf8f8c8fcfcf8c8cfcfc8cc8fcfcfcfcf6fcfcfcff8ccfcfffcfcffcfffffcfcfcfffffcfcfcffcfcffcfcfcfcfcfffcffffffffcffffffffffffcfcffffcffffcfcffcf
                f6fcfcfcfcfcfcfcfcfcfcfcfcf6fffccfcfcf8fcff6ffcfcfcfcfcfcfcffcf6fcfcf8fcfcfcf8f8fccfccfcfcfcfcfc8fcfcfcfcfcf6cfcf8fcfcf6fcf8fcfcc8c8c868c868c8c68c88f886a6a8688688c88688cff868c8fcfc8668cfcc8ccfcfcfc88cffcc8f8fcfcfcfcf6fcfcffcfcc8fcfcfcfffcffccfcffffcffcffcfffffcffffcfffcff6fcffcffcf6fcfcffcfcffcffcfffffffcffffffffffcfff
                cfcfcfcffcffcfcfcfcfcfcfcfcfcfcfccf6fcfcfcfcf6ffcffcffcfcffcfcffcfcfcfcfcffcfccfcf8fcfccf8fcfcf8fcfcf8cfcfcf8f8fcfcf6fcf8fcf8c8f8f68c688688c8f86a8c8c8c888886a6a868c8a8cf8c8c8cfc8f66868c8ffc8cfcf8f8c8fcff8c8c8c8fcfcfcc8fcfcfcf8cccfffffcfcfcfffcffcfcfcfffcfcfcfcfcfcffcfffcffcfcffffffcfcffcffffcffffffcfffffffffcffcfffffcf
                fcfffcfcfcf6ffcfcff6ffcfcfcfffffcfcfcfcfcffcfcfcfcfcfcfcfcffcf6fcf8f6fccfcfcfcf8fcfcf8f8fcf8f8fcfcffcf8fcff8ccfcfccfcf8cfcfccfc8c8c88c8c8a88c8c68c868c8686a886868a888888cfc8688cfc8c68c8cfc8f68fcfcfc8cfcfc8cf6c8fcfffc8c6cfcfcfcf68f6cfcfcffcfcfcfcfffcf6ffcfffffcfffffcffcfcfcffcccfcffcffccffcfcffffcfffffcffcffcfffffffcfffc
                ffccffcfcfcfcfcff6ffcfcfcfccfcfcf6fcfcfcfcfcfcfcfcfcfcfcffcfcfcf8fcfcf8fcffcfcfccf8cfcfccfcfcfcf8cfcfcfcfcfcf8fccfcfcfcf8fccc8cf6f8c686a6868cf8688c68688a886a868688c86c8f8f8668f8f8c88c868fcf8c8fcf8cf8cfcf68c8cc8cccfcc8c8cfcfcf6c8cffcfcfcffcfcfffcff6ffcfffcfcffcf6fffcfffffcfffcfcffffcfff6ffffcffffffcfffffffffffcffffffcff
                cffcf6ffcffcfcfcffcfcffcfcfcfffccfcf8fcfcfcf6fcfcfcfcfcfcfcfcfcfcfcf8cfcfcfcf6f8fcfccf8fccfcfcfcfcfcf8cfcfcfcfcf8fcf8f8ccff8fc8c8c8c8c886a88c88a8c66a6888688866a688c888cfcc86a6cc8c868a8ccfc8c6cffcf8c8cf8cf8c88cf8fcf6f68ccfcfc8f6c8cfffcfcf6fcfcfcffcfcfffcffffcffcfcfffcfcfcfccfcffcfcffcfffcfcffcfffcfffffcffcffcffffcffffff
                cf6fffcfcf6ffcfcfcfcfcfcfcfcfcff6fcfcfcffcfcf8fcfcfcfcfcfcfcf6fcfcfcfcccfcfcfcfcf8fcfcfcf8f8f8f8f8ffcfcf8fcccf8fcf8fccf8f6fc8cf8f6c8c868a6868c86688688a8c8a68698888c68c8ff86668f8f8c868688ffc88ccfc8cf8cfcf68c8c8cfcfc8c8c8cfcfcf6c8cfcfcfcfcfcfcfcfcff6f6fffcfcff6ffffcffffcffcf6ffcfffffffcfffffcfffcfffffcffffffffffcffffcfcf
                cffcfcfcfcfcffcfcfcffcfcf6f8ffcfcfcfcfcfcf8cfcfcfcffcfcfcfcfcfcf8f6f6fcf6fcfcf8fcf6f8fcfcfcfcfcfcfcfcf8fcffcf8fcfcfcf6cf6fc8f6cc8f8c8c86886a88c68ca6a6888688a6666a88a88c8fc8668cc8c86a686c8c8c68fcfc8cf8cfc888c8c68ccfc868ccff8cc8c88fcfcfcfcfcf6ffcfcf8cfcfcfffcffcfcffcf6ffcf6fc8fcfcf6fcfffcfcfffcfffffffffffcffcffffffcfffff
                fcfcfcffcffcfcfcffcfcfcfcfcfcff6fcfcfcfcfcfccfcf8fcf8fcffcfcf8fcfcfcfccfcffcfccf8fcfcf8f8fcfcfcfcfcf8fcfcfcfcfcfcfcfcf8cf8fccf8fc8c8c8c8a688c88a8686888c8c88666a8886868fcfc86a68f886666a68ffc86cfcf8c8cf8fc8c86c8cfcfc8c8c6fcfcf8c86cffcfcfcf6fcfccfff6f8cfffcfcfcfcfcfcfffcfcffcfccfcffcffcfffffcfffcffcfffffcffffffffffffffffc
                fcffcfcffcffcfcfcfcfcfcfcffcfcfcfcfcfcf8fcf8fcfcfcfcfcfcfcf6fccf6fcf8f8cfccf6f8fccf8cfccfcfcf8f8f8fcfcfcfcf6f8fcfcf6f6f8ccc8f6c8cf8cc8c8886a8c6688a86a8888c8666668c8a88cf8f6668c8c6a6866a68c868cf8fccf8ccf68868c68cf6fc868c8fcccf6c8cfcffcf6fcf8cf6fcfc8cfcffcffcf8fcfffcfcfcfccf8f6ffcffcfffcffffcfffcfffcffffffcffcffcffcffcff
                fcf6ffcf6fcfcffcfcffcffcfccfcfcf8fcfcfcfcfcccf6fcfcfcfcfcfcfcf8fcf8cfcfccfcfcfcfcfcf8cfcf8fcfcfcfcfcf8f8ffcfcfcf8fcf8c8cf8fc8f8f6cccc8c86c886888a668868c868869668886688cfc8a6988c86666a666cf868cfcc8c6f8cfc8c6886c8fcf8c8c8fcfc8c86c8ffcf6fcf8fcfcfcf6cf68fcffcf8fcfcf6fcf8ffcfcfcfc8fcffcfcffcfcffcfffcfffffcfffffffffffffffffc
                ffcfcffcffcffcfcffcfcfcfcfcfcfccfcfcfcfcfcf6fcf8fcfcfcfcf6f8cfcfcfcf6c8fcf8fcf8cf8ccfccfcfcfcfcfcf8fcfcfcfccf8fcfcf6cfc8c8c8ccc8f8f8f6c8c868c8a6888a8888c8c866698c86a888cfc6668c8866a6668a88c68cf8f68c8c8f8686a68ccfcf6c8c6cfcfcf6c8fcffcfcfcfcf6f6ffc8c8fcfcf8fcfcf8fcf8ffcfcf8fc8fccfcffffcfffffffcfffcffcffffcffcffffcffcffff
                cfcffcfcfcfcfcffcfcfcfcfcfcfcf6f8fcf8f6fcfc8fcfcfcfcfcf8fcfcf6f8cf8fcfcf6fcfcfcfcfcf6f8f8fcf8fcf8cfcf6fcfcf8fcfcfcfc88ccccfcccfc8cc8ccc8c8c8c8886a686a8c8888698988a6688cf888666886a66668668c8668fc8c68f8cfc86a68a8cfc8c868cfcf68c886cffcf8fc8f6fcfc8fccfc8ffcfcf8fcfcf8fcfcfcfcfcfccf6fffcfffcfcfcffffcffcffffcffffffcfffffffcff
                cffcfcffcffcfcf6fcfcfcfcfcfcfcfcfcfcfcfcf6fccf8fcf8fcfcfcf6fcfcfcfcf8ccfc8fcccf8cf6fcfccfccfcf8fcf6fcf8fcfcfcfcfcc8cf6f8c8c8f8c8f8f6f8cc8c88c8c6888688688c889866686668c88fc698a88666666a66886a68fcf68ccc8c68668668cffc8c8c8cfcf8cc6cfcffcf6fcfc8f8cf8f68ccf8f8fcf6f8f6fcfcf8ffcf8fcfcfc8fffcffffffcfffffffcfcffffcffffffffcfffff
                cf6ffcfcfcfcffcfffcffcfcfcfcfc8cfcfcfcfcfcf8fcfcfcfcfcfccfccf8cf8fcfcf8cfccf8fcfcf8c8f8f6f8f6fcccfc8fcfcffcf8fcfcfc68c8cf6f6ccf6cc8c8ccc8c68c68c86a86a8868c869666a66688c8c866668a6666a668a68666c8f8988f8cf86a66a86ccf8c86c8cf8ccc8c8cfcf6fcf8cfc8c8fcccf88fcfcf8fcfccfcf8fcfcfcfcf6f8ccfcfffffcfcfffcfcfcffffffcfffcfffcfffffcff
                fcfcff6ffcff6ffcfcfcfcfcfcfcfcfcf6f8cf6fcfcf6f6fcfcfccf8fcf8cf6fcf8f6cf8cf8fcf8cfcfcfccfcfccf8f8f6fccf8fcf8fcfcf8c8cf6f68c8cf8c8f8fccccc86c88c86a8688688a88666666666a8886866a668666a666666a8a688cc866c8c68c66686a8fcfc8c88c8fcccc868cffcf8fcfccfcc6fcc8ccccfcfcfcf8f8f8fcf8fcffcfcfcfcccfcfcfffffcffffffffcfcffffffffcffffcfffff
                cffcfcfcffcffcfcfcffcfcfcf6fcfccfcfcfcfcf8cfccfccf6fcfcfcf6fcfcfcfccf8ccc8cf6fcf6f8c8f8c8cf8cccccf8f8cfcfcfcf6fcf6c8c8c8fc8f6cfc8cccf6f8c88c8688688a68a6688a66a66a6668c86c86668a8666668686868668f8698c886c86a6a868cfcf68c8ccfccccf6cfcf8cf6f6f8ccf6cf6f6f6f8fcf6fcfcfcfcfcfcfcf6fcf6f8f6ffcffcfcffcfffcffffffcffcffcffffffffcfff
                cfcfcffcfcfcfcffcfcfcffcfcffcfcfcf8f6fcfcf6fcf8f8fcf8f6fcfcf6cf8f6f8c8cf8fccf8cf8cfcfcfcf8cf8fcf8cfcfccf6fcfcfcf6c8c8c8c8cc8f8c8f6f6cf6c8c68c8c8a6868a6886866666668668866666666866a666a66a686698cc898cf688866668a8cf8c8c8c6f6f8f68c88ffcfccfccfc8c8c8c8c8c8fcfcfcf8f6f8f6f6fcfcfcfcfcccf6fffcffffcffcfffcffcfffcfffffffcffcfffcf
                cfcffcfcfcfcffcfcffcfcf6ffccfcfcccfcfccccfcccfccf6fcfcfcf6fcf8cfcfc8f6c8cccf6fc8fc8c8c8f6fc8fcccf8cccf8ffcfcfcf8c8c8c8ccccf6cf8ccf8f8cf8c68c686868a868686a866686666a688a666a66a6a6668666686a66a888896886a866a66868fcfc68c8c8fcc8c86ccfc8cf8cf8f6f6f6f8f8f8cf6f8fcfcfcfcfcfcfcfcf8fccfcf6cccfffcfffcffffffffffcfffcffcfffffffffff
                cfcf6fcfcfcfcfcff6ffcfcfcfcfcf6fcf6f6f8fccf8f6f6fccccf8fcf8cfcf6fcf6cf8f6f8cf8cfccfcfcf6fccf6f8fcffcfcfcffcfcfcc8c8c6f6f88cf8ccf6c8cf6c868c868c6a868a68a688a66a666866a8866666666686666a686668666c866a8c668a666a86ccfc8c88c6fcf6fcc88fcfcf6f8cfc8c8c8cc6c8cccfcfcfcf6fcfcfcfcfcfcfcfcf6fcf8f6fcffcffcffcffcffcffcffcffffcffcfcfcf
                cf6ffcfcffcffcfcffcfcffcfcf6fcfcccf8cfccf6fccfcfcfcfcfcccfcf6fcf8cfc8cc8ccf8cfc8f8c8ccc8c8f8cfcccccf6fcfcfcfcf6f6f6f6c8ccc8c8f6cf8fccf8c6c68a6886866866686866666666668866a686686668a66666a6866688c669886a666a668c8fcf86c8cc8fcc8f8c6fcf6fccf8f6fcf6f8f8f6f8c8fcfcfcfcf8fccf8fcfcfcfcfcf8cfccfcfcfcfffffffffffffffffffcffffffffff
                cffcfcfcfcfcfcfcfcfcfcfcfcfcf8cf8f6cfc8fcf6fccccf6f8f6fcf6fcf8cfcf8fcfcf8f6fc8fccfcf6f8fcf6fc8f8ff6fcfcfcfcfccf8c8c8c8c8f6fc8cf8cc6f8cc8686868a6a8a66a66a8666986a98966c866666a66a668686a6686a66988698c86686666a88c8fcc88c8cf6f8ccf6cf8cf8f8fc8f8c8c8c6c8f6cfcfcfcfcfcfcfcfcfcfcfcfcf6fcfcf6f6f6fcfcfcfcfcffcfcfcfcfcffffcfcfcfcf
                6fcf6fcfcfcfcffcfcffcfcf6fcfcfcfccfc8cf6fcccf8f6fcfcfcf8cfc8cfcf8fccf6fcfcfcfccf6f6cfcc8c8c8fccf6fcf8fcfcfcfcf6fc8c8cf8cc8c8f6c8f8ccf86c6a6a8686866868666889666666666a866666668668686a668668666a86a668a98a96a66868cfc8c68c6fccf8c8c8fcf6cfc8fcccccf6f8f6c8f68fcfcfcffcfcfcffcfcf6fcfcfcf6fcfcfcf6ffffffffffffffffffffcffffffcffc
                fcfcfcfcfcfcfcff6fcfcfcffcfcf6f6f8c8fccf6f8fccfccf8cf6fcf6ffcf8fcfcfcf8fcc8c8f8fc8f8c8fccfc8c8f6fcfcfcfcfcfcfcf8cf8f6ccf8fcc6f8c6f6f6fc68686a6a86a86a66666a669869666988669a666686a68666686866a6686696a66666668a8a6fcfc68c8ccf8cfcf66fc8fc8f6ccccc6c8c8cf8c8cf8fcffcfcffcf6fcfcfcffcfcf8fcfcf8f6fcf6fcfcffcffcffcffcffffcfcfff6ff
                cf6fcfcfcfcffcfcffcff6fcfcf6fcfccfccccccfccf6f6f8cfccfccfcccfcfcf6f8fcfcffcfccf6fccfc8c8c8cf8ccfc8fccfcfcfcfcfcfc8cccf8cc6f8cccfc8ccf686a6a68686a66666a6986966989669668986668a666866a686a68a66668a666866a66a666868cfc8c8ccc8cfc8c8c6fc8cfccf8f6f8f8f6f68cf8c8cfcfcffcfcfcfcffcf6fcf6fcfccfcfcfc8fcfcfffcfffffffffffcfcfffffcffcf
                6fcfcf6fcfcf6fcfcffcffcfcfcfcf8cc8f6fcf6f8fccfccfccf8cf8cfcf6f8cfcfccfcfc8fcf6cfc8fccf6f6f6ccf8cfccf8ffcfcfcfcf6fccc8cccfcc8f68c8fc8cc686686a68a686a666669666986669898a66989666a66a866668668666a86966a6666986a6a66cfcc868ccc6fcfcf68cfc8ccccc8cc6cc8c8cf8c8f6f6ffcfcfcffcfcffcfcfcfcfccf6fcff6fcf6fccfffcfcffcfcfcffffcfcfffcfff
                cfcf6fcfcf6ffcffcf6fcfcf6fccf6fcfccf6f6fccccc8f6cf6fcf6fccfcfcfcf8fcf8fcfcf6cf8c8fcf8c8cc8c8c8cc8f8fcfcfcfcfcfcf6f8fccf6f8f6ccf6ccfcc8c6a6a686a68666a66a6666666a6989666666686686868668a668a66a6666669866a6666686a8cff8c8c8f6f6f6c8c68c8f6f8f6f8fcf6f8c8c8f6c8cfcfcffffcffcfcffcf6fcf8fcfccfcfcf8cfcf6fcffffcfffffffcfffffcfffcfc
                fcf6fcfcfcfcffcfcffcfcfcfcfccfc8cf6cf8cc8f6fcf6fc8ccccfcf6f8cf6fcf6fcfcfcfc8f6cfcfc8c8c8cc8f6f8fccfcfcfcfcfcf8f6c8cccccf6ccf8c8fcc6f8c8c686a68686a66666666a969666698966698989a666a686666a6866666a66989a696a6a6a668cfc86c6c8cc8cf8c8cc8c6ccf6f6c8c8c8cfcf6ccf8c8fcfcfcffcfcfcfcfcfcf6fcf6f8fcfcfcf6fcfffcfcffcfcfcfffcfcfffcfcfff
                6fcfcfcf6fcfcf6ffcfcfcfcfcf6fccf6cf8ccccccf6ccc8fcf8f6f6fccfccf8cfcfcf6f8fc8ccf8ffccf6fc8cc6ccc8f6fccfcfcfcfcfcf8fcf8f6fcf8ccf6cfcf6cc686a686a6a668a6a6696666a66966666a6668668686686a6a686686a6686a666666666666a68cfcc886cf8cc8cf6f68c6f8c8ccfcccf6fcf6cf88cccf6fcfcfcfcfcf6fffcf6fcfcfcfcfcffffcfc8ccfffffffffffcfffffcfcfffcfc
                fcfcf6fcfcfcfcfcfcfcf6fcf6fcf8fcfc8cf6f8c8cf8fccc8cccfcc8f8cf8cfcfcf6fcfc8cf8cfcfc8c8c8cc6f8c8f6fcf8fcfcffcfcf6fc8ccfcf8fcccc8cf6c8fc8c686a686866a66666a66696666666a6966989866a686a6666688a66666a666a96a6a98a666a8cf8c6c86cc8cf6c8cc6c8cccfc8c8f6c8fcff8cf6f6c8fcfcffcfcfcfcfcffcfcf8f6fcf6fcfcfcfcffcfcfcfcfcfcffcfcfcfffcfcfff
                cf6fcfcfcfcfcfcfcf6fcfcfcfcfccc6f6f6c8cccf6cc6f6fccf6c8fccf6fcf6f6fcfcf8fc6cfcfcf6f6cf6c8c6ccc8cf8cfcfcfcfcf6fc8cf6f6ccccf6f6f6ccfc6cc86a686a66a6666a66666a666989a6966666a66a666a688686a68686a6686a9689666666a6a68cfcc8c6c8c6c6f8f68c8c6f68f6f6ccf6cfcff6c8cf8cfcfcf6ff6fcfcffcfcf6fcfcf8fcffcfffcf6f6fcffffffffcffffffcfcfffcfc
                fcfcfcfcfcfcfcfcfcfcfcf6fcccf6fccccfcccc6c8cfc8ccc6cfcf6f6cf6ccfcf8cf8ccccf6fcfc8c8c8c8cc8c8ccf6fcfcf6ffcfcfcfccc8ccf8fcf6fcccf8c6fc8c6c66a66a6868a6666a966666666666666a6668686868686a6868a6666a666666a6a6a6a66866cf8c8c8ccf68c8ccc6c8c8cf6ccc8f6c86ffcfcfc8cccccf6ffcffcfcfcfffcfcfcf8fcfccfcfcffcfcf8f6fcfcfcfffcf7fffcfcfcfff
                6fcfcfcfcfcf6fcfcfcfcfcfcffcfcfcf8f6cccf8cf6c8f6f8f6ccfcfc8cfc8c8cfc8fcf6c8cfffcfccf6c8ccfcc6ccfccf6ffcfcfcfc8f6fcc8cccc8cc8f6cfcf6fc6c686686686a666a6666669a66a66666a6666a66a66a68a6668a6866a666a6a6666666a66a6a8cfc6c668c8c6cf8c8c8c6c8cfccf6cf8c6cfffc8ccccf6fcfcfccfcf6fcfcffcf6fcfcf6fcf6fffffc8cccfcfffffcfcfffcfcfffff7ff
                cfcfcfcfcfcffcfcfcfcfcfcfcf6fcf6fccf8f6cc8cccccc6cc8fcfc8fcc8fcf6c8fcccfcfcfcfc8c8c8c8c8ccf6f8c8f8fcfcfcf6fcfcc8cccc8f6fcfcccf6c8ccc8c86a6a6a6a666a666a66a66666666a69666a6686868686686a686a6666a6666a6a6a6a666a668cfc8cc8c8c68c8c6c6c6c8c6c8ccf6c8c8fcfcff6f6f6fcfcf6ff6fcfcfcfffcfcffcfcfcfcfcfcfcfffcf6f6fcfffffcfffffcf7fffcf
                fcfcfcfcfcfcfcfcfcfcfcfcf6fcfcfccf6cc8cccf6f6f6f8f6fcffcc6fcfcf6cfc6f6f6c8ffcfcccf6c8cccfcc8c8fccfcfcf8fcfcfcf6f6f6f6cccc8f68cccf6fc6c66666866686a666666666a669a69666866686a66a686a6a6686866a66686a66666666a6a66a6cf6c8c68c6c6ccf6c86c8ccfcf6f6c8c6ccfffcf6c8c8cf6fcfcfcfcf6fcfcffcfcffcf6fcfcffffffcfcf6cfcfcfcfffcfcfffffcfffc
                fcffcfcfcf6fcfcfcfcfcf6fcffcffcf6fcfcf6f6c8c8c8ccccfcfcfcf6cfccf6c8ccfcfcfcff8cf8c8cc6f8ff6f6ccf6fcf8fcfcfcfcfcc8c8c8cf8f6ccc8c6cf6cc86a6a66a86a6668a6a6a6666a66666a66a6a6686868a668686a6a6a66a66a66a6a6a6a6686a68cc8cc68c6c6868c86c8c686c8cc8cfcc86fcfcffccfcf6fcf8fcf8f6fccfcfcffcf6ffcfcf6fcfcfcffffcfc8fcfffcfffffcfcfffcfcf
                cfcf6ff6ffcffcfcf6fcfffcfcffcfcfcf8cccf6fccfccf6f8fcfcf6ccfcfcc8cfccf8c8fffcfcf6f6c8ccfcfcf6c8cfccfcfcf6f6fcf6f8ccccc6fc6cf6cc8c8cc8c6c686a66a66a6a66666698966666a666666868a6a66686a6a668866666a66666666a66a6a6686cf68c6c6c86ccc8c6c68cc8f6fcf68c6c8cffffcf68c8c8ccfccfcfc8f6ffffcff6fcffcfcfcfffffcfcffcfccfcfcfcfcfffffcfcffff
                cfcffcffcfcf6fcfcffcf7ffcfcffcfcfcfcf6cc8f68c8cc8cffcf6f8fcff8f6c8c8ccfcfcffcfcfc8cccfcff6fc8f6cf8cf6fcfcffcfccccc6f6fcf6c6c86cc6f6f6c86a668668686666a6986a686a66666a6a66a66868a86a68686a6a6a66689a6a6a66a6666a6a68cc68c68c6668c6c68c6c6c6cc8ccc8cc6fcfcffcf6f6fcf6f6f6f6fccf6fcfcfcfcfcff6fcfcfcfffffcfffcf6fcfffffcfcfffffcfcf
                fcfcfcfcfcfffcfcfcfcffcffffcffcf6fcf6ffcf6cf6f6fcfcffcfccffcf6cc8cccccffffcfcf8f6c8fcffcfc8cc8cf6fcfc8f6fcff8f68cc8ccf8c6c8cc6c6c6cc86c666a6a6a6a86a666a66666666a6666668a686a6866a6866a686666a6a686a666a66a6a6a686c8c8c66c8c6a6f86c6c868ccfcf6f6cc8c8fcffcfc8cc8c8ccfcfcc8f6cfcfffffcf6ffcfcfcfffcfcfffcfffcfcfcfcfcfffcfcfffffc
                fcfcfcfcffccffcfcfcfcfcfcfffcfcfcf6fcf6f8cf8cc8cfcfccccfcfcf6c8c6c8f6f6fcfffcfcc8ccfcfcfcfc8ccc8fc8cfccfcfcfc6cf68c6fcf6c8c68c8c8c8cc86a866686866a686a666a66a69666a6a6a666a686a6866a666a68a66666a666a6a6666a6686a68c66c6c8c666c8c6c6a6cc68c8cc8cc8cccffcfffcc6f6fcc8c8c8fccf8cfcfcfcfcfcfffcfccfcfffcfffcfcffcffcfffcfffffcfcfff
                cfcfcfcfcfffcffcfcfcfcfffcfff6fcfcfcfcfccf6ccfcf6fcff6fcfcfccc6f6cc6fcfffcfcfcfcf8fcffcfccc6c8fcccfccf8fcffc8c86ccccff6cc6c6c6c6cc6c6c66a6a6a6a6666a688a666666a666666868a6686a66a686a6866a66a6a66a66666a6a66a6a66a68b86a6c6a6a8c6c686c68cccf6fcc6f68c6fffcff6c8c6ccf6ff6cc6cf6fcffcfcf6fcfcfcfcfcfcffcfffffcff6ffcfffcf7fffffcfc
                fcfcfcfcfcfff7ffcffcffcfffcfcffcfcfcf6f8f6f8c8cffcf6fcfcffcf6c8c8c8fcffcfcffcfc8cfcffcfff6f68c68f6cf6cfcfcfcf6cc86fcfcf6c8c6c8c6c8c8c8c68686666a6a668a66a6a6a666a6a6a6a668a6668686a66a6a666a666a66a6a6a666a6666a66a66a66686a66c8c6a6a6a6c86cc8ccc6ccfcfcfffcf6c8c8c6f6fcf8f6fc8fcfffcfc8fffcfcfcfffcffcf6fffcffcfcf6fffffcfcffcf
                cfcfcffcffcfcfcfcfcfcfffcfffcfcfcfcfcfcfcccfcfccf8cfcf8fcfc6c8c6c6fcfcffcfcfcf6fcffcffcfcc8c8ccc8c8cf8fcffcf6c8cccffcfc8c6c8c6c6c6c6c68c6a6a6a86666a66a86866666666686668a66a6a6a6a686666a666a666a6666a66a66a6a68a686a66a6a66a68c68668686cc8fccc6f8c6cfcffcffcc8c6f6c8cf8cccf6fcfcfcfcfcfcfffcfcf6fcfcffcfcfcfcff6fffcfcfcffcfcff
                cff6fcffcffcfcfcffffffcffcfcfcfcf6fcfcf6fc8ccfcfcf6f8cfffcf6ccc8c8cffcfcfcf6fccfcfcfcffff8c6c68c6f6c8fcfcff8c8c6f6fcfc6c6c8cfc68c6c8c6c68b6868c89a668686a6a6a6a6a6a6a6a666a68686866a6a6a66a66a6a66a6a6666a6668a66a666a6866a66a6c6a6a6ac68cc6cccc6c8c8cfcfffff6c6c6f8cfcf6f6cf8cfcffcfcf6fcfffcfcfffcfcfffcffffcffcfcfffffcffff6f
                f7ffffcffcffcffcf6fcfcffcfffcfcfcfcf6fcfcfcf6fcf6fccfcf6f6c8f68c6fcfcf6f8fcfccf8ffffcfcfcc68c8c6c8c8fcfffcfc6c6c8fcffc8c6ccfc68c6c8c6c8c86a6a8c6866a6a668686666668668686a866a6a6a6a666a66a6666666a6666a6a66a666a66a6a66a6a66a68c666a668a6c8ccc6f6c8cccfcfcfcff6c8c8f6c8fccf8cf6ffcffffcfcfcfffcfcfcffcf6ffcfcffcfcffcf6fcfcf6ffc
                fffcfffcff7ffcffffffffcffcf6ff6ffcfcfcf6f6cfcf8fc8f8cf6fc8f6c8ccfcfcfcfcfcf8f8cfcfcffcfcf8cc6c8c8c8ccfcfcf6f8c8ccfcfcf6c8cf8c6c6c6c6c8ccc6668c86b66668a6a6a6a68a6a6a6a6a66a68686686a6866866a6a6a666a6a666a66a8a6866a66a666a66686a68c8c6c8cc8f6c8c8c6f6fcfffffcc8c6fccfc8f8cf6fc8ffcfcf8f6ffcffcfcfcf6fcfcfcffcffcfcf6ffcfffcfcff
                cfcfcfffcffcfcfcfcfcfcfcffcfcffcf6fcf6fccf8cf6ccfccf6fc8cc8c8cc8cf8ccf8cf6fccfcffcf6fcfccc68c6c6c6cf8fcf6fc6c6c8f6f6f6c8ccfc686c86c86cfc86a8cf6a66a6a66868686898666866868686a6a6a668a6a6a6a666a66a6666a666a66686a6a6666a6a66a6a66a6cfcc6c8c6c8c8c6f6c8cfcfcfffcc6f68f6fccf6fc8fcfcffcfcfcfffcff6fcfcffcfcff6ff6ffcfcfcffcfcfffcf
                fffffcfffcfcffcfffffffffcffcfcfcfcf6fccf8cfccfcc6f8cfc8f8c8cc6fcc6fcccfccfccf6fcfcfcfcf8fcf68c868c8cfcf6f6c8c8c6c8cfcc8cf8c8c6c8c8c6ccf8666cc866a68666a6a6a6a686a6a6a6a6a6a686868a666a66866a6a66a66a6a6a6a68a6a66a66a6a666a66a68b66ffcc86c8fccc6f6c8c6fcfffcfff6f6cf8c8f6fc8f6cfcfcffcfcfcfcffcfffcfcfcfcfcfcffcfcffcfcfcffcfcfc
                fcfcffcfffcfcffcfcf7fcfcfcffcf6fcfcfcf6cfccf8ccfccfcfcfc8c68c8c8fc8f8c8f8cf8fcfcffcfcfc6cf8c68c8c8cf6fccc8c8c8c8cc8cf8cfcf6c8c8c8c8c8fcc8c8fc8c868a68a6868686a6a686868688686a6a6a68a668a6a66a6666a66a68686a6868a66a6866a666a686a68acffc8c8c6c8f6c8c6c8cf6fcffcfcc8c8fccfc8fcf8c8fffcfcfcfcffcfffcfcfcf6fcfcffcfcfcf6fcfcfcffffff
                ffcffffcfcfffcffffffffcffcf6ffcf6ccc8cf8cc6cf6f6f8fcf8c8c6c8c6ccffc6fcc6fccfcffcfcff8f8f8fc8c686c8cfcccf8fcf8fc68ccfcf6fc8c686cc8c6cffc68cfc8c868c886868a6a868686a8a6a86a8a688686868a66a68a686a6a6a686a6a868a6c68a68a6a68a686a68c668fcfc6ccf6c6c8c8c8cf6fcffcfffc8fc8f8cfcf8cf8fccfcffcfcf6ffcfcfff6fcffcfcf6fcf6fcffcffcfcfcfcf
                cffcfcffffcfffcfcfcfcffcffcfcfccfcf6fc6f6fc8cfc8fcffcfc6c8c68c8fcfc8c8fccf8ffcfcfcfcfccccff68c8c8cf6f8c8fcc6c6fc8f6c8fc8f68c6cff68cfffc8cfcf868ccfc68a868686a88a8686886c868c6c8c8a6868a68686a6868686a86868c68c86a686686a66a6a8c8c68cffffc8c8cf8c8cc8c6cfcfcffffcfc8cf6f8f8cf8cf6ffcfcfcfcfcfcfffcfcffcfcfcfcffcffcfcfcfcfffcffff
                fcffffcfcffcfffffffcffcfcffcf6f6f6cf6fccc8fcc8fcfccf6f68c88c8cfff8c8f6c8fcfccf8ffcfcf68ffcf6c86c8ccf8ccfcf8c8c8cccf8fccf6c86cf8c8cffcf8cf8ccf8ccf868c8c8c8a86c86c8c8cc8c6c8c8c6c6c8cc868c8a868a6a86a68cc8c6c86c8c8c8a686a868c6cc8c68fffffccc8ccccc6f6f8cfcffcfffcfccfcfccf8cf8cfcfcfcffcfcfcffcfffcfcfcf6fcfcfcfcfcfcffcfcffcfcf
                cfcfcffffcffcf7fcfcfcfffcf6fcf6ccf6cc8cfcccf6fccfcfcf6ccfcc8c8cfcc8cc8fc8fcfcfcfcf8fcfc8fcf88c8c8c8ccc8ffc8cfc8f6f6ccf8fcf6c8fc8c8fcfcf8fcf8c8cfcc8c88c8c88c8c8c8c8c8c8c8c8c8c88c8c8ccc8cc6cc8c8c8c8c8c8c8c8cc8c6c6c8cc86c8c8cf8c86cfeffcf6fcccccf6c8cf6cfcffcfffcf6f8cf8cfccfc8f8fffcfcf8fcfcffcffcf6fcfcfcf6fcfcfcfcffcfcfffff
                fffffcf7ffcffffffffffcfcfcfc6fcf6c8fcf6cf8ccf6cf6fcc8c8fcff6cfffc8ccfc8fcfcf8fcfcfc8c8fcfcfc68c8c8c88cfccc686cc8fcf8fcfcc8c8fc8ccfcfcfcfcf6f8cfff8cfcf8f8cf8f8f8f8cf6f8cf8cf6fc8fc8cc8fc8cf8cf8ccc8cf6c8cc8c8c8c8c8c8c6c8cc8c8cfcc88ffcffcf6f8f6f6f8f8c8fcfcfffcffcf8cf8fccf8fcfcfcfcfcfcfcfffcff6ffcfcfcfcfcfcfcf6ffcfcfff6fcf7
                fcf7fffffcfcfcfcfcfcff6fcf6fcc8cf8cc8cf8cf6f6cccf6f6fccffc8c8fcf6cc8cccccf8fc8fcf8fc8cf8fcf8c868c68c6cfcf8c8c8fc6c8cc8ffcfcfcf86f8fcfcfcf6f8cfcfccc8f8f8f8f8cf8fcf8f8cf8cf8cf8fcf8ffcf8fcfcf8cfcfcfccfcf8fccccc8fc8cf8cc8c8cfcccf66cfcffff8c8ccf8c8ccf6c8f6fcfffcfccf8cccf8cf6f8fcfcfcfcfcfccffcffcfcfcf8f6fcfcf6ffcfcffcfcffcff
                ffcffcfcffffcffffcff6ffcfcfcf6fcccf8f6ccc6f6fc8cc8cc6cfcfcccfcfcf8fccccccfc8cc8fcc8cf6fcf8f68c8c88c8c8fc86c8cc8cfcf8fcf6fc8cfcc8cfcf8ffcc8cf8cffcf8fcfcfcfcf8fcf8fcfcfcf8fcfcf8fcfcf8fcfcf8fcfcf8fcf8f8fccf6f8fc8fcccf8fcfcf6fcf6f68fffffcfcfc8ccfcf8c8ccfcffcfffffcfcf8f6f8cfcccf8ffcfcfcfcfcfcfcf6fcfcfcfcf6fcfcfcfcf6fcfcffcf
                cffcffffcfcffcf7ff6fcfcc6f6fccccf6cccf8f6fcc8fcccc8ccf8fc86fcff8cc6f8c8f8cfc8cc8f8f6cffcffcc8c868686cfcfc8c8c8cc8ccc8cfcfcfcf6fcfc8cfcf8cfcfcf8c8ccf8f8f8f6fcfcfcff8fcfcffcfcfcfcf8fcfcf8fcfcfcfcf8fcfccf6fccf6fccf8f6fcf8fcf8fcfc8ccfcffffccfcc8c8c8ccf6fcfcfcffcffcc8cf8cf8cf8fcfcfcfcfcfcffcfcfcfcf6f6f6fcfccf8cfcfcfffcfcffc
                fcffcfcffcfcffcfcffcfcffcfccf8f6cf8f6cccc8cffc6f6cc6fcffcfcffccffc8ccc8ccfc8c8f6c8fcfcffcf8c868a68a8cfcf86cfccf6f8f6fc8fcf8f6fc8cfcfcfcc6fcfcfcf6f8c8ccffcc8f8fcfcfcfcffcf8ff8ff8fcfcf8fcfcf8f6fcfcfcfcfcfcf8fcfcfcfcfcfcfc8fccf8f68fffeffffccf8ffcfc68cf6fcfffcfffcfffccfcfcfcf6fcfcfcfffcfcfcffcffcfcfcfccc8f8cfcfcffcfcffcfcf
                ffcffcfcfffcf6fcfcfcfc6f6fcf6ccf8cccf8f6f6fcfc8c8c8cffcfcffcfffcfcc8f8c8ffc86c8cfcf8cfcf8ff88c86a88cf8f8c8cf8c8ccc8cc8ccc8ccf8cf6f6fcf6f8cfcfcc8c8fcfcffcfc8fcf8f8fcfcf8fcf6fccfcfcf8fcfcf8fcfcf8fcfcf6f8f8fcfcf8fcfcf8fcfcfcfcfcfc6cfffffcffcfcccf6f6cfccffcfcffcfffcf8f8f6f8fcfcf8fcfcfcffcff6ffcfcffcfcfcfccfcf6fcf6fcfcffcfc
                fcfcffffcfcfffcfcf6fcfcfcfcfcfc8cf6f6c6c8cffc8c6f6cfcfcfcfcfcfcff8cc8c8cfcf688c88cfcff8fcfc686a8868cfcc88c8f68c8ccccccc6fc6c8cfcfcf8f6cccfcfcffcfcf6f8fcfcffcf8fcfcf8fcf8f8fcf8fcf8fcfcf8fcfcfcffcfcfcfcfcfcf8fcfcfcfcfcfcfcff8fcf8cfcffeffffccff8fc8cccfcfcfffcfffcffcfcfcfcfcf8fcfcf6fcffcf6ffcfcffcfcf8f8f6f6fcfcfcfcfcfcffcf
                ffffcfcffcfccfcfcfcfcf6fcfcfccfcccc8cfc8fcffcf6c8ccfcffcffcfcfffcc8cc8ccfc8c8c8cf8fcfcfcff8c8a686a8cf8c8c6cfc86c868cc6fc8f6ccc8c8cfccf8f8fcfcfcf6fcfcfffcffcfcfcf8fcf6f8ccfccfcf8fcffcfcffcfcfcfcffcfcf8f8cfccf6fcfcffcffc8fcfcfcf868fcffffcff8cfccfcf8fccf6fcfffcffcffcfcfcfccfccfcfcfcffcffcfcffcf6fcfcfcfccfccccf6fcfcfcf6ff6
                fcfcffcfcfcff6fcfcf6fcfcfff6f6cf6f6fcf6ccffcc8cccfcffcfffcfcfcffccc6c8cfcf6868c8cfcf8ffcffc8686a868fc8f868f8c686c8c8c86cfc88ccf6fc8f6fccfcfcfcfcfcfcfcfcfcfff8f8fcf6fccfcf6f8fcfcffcfcffcffcff8ffcf8ffcfcfcf8fcfcfcfcffcfcfcffcf8fcc8fffcfffccfcf8f6f8ccf6fcfffcfffffcffcf8fcf8fcf8fcfcfcfffcfcfcfcffcfcf6f6f6ccf8fcfcfcfcfcfcff
                cfcfcffcffcfcfcfcf6fcfcffcfc8f6cccfcfcfcffcffcfccffcffcffffcffcff68f6c6ffcc6c8cfff8ffcf8fc8c868688cf8c8fcccf8a8c8c8c6c8fc8cc86c8ccf6fc8f6fcfcf6fcfcffcffffcffcfcfcfcff8f8fcfcf8fcfcfcfccf6fcfcfc8fcfcffcffcffcfffcfffcffcf6fffcfcf8c6cffffeffcf6fcfc8fcfcf6fcffffcfcffcfcfcf6fccfcfcf6fcffcffcfcfcfcfcf6fc8ccf8f6cf6fcfcfcffcfcf
                ffcff7ffcf6fcfcf6fcfcffcffccfcfcccfffcfcffcf6f6fccffcffcfcfcfcfcc8cc88cfcf688c8c8fccfcfcffc88a8a8cfcf8ccf8fc88c8c8c8c8cfcf68c8c8f6c8c8fcfcffcfcfccfcfcfcfcffcfcfcfcf8cfcc8c8c8ccc6f8f8ffcff8fcffcffcfcfcfcfcfcf6fcfc8fcfccfcfffcfcf68cfcfffcffffcf6fccc6fccffcfcffffcfffcf6fc8f6f6f6fcf8fcffcfcfcfcf6fcf8fcf8ccfcfcfcf6fcfcfcffc
                fcf7ffcfcffcfcfcfcfffcfffcf6f6ccfcfffcfcffcfcfc8ffcffcffffcfcfffcccc86fcf8c8c8cfcfffcffffc8c868cffcf868fccfc8c8fc86c8fc8fcf6c8c8c8fcfc6c8fccfcf6fccccfcfcfcfffc8fcfcffcffcfffffcfc6ccccfcfcfcfcffcffffff8f8f8fcfcfcfcfffccfffcffcfc668ffcffcfcffcfc8cf8f6fcfcffffcfffcfcfcfcfcfc8fcf8ccfcfcfffcfcfcfc8f6cc8cf6f6f6fccfcfcf6fcfcf
                cfcfcfcfcfcfcf6fffcfcffcffcfcfccffcfcfffcfcfc6ccfffcffcfcf6ffcfcf6f86cffcc68c8cfcfcf8fccffc8cc8fcfc8c8cff8cf8c8f8c8c8cfcf8c88c8c8c8c8cf8fc8f6fcfcf8f6fcfcfcfcffcffcfcfccf6fccfcfcf8f6f8fcfcf8f8f8f8c8ccfcfcfcfff8ffcfcffccfcffcfccf86ccffcf6fffff6fcf8ccfccffcfcfffcffff6fcf8f6fcf8cfcccfcffcff6fcf8fccf8fc6fccfcfcf8fcfcfcffcff
                cfcfcfcfcfcffcffcfffffffcfcf6ff6fcfffcffcffcfcfcfcffcfffffccfffcfc8cc8fcf8c8ccfcfcfcfcfffcfc8cfcfffc8cfcff8fc8cfc888c8cfcf8c8c8c8fccf8cc8cf6f68c8cccf6ccccc6f6ffccfcf8fcffcfcfcf8fcfcfccf8fcc8c8c8c8f8f8f6f6fc8ffcff6fff6fcffffcfcf68c8fcffccfcfcfcf8cf8cfcfcfffcfcfcfcffcfccfcf8cfccfcf6ffffcffcfcfcf6cf6fc8f8fc8fcfcf6fcfcffcf
                cfcffcffcff6ffcffcfcfcfcf6fcfcfcfffcffcffcfcf6ffffcffcfcfcfcfcff8c86cfffcc68c8fcf8fcfcfcf8c8fc8fcf8fc8cfcfcf8c8c86c8cf8cc8f6c8cc8c88c8f6f6c8cfc8f6f6c8f8f6f8c8c88c8c8f8c88888686c688c8f8cccf8f6c888686c8c8c88cfcfcfcfcffccfcfcffcf8c6ccffcf6fffffcfcc8ccccfcfcfcfffffffcfcf8fcfcfcfcf6fcfcfcffcfcfccccf8cccfcfcfcfcf6fcfcfcfcfff
                6ff6ffcffcffcffcfffffffcfcfcffcffcffcffcffcfcfcfcffcfffffcfcffcfcc6cfcfcf8ccfcffcfcfcfcfcfcc8fcfcffcfcfcf8fc8ccfc88c8cf8fccf8f8f6f6ccc8c8f8f8c8cc8c8fc8c8c8cc8fc8f8cc8c8c8c8c88888688c68f88c8c88c8c86866868c888f8fcfcffcfcffffcfccf88c8fcfc8cffeffcfc8f8cf6fffcfcfcfcfcfcfcf6f8fcf8fcf8fcfffffffcfcff8cfcf8f6fccfccfcfcfcffcfcfc
                fcffcffcffcffcfffcfcfcfcf6ffcfcfcfcffcffcffcfcfffcffcfcfcf6fcffcc8c8fcffcf8c8fcfcf8ffcfff8ccccffcfcf8c8ffcffcf8f8c8c8ccf6f8ccf6cf8ccccfc8ccc8c8c8cc8c8fcf8fcfcfcfcffcf8c8c888c86888888c88cf8c8c8c868a6666a66666c6c8ffcffcfcfcffff6f6c8fcfcf6fffffcff8c8cccfcfcfffcfffffcfcfcfcfcfcf6fcfcfcfefcffcf6f6fccfcfcfcfcf6fcfcfcfcfcffcf
                ffcffcffcffcfffcfffffcf6fcfffcffcfcfcfcffcffcfcfcfcffcfffcfcfcff6cfcfcfcfcfcfcffcffcffcfcccf6fcffcfcfcfcffcfcfcfcf8cf8c8c8c8c8c8ccf8f8cfcf8fccf6f8c8c6c68c688688c8c8f6fcf8cc86c8c8cc8c8c8c8ccf8f8c8c888a6868a8c88c8cffcfcf8ffcfcfcf8ccc6f6fcffefffcffcfcf6fcffcfcfcf7fffcf6f8f8f8fcfcfcfcffffffffcfcfcf8fcfcfcf6ffcfcfcfcfcfcffc
                fcfcffcffcffcfffcfcfcfcfffcfcfcfcfcfcffcffcfffffcffcffcffcccffcfcfcfcfcfcf6fcfcffcfcfcfcf8c8fcfcffcfcfcfcffcfcffc8c8cf6f8cf6f8cf68c8ccc8c8c8c8c8c8cc8c8c8c8c68c68c6c8c88c8c8c88c8688c88c8f8c8c6c8fc8cc88c8c8f8c8cfcfcfffccfcfffffcf88cf8cf6cfffffffcf6f8cfcffcfffcfffcfcfcfcfcfcfcf8fcf6fcfcffeffcf6f8fcfcfcf6ffcfcfcfcffcfffcff
                cfffcffcffcffcfffffcf6fcfcfffffcf6fcfcffcff6fcfcfcffcffcff6fcffccfcfcfcfcfcfcffcfcffcfffc8fcfcffcfcfcfcffcfcffcffcffc8c8c8c8c868c8c8c8cc6f6cccccccccc8c8c888c88c888c8686868c8c868a868c8c8c8f8c8c8c8f8fc8c8fc8cfcf8cfcfcfcf6ffcfcffcc86cfcf8cffcfeffcffc8c8cfcfcfcfcfcfffcfcf8cf8cfcfccfcffcffffcffcfcfcfcfcfcfcfcfcfcffcfcfcffcf
                fcfcfcffcffcffcf7ffcfcfcffcfccf6fcffcfcff6ffcfffffcffcffcfcffcff8fcfcffcf8cffcffcffcffcfccccfcfcffcfcfcfcf8fcffcf8ccfcf8c8c86c8c8c8cc6c8c8c868868c868c6868c686c86c6868c86a68668a668a6868c8c6f8fc8c8c8c8c8f8cf8c8cf6cfcfcf6fcffcfcfcfc8ccfc8fffffffffcf8cf6fcfffcffcffcfffcfcfc8fcf8cf8fc8ffcfcffcffcfcfcfcfcfcfcfcfcfcfcffcfcffc
                ffffffcffcffcfffffcf6fcfcffcffcfcfcfcff6ffcffcfcfcfcffcffccfcfcfcfcffcffcfcfcfcffcffcffcf8fccfcfcffcfcfcfcfffcffcfcf8f6fcfc8f8c8c8c6f88c8c68c8c8c6c8c686866a68a686a68a6a8688a8668a686a86868c8c8cf6f6c8c8cc8c8c8f6c8fcfcfccfcfcfcff6f8c8f6fccfcfeffeffcf8c8cfcfcfcff6ffcfcfcfcfcf8fcfcfcfcfcffffffcfcfcfcfcffcfcfcfcfcfcfcfcffcff
                6fccfcffffcffcfcfcfcfcffcfcf6fcfcfcffcfcfcfcffcfcfffcffcff6ffffcfcfcfcfcfcfcffcfcfcffcfccfcfcffcfcfcfcffcfccffcfccfcfccf8cfcccfcf6f8c6c86c8c8c686886866a6a68a668a68686686a666a6a668a688c8c8868c8c8c8c88c88c88c8c8fc8fcf6f8cfcfcfcfcfc86cf68ffcfffffcfcfcfc8ffcffcfcfcffffcfcf8fcfcf6f6fcfcffcfcfffffcfcfcfcfcffcfcfcfffcfcfcff6f
                feffffcfcffcffffffcfcfcfcf6ffcf6f6fcfcffcfcfcfcffcfcfcffcffcfcfcfcfcffcfcfcfcffcffcfcfffcfcfcfcfcfcfffcfcfffcffff8cfcf8cc86f88c8c8c8c8c8c8c8c8c86a686a68668668a6686a688686a868688a6886a6868c8c8c8c8fc8c8c686868cfc8c8fcfc8ccfcfcfffccfc8f68cffffeffcfcf8c8ccff6fcfffcfcfcffcfcc8f6fcfc8f8fcffffeffcffcfcfcfcfcfcfcffccfcffcfcffc
                ffcfcffffcffcfcf7fcf6fcfcfcfcfcfcfcfcfcfcffcfffcffffffcffcffffcfcfcfcfcfcfcffcfcfcffcfcfcfcfcfcffcfcfcfcfcfcfcfcfcff8fc8fc8cc8c68c8c8c8c8c8c868c886a686a6a6a66666a688a6a6a66a6a8686a6888a888c8cc86cfcf6c88c8c88cffc8fcf6fccccfcfcfcf8c8cc86cfccfffffcfcf8fcf6fcf6fcffcffcfcfcfcfcf8c8fcfcfcffefffffcffcfcfcfcfcfcfcffcfcfcffcfcf
                cffffcfcfffffffcfcfcffcf6fcffcfcfcfcfcfcfcfcf6ffcfcfcffcfcfcfcfcfcffcfcfcfcfcfcfcfcffcfcfcfcfcfcffcfcfcfcfcfffcffcfcfcfccfc8cc8c8c868c8868686c88cc888a8686866a6a688a688686668686a6868a6868c68c8c8c8ffc88c86888c8fcfcccfc8f868cfcfcfcfcc8c88ffcffcfeffcfcc8ccffcfcfcfcfcffcffcf6f8cfcfcf6fcfcffffcfeffcfcfcfcfcfcfcfcfcfcfcfcffcf
                fcfcffffcfcfcf7fffcfcf6fccfcfcf6fcfcfcffcfcfcffcfffcfcffff6ffffcffcfcfcfcfcfcfcffcfcfffcfcfcfffcfcffcfcffcfcfcfcffcfffcfc8fcf8f6c868c868c68c886a686c8c88c8a8a686866669a66a8a68a8686a868a868a8688c8cfff68686a6868cfcf8f8fcc8fcfcfcfcffcf6c86cfc6fffffcfcffcf8cfcfcffcfffcffcffcfcfc8fc8fccfcfffcffffcfffcffcfcffcffcfcfcfcffcfcfc
                ffffcf7fffffcffcfcffcfccfcffcfcfcfcfcfcfcff6fcffcfcfffcfcffcfcffcfcfcfcfcfcfcffcfcffcfcfcfcfcfcfcfcfcfcfcfffcffcfcfcfcfcfcf6fcc8c8c868a68a86a8688a88c8c8c8c8f8886a6a686a88888868a88688686a86886868ccffc886a68a868cffccfc8f6cf8fcfcfcf6f8c8cfffcffcfcfcfccccfcfccf6ffcfcfcff6ffcc8fccfcf8f8cfcfffefffcfcfcfcffcfcfcfcfcfcfcffcffc
                fcfcffffcfcffcffcfcfcfcf6fcffcf6fcfcfcffcfcfffcffcfcfcfffcffcfcfcff6fcf6ffcfcf6ffcfcfcffcfcfcfcffcf6fcfcfccfcf6f8fcfcfcfcfcfc8fcfc8cc8c8c8c888a868868688c8fcfcc8c8868a868c6cc8a686a86a8a8686a68a868fffc8a868888a68fcfc8fccf8cfcfcfcfcfcfc8cfcffcffffffcffcf6cff8fcfcffffcfcfcffcf6f8fccfcfcfffefffcffffcfcfcfcfcfcffcfcffcf6fcff
                cfffcfcffffcffcfffcfcf6cfffcfcffcfcfcfcff6fcfcffcfcfffcfcfcffcfff6ffcfcfcfcffcfcfcfcffcfcfcfcfcf6fcfcf6fcfcfcfcfccfcfcfcfcf6fcc8c8f8c8c8fc8cfcfcccc8a8a86c886868868a866a66868688a868a86888a8886888ccfffc8888c8686a8fcfc8c8cfcfcffcfcf6f6f6fcfcffcfefcffcf8cf8cfcfcffcf6fffcffcfcfcfcfcfcf6fcffffcffcfcffcffcfcffcfcfcffcfcfffcfc
                fcfffffcfcffcffcfcfcf6fcfcfffcfcfcfcffcfcfcfffcff6ffcffffcfcffcfcfcfcfcfcff6ffcfcfcfcfcffcffcffcffcfcfcf8cf6f6f6f8cfcffcf8fcf8fcfccc8c8c8fffcffff8c888688866a68a6a6888888a6a6a66888868a868868a8a688cfcfc8cc8c8c8a68ffcfcfcfccfccfcfcfc8fc8cfcffcfffffcfcffccfcfcffcffcfcfcfcfcffcfcf6fcfcfcffcffffffff7ffcfcff6ffcfcfcfcffcfcffc
                ffcfcfffffcffcffcfcfcfcfffcfcf6fcfcfcff6fcfcfcffcfcffcfcfcff7ffcfcfcfcffcfcfcffcffcffcfcffcfcfcfcfcfcfccf6fccfc8cf6fccf8fcfcfcf8cc8f6cfc8c868c8c8c8c86ca68a686a6886ac8c86888688a66a68868a8c8886888ccffffc8fcfc8c86ccffcc8f6f8ffcfcfccfc8fcfcfcffcffeffff6fcf8fcfcf6fcfffffcfffcfcf8fcfcf8fcfffcfcfefcfffcfffcffcffcffcffcfcffcff
                6ffffcfcfcfcffcffcfcfcfcfcfffcfcffcff6ffcfcfffcfcffcffffcf7ffcffffcfffcffcfcfcffcffcffcfcfcffcfcfcfcfcf6fccf8c8fc8c8f8cf6f8c8f6fcf6cf8c8c6cc8c86c868c686866a868cc8c88c68cc8c88688a68a6a8868c8c8c8c8fcffffcc8fcff8a8fcffcfc8fcfcfcf6fc8cfc8fcffcffcfffcfcfcfcfcfcfcfcffcfcffcf6fcfcfcfcfcfcfcfffffffffcfffcfcfcffcffcffcffcfcff7f
                fcfcffffcfffcffcff6fcfcfffcfcfcfcfcfcfcfcffcfffcfcfffcfcfffcffcf7ffcfcfcffffcfcfcfcfcffcfffcfcffcfcfcfcfcf8cf8cfcfcfcf6cfccfccf8c8c8cccf6f8c86c88c86a88a6a668ccf8c8c88c88c8cccc8c8868868cc8c8c8c8c8fcfcffffcf8fc868cfcfc8fccfcfcfcfcfc8cfccfcffcfffcffffffcfccf8fcffcfffcfcfcfffcfcfcfcfcfffcfcfeffcffcfcffcffcfcfcfcfcf6fff7ffc
                ffffcf7ffcfffcffcffcfcffcffcfcfcfcfcfcfcfcffcf6fcfcfffffcfcfcffffcffcffcf7fcffcffcfcfcff6fcfcfcfcfcf6f6f8cf6cfccf8c8c8f8c8cf8f6cccfccf8cfc8cc8c686a868c6868fcffc8c88cc8c68c888c8c8c8c8cc8c8c8cc8c8cfcffffcf8fcfcf86ccfffcfcfcfcfcfcf8cc6f6fcfcffccffcfcfcfcf8fcfcfcfcfcffffcfcfcfcfcfcfcfccfcffcffefcffcffcfcffcfffcfffcfcfcffcf
                fcffffffcfcfffcffcfcffcffcfcfcf6fcfcffcffcfffcfcfffcfcfcfcfffcfcffcffcffffcfcffcffffcf6fcfcfcf6fcf6fc8fccfcf8fcfcffffccfcf8fccf8f86c8cfccffffc8cc8c8c68c8cfffcfc8c8cf6c8cc8cc8c8c8cc8cf8c8cfc8fccfccfcfcffcfcfcfc6c8fcffcf6fcffcfccfcf8fcccf6fcfffcfffffffcfcfcffcfcfffcf6ffcfcfcffcffcfcffcfcffcffffcffcfffcfcfcfcfcf7fffcfcffc
                ffcfcfcffffcfcfcffcfcff7ffcfcfcfcf6fcfcfcff7ffcfcfffffefffcfcfcfcffcff7fcffffcffcf7ffffeffcfcfcf6fc8fccf8cfcccfcfcc8cfccfcfffcfc8cf8fccf8fc8cffcfcfc8cc8ffcfc868c8c6c8c8c8c8c8c8cc8cfc8fcfc8fc8f68f8ffcffffcfcfc8c8ffffcfcfcfcffcf8fcfccf8fcffcf7ffcf7ffeffcf6fcfcfcfcffcfcffffcfcffcfcffcfcffcfffcfffcffcfcffcffcffcffcfcfffcff
                cffffffcfcffffff7ffcfcffcffcfcfcfcffcff6fffffcfcfcf7fffcfcffcffcfcff7fffcfcfcfcffcffccffcffcfcfcfcfccf8fcf8fcf8ccf8fccfcfcfcfc8cc8cc6f8cc8cf8c8f8c8fcfffcfc8c8cc8ccc8fcf8c8cf6fc8cf8cfccf8fccfccfccfcffcffffcfcfc8ccfcfffcfcfcfcfcfccfcfcccfcffffcffffffffcfcffcfcffcfcffffcf6ffcfcfcfcfcfcfcfcfcffcfcfcffffcff7ffcffcffcfcfcfcf
                fcfcfcffffcfcf7ffcffffcffcf6fcf7ffcfcfcffcfcffcfffffcfffffcffcffcfcffcfcffcffcfcffcfffcffcfcfcfcfcffcfcfcfcf8cfcf6fcfcfcfcfcfcf8f68c8c88cc8ccc8cfcccf6cfcc8c8c8c8ccc8c8c6cf6cf8cf6cf6cf8cfcf6f8fccf6ffcfffcfcfcffccfcffcffcfcfcfcfcfcfcf6f6fcfcfcffcffcfcfffcfcfcfcfcffcfcffffcffcfcfcfcfcfcfcfffcffffffcfcff7ffcffcffcffcfcffcf
                cfffffcfcffcfffcffcfcfcfcfcfcfcfcfcff7ffffffcffcf7fffcfcfcfcffcffcfcffffcffcfffcfcfcfcfcfcffcfcfcfccfcfcfcfcfccc8fccfcf6f8f6f6f6c8c8c8c68cc68fc8ccf8cfc8f6fcf6cccc8cf6c8f8cf8ccf6f8cf8cfcf6fcfcf8fcfcffcfffffcf6fc8cfcffcffcfcfcfcfcf6fcfcfcfcfffcfffcfffcfcfcfcffcffcfffcfcfcfcfcfcfcfcfcffcfcfcffcfcfffffcfffcfcffcfcfcffcfcff
                fcfcfcffcfcfcfcfcffcfcfcfcfcfcfcfcfcfffcfcfcfcffffcfcffcffcfcff7ffcfcfcffcffcfcfffffcfffcfcffcffcffcfcfcfccf6f8fc6f8ccfcfccc8fc8c88c8fcfcf8cc8cf6f6fcfccfc8fcf8c8cf6c8fcc8ccf8fcfcfc8fccfcfcfcfcfcfcfcfffcfffcfcfcf6ffcfffcffcfcfcfcfcffcf6cffcffffcffcffffffcfcfcfcffcfcfffcffcfcffcfcfcfcfcffcfcffffefcfffcfffcfcffcfcfcffcfcc
                ffcfffcffcfcfcffcfcffcffcfcfcfcfffcfcffffffcff7fcffffcffcffcfcffcfffcffcffcffcfcf7fcfcfcffcf6fcff6fcfcfcf8fcfcc8c8ccf8cf6c8fc6c88c6ccf6f8c6cfcfc8ccf8cf8cfc8ccf6f6c8fcc8fcf8cf6f8ccfccf8cccf8fcfcfcfcffcfffeff6fcf6fcfffefffcfcffcfcffcfcf6f6ffcfcfffeffcf7fcfcfcffcfcfffcfcfcfcff6fcffcfcfcfcffffcfeffffefcfcfcfffcffcfcf7ffcff
                cffcfcfcffcfffcfcffcfcf7fcf6fcfccfcfffcfefcf7ffffcfcffcffcffcfcffcfcfcffcffcffcfffffcffcfcffffcfcffcfcfcfcfc8fcfcfcfcfcfcfcc8f8cc8fffcfcfcff8ccfcf8cfccfc8fcf8cfc8cc8cfcf6fcccfccf8fcfcfcf8fcf6fcf6fcfcffcfffffcfcfcfcffffcffcfcfcfcfcfcfc8cfcffffeffffffffffffcfcffcfcfffcffcff6ffcfcfcfcffcfcf7ffffcfcffffffffcfcf7ffcfffcfcf7
                fcffffcfcff7fcfcfcf6f6ffcfcfcfcff6ffcfffcffcffcfcfffcffcff7ffcfcffcfffcffcff7ffcfcfcfcfffcfcfcffcfcfcfcfcf6fcf6fcf8cf6f8fcfcfccfcfcffffcffcfcf68ccfcf8f6fccccfc8fcf8f6f6fc88c88cccf6f6fcfcfcfcffcffcfcffcffffcfcfccccfcfcffcffcfcfcfcfcfcfcfcfcfcfffcfcfefcfcfcfffcffffcfff7ffcffcfcfcfcfcfcfcffffcffffffcfcfcfcfcfffcff6fcfcfcf
                ffcf7ffffcffcfcfcffcfccfcfcffcf6ffcffefffcffcfcffcfcfcffcffcffcfcffcfcfcffcfffcffcffffcf7ffcffcffcffcfcfcfcfcfcf8cfcfcfccf8fcf8fcfffcfffcfcf6fcf8f6fcfcfcfcf6fcfccfccfc8c8c86c8ff8cfcfcfcfcfcfcffcfcffcffcfcfffcf6ff6ffffcfffcffcffcffcffccfcf6ffcfffffffffffffcfcfcf7ffcfcffcfcfcffcfcfcfcfcfcfcffcfefcffffffeffcfcfcfcfcfcfcfc
                fcfffcfcffcfcffcfcfccfcfcff6fcffcffffffeffcffcfcffcffcfcfcffcffcfcffcfffcffcfcfcffcfcffffcffcff7ffcfcfcf6fcf8cfcfcfcfcfcfccf6cfcfcfcfcfcfcfcfcfcfcc8fcfcf8cfc8f6f8fcf6fcfc8c88fccfcfccfcfcfcfffcfcfcfcfffffffffcffccfcfcffcfffcffcffcffcffcffcfcffcf7fcfcffcfcffffcfffcffffcffcffcfcfcfcffcffcfffcffffffcfcfeffcff7fcfcfcffcffcf
                ffcfcffcfcfffcffffcf6ffcfcfcfcfcfcfefeff6ff7ffffcffcffcfcfcfcfcffcfcfcf7fcffffffcfffcfcfcfcffcffcfcfcfcfcfcfcfcfcfcfcf6fcfcfcfcffcffcfcf6f6f8fcccfcf6f6ccfc8fccfccf6fcf8cf8cfccfcfcfcfcfcfcfcfcfcfcfcfcffcfcfeffcfcfcfcfcffcfefcfcfcfcfcfcfcfff6cfffffffffffcffcfcfcfcf6cf6fcff6ffcfcfcfcfcfcfcfcfcfefcffffffcffcffcffcffcfcf7fc
                fcfffcfffcfcfcf7ffcffcffcfcfcfffffffffcfcfffcfcffcfcf7fffcfffcf6ffcfcfffffcfccfcfcfcffcffffcffcfffcfcfcfcf8fcf8cfcf6fcfcf8f8fffcf6fcf6fcfcccc8fcf8fcfcf8f6fc6f8c8c8c8c8fc8f8cf8fcfcfcfcfcffcfcfcffcfcffcfffffffffcf6fcfffcffffffcfcfcfcffcfcfcffcfcffcfefefffcffffcfc6cffcfcf6ffcfcffcfcfcfcfffcfffffffcfefcffcffcfcfcfcfcfcffcf
                cfcfcfcfffcfcffffcf7fcfcfcfcfcfcfcfefffcfcfcffcfcfffffcfcfcf7fffcfcff6fccffcffffcfcfcf6fccfcf6fcfcfcf6fcfcfcfcffccfcf8fccfcfccfccfccfcfcf8ffcf6fcccc8fcfccfcf6fcfcfcfcf6cfccccccccf6fcf6fcfcfcffcfcffcfffcfcfcffcfcfcfcfcfcfcf7fffcfcff7ffcfffcffcffffffffcfffcf7fff6fcfcfcfcfcffcfcfcffcfffcf7ffcf7fcffffffeffcffcfcfcfcfcfcfcf
                ffcffffcf7fffcfcfcfcffcfcfcffcfffffffcff6fcfcffcfcf7fcffcffcfcfcfcfcffcffcffcf7ffffcfffcff6fffcfcfcfcfcfcfcfcfcfcf8fccf8fcfcfcfcfcf8fcfcfcc8fcfccffcfccf8f8ccfc8cccccccfc8f8fcfcf8fcf8fcfcf6fcf6fcfcfcfcfffcffcfffcfcfcffffcffffcffcf6ffcffcfcffcfcfcfcfcffcfcffffcfcccffffcfffcffffcfcffccffffcffffffcfcfeffcffcffcfcfcfcfcfcfc
                fcfcfcffcfcfffffcf6fcfcffcf7fff7fcfcffcffffcfcffcfffcfcffcffffcfffcfcfcfcfcffcffcfcfcfcfcffcfcffcfcfcfcfcfcfcfccfccfcfcfcfcfcfcfcfcfcfcfcfcfcccf8cf6fcfccfcff8fcff8fcf8fcfcf6f6fcfcfcfcfcfcfcfcfcfcfcfcffcffffffcfcf6ffcf7ffcfcffcffcfcffcfcffcffffffffffcffffcfcffcf6fcfccfcfffcfcffffcfffcfcffcfcfeffffffcffcffcffcfcfcf7ffcfc
                ffffcfcfcffcfcf7fcffcff6fcfffcffffffcffcfcfffcfcfcfcfffcffcfcffcfcffcffcfff7ffcffcffcffffcffcfcffcffcffcfcfcf6f8cfccfcfcfcf6fcfcfcffcfcfcf6fcf8fcfcfc8fcf6fcccfccfcfcfcfccfcfcfc8fccf6fcf6fcfcfcffcffcfcffcfcfcffffcfcfcffcffffcff7ffcfcffcf7fffcf7fcfefffcfcffffcfffcfcfccffcfffcfcfcffcf6fffcffcfffcfefcffcffcff7ffcfcfcfcfcfc
                fcfcfcfcfcffffcfcfcfcfcfcfcffffcfefcffcfcfcfcffcffcfcfcfcffcfcffcfcff7ffcfcffcfcffcff7fcffcffcfcff6ffcfcfcfcfcfcfcf8fccfcfcfcfcfcfcfcffcfcfcf6cfccf6fcccfccf8fcf8fcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcff6ffcfcffffcffcffcfcffcffcfcffcffcffcfcffcffcffffffffcfffff7fcffcfcf6fcf6fcfcfffffffcffcfcfcfcffcfcfcfffcffcffcffcff7ffcffcfcf
                fcffcfcffffcfcf6fcfcfcfcfcffcfffffffcffcffcff7ffcffcffcff7ffcfcffcf7ffcffcffcfffcff7fffcfcfcffcfcffcfcffcf6fcf8fccfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf6fccf8fcf8fcfcfcfcfcf6fcfcfccfcfcf6fcfccfcfcfcff6ffcffcf6f7ffcfffcfcf6ffcffffcfffffcffcfcffcfffeffcfcffcf7fffffcffcfcffcffcfffcfcfcfffcffcfcffcfcfcfff7fcffffcffcffcffcffcfcff7
                ffcf7ffcf7ffff6cffcfcfcfcffcffefcfcffcfcfcfcffcff7ffcffcffcffcfcffffcffcffcffcfffcfffcffcffcfcffcfcfffcfcffcfcfcfcfcfcffcfcfffcfcfcffcff6fcfcfccfcfcfcf6fcccf6f6f6f6fcfccf6fcfcfcfcfcfcffcfcfcfcffcffcffcfcffffcfffffcfcffcf7ffcfcfcfcffffcfcfcfffffffffffffcfcffcfff6fcfcf6fcffffff7fffcffcfcff7fffcfcfffcfcffcfffffcffcfcfcfcf
                cffcfcfffffcfcfcfcfcfcfcfcfffcfffff7ffcfcfcfcffcffcffcffcffcffcf7fcffcffcffcffcfcfcfcfcffcffcfcffcfcf7ffcfcfcfcfcfcfcfcfcffccfcfcfcf6f6fffcfcfcfcfcfccfc8fcfccfcfcfcf6f86cfcfcf6fcfcfcfcfcfcffcfcffcfcfcfcfcfcffeffcffcfcffcffffffcffcfcfcfcf6fcffefefcfcfcffcffcfcfcfcfffcfcffcf7ffffcffcfcfcfcffcfcffcfcfffcffcfcfcfcfcfcfcfcf
                fcffffcffcfffccfcfcfcfcffffcfffcfcffffcffcfcfcffcffcffcffcffcffcffcfcfcffcffcffffffffffcffcffcf7fffcffcffcfcfcf6fcfcffcffcfffcfffcffcfcfcfcfcfcfcfccf8fcfcf6f8cfccfcfcffc6cfcfcffcffcffcffcfcfcffcfcffcff6fcffffffffcffcfcffcfcfcffcffcfcffcfcfffffffffffcfcffcffffffcfcffcffffffffcffffcffcffcfcfcffcfcffcfefcffffefffcffcffcfc
                ffcfcfffeffcf6fcfcfcfcf7fffffcffffcfcff7ffcffcfcfcffcff7ffcfcf7fcffcfffcffcffcf7fcfcfcffcff7ffffcfcfcffcfcfcfcfcfcffcfcfcfcffffcfffffcfcfcfcf6fcf6ffcfcfcfcfcffcfcfcffcffc8fcfcfcfcffcffcffcfffcffcfcff7ffcffcfefcfffcffcfcffcfffcff7ffcfcff7fcfcffeffefffcfcffcfcfcfcfcfcffcfefcfffcfcffcff6fcffcfcffcfcffcfffcf7ffcfcfcfcf7fcf
                cfcfffcffffcfcffcfcf7ffffcfeffcfcffcfcffcfcfcffcffcff7ffcffcfffffcffcfcfcff7ffffffcfcfcffcfffcfcfffcfcfcf6fcfcfcffcfcfcffcfcfffffcfcfcfcfcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcf6fcfcfcfcfcfcffcffcfcfcffcfcffcffcfffffffeff7fffcfcfcfcfcffcffcf7ffffffefffffcfcfcfcffcfcfcf6fffcffffffcfcffffffcffcfcffff7fffcfcfcfffffcfffcffcfcffff
                cffcfffcfcfcfcfcf6fcfcfcfffffffcf7ffcfcffcfcfcff7ffcffcffcfcfcfcffcffcffcffffcfcfcfffffcffcfcfffcfcffcfcffcf6fcfcfcfcffcfffffcfeffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffffccfcfcfcfcfcffcffcffcffcf7fffcffcffffcffefffffcfcfffffcfffcffcffcfcfcfcfffcfcffffcfffcffcffcfcf6fcfcfcfffcffcfefffcffcfcf7fffcffcfffcf7fffcfcfcffcffcff
                cfffcfffffcfcfcf7fcfcffffefcfcffffcf6fcfcfcfcf7ffcffcffcffcfcfcfcffcff7ffcfcffffffcfcf7fcffffcfcfcfcff6fcfcfcfcfcffcfcfffcfffffffcfcfcfcfcfcfcf6fcfcfcfcfcfcfcf6fcfcfcfcfccfcfcfcfcffcfcfcf7ffcffffcfcfcfcffeffffffcfcfffcf7fcff7fffcffcffcffffffcfffffcfefcfcfcff7ff6cffff6fffcfcfcfffffcff7fffffffcffcff7fffffcfeffcff7ffcffcf
                fcfff7fcf6f7fcfcfcfffcffffffffcf7fcfcfcfcfcffcffcfcffcffcfcfcffcfcff7ffcffcfcfcfcffffffffcfcffcffcff7ffcfcfcfcfcfcffcfcfffcfcfcfcfffcfcfcfcf6fcfcfcf6fcf6fcfcfcfcfcfcfcffccfcfcfcfcf6fcfcfffcfcf7fcffcffcfcfffcfefffffcfcffffcfffcfcfcfcf6fcfcfeffffefffffffffffcffcffc8fcffcfcfffffcfcfffcffcfcfcfcfcffcfffcfeffcfcffcffcffcffc
                fff7fffffcfcfcf6fcfcfffefcfcffffffcfcfcff7fcffcffcfcffcfcff7fcffff7fffcfcffcfffff7fcfcfcffffcffcff6ffcffcfcffcffcfcffffcfcfffffffcfcffcffcfcffcfcfcffcfcfcfcfcfcfcfcfcffcf6fcfcfcfcffcffcf6ffcffcffcffcffffcffffffefcfffcfcfcfcfcfffcfcfcffcfffffcffffcf7fcf7fcffcffcfcfcfcfcffcfcfcffffeffcffcfcfcfffcffcfcfcfcfffcfcfcffcffcff
                fcffffcfcf6fcfcfcfcffeffffffcfcfcff6fcfcfffcfcfcffcfcfcff7fffcf7fcffcfffcfcfcf7fffffffffcfcffcffcffcffcffcfcffcffcfcf6fcffcf7fcfcfff7ffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf7fcfcfcfcffffffeffcffcffffcfcffcffcfcfcffffeffffffffffffcffcfff6ffcfcfcffcfffcfcfffffcffcffcfcfcfcffcffcfcfcffcffcfcfcfcf
                ffffcffcf7fcf6fcfcfcffffcfcfffffcfcffcffcfcffcffcffcfcfcffccfcffcfcffcfcffcfcffcfcfcf7fffcfcffcffcffcffcffcfcfcf6ffcffcfcfcfffcff7fcffcfcffcfcffcfcfcfcffcfcfcfcfcfcf6fffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfffcfffffffeffefffcfcffcf7ffcfcff7ffcfcffeffffefcfcfcffefffcffcfccfcfcfffcffcfffffeffffcffcffcfcfcfcffcfffcffcffcfcffcfffc
                fefffcfcfcfcfcfcfffffcfffffcf7fffcfcffcfcffcffcfcfcffcfcfcffcfcfcffcffcfcffcfcffcffcffcfcfff7ffcffcffcff7ffcfcfcfcfcfcfcfcfcfcfcffcfcffcfcffcfcffcffcffcfcfcfcfcfcf6ffcfff6fcfcfcfcfcfcf6fcfcfcfcfcfcfcfcfcfcfcfffffffffffcfcfffcffcfcffcfcffcfffcfffffffffefffcffcffff6fcf6fcffcffcfcffffefffcff7ffcfcfcfcfcfcffcffcfcffcffcfcf
                fffeffcf6fcfcfcfcfcffffefcffffcfcffcfcfcfcfcf7fffcf7ffcfcfcffcffcfcfcffcfcffcfcffcffcffcfcfcffcfcff7ffcffcffcfcfcfcfcfcfcfcfcffcfcfffcffcf7ffcfcff6ffcfcfcffcfcfcfcfcffcfcffcff6ffcfcf6ffcfcfcfcfcfcfcfcfffffffcfcfcfeffeffcfcfcfcffcfcfcff6fffcfffcffeffeffffffefffefcffcfcfffcfcfcfffefffcfcfcfffcffcffcfcfcfcfcf7fff7ffcfcffc
                fffffcfcfcfcf7fffffcfcffffcfcffff6ffcfcffcffcfcfcfffcfcfcfcfcfcfffffcfcfcf7ffcfcfcfcfcffcfffcffff7fffcfcffcfcf6fcfcffcfcfcfcfcfcffcfcfcffffcfffcfcfcffcfcfcfcfcfcfcfcfcfffcfcfcfcf6ffcfcfcffcfcfcfcfcfcfcfcff7fffffffffffcff7ffcffcfcffcfcffcffffeffffffffffefefffcffffcfcfcfcfff7ffcffffcffffffcfffcfcfcfcfcfcfcfcfcfcffcfff7ff
                fefcffcfcf6fcfcfcfffffffcffffcf6ffcfcff7ffcfffcfcfcfcffcfcfcfcfcfccffcffcffcffcfcffcffcffcfcfcfcfffcffffcffcccf8fcfcfcffcfcfcf6fcfcfcffcf6ffcfcfffffcffcffcffcfcfcfcfcffcfcffcfcfcfcfcfcfcf6fcfcfcfcfcfcfff7ffffcfcffeffff7ffcffcfcff7fffcfcfcfeffffeffeffefffffffffcfcf6fcffffcfffcffeffffcf7fffcfffcfcfcfcfcfcfcffcffcffccffcf
                ffffcf7fcfcfcffff7fcfcffffcfcfffcffcf7ffcfcf7ffcfcfcfcfcffcffcffcffcffcfcfcfcffcfcffcfcfcfffffcfcfcfcfcffcff888c8fcfcfcfcfcfcffcfcfcfcf6ffcffcfcf7fcfcff7ffcfcff6ffcffcfffcf6fcffcfcf6fcf6fcff6ffcff6fcf7ffffffffffffffefffcffcfcfcfcfcfcfcfffffffefffffffffffcfefcffffcffcfcfffcfcfffffeffffffcffefffcfcfcfcfcfcfcffcffcfffcffc
                ffcfcfcfcfcfcfcfffffffcfcffffcfffcffcfcffcfffcffcfcfcfcfcff7ffcffcff7ffcffcffcffcf7ffcffcf7fcffffcfffcfcffcfc88cfcfcfcfcfcfcfcfcfcfcf6ffcfcfcffcffffcfcffcffcf6ffcfcfcffcfcffcfcfcfcfcfcfcfcfcfcfcfcffcffcfcfefeffeffeffcfcfcfcfcff7fffcfff7fcfcfffffeffeffeffffffffeffcfcfcffcffcfcffefffefcfffcffcfffcfcfcfcfcfcfcffcfcfcffcff
                feffcffcfcfcfffcfcfcffffff7fffcffcfcfffcfcfcfcfcfcfcfcfcf7ffcfcfcf7ffcffcffcff7ffffcffcffffcfcf7ffcfcffcf7f6f88fcfffcffcffcfcfcfcfcfcfcfcffcfcffcfcffcfcffcffcfcfcfcffcfffc6fcff6fcfcfcfcfcfcfcfcf7fcfcfcfcfffffffffffffffffcfcff7ffcfcfcfcfffffcfcffffffffffeffcfcfffffcfffcfffffcfcfffcfffffcffcff7fffcfcfcfcfcfcfcfcffcfcfcf7
                ffcfcfcfcfcffcffffcfcf7fcffcf6ffcfcfcfcfcfcfcfcfcfcfcfcfffcffcffcffcffcfcfcfcffcfcffcff7fcfffcffcffffcfcffcf8cfcfcfcfcff6ffcfcfcfcffcffcfcffcfcfcfcf6ffcfcfcfcfcff6fcffcfffcfcfcffcffcfcfcfcfcfcfcffcfcfcffcffcfeffeffefcfcffcf6ffcffcfffcfcfcfffffefcffeffeffffffffeffcfcfcffcfcf6fffcffffcfffcffcfffcffcfcfcfcfcfcfcfcffcfcfff
                cffcfcfcfffcfff7fffffffcffffffcffcfcfcfcffcffcfcfcfcfcf7fcfcfcfcfcffcfcffcffcfcffcfcfcffcfcfcfcffcfcfcfcfcfcfcfcfcffcfcffcffcffcffcffcffcfcffcfcfcfcfcfcfcfcf6fcfcffcfcff7ffcfcfcfcf6fcfcfcffcfcffccfcfcfcffcffffffffffffff7ffcfcfcfcfcfcffcffcfefcfffefffffffefefffffffcfffcffffffcffffcfffefffcfffcffcffcfcffcffcfcfcfcfcff7fc
                ffcffcff7fcffcffffcfcfcfcfcfcffcffcfcfcfcff7fcff7ffcfcffcfcfcfcfcfcfcffcff7ffffcffcffc8cfffcfffcffcffcfcfccfcfcfcfcffffcffcff7ffcff7ffcffcfcffcffcffcffcff6ffcffcfcfcffcffffcfcfcffcffcffcfcfcff6fcfcf6fcfcffcfcfcfefefcf7fffcfcfcfcffcff7ffcffffffcfffffeffefffffefcfcffcfcfcfcfcf6feffffefffeffcfffcffcffcf7ffcfcffcfcfcf7ffcf
                cffcff7ffffcffffcffffffcfcfffcffcfcffcfcf7ffcfcffcfcfcfcfcfcffcffcffcfcfcffcfcffcfcfcc8cfcffcfcfcffcffcf6ffcf8fcfffcfcff7ffcffcff7ffcffcffcfcff7ffcffcff6ffcf6fffcfcfcfffcffffcffcffcffcfcfcff6ffcfcfcfcfcfcfffffffffffffffcffffcfffcffcffcffcfcf7fffcfcfffffffcfffffffcffcffcffcfcffffcffffcfffffcfcffffcffffcfcff7ffcfcfffcffc
                fcffcffcfcfffcfffffcfcffffcfcffcfcf7ffcfffcffcfcfcfcfcfcfcffcfcfcfcffcfcfcffcfcfcffffc8ffcfcfcfffcff7ffcfcfcfcfcfcfcfcfcffcfcffcfffcfcffcffcf7ffcffcff6ffcfcfcfcffcfcfcfffcfcffcff6ffcfcffcfcffcfcfcfcfcfcffcfcfefcfcfcfcfffcfcffcfcfcfcfcffcffffffcfffffcfcfcfffeffcfffcffcffcffffcffeffeffffcfcffffcfcfffcfcffcfcfcffcfccfcfcf
                ffcffcfffffcfffefcfffff6fffffcffcfffcfcf6fcfcfcfcfcf7fcfcfcfcffcfcfcffcffcfcffcffcf7fffcfffcffcfcfcffcfcfcfcfcffcfffcfcfcffcfcffcfffffcff7ffffcffcffcffcfcffcfcfcffcfffcfffffcfcfcfcfcff6ffcfcfcfcfcf6fcf6fcfcfffcfffffffefcffcfcfcffcffffcffcfcfcffcfeffffffffefffffefcfcff7fff7fcfcffffffeffffffcffffffcffffcfcffcfcfcfffcfcfc
                fcfcffcfcffffffffffcfffffcf6ffcff7fcfcfcfcfcffcffcfffcfcfcfcf7fcffcf7ffcffcfcffcfcffcfffcfcfcffcfcfcfcfcfcf6fcfcfcfcfcfcfcffcfcffcfcfcfcffcfcffcffcffcffcfcfc6fffcff7fffcf7fcfcf7ffcff6ffcfcfcfcf7fcfcf6ffcfcfcfcfcf7fcfcfffcffffffcff7fcffcffffefcfffffefcfeffffcfeffffffcfffcffffcfffefffffeffefffefcffffefcfcfcfcfcff7fcffcff
                cffcfcfffcffeffffcffcfcffffffcfcffcfcfcfcffcfcfcfcf6fcffcfcfcffcfcfcfcfcf7ffcfcfffcffcfcffcffcfcffcfcfcfcfcffcffcfffcfcfcfcfcfcfcfcfffffcffcfcffcff7ffcffcfcffcffcfcffcffffffcfcfcfcfcfcfcfcfcf7ffcf6cfccfcffcfcfcfcfffffcfcfcf7fcfcfcfcfcff7fcffcfcfcffffffffeffffffcfcffffcfffcfffcffffeffffffffcffffcfeffffcfcfcffcfcffcfcfcf
                fcff7fcfffffffefffcfffffcfcfcffcfcffcffcfcfcfcfcfcfcffcfcfcffcfcfcffcfcfffcffcfcf7fcffcfcffcffcfcffcfffcfffcffcffcfcfcfcfcfcfcfcfcfcfcfcfcffcfcffcffcfcfcffccfffcfcfcffcfcfeffcfcfcf6fcfcfcf6fcfccfcfccf6fccf6fcffcfcfcfeffffffffffcfcffcf7fffcfcfffcfcfcfcfffffcffcffff7ffcffcffcfcffeffffeffefffffcffffffcfff7ffcfcffcfcfcfcfc
                fcfffffcfcffeffffffcfcfffffffcfcffcfcfcfcfcfcfcfcfcfcfcfcf7fcfcfcf7ffcfccfcfcffcffffcffffcff7fffcf7fcfcfcfcfcffcffcfffcfcfcfcf7fcffcffcffcfcfffcffcffcfff7ff6fcffcfcfcffffcfcfcf6fcfcffcfcfcfcfcfc6f6f6cfccfcfcf7fcffcfcfcf7fcfcfcffcfcfcffcfcffcf7ffffcfffcfefffefffcfffffffcffcfffcffffcffffffefeffcfcfcfff7ffcfcff7fffcffcffc
                ff7fcfcfffffffffcffffffcffcfcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfffcfffcffcfcffcfcfcfcffcffffffcffcffcfcff7ffcf7ffcfcffcffcfcfcff7ffcfcfcfcfcfcfcfcfcffffcffcfcfcf7ffffcfcfcfcfcfcfcfcfcf6fcfcccfcccf6fcfcfcfcfcffcfffcffcffcfcfcffcffcfcffcfcf7ffcffffffefffcfffeffefffcfffcffffeffffefcffffffffffffcfffcf6fcffcfcfcffcff
                7fffcfffcffeffffffcfcffffffcfcfcfcfcffcfcfcfcfcfcfcfcfcfcfcffcffcffcffccff7fcfcffcfcffcfffcfcffcf7fcffcff7fffcfcffcfffcffcfcffcfcfcfcfcfcffcfcfcfcfcffcffcfccfffcffcfffffcfcf7fcfcfcfcfcfcfcf6fccfccfccf6fcf7fcfcfcfcfcffcfcfcffcfcff7fcffcffffcffffcffcfcfefcfffffffeffffffefffcffcfcffffefffffcffefcfefcfffcffcfcfcfcfcff7ffcf
                fcfcffcfffffffefffffffcfffffcfcfcfff7ffcfcfcfcfcfcfcfcfcfcfcfcf6fcfcfcff7ffcfff7ffffcffcf7fffcfcfffcfcfcffcfcffcfcfcfffcff7fcf6fcfcffcfffcffcfcffcffcff6ffcffcfcfcfcf7fcffcfcffcfcf7ffcfcfcfcfcfccf6fcccfccfcfccf6fcfcf7fcffcfcfcfcfcfffcffcfcffcfcffcfffffffffcfefefffcfcffffcffcffffffeffffcfffefffffffffcffffcfcfcffcfcffcffc
                fffffcffcffefffffcfcfffffcfcfcfcf7fffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf7ffcffcfcffcfcfcfcfffcffcfcfcfffcfcffcfcffcfffcfcf7ffcfcfcfcf7ffcfcfcffcf7ffcfcfcfcffcfffffcf6ffcfcfcfcfcfcfcfcfcfcf7fcfcfcfcccf6f6fccf6fcfcfcf6ffcfcffcfcfcf7fcfcfcff7fcffcfcffcfcfcfeffffffffcffffefcfffffcfcfeffffefffeffffcffcfffffeffffffffffffcffcff
                cfcffffffcfffffffffffcffffff7ffcffcffcfcfcfcfcfcfcfcfcfcfcfcfcffcffcfffcfcfcfffcffcfffcfcfcfcffffcfcfcfffcffcfcffcfcfcfffcfcfcfcfcffcfcffcf7ffcfcff7ffcffcffcf7ffcffcffcfcf7fcfcf7fcfcf7fcfcf6f6ccf6fcccfcf6fcfcf6fcfcfcfcfcffcfcfcffcffcfcffffcffffcffffefffcfcfcfcfffeffffffefeffffffffcfffffffcfffefffefefffcfcfcfcfcfcfcfcfc
                ffffcffcfffffffcffcffffcffcffcfcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcffcff6fcfcfffcfcfcffcf7fffffffcfcffffcfcfcfcffcfcfcfcffccfcfcfcf6fcfcfcfcfcffcffcfcffcffcfcfcfffcffcfcfcfcfcffcfcffcfcfcfcfcfccfcfccf6fcc6fcfcfcfcfcfcfcfcfcfcffcfcfcffcffcfcfcffcf7ffcfefffcfffffffffcfffcfcffffffcfcffeffffefeffffefffcfffffcffffffffffeffcffcf
                fcfffffffcfcffffffffcffffcfcfcfcffcffcfcfcfcfcfcfcfcf7ffcffcfcf7fcfcfcffcfcfcffffcffcffcfcfeffcfcfcffcfcffcfcffcfcff7ffcfcfcf6fcfcfcffcfcfcfcfcffcfcfcfcffcfcfffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf6fcccfccccf6f6fcfcfcfcfcfcfcff6fcfcfcfcfffffcffffcffffcfffcfcfefcfffcfffffefcfcffffffffcffffffeffffcfffcfffffefcfcfcfffcff7ffc
                ffffeffeffffffcfcfffffcfffcfcf6fcffcfcfcfcfcfcff6fcfffcff6fcffcfffcfcfcffcfffcfcffcffcffeffcfcffcfcfcfff7fffcf7ffcfcfcfcfcf6fcfcffcfcfcffcfcfcfcffcffcff7ffcfcfcfcf7fcf7fcf7fcfcfcfcfcfcfcf6fcf7fcfccf6fcf6fcfcfcfcf6fcfcfcfcf7ffcfcfcffcf7fcffcfcffcfcffcfefffffffeffcfcfefffffffcfcfeffffeffcfffcffffefffefcffffffffefff7ffcff
                fcffffffffffffffffcffffcfcf7fcfcfcfffcf6fcfcfcfcffcf6fcfcfcfcffcfcffcffcffcfcffcfcfcffcffcffffcffffcfcfcffcffffcffcfcfcf6fcfcfcfcfcfcff7fcffcfcfcffcff7ffcffcfffcfcfcfcffcfffcffcfcfcfcf6fcfcfcfcfcfcfccfcfcfcfcfcfcfcfcfcfcfffcfcffcfcfffffcffcffcffffcfffffcfefcffcfcffffcfcfeffffffffefffffffcfffeffffcfffffcfcfefcff7fffffcf
                fffeffefffefffcfffffcffff6fcfcfcffcf7fcfcfcfcf7fcfcfcffcffcfcfcfcfcffcffcfcffcffcfffcffcffcf7ffcf7fffcffcfcf7fcfcfcfcf6ffcfcfcfcfcfcf7ffcfcfcffcf7fcfcfcffcffcf7fcf6f6fccfcfcfcffcfcf7fcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfcfcf7fcfcfcfcfcf7fcffcff7ffcfcffcfcfcffffffffcfcfcffcfffcfeffeffffcfefffffefffcffffcfcffffffcffffffcfcfc
                feffffffefffffffcfcffcfcffcfcfcfcfffcffcfcf7fffcfcfcfcfcfcffcffcffcfcfcfcffcff7ffcfcfcffcffffcffcfcfcfcffcfffffcfcfcfcfccfcfcfcfcf6ffcfcfcfcf6fcffcfcfffcfcfcfffcfcfcfcffcfffff7ff7fcfcfcfcfcfcfcfcfcfcf6fcf6fcfcfcfcfcfcf7ffcfcfcfcfcfffcfcffcfffffffcffffffcfcfcfefcffffcffcfffffffffcffffffefefffffffeffffffcffeffcfcfcfffffc
                ffffefffffffffcfffffffffcfcf6fcffcfcfcfcfcffccfcffcfcfcfcfcfcfcfcffcffcff7ffcffcffcfffcff7fcffcffffcfff7ffcfcfcffcfcfcfcfcfcfcfcfcfcfcfcffcfcfcfcfcffccfcffcfcfcfcfcfcfcffcf7fffcffcfcfcfcfcf6fcf6fcf6fcfcfcfcfcfcfcf6fcfcfcfcffcfcfcfcfcfffcffcfcfcfcffcfefcfffffcffcfcfeffcfcfcfcfcffffeffcffffffefeffffeffeffffffffffffcfcfcf
                ffcfffcfffeffffffcfcfcfcf6fccfcffff7fcf6fcfcfcfcf6fcfcfcfcfcfcfcfcff7ffcffcffcffcffcfcfcffffcffcfcffcfcffcfcfcfcfcf7fcfcfcf6fcfcfcfcfcfcfcfcffcfcffcffcfcfcfcfcfcfcf7fcfcffffcfcfcfcfcf6fcf6fcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfcfffcfcfcffffcfffcffcfffcfcfefcffcfffcffffefffffefcffffffcffcfffffefffffffefcfcfcfefffffefc
                ffffffffeffffffcffffffffcfcfcfcf7fffcfcfcf7fcfcfcfcfcf7fcfcfcffcff7fffcfcffcffcffcffcfffcfcffcffcfcffcfcffffcffcffcffcfcf6ffcfcf7fcfcfcfcfcfcfcfcf6fcfcfcf6ffcfcfcfcfcfffcfcffffffcf6fcfcfcfcfcfcfcfcfcfcfcffcfcfcf7fcfcf6fcf6fcf6fcff7fcfffffcfcffcfefcffcfefffffffcffcfffcf7ffcf7ffffffcfeffffffffcffffcfcfeffffffffcfcfefcfff
                feffeffffffffcfffcfcfcfcfccf7ffffcfcccfcfcfcfcfcfcf7fcffcfcfcf7fcfffcffffcffcffcffcff7fcfffeffcffcfcffcfcfcffcff7ffcfcffcfcfcfcffcfcfcfcfcfcfcfcfcfcf6fcfcfcffcfcf7fcfcfff7ffcfcfcfcfccf6fccccf7fcf6fcfcfcfcfcfcfcffcfcf7fccfccfcfcfcffffcfcfcffcfcffcffcfcffcf7fcffcfff7ffcffcffffcfcfcfffffefefeffffefffffffffcfefcffffffffcfc
                ffffffefffeffffffffffff6fcfcfcfcffcffcf6fcfcfcf6fcfcfcfcfcfcfffffcfcfcfcffcff7ffcff7ffffcfcfcffcffcfcfffcff7ffcffcfcff6fcfcfcfcf6fcfcf6fcfcfcfcfcfcfcfcfcfcf7ffcfcfcfffcffffcfcfcf6fccf6ecf6f6cfcfcfcfcfcfcf6fcfcfcfcf6fcfcccfcfcffcfcfcffcfcfcffcfcffcffcfcfcffffcfcfcfffcfcffcfcffffffefcffffffffeffffeffeffeffffffcfcfcfefffc
                fffeffffefffffffcfcffcfcf7fcffffcffccf7fcfcfcfcfcfcfcfcfcfcf6fcfcfffffcfcff7ffcffcfffcfcfffffcff7ffff7fcfcffcffcffcfcffcfcfcf7fcfcfcfcfcfcf7fcfcfcfcfcfcf7fcfcffcffcfcffcfcffffcfcfcf6cfcfccfcccf6fcfcf6fcfcfcfcfcf6fcfcccfcf7fcfcfcffcfcffcfcf7fcfcf7fcffcfcfcfcffcffffcffcfcffcfcfefcffffefcffcffffeffffffffffcffcffffffcfcfcf
                fcfffffffffffcffffffffcfcfcfcfcffcfcf6fcfcfcfcfcfcfcfcf6fcffeffcfcfcfcffcfcffcfcffcfcfffcf7fcfcfffcfcfffffcffcffcffcfcfcfcfcffcfcfcf7fcfcfcffcfcfcf6fcf6ffcfcfcffcffcfcffffcf7fcfcf7fcfcccf6cf6fcfcfcfcfcfcfcfcfcfcfcfcfcf6cfcfcffcf7fffcfcf7fcfcfcfcffcfcffcfcfcfef6feffcfffcfcfcfcfffcf7ffffffffcffffcfeffeffffffffefcfefffffc
                ffffcfeffcfcfffffcfcfcf6fcfcfcfcff7fcfcfcffcfcfcfcfcf6ffcfcffcffffcfcfcffcfcffffcffcfcfefffffcfcfcfffcfcfcfcffcffcffcfcfcfcfcfcffcfcffcfcfcfcfcf6fcfcfcfccfcfcfcff7ffff7fcffcffcf7fccccf6fccccccccf6fcfcfcfcfcfcf6fcfcf6fccfcfcfcfcffcfcfcfcfcfcfcf7fcfcff7ffcfcfcfcffffefcfcfcffcffcfcffffcfcfefffeffffffffffefefefffffcfcf7fcf
                ffefffffffffffffffffffcfcfcfcfffcfcfcfcffcfcffcfcf7ffcfcffcfcfcf7ffffcfcffffcfcffcffffcfcfcfefffffcfcffcffcfcff7ffcffcfcfcf6fcfcfcfcfcf6fcf6fcfcfcfcfcfcfcfcffcfcfffcfcfff7ffcfcfcfcf6f6ccf6f6f6fcfcfcfcf6fcf6fcfcfcf7fcccf7fcf6fcfcffcfcf7fcf6fcfcfcfcfcffcfcfcfcfcffcffffeffcfcfcfcffcfcffffffcffffefcfcfeffffffffefcffffffffc
                fffffffeffcffffcfcfcfcf7fcfcfcffffcfcfcfcfcfcf7ffcfcfcffcffcffcffcfcffcfcf7ffcfcfcfefcfffcfcfcfcfefffcffcfffcfffcfcf7ffcfcffcfcf6fcfcfcfcfcfcfcfcfcf6fcfcfcfcffffcfcfffcfcfcfcfcfccccfccf6cccccf6f6fcf6fcfcfcfcfcf7fcfccf6fcfccfcfcfcffcfcfcccfcf7fcfcfcfcffcfcf7fcfcfffcfcfcffcfcf7fcfcffcfefcfffeffffffffffcffcffffffcf7fcfcff
                effefffffffffcfffffff6fcfcfcff7fcfcfcfcffcfcfffcfcffcfcffcffcffcffcfcffcfffcfffcffcfcfcfcfffffcfffcfcfcff7fcfcfcfffcfcffcfcfcfcffcf6fcfcfcfcfcfcfcfcfcf6fcfcfcf7ffffcfcfcffcffcf6ff6f6cccfcf6f6cccfcfcfcfcfcfcf6fcfcccfccccfcfcfcf7fcf7fcfcfcf6efcfccfcfcfcffcffcfcfffcffffffcfcfcffcfcfcffffffcffffcfcfeffcfffffefcfcffffffcfcf
                fffffeffeffeffffffcfcfcfccff7ffffcf7fcfcffcfcfcfcfcfcffcfcfcf7ffcfffcf7fcfcfcfcfcffffffcfcfcfefcfcfffffcffffcfffcfcfffcfcf7ffcf7fcffcfcf7fcfcf7fcf6fcfcfcfcfcffffcfcfcfcfcfcfcfcfccccfcf6ccccccfcf6cf6fcfcf6fcfccfcfcf6fcfccf6f7fcfcfcffcf6f6efccfcfcf6fcffcffcfcfcfcffcf7fcfcfcfcfcffcffcfcf7ffcfcffffffffffefeffffffcfcfcffffc
                ffcfffffffffffffffffcfccfcfcfcffcfcfcfcfcffcfcfcfcfffcfcff7fffcffcfcfffffcfffcfffcf7fcffffcfffffcfcf7fcfcfcffcfcfcfcfcfcfcfcfcffcfcfcf7ffcfcfcfcfcfcf7fcf6fcfcfcffffcfcfcfcfcf6fccf6fccccf6f6fc6ccfccfcfcfcfccfcf6cf6fccc6fcfccfccfcfcfcfccefccfccf6fcfcf7ffcfcfcfcffcffffffcffcffcfcfcfcfcfffcffffcfcfcfcfefffffcfcfffffefcfcff
                cffffcffeffcffffcfcfcfcf6fcffcfffcfcfcffcf7ffcffcfcfcfff7fffcffcffcfcfcfcfcfcfcfcffffcf7fcfcf7fcfffffffcffcfcfffcfcfcfcfcfcffcfcfcfcfcfcfcf6fcfcfcfcfcfcfcffcfffcf7ffcfcfcfcfcfcf6cfcc6f6ccccccf6ccf6fccf6f7fc6fcfccfccfcf7fcfccfccf6fcfcfcf6fccf6fcfcfcffcfcff7fcfcffcfcfeffcfcf7ffcffcffcfcffcfcffffffffffffcfffffcf7fffffffcf
                ffcfffefffffffffffffccfcfcfcffcfcf6fcfcffcffcfcffcfcfcfcffcffcffcffffcfffcfffffcfcfcffffffffffffcf7fcfcfcffcfcf7fffcfcfcfcfcffcfcf6fcfcfcfcfcfcf6fcf6fcfcfcfcf7ffffcfcfcf7fcf7fccfcccfccfcfcf6f6fcccccfcfccfcfccf7fccf6f7fccf6fccf6fcfcfcc6fccccfccfcf7fcfcff7ffcfcffffefffcff7fffcfcfcfcff7fcffffcfefcfeffcffffefcffffcfcfcfefc
                fffeffffcfefcffffcfcf6fccfff7ffcfcfcfcfcffcffcfcffcffcffcffcffcffcf7ffcfcfcfcfefffcfcfcfcfefcfcffffffefffcffffffcfcfcfcfcfcfcfcfcffcfcfcfcfcfcfcfcfcfcf6fcf7fffcfcffcf7fcfccfccf6cf6ccf6cc6f6cccccf6fccf7fccccf7fccf6fccccfccfccf7fcfcfcfcf7cfc6fcfcfcfcfcfcffcfcfcfcfcfcfcfcffcfcfcfcfcf7ffffcfcfffffffffeffefffffcfcfffeffcfff
                cffffcfffffffffcfffcfcfcf7fcfcfffcfcffcfcffcffcfcff7ffcffcffcffcfcffcffcfffcfcfcf7fffcffeffcffcfcfcfcfcfcfcf7fcffcffcff7ffcffcfcfcfcfcfcf6fcfcfcfcf6fcfcfcffcfcfcfcfcfcfccf6fcccfccfc6cfcfcccfccf6cccf6cfcf6fcfccfccfccfcf6fccf7fccfcfcf7fccfcfccf7fcfcfcfcfcfcfcfcffffffffffcfcfcffcfcfffcfcffcfcfcfcfcffffffcfcfffefcfffcffcfc
                ffcffffeffcffefffcfcfcf7ffffffcfcfcfcffcfcfcfcffcfcfcff7ffcffcfcffcffcffcfcfffcffffcffcffcffcffcffeffffcffcffffcffcff7ffcffcff7fcfcfcf6fcfcfcf6fcfcfcfcfcfcfcfcfcfcf6fccf6cfccf6cc6fcfcc6cf6f6cc6fcf6cfcccfccf6fccf6cf7f6cfcf6cfccfccf7fccfccccf7fcfcfcfcfcfcfcfcffcf7fcfcf7ffcfcfcfcff7fcffcfcfffffffffefcfcffffefffffcfcfcffff
                cfff7ffffffffffcffcf7fcfccfcffffcf7fcfcfcffcffcffcfffcffcffcffcfcffcffcffcfcf7fcfcffcffcffcffcffcffcfcffcffcfcffcff7ffcffcff7fffcffcfcfcfcfcfcfcf6fcf7fcf6fcfcf6fccfcfcfcfccf6cfcfccc6fcfccccfcfcc6cfccf6f6fccccf6cfccfcfccccfcccf6fccfcfccf6f6fcfccfcf7fcf7fcfcf7fffffffeffcfcffcfcfcffcfcffffcfcfcfefffffffcfcffcfcfcfffff7fcf
                fcfffffcfefcfffffcfcfccfcfffcfcffcfcfcfcfcff7ffcffcfcfcffcff7fffcfcfcffcffcfffffcfcffcffcffcff7ffcffffcffcffcfcffcffcffcfcfcfcfcfcfcfcffcfcf7fcfcfcfcfcfcfcf6fcfcf6fccf6ccf6cfcc6fcfcf7f6cfccc6ccfcf6fccfcccf6fccfccf6cccfcfccfcccccfcfccf6fccfccfcfcfcfcfcfcfcfcfcfcfcfffcffcfcfcffcfcffcfcfeffffffffcfcfefffffcffffcfcf7fffffc
                fffcfcfffffffcffcf6fcfcffcfcfffcf6fcffcfcf7ffcfcf7ffcffcffcffcfcfffcfcfcf7fcfcfcfffcfefcfcff7fffcfcfcffcff7fffcfcfcffcfcffcffcfcffcf7fcfcfcffcfcfcfcfcf6fcfcfcfccfccf6cfcf6fcccfcc6f7cfcccccfcfc6cccccf6cfcccfccf6fccfcf6f6cf7cf6fcf7fcf6fccfccfccfcf6fcfcfcfcfcfcfcfffefcfcffcfcfcfcffcffcfffcfcfef7ffffffcf7fffcf7ffffffcfcfcf
                cffffffeffcffffffcfcfcf6fffcfcffcfcfcfcffcfcffcfffcffcffcffcffffcf7fffcfffffcfffcfcfffcfff7fffcffffcfcff7fffcffcffcfcffcfcfcffcfcffffcfcfcf6fcfcfcf6fcfcfcf6fcfcf7f6fcfcccccf6f6fcfcfc6fcf6f6ccfcf6fcf7fccf6f7f6cccf6fccfcfccfccfcfcfccfcfcccf7fcfcfcfcfcfcfcfcfcfcfcfcfffffcffcfcfcfcfcfcfcfcfffcffffcfefcfffcfeffffcfcfcffcfff
                f7fcfefffffcfcfcf7fccfcfcfcffff7fcfcfcf7ffcfcffcfcfcff7ffcffcfcfcffcfcfcfcfcfcfcffcfcffcfcffcffcfcffff7fffcffcff7ffffcffcffcfcffcfccffcfcfcfcfcf6fcfcfcfccfcfccf6fcccf6cf6fcccccccc6cfccccccfc6cccfcccfcf6fccccfcf6fecf6cccfccfcccf6fcfcf7fcfcccf7f6fcf7fcfcfcf7fcfffffcfcfefcffcfcfcfcfcfffcfcfcfcfcffcfffcfffffcfcffcfcfcffcf7
                fffffffcfeffffffcfcfccfffffcf7fffcfcfcffcffcfcfcffcfcffcffcffcfffcffffcffcffffefcffcfcffcffcffcfffcf7fffcffcffcffcfcfcfcfcfcffcffcffcfcfcfcfcfcffcfcfcf6fcfcf7fcccfcf6fccfccf6fcf6fcf6cf6fcf6fcf6f6fcf6ccfccfcf6fcccf6fcfcf7fccfcf7fcfcfcfcccfcfcfcfcfcfcfcf7fcfcfcf7fcffcffcfcfcffcfcfcfcfcfffffffffcffcfcfcfefffffcffffffcffcf
                ffcffcfffffcfcf7fcfcfcf7fcfffffcfcfcfcfcfcfcfcffcfcffcffcff7ffcf7fcfcffcffcfcffffcffff7ffcffcffcfeffffcffcffcffcffcffcffcfff7ffcffcfcfcfcfcfcf6fcfcf6fcfcf6fcfcf6f6ccfccf6cccf6ccfcccfcccc6cccccfccc6cfcccc6f6cccfcf6ccf6fcccf6f6fcfcf6f6cf6f6ccccfcccfccf6fcfcfcfcffffcfcfcfcfcfcfcff7fcfcfcfcf7fcfcfcfcffcffcfcfeffcf7fcff7ffc
                fffefffefcffffffcf6fcfcfffcfffffccf6fcfcfcffcfcfcffcfcfcfcfffcfffffcfcff7ffcfcf7ffcf7fffcfcffcffffcfcffcffcffcffcffcff7ffcfcfcffcff7ffcfcfcfcfcfcfcfcfcfcfcfcccfccfcf6fccfcf6cfcc6c6c6c66cc6c6c6c6cfc7c66cfc6ecc6c6c7cccf76c66cc6cccf6ecc7ccccc6f6cc67ccf6ec6c6c6c6ccc7ccf7f6fcf7f6ccfc6cf6f6ccfcfcf76c7f6c7c6f67cf6cfcfccfcffff
                cffffcfffffcfcfcfcfccffcfffcfefcfcfcfcfcfcfcfcfcf7fcffcfffcfcfcfcfcfffcffcffffffcfffffcffffcffcfcffcfcffcffcfcfcfcff7ffcffcfffcff7ffcfcfcfcfcffcfcfcfcf7fcfcf6f6fccccfcc6f6cfcccfc7c6cc6b6c6b6c7c6b6b6ccc67b66c7c7c6cc67fcccbb7cc6c6bc6cc6c6767cb67cccc67cc6cb6c6bc6cf666c6bc766bcc766cbc67c76c766b6ccc6bc6c6cccc6b6c76b66cfcfcf
                fefcfffcfcffffcf6fcfccfffeffffffcfcfcf7fcfcfcfcfffcfcffcfcfffffcfffcfefcffcfcfcffcfcfcfcfcffcffefcffffcffcffcffcff7ffcffcffcfcfcffcffcfcfcfcf7ffcfcf7fcfcf6fcfcccf6fccfcfcccccf6cf6ccc6cccccccc6cb6bccc6cb6bcb6c6bcc6cccc8cc6c6ccc7b6ccc6c6bccb8ccb8c6ccc8fbc6ccc6c7ccccccc6cccccfccccf6fbcccc6cccbfcccc6bccccf6ccc7ccc6ccccfcfc
                fffffefffffcfcfcfccfcfcffffcffcfcf7fcffcfcf7fcf6fcffcfcfcfcfcfcfcfcfcfffcffcfcfcffcfffffcfcffcffffcfcffcffcff7ffcffcffcffcffcffcfcfcffcfcfcfffcffcfcfcfcfcfcfcfcf6fcf6f6ccfcf6cfcccf6fcccccc6fcccfccc8fc6ccf6fccc8fcfccccfcfcfcfccffccfcfccfccfccfcffcfccfcfcfcfccfcffcfcfcfffcfcfcffcffcffffcffcf6fffffccfcfcffffcffcfffcffffcf
                fcfcfffcfcfffcf7fcf7fcffefffcffcfcfcf6fcfcfcfcfcfcfcfcfffcffcffcffcffcfcfcffffffcffcfefcfffcffcfcffcfcffcff7ffcffcffcffcffcffcffffcfcfcffcf7fcfcffcfcfcfcfcfcf6f7cccfccfcf6ccfc6fc6cfcccf6fcfccfccfcfcccfccccccfccccccfcfcfcfcfcfcfcfcfcfcfccfcfccf6cfcfcfcfcfcfcfcfcffcfffcfffffcfcffcffcfcffcffffcfcfcffcfffcfcfffcffcffcfcffc
                fffffcfffffcf7ffcfcfcfcffcfffffefcfcfcfcfcfcfcfcfcfcff7fcfcff7ffcffcffcfffcf7fcffcffcfffcfcfcffcfcffffcffcfffcfcffcffcffcff7ffcf7ffcffcfcfffcffcf7ffcfcfcfcf6fccfcfccf6f7cfc6cfccfccccf6cfcccf6cf6fccccccfcfcfccfcfcf6cf6cfccfcfcfcfcfcf6fcfccf6fcfcfccfcfcfccfcfcfffcffcfcfcfcfcfffcffcffcfcffcfcffcfcfcffcfcfffcfcffcfcffcfcff
                cfefffcfcfffffccfcfcfffcffcfcffcfcfcfcfcf6fcfcfcfcfcfcfffcfcffcffcff7ffcf7fffffcff7ffcfcfffffcffff7fcff7ffcfcfffcffcffcffcffcfcffcffcffcf7fcfcffffcfcfcfcf6fcfcfcccf6fccfc6fcf7cc6fcf6cfccf6f6fccfccf6f6f6cc8ccc6cc6fcfcfccfcfccfcf6fcfcfccfcfcfcfcfcfcf6fcfcfcfcfccfcfcfcfffcfffcfcfcffcffffcffcfcfffcffcffcfcfcfffcffffcffcfcf
                """))
        if player1.y >= 2500:
            scene.set_background_image(img("""
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcffffffffffffffffffffffffffffffffffffffffffffcf8fffffffffffffffffffffffffffffffffffffffffcfcffcfcffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffcffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcfffffffffffffffffffffffffffffffffffffffffffffffffff8fcfcffffffffffcfffffffffffffffffffffffffcfffff8fffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffcffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffcffffffffffffffffffffffffffffffffffffffffffcfcfffffffffffcffffffffcffffffffcffffffffffffffffffffffffffffffffffffffffffffffcfcf8fffffffffcfffffffffffffffffffffffffcfff8fcffcffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffcffffffff8fffffffffffffffffffffffffffffffffffffffffffffffff8cffcffffffffffffffcfcfffffffffffffffffffffffff8fffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffff8ff8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcffffffffffffffffffff8fcf8fffff8fffffcffcffffffcff8ffffffcffffffffffffffffffffffffffffffffffffffffffffcf8fffffffff8ffcffffff8ffffffffffffff8fffcfcfcffcffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcf8fffcf8fffffff8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfccf8ffffffffffff8fcfffffffffffff8ffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffcffcffffffffffffffffffcfcf8ffffffffffffcff8ffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffff8f8fcffffffcfcfffffffcfcff8fcfffffffffffcf8fcffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcffcfcfcffffffcfffff8fffffffffffffffffffffffffffffffffffffffffffffffffffffcfcfffffffffff8fffcf8ffffcffffffffffffcffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffff8f8fcfffffffffff8fcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8f8cfffff8fcffffffcfcf8ff8cf8ffffffcffffcf8fffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffcffffffffffffffffffffffffff8ffffffffffffffffffffffffffffffffffffffffcffcff8fcfffffcfcfcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcfffffffffffcffff8f8ffcfcfffffff8ffffff8ffcffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffcffffffff8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcfcfff8ffffffffcffffffffffcfffffcfffffffffffffffffffffffffffffffffffffffffffffffffcf8fcff8fcf8fffffffcfcff8fc8ffffffffffffcfcfffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffff8fffffffcfff8fcfffff6cfcffffffffcffffff8fffffffffffffffffff8fcfffffffffffffffcffffffffffffffffffffff8fffffcfffcfffcfff8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffffffffffffcf8fccfcffcfffffffcff8ffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcff8fcfccfff8ff8ffffffffffffff8ffffffffffffffffffcffffffffffffffff8fcffffffffffffcf8fcfffcfffffcfffffffcffffcffffffffffffcffffffffffffffffffffffffffffffffffffffffffffcffcfffffffcffffffcfffcf8c8ffffffcffcfffcfffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffcffffff8ff8fcfcf6fcc6fcffcfffffffffffcffffffcfffffffffffcfcff8ffffffffffff8fffffffffffffffcfffffffcfffcffffffcffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffcfffcfffffff8fcfcfcf8fffffffff8fcffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffff8ffffcffffff8ffffcf6f6fc6fcf6f6cf8cfffffff8ffffffcfffffcfcffffffff8fffffffffffffffcfcfcfffcffcfffff8ffcffffffffcfcffffcffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcf8fffffffffffffffffffc8f8fffffcf8ffcffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffffffffffffffffffffffffff6ffccf6f6cc6f8cf6fffff8fffffffffffffff8fcffff8fffcffcffffffffffffcffffffffffff8fffcffffcfffffffffcffffcfffffcfffffffcffffffffffcfffffffffffffffffffffffffffffffffffffffffcf8ff8ffffffffffffffcfcfcfffffffcfffcf8ffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffcffffcf6f6f6f6fccf6fcfffffffffffff8ff8ff8ffff8fffffcffcffffffffffffcff8fcff8ff8fffffcfffcffffcffcffcfffcfffffffffffcffffffffcffffffffffffffffffffffffffffffffffffffffffffff8fcffcfffffffffffffffff8fcffcff8fffcff8ffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8ff8ffffffffffffff6f6f6c6f66f6fcffffffffffffffffffcfcffffffcfcffffffffffffffffcffffffffffcfffffcfff8ffffffffffcfffcfcfcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcf8fffffffffffffffff8ffff8ffffffcff8ffcfffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffff8fffffffffffffffffffffffffffffffff8ffffffffffffffff8ffff8ffcff6f6f6f6f6f6fffcfffffffffffffffffcfcfcffffff8ffcffff8fffffffffcfffffcfff8fcffffcffffffffcfffffcfffffffcffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffcffcfcfffffffffffffffffffcfffffcfff8fcffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffcc6c6f6f6c6f6cfffffffffffffffffcf8ff8ffff8fffcffffffffffff8ffffffffffcfcffff8fffffcffcffffcffcffcfcfffffcffffffffcfffffcfffffffffffffffffffffffffffffffffffffffffff8fcff8ffff8ffffffffffcfffffffffcffcffcfcffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffff8fcf8ffffffffffff8ffffff8ffff8fffffffcffffffffffffffffff6f6c6f6fcfcffffffffffffffcffffcfcffffffcffff8ffffcfcffffffcffffffff8fcfcfffcfcffffffffffffffffffcfcfffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffcff8fffcf8fffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff8ffffffffffffffff8ffffffffffcfffffffffffffff8ffcfffcff8fcfc6f6f6f6ccfcffffffffffffffff8ff8ffcffcff8f8ffffff8ffffffffffffff8fcfff8ffcffffffcffcffcffffcffcfffffcfcfffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcfffffffffffffffffffcf8ffffffffff8fcffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffcf8fcffffffffffffcffffffff8fffffff8fffffffffff8fffffff6f6cf6f6f6f6ffffffffffff8fffffcffcff8ffffcffcfcffffcffffffffffffffffcfcfffffcfcfffffffffffcffffffcfcffffffcffcffffcffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffcffffcf8ffcfffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffff8fcfcff8fffff8ffffffffffffffcffffcffffcf8ccc6f6cc6c6f6fcf8fcffff8fffffcff8fcf8fffc8cf6f8ccf8ffffffffffffffffcff8ffcfcf8ffffcfcfcfffcfffffcfffffcfcfcfffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffcffff8ffffffcffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff8fcf8fcfffffffffffff8ffffffffffffffffffffffffcfffcff8fcf6f6f6f6f6c6f6cfcfff8ffffffcff8fcf8fcf6fcf6f8fcf6fffcfff8fffffffffff8ffcff8ffffcffffffffcffffffffffcfffffcffcffffcffffffffffcfffffffffffffffffffffffffffffffffffffff8ffcfffffffffffffffff8fcffffcffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffcfff8fcffffffffffcfffffffcf8ffff8fff8fcf6f6f6cc6c66f6cf6f6fcffffcfcff8ffcf6fcf6f8ccf6f6f6fc8fc8fffffffffffffffcff8ffcfcffcf8fcfcffffffffffffffcfcffcffcfcffffffffcfffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffffcfffffffffffcffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffcffcf8ffcffffff8fcff8ffcfffc8fcf8f6f6f6f6f6c6666f6cfcffcff8f8fcfcf8cf6f6fcf6ccf6fcfcf6f6fcfcfffffffffffffcffcffffcffffffffffcffcffcffcffffffffcfffffffcfffffffffffffffcfffffcfffffcfffffcfffffcfffffffffffcfffffffffffffffff8fcffcf8ffffffffffffffffffffffffffffffffff
                fffffffffffffffffffffffffffffffffffffffffffcfffcf8fffffcff8ff8fffcff8fffffcfcffcffffcffcfcc6f6f6f6c6c66c6f6f6f6fcf8fccf6fcfcf6f6fccc6f6f6f8f6f6f6f6fffffffffffffcfffcffcfcffcfcfcfcfcffffffffffffffffcfffcfcffcffffcfffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffff8ffffff8f8fffcffffffcffffcff8fffcfcff8f6ff8fcff8f8f6f6f6f6cf6f6c6666c6f6f8f6c6f6ccccc6f6f6f6fcf6c6f6f6f6fcf6f6fcff8ff8ffffff8ffcffcfcfffffffffffcffcffffffffcffffcffffcffffcffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffff8fcfffcfffffffffffffffffffffffffffffffffff
                cfffffffffffffffffffffffffffffffffff8ffffff8ffcfc8fff8fcf8fffcff8ffcf8fff8c6f6cfcff8fcf6cc6f6f6f6866c666c66f6c6f6fcf6f6f6f6f6ccccf6c6f6f6f6f6f6f6f6ffffffffffcffffffff8ffcfcfcf8fcfcffffffffcffcfffffffffcfffcfcfffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffcfff8fffffffffffffffffffffffffffffffffffff
                ff8ffffffffffffffffffffffffffffffffffffcfffffcf8ffcf8ffffcfff8ffcf8fcf8fccf6cf66f6fcf6cc6f6c6f6ccf6f66f76666cf6f6f66f6f6f6f6c6c6f6fcc6f6fcf6f6f6f6f6ffffffffffffffcfcffcffcff8fffffffcffcffffffffffffcffffcfffffcfcfcfffcffffffffffffffffffffffffffffffffffffffff8ffcfffffffffffffffff8fcfffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffcf8f8ffcf8fcf8fcfc8ff8ffffcff8fcf8fcc6f66c6f6c6f6f66f66f6f6f66c6666666766f6cc6f6f66c6c66c66c6f6f6fffcfcf6f6c6f6c6cffffcf8ffcfffffcffcffcffcfcfcfffffffcfffffffcfffffcfffcfcffcfffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffcffffffffcfffffcfffffffffffffffffffffffffffffffffff
                cffcf8fffffffffffffffffffffffffffffff8fcff8fffcf8fcf6ff6fcfffcf8fff8fcf6f6f6c6c666fcf66666f6f6c6f6f6c676666c66f6f6f6cc6c667676c6c6f6f6fcf8fcfcfc6c6f6ffffffffcffff8fffcf8fcfcffcfffcf8fcffffcffcfffffffffffcfffcffcffcffffffcffffffffffffffffffffffffffffffffffffffffcfffffffffffffffff8fcfffffffffffffffffffcfffffcffffffcfffff
                f8ffffffffffffffffffffffffffffffff8fcfcf8cc6cf8fcf6ff6fff8ffffffc8fcf8f6f6c66c67678ccfc6f66c6f6f666c666b69766c66c6c6f66676b6bb676c6ccffffcff8fff6f66fcffff8ffffcfffcfcfcfcffcfcffcfffffffcffffffffffffcffffffcffcffcfffcffcffffffffffffffffffffffffffffffffffffcfffffffcffcffffffffffcfcffff8ffffffffffffffcffffffffffffffffffff
                fffcffcfffffffffffffffffffffffcf8ffff8f8c6ff6f6f6fccfcf6ffffff8fcfcf6f6f6f6c766666fccff66cf6f6c6f6f6676b9796b6766c6c66766b9b99b9b6c6ffcfffcfffcff6ffffffffffcf8fffcfffcffcfcfffcffcfcfcfffffcfffcffcfffffcfffffffffffcfffffffffffffffffffffffffffffffffffffffffffffcfcfffffffffffffffff8fffffffffffffffffcffffffffffffffffffffff
                cfff8ffffffffffffffffff8ffffcf8fcfcf8fc66f6cf6f6f6ff6fcfffffcffcf8f6f6f6f66667676ccf8cfc6f66ccc6c6c66b969b9b96b67666766b9699b9d9b7ccfffcf8ffcffffffffcffffff8fffcffcf8fcffcfcfcfcfffffffcfcfffcffffffffffffcfcfcfcfcfffcfcffcfffffffffffffffffffffffffffcfffcffcfcfffffcfcffffffffffffffcfffffffffffffffffffffffffffffffffffffff
                f8fffcf8fffffffffffff8ffffcfcfcc8cf6c66c666c6f6fcf6ff6fcfcffffffcf6f6f6f6c67666c6cfcfcfc6cf6f6f6f66c76b9d999b96b6b676b96b9d9d9db6b6cfffffffcfffcfffcfffcfffffcffffcfcffcfcfcfcfffcf8fcfffffffffffffffcfffffffffffffffcffffcffffcfffffffffffffffffffffffffffffffffffffcffcffcffcfffffffcff8ffffffffffffcfffffffffffffffffffffffff
                ffcf8ffffcffffffffffffcfcfffcfcccc66666666c66c6f6fccfcf8ffffffff8ff6f6f6c666b66cffcfcfff66f66f66c6c6b9d9d9d9d9d9b9bb969b99d9d99bb6cccffcfcfffcfffffffcffffffffcfcffcfcfcf8ffcfcf8ffcffcfcffcffcffcffffffcfffcffcfffcfffcffffcffffffcfffffffffffffffffffffffffcfcffffffcffcffcfffffcffff8ffffffffffffcfffffffffffffffffffffffffff
                cffffcf8ffffffffffffcfffffcfc8c6c6b6b766c66c66c6c6f6f6ffffffcf8ffcfccc6f66c666ccf8cff8fcf66f6ccf66679b9d9d9d99b69699b9b9d99b9d9b9b6cfffffffcffffffffff8fffffcffff8fcfcfcffcffcfcffcffffffffffffffffcfffffffffffffcfffffffcfffcfffcffffffffffffffffffffffffcfffff8fff8ffcfcfcffcffffffffffffffffffcffffffffffffffffffffffffffffff
                f8fcf8fffffffffffffff8f8fffccc6b796969676676766c6f6f6fcfcffff8ffff8f6f666676b6fcffcfcfff6cf6f666c67b99d9d919d9b7bb9b99999d9d9d9b7bc7cffffcfffffffffffffcffffff8fcfcffcfcfcfcfcffcffcfcfcfcfcfcffcfffffcfffcffcfffffffcffffcffffcffffffffffffffffffffffffffffcfffffffffcfcfcfcffcfcfffffcfcfffffcffffffffffffffffffffffffffffffff
                fff8ffcfffffffffffffffffffcc6b7b9b9b96b6b6c6b6766c6fcf8fffffcfcffcf6c66c66666c8cffffffccf66c6fcc67b9b9d919d9d9b6b6b9db9b9d99d9d9b6bcffffffff8ffffffffcff8fffffffcffcfcfcfcfcffcffcffffffffffffffffffcffffffffffcfffffffcffffcfffffffcfffcfffffcfffffffcfffcfffcffffffffcffcffcfcfffcffffffffffffffffffffffffffffffffffffffffffff
                cfffcfffcfff8fff8ffffffffcf6cb99d99b7b6b6b96b9666c6f6fcffcfff8ffff8f666666666cfcf8fffff8cff6f6c66b9b9d9d9d19dbbb6b9b69d979d9d9db9b6c6fffffcffffffffffffffcffcfcfcfcf8fcfcfcfcf8fcfcfcf8fcf8fcfcffcfffffffffcfffffcffffffffffffcfcfcfffffffffffffffffcfffffffcfffcfffcfffcffcfcffcfcffcffcfffffffffffffffffffffffffffffffffffffcf
                f8fff8fffffffffffffffffcfcccb9d99b9999b99b9b96bb6666f6ffcf8fffff8fcc6c666766cfcfcfffc8fffcf6c6f67b99d9d919d9d96bb6bbdb9b99d99d9bb6bccffffffffffcfffff8fcffffffcfcfcfcfcfcfcf8fcfffcffcffffffffffffffffcffcfffcffffffcffffffffffffffffcffffffffffffffffffcfcfffffffffffcffcffcfcfcffcffffff8ffffffffffffffffffffffffffcffffcfffff
                fffcffffff8fcffffffffff8fcc6d9d9d9db9b9b99799d969766cf6ffcffcfccf6f666666666fcffffc8fffcfff8f66c69b9d91d919d9bb6cbb9b999d99d9d9b6b7cfcfffffffcffffffffffffcffcfcfcfcfcfcfcfcffcfcffcffcfcfcffcfcffcfcffffffffffcffffffffffcffffcffcfffcffcffffffffffffffffffcfffcfffffffffcffffcfcfcfcfcfffffcffffffffffffffffffcfffffffffffffff
                fffffffffffff8ffffffffffcc6b79d9d99d9b99d9d9b97966666cf6fcf6f6f6f6c6ffc6c6cfffcffcfcffffffcf6c67bb9d9d919d19dbbb6c6bb6d79b9d9d9b7bc6cffffffcffcf8ffffffcffffcf8fcfcfcfcfcfcfcffcfcffcffffffcfffffffffffffffcfffffcffffffcffffcffffffcffffffffffffffffffcffcfffffffffffffcfffcffffcffcffffffcffffffffffffffffcfffffffffffffffffff
                fffffffff8fcfffffffffcfffc6b9d9d9d9b9d9d9d99d696b66666cc6f6f6f6c6f6f6cffffcfcffff8fcfffcfffcf6c669d9d9d9d9d9d6b6ccb6b999b9d9b9d9b6ccfcfffcfff8fffffffffff8ffcfcfcf8fcf8fcfcfcfcffcf8fcfcfcfffcffcfcffcffcfffffcfffffffcffffffffffcffffcfcffcffcffffffcffffffffcfffffffffffffffcfffcffcfcffffffcfffcfffffffcfffffffffffffffffffff
                ffffffffffff8fffffffffffccbb9d9d9d9d9d9d9d9b9bb696c6c66c6f6c6c6f66f6fc6fcf6fffcfffff8fff8fffcfc6bb9b9d9d1919b9bccc6bb9b9b9b99d9bbccccfcffffcffcfffffcff8fffcfcfcfcfcfcfcfcfcfcfcffcfffff8ffcfffcffffffffffffcfffffffcffffffffffffffffffffffffffffffcffffcfffcfffffffffffffffffffcffcfcfffcfcfcffcfffffffcfffffffffffffffffffffff
                ffffffffffcfffffffffffffcc6bb9d9d9d9d9d9d9db9b6cccc6f66666f6f6666cfccffffffffcfffcfffffffffcf8fc66b9b9d9d9dd9bb6ccc6b9b9b99b9b9b6bcfcfcfffcfcffcfcffffffffcfcfcfcfcfcfcfcfcfcfcfcffcfcfcffffcffffcffcffcffcffffcffcfffffffffffffffffcffcfcfcffcffcffffcffffffffffffffffffcffffffffffffcfffffcffcffffcfffffffffffffffffffffffffff
                ffffffffffffffffcfffcffffcc6d9d99d9b9d9d999bb6bc6fcfcf67c66666c6f6ff8fcffcfcff8fffffffcfffcfcccfcc6c7b9d9d9dbb6cccc7b9796d9d99d9bc6f6ffcfff8fcffffcfffffcfcfcfcfcfcfcfcfcfcffcffcfcfcfffcfcfffcffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffcfffffffcfffffffffffffffcfcffffffcffcffcfcfffffffffffffffffffffffffffff
                ffffffffffffffffffffffffcf6cb9b9d9b9d9d9dd9bbbcccffff6f666c6c6f6cfcffcfffffffcfcfffcfffffff8ff8fcfcf6bb9d919b6bccfc6b9b9b9b9b9db6c7fccfffcffcfffcffcfccfcfcfcf8fcf8cfcfcfcfcfcfcf8fffcf8fffcfff8fcfcfcffffffcffcffffffffcffcffcffffffffffcfcfffcfcfcfcfcfffffffffffffffffffffffffffffcffcffcffcffcffcfcffffffffffffffcfffcfffcff
                fff8ff8ffffffffffffffffffccc6d9b9b9d9d999d9b66c6cffcffcff666f67ffffcfffffffffffffffffffffcffcffcfcfccb9d9d9dbb6cc6c679b9b99b9d9b7cccfcfcffcf8ffcffffcfcfcfcf8fccfcfcfcf8fcfcf8fcffcfcfcffcffcffffffffffcffcfffffffffcffffffffffffffffffcfffffcffffffffffffffffffffffffffffffffffffffffffffffcffcffcfffffcfffffffffffffffffffffff
                ffffffffffffffffffcfffffffcc6b9b99b99d9d9db9bccccfffffc8cf6f6ffcfcfffffffcffffffff8fcffffffffcff8fff6cb9d9d9b6cccfc7b69b9b9b99d6b6cfcfcffffffffffcfcffcfcf8cfcfcfcfcfcfcfcfcfcffcfcffcffcffcffcfcffcffffffffffcffcfffffffffffffffffffffffffcfffcfcfcffcffffffffffcfffffffffffffffffcfffffffffcffcffccfcfffcfffffffffffffffffffff
                f8ffcfcf8fffffcfffffffffcf8ccb69b9d9b9d9d96bcc7f6cfffcffcffcfc8ffffffffcffcf8ffffffcffffff8fff8fffcfc7bb9d99bcccfcc66b9b9b99b9b9cccfcfffffcffcfcffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffcffcffcffffffffcffcfffcfffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffcffcffcfcfcfffcffcffffffffffffffff
                fffcffffffcfffffffffffffffcc6b9b9b9d9d9d9bb6cccccfcfffcf8fffcfcfcffffcff8f8ffcfffcf8f8ffffffcfffcffccc6d9d9db6cfcfcc6b69b96d979bc6ccfcfccffcfffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfffcfcfcfffffffffffffcfffffcffcfffffffffffffffffffcffcfcffcffffffffffffffffffcfffcfffffffffffffffcffcffcffcfcfcfcffffffcfffffffffffff
                cfff8f8fcfffffffffffffffcfcc6b79b9b9d9b99b6cccfcf8fffffcfcff8fffffcffffcffcfcfffffffcfffffffffcfffffc6bbb9d9bcccf6cc6b9b69b9b9b9c7cccfcfcfcffcfcffffcfcfcfcfcfccf8cfc8fcfcfcfcffcfcfcfffcffcfcffffff8fcffcfffcffffffcffffffffcffffffffffffffffffffffffffffcffffffcffffcfffffffffffffffffffffffffcffcffcfffcffcfcfffffffcfffcffff
                ff8ffffcf8fcfffffffffffff8cc7b9b9b99b99d9bcccf6fcfffff8fcfffffcffffffcffcff8fffff8fffffffffffffffffcfc76b99d6ccffcf6c66b9b9696db6cccf6fcfcfcfffffcfffcfcfc8fccfcfcfcfcfcfcfcfcfcfcfffcf8ffcfffcfcfcffffffffcffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffcfcfcfcffcffcfffcffffffffff
                8ffcfcfffcfffffffffcfffffcc6b6b999b9d9b9b66cfcfffcffffffffffcffffffffff8fcffcffcfffcfffffffcffffffffcccb6d9d6ccfcfccc66b69b6b97b6cccfcfcfffffcffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffcfffffffcffcfffffffcfffffffffffcfffffffffffffcffffffffffffffffffffffffffffffffffffffffcffffcffffffcfcffcffffffffcffcfffcffffffffffff
                fffff8f8f8f8fffffcffffffffcc7b9b9b9d9b9b96cfcffffffffffffffffffffffffcffff8fffffffffffffcffffffffffcfc6c7d9bbcfffcfcf6c6b67969b6bccfcfcfccfcfffcffffcfcfcfcfcfccfcfcfcfcfcfcfcfcffcf8ffcffcffcfcfcffffffffcfffffffffffffcffffffffcfffffcfffffffffffffffffffffffffcfffffffffffffffffffffffffcffffffffffcfcfcffcffcfcfffffcfffffff
                cfcf8ffcfcffffffffffffffccc6bb9b979b9d996bcffffffffffffffcffffffffffffffcfffcfffffffffffff8fffffffffcfccc99b6ccf6fcf6c666b6b9b9bccccfcfcffcffcfffcfcffcfcfccfcfcfccfcfcfcfcfcfcfcf8ffcffcffcffffff8ffcffcffffcffcffffcffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffcffcfffffffffcffcffffcfcffffffcfff
                ff8ffcff8fcfffffffffffffffc7b6b969b99b6b978fffffffffffffffffffffffffffffffcffff8ffcffff8fcfffffff8fffcf6cb99e6ffffcfcc6c669669b66cf6fcfcfcffffffffffcfcfccfcfccfcfcfccfcfcfcfcfcfcfcffcffcffcf8fcffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffcffffffffffffcffffffffffcfcffffffcfcfffcfcfcfffff
                cffcff8fcf8fcfffffffffffcccc6b79b69b9b99b6cfffffffffffffcfffffffffffff8ffffff8ffffffffffcfcfcfffffcf8fcfc79b6ecfcff8f8c66b6b969bcccfcfcfcfcfcfcfcfcffcfcfcfccfcfccfcfcfccfcfcfcfcffcfcfcffcfffffffcfcfcfffcffcffcffffffffffcfffcffffffffffffffffffcfffffcffffffffffffffffffffffffffffffffcfffffcffcffffffffffcfffcffcfcfffffffcf
                ffff8fcf8ffffffffffffffffcf6e6b69b6b9b6b97cffffcfcfffff8ffffffffffffffffff8fffffcfcfffcfff8fffffcffcfcfcc697cccfffcfcc6c66696d76bcfcfcfcfcfffffffffcffcfcfcfcfccfcfcfcf8fcfcfcfcfcffcfffcffcfcfcffffffffcffffffffffffffffcfffffffffffcffffffffffffffffffffffffffffffffffcfffffffffffffcffffffcfffffffffffffcfffcfffcfffcfcfcfcff
                f8fcfcf8fcfcfffffffffcfffcccc7696b96b6969bcfffcf8fffffcffcffffffffffffffffffffffffffffff8ffcfffff8f8f8fcf9b9c6fcffffcf6666b6969bcfcfcfcfcfcfcfffcfffcfcfcfcfccfcfcfccfcfcfcfcfcfcfcffcf8fcffffffcfcffcffffffcffcffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffcfffffffcfffcffcfcffffc
                ffff8fcfcffffffffffffffffffccc6b66b69bb9b9ccff8ffffffff8f8fffffffffffffffffffffffcffff8ffcfffffffffcfcfcf969cccfffcf86f6c66769b6ccfcfcfcffffffcfffcffcfcf6fcfcfcfccfcfcfcfcfcfcffcfcfcffffcf8fcffffffffcffcfffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffcffcffffcfffcfffffffffffffffcfffcfcff
                ffcff8f8ff8ffffffffffffffcff6c76b66b696b9678ffcfcffff8fcffffffffffffffffffffffffffffffffcfcffff8fcffcf8ffb97ccfffffcf6c6c66696b7cfcf6fcfccfcffffcffcfcfcfcfcfcfccfcfcfcfcfcfcfcfcfcfcfcfcffcfffcfcfcfcfffffffffcfffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffcfffffffffffffffffcfffffcffcfcf
                fff8fcffffffffffffffffffffcffc6666696b969bbccff8ffffffcf8fcfffffffffffffffffffffffffffcffffffffffffcfffff66bcc8fffcfc6f6666669b6ccfcfcfcffcffcffffffcfcfcfcfccf8fcfcfcfcfcfcfcfcfcffcffcfcffcfffffffffffcfffcfffffffcfffcfffcfffcffffffffffffffcffffffffffffffffffffffffffffffffffcfffffffffcffcffffffffffffffffffffffcfffcffffc
                ffffffcfcffffffffffffffffffffcc676b6b6b9796ccffffffffcfcffffffffffffffffffffffffffffffffffcfffffffff8fcff969fcfffff8f66f6c6676b6cfcfcfcfcffcfffcfcfcffcfcfccfcfcfcfcfcfcfcfcfcfcffcffcffcfcffcfcf8fcfcffffffffffcffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffcfff
                ffcffffffffffffffffffcffffffcf766666b66b9bb6fffffffff8f8fcffff8fffffffffffffffffffffffffcffffffffcfffffffb6bc8cfffcf6cc6c66669b6cfcfcfcfcfcffcffffffcfcfcf8fcfcfcfcfcfcfcfcfcfcfcf8fcfcffffcfffffffffffcffcffcffffffffcffffffffffffffffffffcffffffffffcffffffffffffffffff8ffffffffffffffffffffcffcfffffffffffffcffffffffcffffcfc
                fffffffffffffffffffcfffffffffc66b6b66b969d6eccfcffffffcffffffffffffffffffffffffffffffffffffffffffffffffff696cfffffcf6c6f6c666b67cfcfcfcfcffcffffcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcff8fcfcfcfcfcfcffcffffffffffcffcffffffcffffffffffffffffffffffffffffffffcfffffffffff8fffffffcffffffffffffcfffffffcfffffffffffffffffffffcfffff
                fffffffffffffffffffffffffffffc666666b6bb9bbcfcffffffcf8fcffffcffcfffffffffffffffffffffffffffffffffffffffc6b7ccffff8f6cc6c66667b6cfcfcfcfcfcffcfffffcffcfcfcfcf6fcfcf6fcfcfcfcfcfcfffcffcfcffffffffffcfffcffcffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffffcffcffffffcfffffffffcffffffffffff
                fffffffffffffffffffffffffffcff766b666b66997c6c8fffffffcffffffffffffffffffffffffffffffffffffffffffffffcfcfb96cffffcfc86f6f6c669bccfcfcfcfcffcfffcfcffcfcfcf6fcfcfcfcfcfcfcfcfcffcfcfcfcffcfcfc8fcfcffffcfffffffcffcffffcffffffffffffcffffcfffffffffffffffffffffffffffcffffffffffffffffffcffffffffffffffffffffffffffffffffffffcffc
                fffffffffffffffffffffffffffffcc666b666b6b9bccfcfffff8ff8ffffff8ffffffffffffffffffffffffffffffffffffffff8c669cfffffff6c6c66666766cfcfcfcfcfcffcfffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcfcfcffcfcffffff8fcffffcffffffffffcffffcffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffcffcffffffffffffffcffffffffcffffffff
                fffffffffffffffffffffffffffffc66766b666b9b6c8cffcffffcffffffffffcfffffffffffffffffffffffffffffffffff8ffcf9b7cffffcfc66f6f6c66bbccfcfcfcfcffcffffcffffcfcfcfcfcfcfccfcfcfcfcfcfcfcfcffcfcffffcfcfcfffffcffffcffcffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffcfffffffffffffcffffffffffffffffffffffffffffff
                fffffffffffffffffcfffffffcffffc66666c6b669bccf8fffff8fcfffff8fcfffffffffffffffffffffffffffffffffff8ffffcc69bcfcffff86c6c6c666966cfcfcfcfcffffcffffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffffcfcfffffffcfcfffcfffffffcffcffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffcfffffffffffcfffffffcffffffffffffffcfffffcfffff
                fffffffffffffffffffffffcffffcf666b6b6c66b97fc8ffffffffffcffffcf8fcfffffffffffffffffffffffffffffffffffffcc7b9ccfffffc6ccc6c6676bccfcfcfcfcfcffffcfffcffcfcfcfcfcfcfcfcfcfcfcfcffcfcf8fccff8fcfcf8ffffffcfffffcfffffffffcffcfffcffffffffcfffffffffffffffcfffcffffffffffffffffffffcfffffffffffffffcffcfffffffcfffffffcfffffffffffcf
                ffffffffffffffcffffffffffffffcc766666c6c6bbcffcffffcf8ffff8fcfcfffffffffffffffffffffffffffffffff8ffffffcf96b6fcffff666f6f6666b67cfcfcfcffcfcfcfffcffcfcfcfcf6fcfcfcfcfcfcfcffcfcffcfcffcffffffffcfcfcffffcfffffcffffffffffffffffffffcfffffffffffffffffffffffffffffcfffcfffffcffffffffffffffcffffffffffffffffffffcfffffffffffffff
                ffffffffffffffffffffffffffffff6666c6c6c6697cfffffffffffffffcf8f8fffffffffffffffffffffffffffffffffffffffcc69bcffffff666c66c6667b6fcfcfcfcfffffffcffcffcfcfcfcfcfcfcfcfcfcfcfcfcffcffcffcfcfcfcfcfffffffcffffffcfffcffcffffffcffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffcffffffffffffffffffffffffcfffffff
                ffffffffffffffffffffcfffffffcfc66b66c6f66b9ffffffffffcffcfcf8fcffffffffffffffffffffffffffffffffffcffffffcb976cfcfcf66c6f6f66696ccfcfcfcfcfcfcffffffcffcfcfcfcfcfcfcfcfcfcfcfcfcf8fcfcfffffcff8ffcfcfcfffcffcfffffffffffcfffffffcfffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffffcfffcffffffffffffffffffffffffffffff
                ffffffffffcffffffffffffffffffc6c666c6c6c67bcfcfcffffffffff8fcffffcfffffffffffffffffffffffffffffffffffcfcc69bcffffff666c6c6667b6ccfcffcfcfcffffcfcfffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfffcfcf8ffcfffffffffcffffffffcffcfffffffcfffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffcffffffcffffffffffffffcfff
                ffffffffcffffffffffffffffcffff676666c6f669b6f8fffffffffffcfcf8fcfffffffffffffffffffffffffffffffffffffffc6b79c7fcfcf66c6f66c669b6fcfcfcffcffcffffffcff6fcfcfcffcfcfcfcfcffcffcffcffcfcfcfffcfffcfcf8fcfffcfffcffffffffcfffffffcffffcffffffffffcfffffffffffffcfffffffffffffcffffffffffffcffffcfffcffffcffffffcfffffffffcffffffffff
                ffffffffffffffffcffffffcffffccc66c6c6f6c6b9fcffcfffffffff8f8fffffffffffcfcffffffffffffffffffffffffff8fcf6b9b6cfffffc666c6f666b6ccfcfcfcffcfffcffcffcfffcffcfcfcfcffcfcfcffcffcffcffcfffcfcffcfffffffffcfffcffffcfffcffffcfffffffffffffffffcffffffffffffffcffffffffffffcfffffffcfffffffffcfffffffffcfffffffffffffffcfffffffffffff
                fffffcffffffffffffffcfffffffff6c7666c6f667bccf8fffff8fffffcfcfcfffffffff8ffffffffffffffffffffffffffffcfcb6d9ccfffcff66c6c666797cfcffcfcfcfcfffffffffcfcfcfcfcfcffcfcffcfcfcfcfcfcfcfcf8fffcffcfcfcfcffffcffffffffcfffffffffffffffffffffcfffffffffffffffffffffffffcffffffffffffffcfffcff8ffcffcfffffffffffffffffffffffffffcfffffc
                ffffffffffffffffffffffffffffccc6666c6f6c6b9c8ffcffffffffcffffffffffffffcfffffffffffffffffffffffffffffcc8c9bb7cffffcf666c66666b6ccfcffcfcfffcfcfcfcfffcfcfcfcfcfcfcfcfcfcfcfcfcfcffcffcffcffcffffffffcf8fffffcffcffffffcfffcffcffcffffffffffffffffffffffcfffffffcffffffffffffffffffffffffcfffffffcfffffffffffffffcfffffffffffffff
                fffffffffffffffffffffffffffffc676b66c6f666bccfcffffcfcffff8f8ffffffffffffcfffffffffffffff8fffffffffcf8fcb79b6cfffcfc6666f6667b6cfcfcfcffcfffffffffcfcfffcfcfcfcfcfcfcfcffcffcffcfcfcffcffcffcfcf8fcffffffcffffffffffcffffffffffffffffcffffffffffffffffffffffffffffffcfffffffcfcffcfffcfcf8fcffcfffffffffffffffcffffffffffffffcff
                cfffffffffffffcfffcfffffffcfcf6b6766c6c6c79c8ffcfffffffffffffffffffffffffffffffffffffffffffffffffffffccc6b6b6cffff8f666c66c66b6cffcfcfcffcfcffcffffffcf6ffcffcfcfcfcffcfcfcffcff8fffcffcffcffffcfffcfcfcfffffcffcfffffffcfffffffffffffffffffffffffffcfffffffcfffffffffffffffffffffffffffffcffffffffffffffcfffffffcffcfffffffffff
                ffffffffffffffffffffffcffffff6c76b6b6f6f696cccff8ffffffffffffffffffffffffffffffffffffffffffffffffffcfcccc6b9ecffcffc6666c6666bcccffcffcfcfffffffcfcfcfffcffcfcffcffcfcfcfcfcf8fcffcffcffcffcf8fffcffffffffcfffffffcfffcffffcffffffcffffffffffffffffffffffffffffffefffffcffffffcfcfffff8fcff8fffffffffffffffffffcffcfffffcfffffff
                cfffffffffffffffffffffffffffcc6b696666c66b7cf8cfffffffffffffffffffffffffffffffffffffffffffffffffffffcf8c6b6bcfffffcf666c6f676b6cfcffcffcfcfcfcfffffffcfcfcfcfcfcfcfcffcffcffcfffcfcf8fcffcffffcfcffcf8fcfffffcffcfffffffffffffcffffffffffffffffffcfffffffcffffeffffffefffffcfffffffffffff8fffcffcfffffffffffcffffcffffcfffffffff
                fffffffffffcfffffffcfffffffffcc6b6bb6c6c66bcfcf8ffcffffffffffffffffffff8ffffffffffffffffffffffffffff8cccc76b6fffffff6666c66667ccffcfcfcffffffffcfcfcffcfcfcfcfcfcfcfcfcfcfcffcfcfffcfffcffcfcffffcfffffffcffffffffffcffffcffffffffffffffffffffcffffffffcffffeffffffffffffffffffcfffcffcfcffcffffffffffcfffffffffcfcfcffffffffcff
                fcffffffffffffffcffffffffcfffc676b6676c6c766ffcfff8fcfffffcffffffffffffffcff8ffffffffffffffffffff8fffcf6ccb7cffffffc666c6666b6bcfcffcffcfcfcffffffffcffcfcfcfcfcffcfcffcffcfcfcfcfcffcffcffffcfcff8fcfcffffcffcffcfffffcffffffffcffffffcfffcfffffffffffffffffffffefffffcfffffcfffcfffffffffffff8ffffffffffffffcffff8ffffffffffff
                ffcffffcfffffffffffffffcfffffcc6b6b6b6c66bbccfffffcffffff8ffcffffffff8fcfffffffcfffffffffffffffffffffcccc66bcfffffff666cf6c66b6cffcffcfcfffffcffcfcffcffcffcffcfcfcffcfcfcfcffcff8ffcfcff8fcff8fcfffffffcffffffffffffcfffffcffcfffffcffffffffffffffffcffffeffffeffffeffffcffffffffffffff8fcffffffffffffffffffffffcfffcffcfffffff
                cf8cfffffffffffffffffcffffffcfc6666b66c676b6ffffffffffffffcffffff8ffffcf8fffcfffffffffffffffffffcffffffcc76bcfcffcff66c66c6676ecfcfcfcffcfcffffffffcff6ffcfcfcfcfcfcfcfcfcffcffcffcffffcffffcffffcfcfcffffcfffcffcfffffffffffffffffffffffffffffffffcfffffffffeffffffffcfffffffcffffffffffffffcfffcfffffffffffffffffcfffffffcffff
                fcfcfffffffffcffffcffffffffffcf76b66b6c6c6b6fffffffffff8fcffffffffffcfffffffff8fffffffff8ffffffffffffcfcf6b6cfcfffff666cf6666b6cffcfffcffcffcffcffffcffcfcfcfcffcfcfcfcfcfcfcfcfcffcfcffcfcfffcfcfffff8fcfffcfffffffcfffcfffffffffffffffffffffffffffffffeffffffffeffcfffeffefffffcfffcfffffffffffffffffffffffffff8ff8fcffcffffff
                ff8ffffffffffffffffffffffffffc6c66c6c76c67b6effcfffcfffffffffffffffffffcfffffffcffffffffffffffffffffffff7c7bcccfffcfc6666f676bccfcfcfcfcfffffffffcfcfcfcfcfcfcfcfcffcffcffcff8fffcff8fcffffcffcffcfcfcfffffffffcffcffffffffcfffcffffffffffcfffffcfffffeffffefffeffffffeffffffffffffffffffcfffffffffffffffffffffffffcffffff8fcffc
                fffcffffffcfffffcfffffffcffcffc6c66c6c666b6cfffffffffffffffcff8ffffffffffffcffcfffffffffcfcffffffffffffcc66bcffffffc66cf66c6676cffcffcffcfcfcfcffffffcffcfcfcfcfcfcfcfcfcfcfcfcfcfcffffcf8ffcffcfffffffcfcfffcffffffffcfffffffffffcfffcfffffffffffffeffffffffeffffefeffffffffcffcffcfffffffffffffffffffffffffffffcfffcf8fffcfcff
                fffffffffffffffffffffcfffffffcc66c6c6c6c66b6cffffcfffffffcfffffffffffffffffffff8ffffffffffffffffffffffcf6b67cfffcfcfc666f666bb6ccffcffcffcffffffcfcfcfcfcffcfcfcfcfcfcfcfcfcffcffcfcfcffcfff8fffcf8fcffffffcfffffcfffffffcfffcffffffffffffffffcffffffffffeffffffefffffffcfefffffffffffffffffffffffffffffff8ffffffff8fffffcff8fff
                fcfcfffcfffffffffffffffffffffcf6c6f66f6c67bcffcfffffcffcfffffffffcffcffcfffffffffffffff8ffffffffffffffccc7b6cfffff8f6b6c6f6667bfcfcfcffcfffcffcffffffcfcfcfcfcfcfcfcfcfcffcfcffcffffcfcffcffcfcffffcff8ffffffffcffffcfffffffffffffffffffffffffffffeffffefffeffefffffefffffffffcfffffffffffffffff8ffffff8fffffff8ffffffffff8fcfcf
                fffffffffffffcffffcffffffcfffc6c676f6c6c66b6ffffffcfffffffffcffcfffffffffcffcffcfffcffffffffffffffffcfcc6b6bccfffcfcb66f6c667b6cfffcfcffcfffffffcfcf7ffcfcfcfcfcfcfcfcffcfcffcfcfc8ffffcffcfcffcfcffcfffcfcfffffffcffffcfffcffffcffffffffcfffffffffffffffffffffffeffffeffeffefffffcffffffffffffffffffffffffffcffffcfffcffcfffcf8
                ffcfffffffffffffcfffffcfffffffc6f66c6f6f667ccffcfffffffffcffffffffffffffffffffffffff8ffffffffffffffffcc6e79b6fffffcf666c6f666b6ccfcfffcffcfcfcfffffffcfcfcf6fcfcfcfcfcfcfcfcfcfcfffcfcffcffffcffff8fffcfffffcffcffffffffffffffffffffcffffffffcffffffeffeffefefefffefeffffffffffcfffffffffffffffffffffffffffffffffffffffffffcffcf
                fcfffffffffffffffffffffffffcfcf76c6f6c6c6cb6ffffffffcffcffffffffffcffcffffcffffffffcffffffcffffffff8fcc6bb6bccffffffb66f6c66b6bcffcfcfcfcffffffcfcfcffcfcfcfcfcf7fcfcfcf6fcfcfcfcfcffcf8ffcf8ffcfcffcffffcffffffffffcfffcffffcfffffffffffffffffffefffffffffffffefeffffefefefcfffffffffcffffffffffffffffffffff8fffffffffff8ff8ffc
                ff8ffffffcffffffffffcffffcfffc6c66c6f6f6676ccfffcfffffffffffcfffcffffffcfffffcffffffffffcfffffffffffcf6e6db9cffcffcf9b6c6f667b6cfcffcffcffcfcfffffcfcfcfcfcfcf7ffcfcf6fcffcfcffcfcfcffffcffffcffffcfffcffffffcffcffffffffffcffffffcfffffcffffffffffffeffefefefffeffefffffffffefffefffffffffffffffffffffffffffffffffffffffffffcff
                fffffffcfffffcffffcfffffffffffc6c6f66f6f66bcffcffffcfffffcfffffffffffffffffcfffcfffcfffff8fcf8fffcffccc7b6b6ccfffffc666f6c666b6cffcffcffcfffffcfcfffcffcfcf7fcfccfcfcfcfcfcfcfcfffcfcfcffcffcffcf8ffcffcffcfffffffcffcfffcffffffcfffffffffffcfffeffffffffffffefeffcffefefefcfffeffffffffffffffffff8fffffffffffffffffff8ffffcfff8
                ffffffffffffffffcffffffcffffcfc6c66f6c6c6c76cfffffffffcffffffcffffcffcfffcfffffffffffff8fcfffffffffffcc6bb6bccfcffcfd66c6f667b6ecffcfcfcfcfcfffffcfcfcfcf7fcfcfcfccf7fcfcfcfcfcfcffffcfcffcff8fffffcffffcfffcffcffffffffffffffffffffffcffffffffffffeffefefecffeffefefffffffffeffffffeffffffffffffffffff8ffffffffcfff8ffffcffcfff
                fffffffffffffffffffffffffffffcc67f66f6f666bcfffffcffcfffffcfffffcffffffffffffcffcfffffffcf8cfcfffffcffcc6bb6ccfffffc96c6f6666bbcfcfcffcffffffcfcfffcfcf7ffcfcccf6fcfcfcfcfcfcfcfcfc8ffffcfffcfcfcfffcf8ffffffffffffcfffcfffffcfffffffffffffcfffcfffffffffeffeffeffffefefefefffffffeffffcffffffff8fffcfffffffffffff8fffffcf8ffcff
                ccfffcffffffcffffffffcfffcffffc6c66f6c6f6c7ccffcffffffffcfffffcfffffffcffcffffffffcfffffcffcfffffcffcfccc6bb6fcffcfcb66c6c6c6b6cffcfcffcfcfcffffcf7ffcffccfcfcfccf7fccfcf6fcfcfcfcffcfcffcffffcffcffffffcffcfffcfffffffffcffffffffffcffffcfffcfffeffefefffcfefefefeffffefffeffeffffffffffffffffcfffcfffffffffff8fcffcfcffffcff8f
                f8ffffffffcfffffffcfffffffffcf6c6c66f6f6666cffffffffffcfffffcfffffcffffffffcffcffffffffff8cf8fcffffffcf6c7c6cfffcfcc966f6f6679cccffcfcffcffffcfffffcfcfcfccccf7fccfcfccfcfcfcfcfcfcffcfcff8fcf8ffff8fcfffffffcfffcfffcfffcffffffcfffffffffffcffffffffffefefeffffefefeefffeffffffefffcfffffffffffcfff8ffffff8ffcfcfcf8ff8fcffffff
                cffffffffffffffcffffffffffcffcc7c6f66c6c6c7ccffffcffcfffffcfffffcfffcffcffffffffcffcfffffcfcfffffcfcffccccccffcffff67666c6666b6cfcffffcffcfcffcfcfcffcf6fcfcf6ccfccccfcf6fcffcf7cccccfffcfffffcffcfffffcfcfffffffffffffffcffcfffffffffffcfcfffcfcffeffffffefcfefeefeffefeffefeffffffffffffffffcfffffffffffffc8fcf8fcfcfcff8fcfcf
                cfffffffcfffffffffffffcfffffffc6c66f6f6f66b6ffcfffffffffcfffffcffffffffffcffcffffffffcfffffffffcfffffffccc67cfffcfccb6c6f6c67b6effcfcf8fcffffffffcfcfcfecf7f7fecccf7fccfefcfcc7c7ccfccfcffcfcffcfffcfcfffffcfffcfffcfffcfcffffffffffffcffffcfffffffffefefefffefeeeeefefffeffffeffeffeffcfffcfffff8fffffffcf8fcf8fcf8fcff8fffffff
                fffffffffffffffffffcfffffcfffcc66c66f666676ccfffffcfffcfffffcfffffcffcffffffffcffcfcfffcffffcffffcffcffcf6fccfcfffcc966c6c666bccfcfcfcfffcfcfcfcffcfcf7fccfccccf7ccccf7fcfccf7cbccffcfcfcfff8ffffcfffffcffffffffffffffffffffffcffcffcfffcfcffcfcfeffffffffefefeefeefeffeffefeffffffffffffffffffffffffffff8cfcfcfcfcfcf8ffffcff8f
                ffffcfffffffcfffcffffffffffffcc7c6f66f6f66bcffffcfffffffffffffffcffffffcffcffffffffffcfffcffffcffffcfffcccc6fffcfcfc766cf6667b6cffcfffcfcfffffff7ffcfcfcfccccf7ccfef7fccf6fc7cc7cefcfcfffcffcfc8fffcfcfffcfffcffffcffcfffcfffffffffffffffffcffcffffefefefefffefe2eeefeffefffffefefeffffffffcfcfffffffffcfcfcf8fcf8ffffffcfffffff
                ffffffffffcfffffffffffcffffcff6c66c6f6666c7cfcffffffcfffcffcffcfffffcfffffffcfcfcffcfffffffcffffcffffcfcf6eccfffffc6b6666f66b6ccfcfcfcfcfcfcfcfffcffcfcf7fcf7cccec7cccfccfcfffceccffffcfcffcfffffcfffffcfffcffffffffffffffffcffffffffffcfcfffcfcfcffffffffefefeeeeefefeffefefefffffffeffeffccfcffffffff8cf8fcfcf8fcf8ffffffcffcf
                fffffffcfffffffffffcfffffcfffcc6c6f66cc6c66ccfffffcfffffffffffffffcffffcffcfffffffffffcfcffffcffffcffffccf6cfcfcfcfb96cc66c67b6fcffcffcfffffffcfcfcfcf7fccccccecccfccccfccfcffc7fcfcffcffcff8fccfffcfcfffffffffcfffffffcfffffffffcffcffffffcffffcfffefefeffeffef2eeefefeffeffffeffefffcffffcf8fffffffc8fcfcf8f8fffffffcffcffffff
                ffcffffffffffffcffffffffffffffc6c66f66f6676cfffcffffffcffcfffffcfffffcfffffffcffcfcfcfffffcffffcfffcfcffccf7ffffffcc676f6f666bccfcffcffcfcfcfcffffcf7fcfcf7fecc7f7ccf7fcf7ffcfcccfffcffcfffcfffffcfffffcfcfffcffffffcfffcffffffcfcf8ffffcffffcfcffeffffefeffefefe2e2efefeffefefffefffcffffcfcfcfffffcfccf8fcfcffcfffffffffff8ffc
                ffffffffffffcffffffffcfffffcfcc6c6f6c66666b6cfffffffcffffffcfcfffffcffffcffcfffffffffffcffffcffff8ffffcfcf6cfcfcf8fb666c6666b6ccffcfcfcfcfffcffcfefffcfccccc7cfecce7cccccfcfff7cfcffffcfcfffcfcf8ffcfcfffffcfffffffcffffcff8fffffffcfcffffffffffffffefffffeffefeeeeeeeffefefffeffffefffffcfcf8f8fffc8f8fcfcf8fffffcffcff8fffffff
                ffffffffffffffffffcfffffcfffffc7c666f6f667ccffffcffffffffcffffffcfffffcfffffffcffcffcffffcffff8ffffcfffcfcfccfffcfc6d66cf6c67b6fcfcff8fffcfcffcffcfccfccf7fcce7e7cccfecfccfeffcefcf7fffffcfcffffcffffffcfffffffcffccffffcffffffffcfcfffffcffcfcfcffffefefefefefef222eeeffeffeffefefffffefffcffffffffcfcf8ffcffcf8fffffffffcffcff
                fffffcffcfffffffcfffffffffffcf6c6f6c6666c667cfffffcfffcfffffffcffffcfffffcffcfffffffffcffffcfffcfcfffcffcf6cffcfffcc766c66666bcfcffcffcfcfffcffcffcfcfcf7ccecccfec7cc7f7fcfcfccfcfffffcfffff8cffcffcfcfffcfffcffffcffffcffffffcffff8fcffffffffffffefffffefffeffeeeee2eeeffeffefffffffefffcff8fcfffcff8fcfcfffcffffff8ffcfffffff8
                ffffffffffffcffffffffcfffcfffcf6666f6f6667bcffcfffffffffffcffffffcffffcfffffffcfcfcfcfffcffffcfffffffffcfcfcfcffcfc696c6f6c676ccfcffcfcffcfffcffcfcf7fccfccc7f7e7fececccfccf7ff7fffffffcfcfcfff8fffffffcfffcffffcfffcffffffcfffffcfffffcf8fcffffcfffefeffefefefeee24e2efeffeffefeffefcffffcffffffff8fcfcf8fcf8fccfffffffff8ff8ff
                fffffffffffffffffffffffcffffff6e6c66666c666ccffffcffcffcffffcffcffffcffffcfcffffffffffffffcfffffcffcfcffffcfcffcfccc766c6666bccfcfcfcffcffcfcffcff7ffcf7cf7fceee7ec7fcfccf7ffcfcfcffffffffff8cffcfcfcfffffffffffffffcffffcfffffffffcfcffcfffffcfffeffffeffeffefeee444e2efefefffffffffcffcffffffffcffffcffff8fcf8ff8fffcfffffffff
                fffcffffffcffffcffcffffffffcfcc6c6f6f66666bcffffffffffffffcfffffffcffffcfffff8ffcffcffcfcfffcfcffffffffcfcfcffffffc696c6f6c676ccfffcfcffcffffcffcffcfcfcccecec7cececc7ccfcfcc7becffcfcffcfcfcfffcfffff8ffcfffcfffcfffffffffffffffffffff8ffcfffffffffefefeffefeffeee444eeefefefefefeffffffffffffffffcf8fcf8cfcfcfcfffffff8ffcffcf
                fffffffcfffffffffffffcffffffffcc66666c6f676cfcffcfffcfffcffffcffcffffcffffcfffffffffffffffcfffffcfcf8fffffffcfcfcfc7666c6666b6cfcfcfffcffcfcffcffcfcfccfefc7ccf7ecc7fcef7cfcc7b7fcffffffffffcfffffcfcffffffcfffcfccffffffffffffffcfff8ffffffcfffeffffffffefeffeef2e44544effffeffffffefcffffcffffcffffffffcfcf8fffffcff8fffffffff
                ffffffffffffffffffffffffcffffcf67cc6f66666bcffffffcffffffffcffffffffffffcfffcffcfcffcfcfffffcfffffffffcfcfcffffffcc6b66cc6c66cccfcfcfcfcffcffffcffcfcf7fc7ccc7eb7eccecccfcfc7bbccfcfcfffcfcf8cffcfffffffcfffffffcccffffcfcfffffffffffffcfcffffffffefefefeffefeffee4444e4eeefeffefeffffffcffffffcf8fcfcf8fc8fcfc8fcfffffffcffcffc
                ffffcfffffffcffcffcffffffffcff6c66f666f6676cfcffffffffcffcfffffcffcffcffffffffffffffffffcfcfffcfcffcffffffffcfcfcfc696c6f66767cfcfffcffcfcffcfcfcff7fcfccfcecce7cc7cc7fccfcececfcfcffffffffcfffffcffcfffffffcffcc8fcfcff8fcffffffffffcffffffffcffffffffefeffefefeee47452effefefcffefcfccffcfcffffffffffffcfc8fffcffffcffffffffff
                ffcfffffffcffffffffffcfffcfffcf6c666f66666c6ffffcfffcffffffffcfffffffffcfcfcfcffcfcfcfffffffcffffffffcfcfcfffffffcc7b6666c66bc6ffcfcfcffcffcfffff7ffcfcf7ccc7fce7cecfccf7fcf7ccfefcfcfffcfffc8fffffffcfcffcffffcccfffffffcfffffffffffffffffcffffeffefeffffeffefefe444444eeffecfcfffffeffffffffcffcfcffcf8c8fccf8fff8ffffcff8ff8f
                ffffffffcfffffffffffffffffffffc66c666666676cffcffffffffcfffcffffcffcffffffffffffffffffcf8fffffcfcf8fffffff8fcfcfcfc666ccf6666cccffcfffcffcfffcf7ffcfcfccfcefc7cccef7ce7fccf7cceffcfffffffcfcfcffcf8ffffffffffcfcf8fffcffffffffffffffffffcfffffffffffffefeffefeffee2454e4efefcfcfefeffffcffcffffcfffffffffccfcfffcfffffffffffffff
                ffffffffffffffffcffcfffcffffcfcc66f6c6f66c6cffffffcffffffcffffcffffffcffcfffcffcffcfffffffcfcfffffffcf8fcffffffffcc796666c67c7cfcffcfcfcffcffffffcffcfefccc7cfe7e7ccefccfcffcffcffffffffffff8fffffffcf8fcffcffffcffffffffffffffffffffffffffffffeffefeffffefeffefeee4e44eefefecfeffffefffffffcfffffffff8fcf8cf8fcfffffcf8ffcffcff
                fffffcfffffffcffffffffffffcfff6c76666666667cfcffcfffcffcffffcffffcffffffffcfffffffffcfcffffffffcffcfffffffcffcf8fcc6b6ccf6666ccfcfcfffcfcffcfcfcffcfcfccf7fceceecfecc7fccfcfccfffcfcffffcfcfccfffcfffffcffffffffffffffcffffffffffffffffffffffcffffffffefefffefeffeee4eeeeffefcffcfefffcffcfffcfcffffffffc8fcffcff8fffffffffffffc
                fffcfffffffcfffffffffcfffffffcf66c6f666c66ccfffffffffffffffffffcfffcf8fcfffffcfcfcffffffcffcfcffffffcffcffffcffffcc696666f66b6cffcfcf8fffcffffffcffefcf7fcccc7f7ec7fcccfcfcff7c7fffffcfffffcfffffffcfffcffcfffffffffffffffffffffffffffffffcffffffeffeffffefefefefefeeeefefefcfefffffcfcfcffcfffffffffffffccf8fffffffffffcff8ffff
                ffffffffcffffffffcffffffcfffffc6c6666f66676cffcfffcfffcffcffcfffffffffffffcffffffffcffcffffffffcfcfffffffcffffcffc6766cf6667cccfcfffcffcfffcfcfefcffcfcfccf7fccfcecccfccf7fcfcecfffcfffffcff8fcffcfffcffffffcccfffccffffffcff8ffffffffffcfffffffffffffefefffeffefefefefefeffefcfefefcfcfffffffcff8fff8ffcf8ffcf8fffcffcffffffcff
                fffffffffffffffcfffffffffffcfcc666c6666666c6ffffffffcffffffffffcffcffffcffffcffcffffffffcfcffcfffff8fcfcfff8fffcffcb6766f6c66c6ffcfcffcffcffffffffcfcf7fcfccececccf7f7fcfcfcff7cfcfffffffffcfcfffff8fff8fcfffffffffffffff8ffffffffffffffffffffffeffefffffefeffeffefefefeffefcffefffcfcfcfcffffffffcffffffffcffffcffffffff8fffff8
                ffcfffcffffffcfffffcffcfffffffcc666f6666c67cfffcfffffffffcffcfffffffcffffcfffffffcffcffffffffffcfffffffffcffcfffcc6b66c6c6667cfcffcffcffcffcfcfcfcfcfcfcf7fcfcc7f7cccfcefcfcffccfffffcffcffcffffffcfffcfffffff8fff8fffffffcf8ffffffffffffffffffffffffefeffffeffefeffefefeffefefffccfcfcfffcffffffcfffcffcf8ff8ffffff8ff8fffcffff
                fffffffffffcfffffffffffffcfffcf67c66666667ccfcfffcfffcfffffffffcffcffffcffffcffcffffff8ffcfcfcfffcfcffcfffffffcfffc6b66f6f6c6ccfcffcffcffcffffffffcfcfcfcfccc7fccfcfecfcfcffcfffcfcfffffffff8ffffffffffcffffffffffffffff8f8fffffffffffffffffffefffeffffffefefefeffefefefefefffefefccfcfcffffffcfff8ffffffffcfffcff8fffffffffffcf
                fffffffffcfffffffffffffcffffff6c666666f6666cfffffffcfffcffcffcfffffffcffffcfffffffcf8ffffffffffcffffffff8fcfcfffcc6b666c6c667cfcfcffcffcfffcfcfcfcffcfcfccfcfcfcecccfcfc7fc7fccffcffffffffcfcffcffffcfffcfffffffffffffffcfffffffffffffffffffffffffffeffeffefffefefeffffefffefcfcfffcffffcfcfffffffcffff8fffffffffffffffcffffcfff
                ffcffcfffffffffcffcffcfffffcfcf666c6666666c6fffcffffffffffffffffcffcffffcffff8ffcffffffcffcffcffffcfcf8fffffff8ffcc796ccf666c6cfffcffcfffcffffffff7ffcfcfcf7fccfcfcf7fcfcfccfcfcffcfffffffffcffffffffffff8fcfffffffffffffcfcffffffffffffffffffffefffffffefffefefcfefefefeefefeffcfcfcfcffffffffffff8fffffcff8ffffffffcffffcfffff
                cffffffffffffcffffffffffffffffc6c666f666767fcfffffffcfffcffcffcfffffffcffffcfffffffcffffffffffffcfffffffcffcfffcfc66b66c6f667cfcfffcfffcfffcffcf7fffcfcf7fcfcf7fc7fcfcfcffffcf6ffffffcffffcffffffffcf8fffcfc8fcfffffffff8fffffffffffffffffffffffffcfefefffefefcfefcffeffefffcfcfffffffffcffccfcfffffffcfffffffcfffcfffffffffff8f
                fffffffcffcffffffffffffcffcffcc666c666666c6cffffcfcffffffffffffffcffcffffcffffcffcfffcffcffcffcfffcffcffffcffcfffcc766cc66c6ccffcfcffcffcffffcffffcffcfcfcfcfcfcfcfcfcfc7fcfcfcfcffffffcfcfffcffffffffcfff8fcffffffffffffffffffffffffffffffffcffcffcfffffffeffefcfefeffeffeffffefcfcfcfffffc8fcffffcfffff8fcffff8ffffffffff8ffff
                ffffcfffffffffffcffcffffffffffc6c666666666ccffcfffffffcffcffcffcfffffffcffffffffffffffffffffffffcffffffcffffcffcfc6b666f6f666ccffcffcfcffcfcfffcfffcffcffcfccfccfcfcfcf7cfffcfcfffcffcfffc8fffc8ffffcff8fcfcf8ffffffffffcffffffffffffffffffffffffcfffcffefffcfcfcfcffeffeffececfccfcffcfcfffcfffffffff8ffffff8fffffff8ff8ffffcfc
                ffcfffffffffffcffffffcffffffcfc676666666676fcfffffffcfffffffffffffcffcfffffcffcffcffcffcffcf8fffffcfcffffcfffffffc6b66c6f667ccfcffcffffffffffcfffcffcffcfcffcfcfcf7fcfccefcfcffffcfcffcfffffffcfcfffffcffcf8fffffffffffffffffff8ffffffffffffffffffcffffffefeffefcfefeffffefffcccfccfcfcffffffcf8fffffffffcfffffffffcffffffcfffff
                ffffffffcffcffffffffffffcfcfffc66c66676666ccffffcfffffffcffcff8ffffffffffcffffffffffffffffffffcfffffffcfff8fcf8fcf6b66c66c66c6ffcffcfcfcfcfcfffcffcffcfcfcf7fcfcfcff7fc7cfffcfcfcfcfffffcffcff8fffffffffff8ffcffffffffffffffffffffffffffffcfffffcfffcffefffffeffeffffefefffefcfccfcccfcfcfcfffffffcff8fffff8ffcffcfffffcffff8ff8
                fcfffcfffffffffffcffffcffffffcf666f666666c6fcfffffcfffcffffffffffcffcffcffffcffcffcffcffcffcffff8ffcfff8fffffffffc6b766f6f66ccfcffffff8ffffffffffffcffcfcfcffcfcfcffccffcfffcfffc8cfcffffcf8ffcffcfffffffcffffffffffffffffffffffffffff8fffffffffffffffffffefffcffefeffcffeffccccccfcfc8fcf8ff8fcffffffffcffffffffffffffff8ffffff
                ffffffffffffffcfffffcfffffffff6c76666666676cffcfffffffffffcffcffffffffffffffffffffffffffffffffcffffff8fffcffcfcfcf6b66c6f667c6fffcfcfcffcffcfcfcfcffcffcffcfcfcfcfcffeffffcffcffcfcffffffcfccfffff8ffffffffcfffffffffffffffffffffffffffffffcffffffcffeffefffefffffffcffffccffcfcfcf8cfcc8fcffffffffffffffffffffffffff8fffffcfcff
                fffcffffcffcffffffffffffffcffcc66666666666cfcffffffcfffcffffffffcfffcfffcffcffcff8ffcff8ffcffffffcfcfffcfffffffffc6b66c6c6c6cfcfcfff8fffffcfffffffcffcffcffcffcffcfcfffcffcfffff8f8ffffff8ff8fffcfccf8ffffffff8ffffffffffffffffffffffffffcffffffffffffffffffffefefeffefeffcfefcfcfcfcfcffcfcffcffff8ffffffcfffcffffffffcfcfffffc
                ffffffcfffffffffcffffffcffffffc6c6666666676fffffcffffcfffffcffffffcfffffffffffffffffffffffffcffcfffffffffcfcf8fcfc6b66c6f6666cfffcfcffcfcfffffcffffcffcff6ffcfcfcfcffcffffccffffcfcffffcffcfffff8fcfcfffffff8ffffffffffffffff8fffffffffffff8ffcffffffffcffeffcffffffffffffefffcfffcffcfcfcff8fffffffffcf8fffcfffff8fcfffffff8fff
                fcfffffffffffcfffffcffffffffcf6c66c666676c6cfcfffffffffffcffffcfffffffcffcfffcfffcfffcffcfffffffffcfcfcfffffffffcf6b766f66c6cfcfffffffffffcfffffcfffcffcffcfcffcfffcffffcfcfcfcffcfffffffcf8cfffcf8ff8ffffffffffffffffffffffffffffff8fff8fffcffffffffffffffcfffeffefefefefcfcfffcffcf8ff8fcfffffffffffffffffffffffffff8ff8ffffcf
                fffffcfffcffffffffffffcffffffcf76666666666ccfffffcfffffcfffffffffffcfffffffcfffcffffffffffcff8ffcfffffffcffcfcfffc6b66c6f667ccfcfcfcfcfcffffcffffcfffcffcffcfcffcf6fcfcfff6ffcffffffffffffcffffffcfcffffffffffffffffffffffffffffffffffffffcffffffffcffefcffffeffffcffffffffcffcfffffffcffcfffcfff8ffcf8fcfcf8fffffcffffffffcffff
                fffcffffffffcfffcfffcfffffcfff6c66666666667fcffffffcfffffffcfffcfcfffffcfffffffffffcffcffffffffffffcffcfff8ffffcfc6b666c6c66cfcfffffffffcfffffcfffcfffcffcffffcfcffffffcfffffcfcfffffff8ffffcffcf8ff8ffffffffffffffffffffffffffffffffffcfff8fffffffffffffcfcffffeffffefcffcffcffcfcfcffcffffffffffffffffffffffff8fff8ffcffffff8f
                fcffffffffcffffffffffffffffffcc66c66676666ccfffcffffffcffffffcfffffffcfffffffffffcfffffffcffcffcfcffffffcffffcffcc676c6f66c66fcfcfcf8fcfffcfffffcfffcffcffcfcffcfcfcfcffcffcff8ffffcffffff8fffffffcffcfffffffffffffffffffffffffffffffffff8fffcfffcfffffcffcffffffffefffcfffcffffffcffcfffffcfffffcfcf8fcf8fcfffffffffffffcff8fff
                fffffffcffffffffffcfffffcfffffc666666666676ffcffffffcffffcfffffffffcfffffcffcfcffffffffcffffffffffffcfcffffcfffffccb6666f666ccfffffcffffcfffcfffffcffcffcffcfcfffffcffcffcffcfffffcffffffffffff8ff8fffffffffffffffffffffffffffffffff8ff8fffcffffffffcfffcffffefffeffffcffcfffcfccc8ccfcfcfffffff8ff8ffcfffffffcfcfcffcffffffffff
                fffffcffffffffcfffffffcfffffcf6c6666666666ccfffffcffffffffffcfffcffffffffffff8fffffcfffffffcffcffcffffffcffffcf8fc66b6c66c676fcfcffffcffffcfffcfffffffcffcffffcfcfcffcffcfffcfcffcffcffffffffffffffcf8ffffffffffffffffffffffffffff8ffffffffffffffcffffcfcfcffffffffffffcfffcfccc8fcf8fcf8fcffffffcffcfffcfff8f8fcf8ffff8ffffffcf
                fcffffffffffcfffffffcfffffffffc676c66666666ffffcfffffffcffcfffffffffffcfffcf8ffcf8fffcfffcfffffffff8ffcfffcfffffccc766cf666c6cfffcfcffcfcfffffffcfcfcfffcffcfcfffcfcffcfffcfcffffcfffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffcffffcffffcfcfffffeffffeffcffffcfccccccccfcfffffffcffcfffcffffcfccf8fcfcfffffcfffff
                fffffffffcfffffffcffffffffcffcc66666676667ccfcffffffcfffffffffcfffcffffff8fcfcffcffcfff8ffffcff8ffffffffcfff8fcffc6b6666c666cfcfffffcffffffcffcfffffffcffcffffcfcffffffcffff8fcffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffcff8fffffcfcf8fffffffffefffcfcfcfcc8fc8fc8f8fcf8fcfff8fff8fffff8ccf8cfcfcffcfffffcfff
                fffcfffcffffffffffffffffffffff6c66666666666fffffffcfffffffffcffffffffffcffcfcf8ffcf8cffffffffffffcfcfcffff8fffffcf6b6c6f66c76cfcfcfcffcffcffffffffcffcffffcfcffffcfcfcfffcffcfffffffffffff8fcffffffffffffffffffffffffffffffffff8fffffffcffff8ffffffffffcfffffefffffffffffffcfcccccc8ccfcfcffffffffcffffffccf8cfcfcf8fffff8fffff8
                ffffffffffffffcfffffffcffffffcf666666666667cffffcffffffcffcfffffcffffcffcf8fcffcf8fcf8fffcfffcfffffffff8ffffcfcffc6766666c666cfffffffffcffffcfffcfffffcfcffffcfcffffffcfffcfffcffffffffffffff8fffffffffffffffffffffffffffffffffffffffffff8fffcfcffffffffffffffffffffffcfcffc8c8f8cfcfcf8ffcfffffcffffcff8f8cfc8fcfcfffffffffffff
                fffffcfffffcffffffcfffffffcfff676666766676cfcffffffffcffffffffcffffffff8fcfcfcfffcfcfcfcfffffffcffcffcfffcffffffccc66c6f6667ccfcfcfcfcfffcfffffffffcffffffcfffffcfcfcffcffffcffffffff8ffffcfcfffffffffffffffffffffffffffffffffffffffffcfffcf8fcffffffffffffffffffefffffcffffcccccf8cf8cfcfff8ffff8fffffffccc8fcf8fffffcfffffcfff
                ffcfffffffffffffffffffffcffffcc66c666966666cfffffffcffffffffcffffff8fcfcf8fcfff8ff8fcff8fcffcffffffffffcfffcffcffc6b6666c6666cfffffffffcffffcffcfffffcfcfffcfcfffffffcfffcfcfffffff8ffffff8fffcffffffffffffffffffffffffffffffffffffffffffffcfcf8ffffffffffcffffcfffffffffcfccf8fccfccfcfff8ffffffffcfffcf8cfcfcffcffffffffcffffc
                ffffffffcffffffcffffcfffffffff6c6666666666ccffcffcffffffcffffffffcffff8fcfcf8ffffcfcf8fcfffffff8ffcfcffffcffffffcfc66c6c6667ccfcfcfcfcffffcffffffcfffffffcffffcfcfcffffcfffc8cfffffcfcffffcfcfffffffffffffffffffffffffffffffffff8fcfff8fcf8ff8ffffffffcfffffffffffffcffcfff8cccc8fc8fcfcfcffffffcfffffff8cf8cf8fcfff8fffffffffff
                ffffffffffffcfffffffffffffffcfc666676966676fcffffffffffffffcfffcfffcfcfcfcfcffcffcf8ffcfc8fff8ffffffffcffffcfcfffc67c66c6c66c6fffffffffcfffffcfffffcfcfcfffcfffffffcfcfffcfccffffffcfffffff8fffffffffffffffffffffffffffffffffffffffffffffffcfcffffffffffffffffffffffffcfffcfcf8fccfcf8fffffcfffffff8fffcfccfcfcfffffffffffffffff
                fffcffcfffffffffffcffffcfffffcc67666966666ccfffffffffcfffcfffffffffff8fcf8ffcff8ffcfcfcf8ffcffffcffcffffcfffff8fcfc666c666c6cfcfcfcfcffffcffffffcffffffffcffcfcfcffffffcffc8fcffffc8cffcffcfffcfffffffffffffffffffffffffffffffffcfffffffcf8f8fcfffffffffffffffcfffffcfffffc8ccccf8cf8fcf8fffffffffffffff8fcf8ffffcffffffffff8ff8
                ffffffffffffffffffffffffffffff6666666696667fcfffcffcfffffffffcfffcf8ffcfcfcff8ffcff8ff8fcfcffffffffff8ffff8fcffffc6c666f66766ffffffffcfcfffcffcffffcffcffffffffffcfcfcffffcccfffffcfcfffffffffffffffffffffffffffffffffffffffffffffffffcffffcff8fffffffffffffcfffffcffcffcffcf8f8cfcfcffcffcff8fffffffffcfcffffcfffffffffffffffff
                ffffffffffcfffcffffffcffffcffcc766669666766cfffffffffffffffcfffffffffcff8ff8ffcffcffcffcfcfffcffcffcfffcffffffcffcc66c666f66ccfcfcfcfffffcfffffffcffffffcfcfcfcffffffffcff8cffffffc8ffffffffffffffffffffffffffffffffffffffffffffffffffff8fcf8fffffffcffffffffffffffcffffff8ccfcfcf8fcf8fffffffffffffffffffcfcfffffffffffffffffff
                ffffffffcfffffffffcfffffffffffc66666696666ccffcfffffffcffcfffffff8fcff8ffcfffffcffcfffcf8fcffffffffffcfffcffcfffcf6c766c666c6fffffffcfcfffffcfffffffcffffffffffcfcfcfcfffccc8fcffffccff8ffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffcfffffccccfcfcffcfcf8ccf8fcf8ffcf8ffffffffffff8ffffffff8fffffffffffffff
                fcffcffffffffffffffffffffffffcc66669667666ccffffffcffffffffffffcffffffcfcffcffcfccccfffcfcffffcffcffffffffffffcffc666c66c676cfcfcfcfffffcffffffcffcfffcfcfcfcffffffffffcffcfcfffffcffffffffffffffffffffffffffffffffffffffffffffffffffffcffff8ffffffffffffffffcfcf8c8fcf8ffcf8cff8fcfffffffffffffffffffffffcfff8ffffffffffffffffc
                ffffff8fffffffcffffffffcfffcff6766667966667fcfffffffffffffffcfffffcffffff8fffffcfccfcff8fc8fcffffffcffcfcfcfcfffcfc666c6666c6fffffffcfcfffcffcffffffffffffffffcfcfcfcffff8ccfffffff8cfffcfcffffffffffffffffffffffffffffffffffcff8ffffff8fcfffffffffffffffffffff8cfcfcfffcfffffcffcffcffcffffcffcffcfffffffffffffffffffffffffffff
                fffffffffcffffffffcffcfffffffcf66669669666c6fffcffffcffcffcfffffcffffcf8ffffffffcfcfcfffcffcfcf8ffff8fffffffffcffc676666c66c6fcfcfcfffffcffffffffcffcfcffcffcfffffffffcffccfcfffffffffcff8ffffffffffffffffffffffffffffffffffffffffcf8ffcffffffffffffffffffffcfcfc8c8fcfffffcff8fffffffffcfcffffffffff8fffffffffffffffffffffff8ff
                ffff8fffffffffffcfffffffffffff6b6666696666ccffffffcfffffffffffffffffff8fffffffcffcffffcff8ff8fcfcfcffffcff8fcfff8cc6b6c66c67fcffffffcffffffcfffcffffffffffffffcfcfcfcffffc8ffffcffffcffccfcffffffffffffffffffffffffffffffffffcffcffffcffcffffffffffffffffffffff8fcfcff8fcffffffffffcf8c8ffffffffc8cfffffffffffffffffffffffffffff
                ffffffffcfffcfffffffffffffcffcc666769666676fcffffffffffffffffcfff8fffffffcffffffffcfffffcfcfcf8ffffffcffffffffcffc66666c666c6fcfcfcfffcffcffffffffcffcfcfcfcffffffffffcfffccf8fcfffffff8fcfffffffffffffffffffffffffffffffffffffff8fcfffffffffffffcffffcfffff8ffccf8fcffffffffcffcfff8cfcf8fcfffffcffffffffffffffffffffffffffffff
                ffffffcfffffffffffffffffcfffffc67666696666bfffffcfffffcffcfffffffffffcfffffffffffcfcffffffff8cfc8fcfffffcfcfffffcf76b666766ccfffffffcfffffffcffcffffffffffffcfcfcffcfffcff8ffffcffffffcccf8fffffffffffffffffffffffffffffffffcf8fffff8fcffffffffffffffffffffcfcff8cfcfffffffffffffffccf8cfcfff8ffcf8fffffffffffffffffffffff8fffff
                fff8ffffff8ffffffffcfffffffffcc666696696667cffcfffffcffffffcffffffffffffffffffffffcffffffcfffcfcfcfffcffffffcfcff6c666c66c67cfcfcfcfffcfcffffffffffcffcffcfffffffffffcfffffcffcfcfffffc8cfffcffffffffffffffffffffffffffcffffffffcf8fcfcffffffffffffffffffffcfffcfcff8ffcffffffffff8c8cfcf8fcfffffcffcfffffffffffffffffffffffffcf
                fffffcfffffffffcffffffffffffff676666966766ccfffffffffffffcfffffffffffffffffffffffffffcfcfffcff8fcffcfffcffcfffffcc6b6676666c6fffffffcfffffcffcffcffffffffffcffcfcfcffffcfcffffffffffffccc8ffffffffffffffffffffffffffffffffffffffffcfcf8ffffffffffffffffffff8fcff8f8ffffffffffffffcfcfc8cfcffcffff8fcf8ffffffffffffffffffffffffff
                fffcfff8ffffffffffffffcfffffcfc6666696966678ffffffcfffff8ffcffffffffff8ffffcffcfcfefeffefffffcfff8ffffffffffcfcffc67666c6c67cfcfcffffffcfffffffffffcffcfcffffcfffff8fcffffffcfcfcffffc8cffcffffffffffffffffffffffffffff8ffffcff8ffcf8fccffffffffffffffffffccfffffcffcffffffffffff8c8cfcf8fcfffffffffcfffffffffffffffff8fffffffff
                fffff8fffffffcffffffcfffffffffc6669669666b6fcffffffffffffcfff8fffffffffffffffffffefefeefeffcfffcfcfcfffcff8fffffcc6b66c6666c6fffffcfcffffcffcfffcfffffffffcffffcfffffffcffcff8cfffffffcc8fffffffffffffffffffffffffffffffcffffffffcf8cfcffffffcfffffffffffcf8fcfcffcfffffff8ff8fffcfcf8c8fcf8fcffffcffffffffffffffffffffffff8fff8
                fff8fffcffffffffffcfffffffcffcc676669679667cffffcfffffcfff8fffffff8fffffffffcffefefefef2ffff8ffffffff8ffcffffcfff6b66666676ccfcfcfffffcfffffffcffffcffcfffffcffffcffcffffff8fcfcffffff8ccfcfffffffffffffffffffffffffffffffffffcfff8fcc8cfffffffffffffffff8fcff8fcffffcffcffffffff8c8cffcfcfffffff8fcfffffffffffffffffffffcffffff
                fffffcffffffffffffffffffffffff6c6669669666ccffffffffffff8ffcfffffffcfffffffffefefefefefeefcffcff8fffffcff8fffffcfc6b666c6666cfffffcfcfffcffcfffffcffffffcfcfffcfffcfffcfcffffcc8ffffffccffffffffffffffffffffffffffffffcffcffffff8fcfcfcffffffffffffcfffffccfffcf8fcfffcfffffccffffcf8c8fcf8fcf8ffccfffffffffffffffffffffffffffff
                fffcffffcffffffcffffffffcffffcc666669666667fcffffffffffffffffcfffcff8ffffffcffffefefecefefffcffffffcff8fcffffcffcc676b666c7cccfcffffffffffffffffffffcfffffffcfffcfffcfffffcfc8fcfffffff8cffffffffffffffffffffffffffffffffffffffffcfc8c8fffffffffffffffffcf8fcf8cfff8fffcfcff8ffffc8cffcf8ffcfffffc8fff8ffffff8fffffffffcffffffcf
                fffffcffffff8fffffffffffffffff676696696966bcffffffffcffffcfcffff8fcfffffffffffeffeccccfeffffffcffcfffcfcfcfcfffff6b666676666cfffcffcffcffcffcffcffcfffcffcffffcfffffffcffffffccffcffffcffcffffffffffffffffffffffffffffff8fffffffff8fcffffffffffffffffffff8cfffcfcffffffcffffcfcfffcf8cfffcfffffcfcffffccffffffcfffffffffffffcfff
                ffffff8ffffffcfcfcffcfffffffcfc666669667666fffcfffcffffffffffffffcfcfcffffffeffefeccecefeffcfffcffffff8f8fffffcfcc6b66666b6ccfcffffffffcfffffffffffffffffffcffffcfcfcfffcfcffc8ffffffffcfffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfffcf8ffcffffcfffcfffff8ccfcf8ffffcfffff8fffc8cfffcfffffffffffff8fffff
                ffcfffffffcfcf8fcfcfffffffcfff6b6696696966bcffffffffffcfffffff8fcff8fffffffffffefcf7ccfefeffffffffff8fcffcf8fffffc76b6b66667cfffcfcfcffffcffcffcfffcffcfcffffcffffffffcfffffffcfcffffff8fcfffffffffffffffffffffffffffffcfffffff8fcfffffffffffffffffffffff8fcffcffffffffffffff8fffff8f8ffffcffffffffffffcf8fffcffffffffffffffffff
                fffffcffcfff8fcf8f8ffcffcffffcc666669666676fcffffffffffffff8fffcf8fffcfffffffeffefeccfcffffffff8fffffffcffcffcffcc696666b6b6cfcfffffff8ffffffffffcffffffffcffffcffcfffffcffcfffcffcfffffffffffffffffffffffffffffcfffffffffffffffcfcffffcffffffcffffffffffcfff8ffcf8ffffffff8ffffffccffcffffffffff8ffff8fffcffffffffffffffffffff8
                fffffffff8fcfcfccfccffffffffff676696696966bffffffffffcffcfffffcfffcffff8ffffffffefcfcfcfffffcffffcffcffff8fffffcfcb66b666666cfffcffcfffcfcfcffcfffffcffcffffcfffffffcffffffffcffffffffffcfffffffffffffffffffffffffffffffffffffcff8cfffcffffffffffffffcffff8fffcffcfffffffffffffffff8fcfffcfffff8fcffffffcfffffffffffffffffcfffff
                fffffffcfcff8fcf8cf8cf8ffffffcc666669666667cfcfffffcfff8fffffcfcfcfcf8fffffffffffcffcfffcfffffffffffffcffffcff8fcc676676b67bcfcfffffcfffffffcfffffcfffcffcffffcfcfcfff8fcfcfffff8fcfffffffffffffffffffffffffffffffffffffcffffffffcf8cff8fffffffffffffffffcfffcffccfcfffcfcffffffffffffffffff8fffcfcffffcfffffffffffffffffffffcff
                ffffffff8fcffcf8fccfcfcfffffff6b6696696966ccfffffcffcfcfcfcfffff8ffffffcfffffffeffffffffffcfffcffffffffffffffcffcc696b666b66cfffcfcff8fcf8ffffffcfffcfffcffcffffffffcfffffff8ffcffffffffffffffffffffffffffffffffffffffffffffff8ff8ccffccfffffffffffffffffffffffcfccffffccffffffffffcffcffffffffffcfffcf8fcffffff8fcfffffffffffff
                ffffff8ffcfcf8fccf8f8cfffffffcc66666969676b6ffffffcf8ff8ffff8fcfffcfcffffffffffffffffcffffffffffff8ffffffff8fffcf6b666b6b6976fcffffcffffcfcfcfcffffffcfcfffffcffcfffffffcffffffffffcffffffffffffffffffffffffffffffffffffffffffffcffc8ff8fffffffffffffffffffffcfccfccffccfcffffcfffffffffffffffcffff8ffcfc8fffffffcf8ffffffffffff
                fffffffcff8fffcf8fccfcfcffffff6766966966666cfcff8ffcfcffcf8ffff8fcfff8fcfffffcfcfffcffffcffcf8fcffffffffffffffcf8cb96b66966bcfcfcfffcfcfff8fffffffcff8ffcfcfffffff8ffcffffcffcfffcfcffffffffffffffffffffffffffffffcfffffffffffcffc8fcffcfffffffffffffffcfcfffffcfcfcffcccfcfcf8cfffff8cf8fffff8cf8ffffffffcffffffcfffffffffff8ff
                ffffffffcffcfcfcfcfcf8fffffffcc6666966966b7cf8fffcf8ffcffffffcfffff8ffffffffff8ffcffffffffffcfffffcfffffffffff8fcc6b666b6696ccfff8fffff8fcffcffcfffcffcfffff8ffcfffffffcfffffffcfffffffffffffffffcfffffffffffffffffcffff8cffffffffcccffffffffffffffffff8fffcffccfcffffcffcff8cfcf8fffcfffffffccf8ffffffcfffffffff8ffffffffffffff
                ffffffcff8ffff8fcf8fcfcf8fffff6669669667666ccfcfcfcfcf8f8fcfffcfcfcfcfcf8ffffcfcffffffcffcf8fc8fcfff8fffffffcffcfc96769676b9cfcfcffcf8ffffcff8ffffffcff8fcfffffffcffcfff8ffcfffffffcfffffffffffffffffffffffffffffffffffffffffffcf8f8cfffffffffffffcfffcccfffffcfcfffffcfcfffcf8fcffffcfcfcfff8ccffffccfffffffffffffcffffffffffff
                ffff8fffcfcf8ffffcfff8fffcff8fc76669696966b8cffff8fffcffcffff8ffffff8fcffffff8fcf8ffcff8ffcfcffcffffffffffffffffccb66b696967ccf8fffffffcfff8ffffcf8ff8fcff8fcffcffffff8ffcfffcfffcfffffffffffcffffffffffffffffffffffffffcffc8ffffcfcffffffffffffffffff8f8ffcffcfffcfffcfcfcfccfcfcfcffff8cfffcc8fcffff8fcfffffffffffffffffffffff
                fffffcffffffffcfcfcfcffcff8fff6b6966669666bcf8cfcfcf8ffcfffffffcf8fcfcf8ffffffcf8ffffcffcff8fcffffcfffffffffffcf8c6966b6b699cfcfffcffffff8fffcffffffffcfcfffffffffcffcffcffffffcfffffffffffffffffcfffffffffffffffffffffffffffcfffffffffffffffffffffffffcffcffffcfffffffcffff8f8f8fffffffcfffc8cfcffffcffffffffffffffffffffffffff
                ff8fcff8fcfcffffffffffcf8ffffcc666696966676ccff8fffcfcffffcffcffffcf8cffffffcf8fcfcfff8ffcfcc8f8fffffffffffffffffcb67969696b6fffcffffcffffcffffcfffcfffff8fcfcfcffff8ffcffcf8fffffcfffffffffcffffffffffffffffffffffffffffffcffffffffc8cffffffffffffffffcffffcffffffffcfffcfcfccfcf8fcffffffffcc8ffffffffffffffffffffffffffffffff
                ffcfcfcfffffff8fcf8fcfffcfcffc666966969666b6f8ffcf8fff8fcffffff8fcf8fcfcffffffcfffff8ffcf8f8fcfcfffcf8fffffffffcfc6666b69769cfcfffffffffcfffcffffffffcf8ffffffff8fffffcfcffffffffff8fffffffffffffffffffffffffffffffffffffffffffffcf8ffcfffffffffffffffffcffffffffffffffcfffc8fcf8ffcf8fffcfff8cfcf8fffffffffffffffffffffffffffff
                cff8ffffffffffffffffff8ffcffffc76669666966bccfcffffcfcffffff8fffffcccf8ffcfffcfcfcfffffffcfcfcfffcf8fcfffffffffffc6b9697696dcfffcff8fffffffffffff8ffffffcfcff8ffffcfcff8f8fcffcfffcfffffffffffffffffffffffffffffffffffffffffffffffffcfcffffffffffffffffff8fffcffffcffcfffffcfcf8fcfffffcfffffccf8fffffffffffffffffffffffffffffff
                f8fcfcf8fffffffcfcfcfffcfffcfc6669669696676c8fcf8fcffffcff8fffffcf8f8fcffffffff8ff8fffcfffc8c8cffffcfcfffffffffffc666b969696cffffffffffff8fff8fffffff8ffffffffcfcffff8fffcffffffcfcffffffffffff8ffffffffffffffffffffffffffffffff8fcfc8cfffffffffcffffff8cfcffcfffffffffffff8f8ffffcfcfffffffff8fffffcff8fffffffffffffffcffffffff
                cfcfcffffffffffffffffffff8ffffc66696696666bcfcfffffcf8ffffffffcffcfccfcffffff8ffcffffffff8fcffcf8ffcf8ffffffffffffb7969b6b6dcffffffffffffffffffffffffffffffcffffff8fffcfcff8fcffff8fffffcfffffffffffffffffffffffffffffffffffffffffcfffcffffffffffffffffccfcffffffffcffffcfffcffcfff8ff8ffffffcccfcfcfffffffffffcffffffff8fffffff
                fcf8ffcffcffffff8fffffcfffffc8cb6669669696b6f8fcfcffffcffffcfffff8fcf8ffcfffffffffffffffffcfc8fffcf8fcfcfffffffffc6669699697cfff8fffffffffffffffffffffffcfffff8fcffffffffcfffffffccfffc8c8fffffcfffffffffffffffffffffffffcfffffcfcf8fc8fffffffffffffffc8fcf8fffcfffffcccfffffcffcf8ffcffffffff8ffff8ffcfffffff8ffcffffffffffffff
                8fcffcffffffffffffffffffffcfff6696669696676ccfcffff8ffff8fffcf8fffcf8fcffffffcfcfffffffcfcf8cfcffffcfcfffffffffffc696b97b966cffffffffff8ffffffffffffffcffffffffffffcffcf8ffcfff8fcfcffcccfcffffffffffffffffffffffffffffffcfffffffffcffffffffffffffffffcfcfffcffffffcff8fffffffff8ffcffffffffffcffffcfffffffffffcffffffffffffffff
                fcfcff8fcffffffffffffffffffffcc66696969666bcfcff8fffcf8fffff8fcfcffcfcfffffffffff8ffffffffcfcf8fcffcf8fffcfffffffc6769b96979ffffffffffffffffffffffff8fffffff8ffcfffffffffffff8fffc8ff8cc8fcffcfffffffffffffffffffffffffcffcffffcf8ffcfcffffffffffffffff8fcfcfffffffffcfcffff8fcffcff8fcffff8cffcffffcfffffffffffffffffffffffffff
                cfff8fffffffffffffffffffffffcf6b6669696796b8f8ffffcfffffffcffcfcfcffcfffcfffff8ffffffcf8fff8fcffff8fcfcffffffffffc69b699796bcfffffffffcffffffffffffffffffffffffff8fff8ffcff8fffffcfcffccccfcfffffffffcfffffffffffffffffff8ffcfffffcfff8ffffffffcffffffcff8ffcfcfffffff8ffcfffff8cf8ffffffffccfff8ff8fff8fffffffcffffffffffffffff
                f8fcffcffcfffffffffffffffffffcc66966969666bcffcffffffcfffffcf8fcff8fffcfffffffffffffffffcfffcffcffffcfff8ffffff8fc669b9b9696cffffffffffffcfffffffffffffffffffffcffffffffffffffffff8ffc8f8f8fffffcffffffffffffffffffffffcffcc8c8ccffcfcfffffffcfcfcfffffcffffff8ffcfffcfcfffffcffcfcfcfcffff8c8ffffffffffcfffffffffffffffffffffff
                fcffcffcffffffffffffffffffffff6766696969676cfcffcff8ffffcfffcfc8fcfffffffffffffcffffffcfffcf8fffffcff8fffffffffffcb6969799b9cffffffff8fffffffffffffffffff8fffffffffffffffcffffcfffffffcccffffcfffffffcffffffffffffffffffcc8fcfcf8f8fffc8fcfcff8f8fffffcffffcfcfccfffffffffffff8ff8fcf8ffffccfcffffffcfcfffffffcfff8fffffffffffff
                ffcfffcffffffffffffffffffffffcc66696697696b6ffffffffffcfff8fcf8fcfffcffffffffffffffffffcf8fffcfffff8ffcfffffffccc6b979b99b97bcfffffffffcfff8ffffffffffffffffcfffffffcffcffffcfffcfcfc8fcfccffffffcffffffffffffffffffffcf8cfc8fcfcfcfcf8fcf8f8ffcfcfcf8fcfcfff8c8fcffff8cf8fffffcffcfffffff8fc8ffffcfff8fcfffff8fcfffffffffffffff
                cff8ffffcfffffffffffffffffffffc6666969966b6cffcfffcfffffffff8fccfcfffffffffffffffffffff8fffffff8fffffcfffffffcccc69b999b99996cffcfffcffffcfffffffffffff8ffcfffff8ffffffffffffffff8fcfff8f8fffffffffffffffffffffffffffffcfc8fcf8fcfff8ffcfcfcffffcfffcff8ffffcfcccffffcfcffffcffffff8fcffffcfcfcfffffffcfffffffcffffffffffffcffff
                f8ffcf8ffffffffffffffffffffffcc669669696967cffffffffcffffcfcfcfc8ffcfffffffffffffffff8ffcffffcffffffffffffffccc6bb99b9d9b9b9bccffcffffffffffffffffffffffcfffff8fffffffffff8ffcf8fcff8cffcffffff8fcfffffffffffffffffccf8c8fcfcfcf8f8fcfcf8fcfcfcfff8fcfcffffff8cf8cffff8cfcffffffcffffffffff8fcfffffff8ff8ffcffffffffffffffffcfff
                ffcfffffcfffffffffffffffffffff676696979676b8ffffffffff8ffffffc8fcfffffffffffffffffffffffffffffffffffcfffffffcc67b9d9d99d999d7cc6fcfffcff8ffffcffffffffcfffcf8fffffffcfff8fffffffffcffffffcfffffcffffffffffffffffffc8cffcfcf8f8fcfcffcffcff8fffff8ffcf8fcfcffffc8fcfffcfcffffffffffcffffcffffffffffffffcffffffffcffffffffffcfffff
                cfffcfcfffffffffffffffffffffffc66669696966bfffffffffffffff8fcffcf8fcffffffffffff8fffffcfcfffffffffffff8ffffcc6cb9b9d9d9d9d79b6cccc8ffffffffcffffffffffff8fffffffffffff8ffffffcfcffffffffffffc8fcfffffffffffffffffcccffcf8fccfcf8ffcfff8fcffcff8ffcfffcfffff8fcfcfcffffff8fffffffffffcffffffcffffff8fcfffcfffffffffffffffffff8fff
                ffcffffffffffffffffffffffffffc666969699696bcfffffffffffffffffcf8fffffff8fffffffffffffffffffff8fcffff8fccccffc7b9d9d9d9d9d999bc7c6ccccffffffff8ffffffff8ffcfcfffffffcfffffffcffffffcfcfffffcfffffcffffffffffffffffcf8fcf8cf8fcfcfcff8fcff8ff8ffffffcfff8f8fffffffffffffffffffff8ffffffffffcffffffffcfff8fff8fffffffffffffff8fffff
                ffffcffcffffffffffffffffffffffc766697969676ffffffffff8fffffcffcfcfcffffffffff8ffffffffffffffffcf8fffccccccc6bb9d9d91919d9d9d9b6bb6cccfcffcffcffcfffffffffffffcfffcfffffffffffff8ff8fcffc8ffffcf8ffffffffffffffc8cfffffcffcff8ffff8ffcffcffcffcfcf8fcfcffcfcfcfffffffffffcfffffffff8fcfff8ffcf8ffcfffffffffffcfffffffffffffffffff
                cf8ffffffffffffffffffffcfffffc66696969976bbcfffffffffffcfffff8ffcfffffcffcfffffffffffff8ffffcfcffcfcfc6c76c79d9d9d19d1919d91b9bbbb67cccfcffffffffffffffcfcf8fffcffff8fffffffffcffffcfffcfcfcfffffffcffcfcfccfcfcf8fcfff8ffcffcf8ffcffffffcffffffffff8ffcf8fff8ffffffffffffffffffccfcf8ffffffcfcfffffcffffffffffffffcffffffffffff
                fffffcffffffffffffffcf8ffcfcffc666969696966fffffffffcfcffcfffffffcfffffffff8ffffffffffffffffff8cfffcccb6bb9d9d9d19d19d9d19d9d9b99bb6b6ccfcff8ffffcf8fffffffffcffffffffcffffffff8fcfcff8fc8fffffcfc8fc8cc8c8c8c8fcfcff8ffcff8ffcffcf8cfcfffff8ff8fcfffff8fcf8ffcfcffffffffffffc8c8c8ffffffcfffff8fcf8fffffffffffff8ffffffffffffff
                ffcfffff8fffffffffcffffcffff8f6b669699796b6cfffffff8f8fcff8fffcfffff8fcf8ffffcfffffffffffffffffcf8ff6c7b9bd9d9d9d919d19191919d9bd9bbb67c6fcffffff8ffcffffcffffffff8fcfffff8fffffffff8ffcffcc8cff8fcc8cfcccccfcfcf8f8ffffffcfcffffc8fff8fcfffffffff8cc8ffffcfcfcff8fffffffffc8cfccfcfcffffff8f8ffcf8fcfcfffffffffffcf8fffffffffff
                ffffcffffffffffffff8fcffcf8ffcc69679699666bcffffffffcfcf8fffcffffffffffffcfcfffffffffffffffffcf8ffccc6b9b9d9d9d919d19d9d9d9dd9d9b9b9dbbcccfcfffcffffffffffffcf8ffffffffffffffffcfffffcffcf8cfc8fcfcffc8cf8cf8fcfffcfcfffffffff8fcfccfcccff8fffffffccfccccfff8f8cfffcffffff8fccc8cf8fffcfffffffcf8fcfcfff8fcfffffcffcffffffffffff
                fcfffffffffffff8fcffffcffffcfc6766969979967cffffffffcffcfccfffffffffcf8fcfffffffcf8cffffffffffcffffcccbb9bd9d9d19d9d911911919d9d9d9d9b67c6fcfcffcfcffffffffffffffffcff8fffcffffff8fccff8fcccfcfff8fc8fcfccfcfcf8ccfcffcffcffffffc8f8ff8ffffffcfffc8f8cf8f8cffcfcfcffffffffccf8fcfcfcfffffffcffcffcf8f8fffcffffcff8fffcffffffffff
                fffffffffffffffffffcfff8fcffcfc696696996b6b8fcffffcff8f8ff8ffffffffffcfffffcfffffccfcfffffff8ffcfcffc6bb9b9d9d9d19119d9d9d9d9d9db9bd9b9bcccfcfffffffffffffffffffcffffffffffffffffffcfcfffcf8cfcffcf8fc8cf8c8f8ffcf8fc8fc8fcf8fffcfcfcfcfcfffffffffccf8cccfc8ffc8ff8fcff8ff8fccc8cf8ff8ffcffffff8fcfcffcfff8fcffffffcffffffffffff
                fcffffffffffffcffcff8fcfff8ffc666969979966bcfffcffffcfcfcfcfcffffff8ffcf8fff8fff8fcc8cfcfcfcffcfffccc76bb9d9d9d9dd9d9119191d9dd9dd9d9bbb6ccfffcffffcffffffff8ffffffffffffffffffffff8fffcf8cff8ffffcfcffc8ffcfcffffffcccffcfffcfcf8fffcfffffffffffcf8cfcf8fcfcfffcfff8cfffccf8fcf8ffcfffffffff8fff8f8fcffcfcfffffcfffffffffffffff
                ffffff8fffffffffff8fffffcffcffc9669699696b6cfcfffffcffcfcff8fffffffff8ffffcffcffcccccccfcc6cc6cc6c6c6bb9b9dd9d19191919d9d19d9d9d9b9bd9b7bcfcffffffffffffffffffcfffffffffffffffffffcccffffcfcffcfcff8fc8ffcf8ffcfcffc8cf8f8fcfff8ffcfff8fcfffffffff8cf8fcf8fc8fcff8fcfc8fff8cfcfcfcffffcff8ffffffffffffffffffcffffffffcffffffffff
                ffffffffffffffcf8fffcfcfffffcf66669699b9676cfffffcff8ff8f8ffcfffffffcffcffffcfccf68cc86c66c6bc6c6b66b6b69b99d9d9d9dd9d1919d919d9d9d9b9b6cfcfcffcffffffffffffffffffffffffffffffffff8ff8ffcf8fcff8cfffcffcf8fcfcfffffcccfcffcff8ffcff8ffffffcfffffffcfcfc8fcf8fcffcffc8fcffcffcf8fff8ffffffffffcffffcffffcff8fffff8fcfffffffffffff
                ffffffcfffffffffffcfffff8fcffcc69697997969bcffcffffffcfcffcffcfffffffcfffffffc866c686f68c8c68c6c86c8666b6bb9b9b9d9d919d9d9dd9d9b9b9dbb7ccffcfcfffffffffff8fffffffffffffffffffcf8ffcfcfffccfcfcfcfcfffcffcfcf8fffff8c8cf8ffffffcff8ffffcfff8cffffff8f8fcfcfcffffffffccc8fffcf8ffcfcffcf8fcffffffcffffcfffffffffffcffffffffffffffc
                ffffffffcffff8fffffffcffffffff6b669699969678ffffffcffcffcfcf8ffffff8fff8ffffcc66686c68cc6f6c8c86c86c8c86c66c6b6b9b9d9d9d9d99b9b9b9d9b6bcfcfcffffffffcf8fffffffffffffffffffffffffffcffffcf8ffffcf8ffcff8fff8ffcff8ffcfcffcf8ffcffffffcfff8fcf8ffffffffcf8f8fcf8ff8fff8fcfcff8ffff8fffffffffffffffffffffff8ffcffffc8ffffff8fffff8f
                ffff8fcffffffffcffcffffcffcfcfc6696997996b6cfffcffff8fcf8fffffffffffcffcffff86c6c68ccc6f86f6f6c686c666c8ffcf6c6cb9b9b9d9d9bb9b6b69b9b6cffffcfcffffffffffcfffffffffffffffff8fcfffcff8fcffcffcff8cfcffffffcffcff8ffffcc8fffcccfffcffcffffffcc8cfffffcfffffcffffffffffcccf8ffffcfcfffcf8ffcffffffcfffffffffffffffffcfcfffffffffcfff
                ffffffff8ffffffffffff8ffffffff6b669799b966bffffffffffffcfcf8fcffffffff8fffffc6668686ccf6f68c6ccc6c68c8cffcfcf6c6c6bb9b9b9bb6b6b6b6b69c6cfcfcfffcffff8fcffffcfffffffffff8fffff8ffffcfffcf8fc8fccfcffffffff8fcfcffffffcffc8cf8ffffffffff8fffcffcffffff8fcffff8ffffffff8fcffffcfff8fffffffffffffffffffffffffcffffcfc8ffff8fffff8cfc
                ffffffcfffcfffffffcffffffffffcc69696996976b6fffcfcfcfcffffcfffffffff8ffcffcfc6c6686f68cc8fcf6f66f666cffc8fffcfccc6c6bbb9b6b66c66b69b6cffcfffcffffffffffffcfffff8fcfff8ffffcfcfcfffcffcfffcfcfcf8fcffffcfffcfffffffffffc8fc8ffffffffffffcf8fcf8fffffffffff8ffffffcffffcffffff8ffffcffcffffffffffff8fffffcffffffffcfcffffcfcffffff
                ffffffffcffffffcffffffffffffffc666997999697fffffffffff8fcfffcfffffffffcffffcc66686c68f6fc6f6c6c666c6fcccfcfff8cccccc66b6b6b6c6cc66b66ccf66ffffffcffffffcf8fcffffcffffffffffffff8cff8ffffcc8ff8cfff8ffffcfcff8fffffcf8fcfcffcffcfffffcfffffcf8fffffffffffffffffffffffc8ffcfffffcffffffffcffffffffffffffffffffffff8cffffcf8fffcfcf
                ffffcfffffffffffffffffffffffff67696999b966bcffcf8fcf8ffff8ffffffffffffffffcfc6666c68c6fcfc6f6f6c666cfc8fcffffffcf6fcccc6c6cc6c66c6b6cfcc66fcfffff8fffff8fcfffffff8fffffffffffcfffcffffcf8ffcfcfcffffffff8ffffffffc8ccf8f8cffffffffffff8fcf8ffcfcfff8fffffffffffcffffffffffffffff8ff8fffffcfcf8ffffffffffffffffffccf8ff8fffffffff
                ffffff8fcffffffffffffffffffffcc66969799696bffffcfcffffcfffcf8fffffffffffffcf6b66c66c6f6f6fc6c6c6c76ccfcfffcffcfccf6f6f6ecc6c6c6c6b6bcff667cfffffffcffffffffffffffffffffffffffffffffffffcfcffcf8fcfcfff8ffcfcffffcccf8ffcff8fffffffff8fffffcffffffcfffffffffffcf8ffffffffffffcffcffcfffcfffffffffffffffffffffffff8cffffccfcffffff
                ffff8fffffffffffffffffffffffffc696999b976b6cffffff8fffffcfffffffffffffffffccc66668c6f6f6f6fccf676b6cfffcfffff8ff6fccf7f6f6f6c6c6b69bf6fcfcfcffffcfffffcfcff8ffffffffffffcfcfffcfffffcff8fcf8fcfcfffffffcffffffff8f8cfcfffcfcffffff8ffffcfff8fcf8cffffcfffffff8fffffffffffffcf8cc8cfccffffffffffffffffffffffffffccf8fcfff8ffff8ff
                ffffffffffffffffffffffffffffff6667699999697ffcf8fcffcfffffcffffffffffffcfffc6b66c6c6cccf6f6f66c66b9ccfcfcfffffcffcf6cfcf6c6c6c676b9bfcfffcffffffffffffffffffffffffffc8fcf8fffff8ffffffcfcfffcf8ff8fffffffcffffffccfcffffcfffffffccfcffff8fcfff8fcfcffff8fffcfcfcffffffffff8ccc8fcc8c8c8ffcfffffffffffffffff8ffff8cffff8fffffffff
                ffffffcfffffffffffffffffffffffc7969979b966bcffffcfcfffcf8fffcfffffffffffffcfc6666c6f6f6cf6c6cc6cb96ff8c8ffffcfffffcfcfffcf7c6c6b6d69fcfcfc8cffffffffffffffffffffffcffffcffffcffffffcfff8fcff8fcffffcffffffffffcf8fcf8ffcf8ffffff8ccfcffffffcffffcff8fffffff8fcfff8fffffffcc8cfcc8fcfcfccffffcffcffcff8fffffffffcfcfcfffcfcffffff
                ffffcffffffffffffffffffffffffcc669699997967fffffffffffffffcfffffffffffffffff6b666c6c6cc6f6fc6f7676fcccfcfcfffffffffffcfcfc6f76c7b9dbffcfcfffcfcffffffffffffffffffff8ffcf8fffffcffffff8fffffcfcfcffffffffffffff8cff8ffcfcffcffffccc8fffcfcff8fcf8f8fffcfffffcff8fffffffff8cfc8c8ccc8c8c8f8cfffffffffffcfcfffffff8fcff8ffcfffcffff
                ffffffffffffffffffffffffffffff666969b99696b8fffcfcf8ffffcfffffffffffffffffffcb666c6f6f6f6c6c67c6bccffccf8ffffffffffcfcfcffc6c66b6999cffcfcffffffcffffffffffffffffffffcffffcffffffcffcffcffff8fff8ffffffcfffffcfccffcfff8cff8fff8cfcf8fffffffffffffcffffcffff8fffcffffffcf8ccfccf8fcfcfcccf8ff8fff8fccc8fcffffffcffffcffc8fffffff
                ffffffffffffffffffffffffffffffc769979d9b6b6fffffffffffffffffffffffffff8fffffc6666c66f66c6f6c6c6b9ffcff8ffffffffffffffcff8ff6c7b6dbdbfcffffcfcfff8fcffff8fc8fffffffcfcfcfcfff8fffffffffffffffcf8ffffffcfffffff8c8fcffffcff8fffffcc8fcffff8fcff8ffcfffcf8ffcffffcfffffffffccf8c8fccc8c8cf8f8cffffffffc8cccf8fffffcf8ffcffcfcffffff
                fffffcffffffffffffffffffffffffc69699999967bcffffffffffffffffffffffffffffffffc76666f66cc6c666c676bfffffcffffffffffffffcfcfcfc76b69999ffcfcffff8fffcfffffcfffffffff8ffff8ff8ffffcffcf8fffff8ffffffcffcfffffffffcccff8fcff8ffcfffcfcfcf8fffffffcfcffff8ffccff8fcffffffffff8f8cfcfc8f8fcf8cfcfcffcffcfc8cfcf8fcffff8ffff8ff8ff8fffff
                fffffffffffffffffffffffffffffcc6669b9797966cfffffffffffffcfffffffffffccfffffc666666c6c666c66766b6fffcfffffffffffffffffcffcff6b6dbbddcfffffcfffffffffffcf8cfcfffcfffc8ffcffcfcffffffffffffffffcffffffffff8ffffcf8cfffffcfcfff8ffc8c8fcffffff8cc8fcffffcf8ffffff8fffffffcfcfc8f8cccfc8fcf8cf8fff8ffc8fccf8fcfffffcfcfffcffcfffffff
                ffffffffffffffffffffffffffffff67969999b969bfffffffffffffffffffffffff8ff8ffffcb666c66f66c666c66b9bffffffffffffffffffffffc8fcfcbb9b99bcffcffffffffffffcffcffff8ffffcfffcff8fffffffffffffffffff8ffffcfffcfffffff8cfcf8fcffcf8fffffcffcfcffffcffcfc8ff8ff8fffcf8cffffffffff8f8ffcfcf8cfccf8fcfffcfcfcfccf8fcfff8fffcffffcfffffffffff
                ffffffffffffffffffffffffffffffc669697999667cfffffffffffffffffffffffffcfcfcfcf966666c666667666b69bfffcffffffffffffffffcffffff6b979b99fffffcfffffffffff8fffcfffcfcff8fff8fffcffffffffffffcffcfffcf8ffffffffffffcfcf8fffff8fffcffffcfcf8ffffffc8cfcfcffffffffccfcffffffff8fcfc8fcf8fcf8fcfcf8fcf8ff8f8fcfcff8fffff8fffff8fffcffcfff
                ffffffffffffffffffffffffffffffc696979d9b96bffffffffffffffffffffffffff8ffcffcc66666c66667666676d997ffffffffffffffcfffffffcffcb6db9db9fffffffffffffff8fffcffffffff8ffcfcffcffffffffffffffffffcc8cccccffffcffcffcf8fffccccfcccfcfcfff8ffcffffffc8cf8ffcffcf8f8cfff8ffffffcff8fcf8fcff8ff8ff8fcffffcfcfcf8fcffffcffcffcffcffffffffff
                ffffffffffffffffffffffffffffff67696999969678ffffffffffffffffffffffffffcfffffc6b66666c666b66b69b9dbfcfffffffff8fcfffffffffffc6d9b99b6ffffffffffcfffffffffff8ffffffffffffffffffffffffffffffc8cccc8c8c8cffffcffffcfcfcc8c8cc8c8c8f8fffcfffcff8ffcf8fcfffffffcfc8ffffffff8fcfcfcfcff8ffcffcfffc8ffff8fcf8ffffcffffffcfffffcfcfffffff
                ffffffffffffffffffffffffffffffc69699b9b96b6cfffffffffffffffffffffffffff8ffffc66666c6666666666b9d99fffffffff8ffcf8fcffffffcfc9b979b9fcfffffffffffffffffffcfffffcffc8c8c8fffffffffffffffff8cf8cf8cccccffff8fcf8f8ffc8ccccc8cfcfcfcfcffc8fcfffcf8ccff8ffffffc8ffcfffffffff8ff8fff8ffcfff8ffcfffcffcff8ffcf8fffffffcfffff8ff8fff8fff
                ffffffffffffffffffffffffffffff6b69699997967fffffffffffffffffffffffffffffffffcb6666666c66b66b69b9d9fcfffffffcfcfcfffffffffff6d79b9dbffcfcfffffffffffffcfffffff8f8cfcfcfffffffffffffffff8cfccc8cfcf8fc8cfffffccfcffcfc8fcfcf8cf8fff8ffffcf8fffcfcf8ffcf8ffffcffffffffffcffcffcf8fffff8ffffffcffffffcfcfffffffffcfffcfffffffcffffff
                ffffffffffffffffffffffffffffffc66979d79966bcffffffffffffffffffffffffffffffffc67666c666666666b69d9bccfcfffc8fc8cf8fffffffcfcf9b9d9b9fcfffcffffffcfffff8cfffffcfcfc8f8fffcfffffffffffffcfc8cf8fccfcfcfcf8fcfff8fffc8cfc8f8ccffffcffff8fffcffcff8fcfcfffffffff8ffcfffffff8ff8fffffcf8ffffcffffffcfffffffffffffcfffcfffffffcf8ffffff
                ffffffffffffffffffffffffffffff679699999b96bfffffffffffffffffffffffffffcffffffb66b666666b66b69b99d6fc8fff8fcccfcfcfcffffcffcfb9d9d9bcfccffffffcf8fcffcfcfffff8cf8ffcffcffffffffffffff8f8fcf8fcff8f8f8fcfffffffcfffff8fccf8ff8fff8fcfffffffff8fc8ffffcfcfff8fffffffffffffcfff8fcffffffffffcffcffff8ff8fffffffffffff8fffcffffcfffff
                ffffffffffffffffffffffffffffffc66969b996967cfffffffffffffffffffffffffff8ffffc696666c666666666979dccfcfcffcfcc8c8ffffffffcffcb9d9b9bcffffcffffffcffff8f8ffffffcfcfcffffff8fffffffffffffcf8fcfffffcfcf8ff8fcfcfffffcffff8ffcffcfffff8fcffff8ffcffc8fffffffffffffffffff8fff8fffff8fffffcffff8fffffffffffffcfffffffcfffffffcfcffffff
                ffffffffffffffffffffffffffffff6b69699799676cffffffffffffffffffffffffffffffcfcb6666666b66b69b9b9d9ccccfffcfcccccfcff8fffff8ff9d9d9d9fcfcffffff8ff8ffcfcfffffcffff8ff8ff8ffffffffffffcf8ffcfff8fcffffffcffffcf8ffcfcfcfffffff8ff8fcffffffffffcf8fffcf8ff8ffffffcffffffffcffcfcfcfffcfffffc8fcffcffffffffffffffffffffffffffff8fffff
                ffffffffffffffffffffffffffffffc9697999b96b6ffffffffffffffffffffffffffffff8fff696666666666b6699d99cf8fcfffc8cc8ccf8fffffffcfc9d9d99bcffffcfffffcffff8ffcffffff8fffffffffffffffffffffffff8ff8ffff8f8fcff8fcffcfffccfcff8fcf8fffffff8fcffffffcfcfcf8fffffffffffffffffffcfffffff8fcfffffffcfcfcffffffcffcffffffcffcfcffffffffffcffff
                """))
        if player1.y >= 3300:
            scene.set_background_image(img("""
                eceeceeeceeceececcffeeeeeeeceeceeceecececececececececececececececcfcfcfcfcfcfcfcfcfcfcfccfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcccccfccfcfccfcfccfcfccfccfcfccfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf
                ceaeeaeceaeeceeceefceaeaeceeaeeceeaeeceeceeceeceeceeeceeceececececefefcfefcfcfcfcfcfcfcfccfccfcfcfcfcfcfccfcfccfccfccfccfcfccfcffcfcfcfccfcfccfcfccfcfcfccfcfececcfccfccfccfccfccfccfccfccfcfccfccfccfccfccfccfccfccfcfccfcfccfcfcfcfccfccfcfcfcfcfcfcfcfcfcfccfccfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfc
                eeeeeeeaeeeaecaeccfeceeeeeaeeeaeeceeceaeeaeeaeeaeeaeceaeeaeeaeeecfcfccfccfcefcfccfcfccfcfcfcfccfccfcfcfcfcfccfcfcfcfcfcfccfcfccccfcccfcfcfccfcfccfcfccfcfcfceceeeecfcfcfcfcfcfcfcfcfcfcfcfccfcfcfccfccfcfcfcfccfccfcfccfcfccfcfcfccfcfccfcfccfccfccfcfcfcfccfcfcfcfccfccfccfccfccfccfccfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf
                aeaeaeceeceeeeececffeeeaeeeeeeeeaeeaeeeeeeeceeeeeeeeaeeeeeeeeeaeecefcfcfccfcfccfcfccfcfccfecfcfefcfccfccfccfcfccfccfccfcfccfcfcfcfcfccfccfcfcfcfcfccfcfcceceeeeeeeccfccfccfccfccfccfccfccfcfccfccfcfcfcfccfccfcfcfcfcfcfcfcfcfccfcfcfcfcfccf8fcfcfcfccfcfcfcfcfcfccfcfcfcfccfcfcfcfcfcfcfccfc8fccfccfc8fccfccfccfccfccfcfcfcfcfc
                eeececececaeacffffcfaeeeeaeaeaeeeeeeeeaeaeeaeaeaeaeeeeeaeaeaeeececfccfecfcfccfccfccfcccfccfccfcccfccfccfcfccfccfccfcfccccfcccfcfccfcfccfccfcccccfcfcfceeeeeeeeeeaeefccfcfccfccfccfccfccfccfccfcfccfccfccfccfcfccfccfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfccfcfcfc8fccfcf8cfc8fcfcf8cfcfcfcfcf8fcfcfcfcf8fcf8fcfcf8cfc8fc8fc
                ceaecfffceeeeccfcffceeaeeeeeeeeaeeaeaeeeeeeeeeeeeeeaeaeeeeeeeaeecccfccfccfcfccfccfccfcfcfccfccfcfccfccfcccfcccfccfcccfcfccfcfcccfcccfcfccfccfcfccccccfceeee2a2a22ececfcccfccfccfccfccfccfccfccccfccfccfccfccfcfccfccf8fcfcfccfcfccfcfcfcccfcfcccfcfcfcfccfccfcfcfc8fcfccfcf8fcfcfcfccfcfcfc8fcfcfcfcfcfcfcfcfcfccfccfcfcfcfcfcfc
                eeeeecfcfeaeaefcfcffeeeeaeeaeeeeeeeeeeeeaeaeeeaeeaeeeeeeaeeaeeeaececfccfccccfcefccfccfcccfccfccccfcccfccfcccfcccfccfccccfccfccfccfcfcccfccfccfcfcfcfecfeea2e2e2eaeefccfcfccfccfccfccfccfccfccfcfccfccfcfccfcccfcfcfccfcfcfcfcfc8fcfccfcfcf8cfcfcfcfc8fcf8cfcfcf8cfcfccfcfcfccfcfcfcfc8fcfcfcfccfccfccfccfc8fccfcfcfcfcfcfcfccfcf
                aeaecfffeeececfcffcfaeeeeeeeeaeeaeaeeaeeeeeeaeeeeeeeaeeeeeeeeaeeefcfecfccfefccfccfccfecfccfcccfcfccfcccfccfccfccccfccfcfccfccccfccccfcccfcccfcccccfccfeee2a2e2a2e2ccfccccfccfccfccfccfccfcccfcccfccfccccfccfcfcccfcfccfcccfcfcfcfccfcfccfcfcfcccfcfcccccfccccfcfcfccfcfcfccfcfccfccfcfccfcfccfcf8fcfccfc8fccfcfcfcf8cfc8fccfcfcc
                eeeecefccceaeccfcfffeeaeaeeaeeeeeeeeeeeaeea2eeeaeeaeeeaeeaeeeeecececcfecfcccfcccfcceccfccccfcfccccccfccccfccfccfcfccccfccfccfcfecfefecfecfefcefefecefeceaeeea4ebebeecfcfccfcccccfcccfccccfcfccfccfccfcfccfcfccfcfcccfccfcfccfccfcfcfcfcfcccfcffcfcfcfcfcccfcfcfcfcfcfccfcfcfccfccfcfccfcfccfcfcfccfcf8fcfcfcfccfc8fcfcfcfcfcfcfc
                ceaecfefeeeeaefcfcfccee2eeeeeea2aeea2ce2c2ceeaeeeeeeee2ceeeaeeaeecfeeccfecfcccfcccfcfcccfccccccfcfcfecfcfcccccfcccfcfcccfccccecceecececececeecececececeeeee2eeeeeeececececccfcfcccfcccfccccccfccfceceecefcccfccfcfcfcfcfccfc8fcfccfcfcfcf8fcfcccfcfcccccfccccfcfcccfcfccf8cfcfcfcf8cfcfccfcfc8fcfccfcfcfcfcfcf8cfccfccfccfcf8cfc
                eeeeeececeaeeccfcfffaeeaeaeea2ceeeeeeeaeeceeeeeea2c2aec2aee2c2eeaeeeeeeccccfefccfcccccfccfefcfcccccccfceccfcfcccfccccfcfcefefeceecececeeceeaeececececececeaeceeaeececececefccccfcccfcccfcfcfcccccceceececcfccfcccfccfcccfcfcfcfcfccfccf8fcfcfcfcf8fcffcfcfcfcfcfcfccfcf8cfccfc8fccfcfccfcf8cfcfccfcfccfccfccfcfcfcfcfcfcfc8fcfcf
                aeaeaeeeeeeaecfcfcfceeeeeee2cececaeeaeeea2cea2a2eeaeeeeceeaeeaeee2aeeaeecfecfccfeccfccccccccccefcfefcccfccccccfcefcfecceccececeeaeeeeeceeaeeceeaeeeeeceeaeeeeaeeeeeeceececccfcccfcccfcccccccfcfcfeceeaeecfcfcfcfccfccfcfc8cfcccfcffcfcfcfccfcfccfcfcffcfcfcfcfcfccfccfcfcfcfcfcfcfcfcfcf8cfcfccfcfc8fccfccfccfcfcfccfccf8fccfccf
                ee2ee2aea2eeaecfcfffeaea2caeeaefcfeeeeeeeea2eeeceeeeea2eee2ceeeeaeeeaeececfeccfeccfccfefcfcfcfcccccccfcccfcfeccfccccfcfceceeceaeeecaeceaeeececeeecaeceaeeeceeeeceaececeececccfeccfeccfcfcfcccccecfeaeeeafcccfccfcfcfccfcfcfcfcfcfcff8ffcffcfcfccfcfcfcfcfcfcfcfcfcfcfcccfcfccfccfccfccfcfcfccfcfccfcfcfcfcf8fccfccfccf8cfcfcfcfc
                aeaeaee2eea2eefefcfceeeeee2ceeafefceeaea2ceeceeeaeea2eceaeeea2a2eeaeeeaececfececfcececccecccccccfccfcccfceccfceccfccccceceeaeeeeceeeeeeeeceeeaeceeeeeeeeceeaeceeceeceeaececfecfcccfccceccefcfcfcfeeeeeeeccfccfccfccfcfccfccfccfccf8ffcffcfcfcf8fcfcfcfcfcfcfcfcfccfccfcfcccfccfcfcfcf8cfccfcfcfcfcfccfccf8cfcfccf8cfcfcfccfcfccf
                e2e2e2eee2eeeeececefea2aeeeeaeeefeece2eeceaeeea2ee2eeee2eee2eeeeeeeeaeeeefeeefeceefefefefefcefceccccefececeeeccfecfcfcfeeceeeeceeaeeceaeeeaeeeeceaecaecceaececaeeceeaeeececccccfcccfefcfcfcceccecceceaeecfcfcfcfcfccf8fcfcfcfcfcfcffcfc8fcfcfcfcfcf8ffcfcffcffcfcfcfcfccffcfcfcfccf8cfccfcfccfccfc8fccf8cfccfcfccfcfccfcfcfccfcc
                e2ee2ea2ea2e2a2eeee2eeee2ceeeee2ee2eeeaecfeee2eee2cee2ae2a2a2e2ea2cefecce2eee2ee2e2e2e2eeccccccfcfefcccfeeeeaeeefccecfcce2aeeaeeeeeceeeeceeccccecfceccceccccceccceceeeceeaefefecefeccecececefefcfeceeeeafccfcfffcfffcff8fff8ff8ffffcffcfcf8ffffff8ffcffff8fffcfcfcccfcfcccfccfccf8cfcfcfcfcfccfc8fcfcfcfcfcfccfcfcfcfcfccfcfcfcf
                e2b2e24224e2b2e2e2b2e2eee2a2cea2e2a2eeeefeffaea2ea22a2e2e2e2e2a2eaefcfeeeb22b2e2e2b2e4a2aeefcfeccccccfeeea2e2eaecfcfcceeaee2eeeeaeeeaeeeeceecfefcecfcfccfcfefcfefeaeeeeaeeeeeaeeeeeeeceeeceeceaeeeea2aeecfcffcf8ff8ff8ffcf8ffcff8fff8fcfccff8f8ffffff8f8fffcfffccfcfcccfcfcfccfccfccfccfccccfcfcfcfcfccfccfcfccfccfc8fcfccfccfcc
                2e242b2e4e242e4e4e2beeeaeeecee2e2e2e2eaefcfee4e42e4e2e4e2b2e4e2e4eeecefe2e2b2e4e4e2e22e4eefeccccfecfecceeea2aeeefeccefcee2eaeeaeeeceeceaeaececcccfcccefcceccccccceeeaeeeeeaeeeeaeaeaeeeaeeeaeeeeaeeeeeeecffcffffcffcfffcffffcffcff8fffcf8fcffffcf8fcfffffcff8ff8fcccfcfcfcccfcfcfcfccfccfcfcfccfcccfcfccfcfccfcf8fcfccfcfccf8cfc
                e24e2242a24e2e22b2e2e2eeeceecee2b2e2ceeefcfeaeaeee2b2e2b2e242e42b2efefeea2eee2a2a24e4b2aeececfeecefecefee2eee2eeecefeceeee2eaeeccceccecceccccfcfcccfccccfcfcfcfefeaeeeeaeeeea2eeeeeeea2eeae2ea2eeea2ceaecfff8fcff8ff8fff8fcff8ff8ffcf8fccfcfcfffffff8fcfff8fffcfcfcfcfcccfcfccfccfcfccfcfcfccfcfcfccfcfcfccfcfccfccfcfccfcfcfcfc
                2e232b2e242e42b2242b2aeeeeceeee2e2b2e2cefccfccfecee24e2242e4e22e2e2e2e2e2b2eeeee2e2b22e2eeeeeeeeeeeeeeeeaeea2aeeeeeeeeee2ae2eecfecccccccfcefccccfcccfcfcccccccccceeeea2eeea2eceeea2eeeeeeeeeeeea2eeeeeeefcfffff8fffffcf8fff8fffffcffffcfcf8ff8f8fcf8fff8ffffcffcccfcccfcfcfcfc8fcccfcfccfccfcfccfcfccfccfcfcfcfccfccfcfccfccfccf
                42b22e242e42e24e2b2242eeececeee3242e2ceecfccfcefcee2b24e2b224e424e4e4a2b2ebeeceee422e2b24e2ea2eaeea2a2a2ee2eeeeea2e2a2e2e2eaecfccfcffcfecfccefcecfcccccfcfcfcfefceceeeea2eeeeea2eeea2cea2eaeeaeeeea2aeeafcfcf8ffcf8fcffffcfffcf8fff8fcfcfcffffffff8ffcff8fcff8fcfccfcfcfccccfcfcfcfccfcfcfc8fcfccfcfccfccfcccf8fcfcfccfcf8fccfcc
                e22e424e42e42b242e4e2e2eeeeef22e2b2b2eeefcfefcfefe2e24e424e2b22b24a2e4eeeeeeeeee2ae4e24e2ae2eee2e2eeeeea2aeaee2a2ea2ee2a2e2eeecfcfceeeefeeeecefcccfcfcccccceccccceea2aeeeaea2eeeaeeeee2ece2ee2eeeeeeeeeecfffffcffffff8fcff8fffffcfffff8fc8fcf8fcffffff8ffff8fffcfcfcfcccfcfccfcccfcfccfcccfccccfccfcfccfccf8fcccfccfcfc8cfcfcfcf
                b2b2b242b24242eeb2e24e2eeee2eb242422b2eeeeeeeeeeee24e22b2e242e42b2eeeeeeeececcece242e42a42beb2aeb2a2b2eeeee2eaeeeeee2b2eeeb2aeecceceeee2eeeeeeeefecccfcfcfcfcfcfeceeeeeeee2ecea2ee2aeeaeeeaeeaeea2aeeaeecfcf8ff8f8f8ffcf8fcf8c8ff8fcf8fcfcffffff8fcf8fffcffffcfccfcccfcfcfcfccfcfcccfccfcfcfcfcfcfc8cfcfcfcfcfcfcfccfcfcfccfccfc
                ceee2e4224e2b2e2ee2b24a2222e22b2e2b2242e22e2e2e22e2b2b2242b242e2eeecececcecceceee2b24a24eeeeceee2beeea2ae2aee2eea2ebeeee2b2eeeececeee2a4e2a2eaeccfcfceccccccccccceaeeea2aeeae2eeeaee2ee2a2ee2ee2eeee2eeafffff8ffffffcfcfccfcfcfccfcfffcfcfcf8fcfcf8ffcfff8f8ff8fccfcfcccfcccfccfccfccfccfcccfcfcc8fcfccfccfcccfcccfc8cfccfccfccf
                cffee4e4e242e4eb2be2e2424e42b242424e4e24e242e24e4e42e24ee42e2b2b2bececcececeeeee2e2e24e2beefcfebe2ee2eeeeeeeaeeeebeea2abeaeb2aecfeceae2b2b2eb2cfececcfcfecfccfcefeeea2eeeeeeeaeee2eeeeeeeeeeeeaeea2ceaeecfcfcffcfcffff8cfcf8cfcf8cff8fcfc8ffffff8fcfcff8ffffcffcfcfccfcfccfccfccfcfcccfccfcfcccfcfccfcfc8fccfccfcfcfcfcfccfccfcc
                fcfee23242b242e2e2ee42e422e42b2beb2b2b2b2e2b242e2b2b2be4a2b4e4e4eecccfcceceeeee2e42b2e42eefceceeb2beaeea2a2eeea2ceceeceeeeeecccecfeeeeeeeeeeececefcecececfececefeae2eeaeea2eeeea2c2a2e2a22e2a22e2eea2eecfcfff8ff8fc8ccfcf8cfccfcfcffffc8fcfcf8ffcfcff8ffcf8ff8fcfccfccfccfcfccfccfccfccfccfcfcfcccfccfccfccfcfcfccfcfcccfccfcfcf
                cfcfb22e2424e2324e424242e44eeeeeeeeeeeee24242e42beeefeceefecececccfcfccfcfe2e2e24a2424a2b2fcffe2eb2e2a2eeeea2eeaeefcfcfcfcfccfefcccee2e2eeeeeeeeceeceeceeeceeceeeeaeeee2eeeae2eeeee2e2a2ee2b2eeaeeeeeaeecff8ffccfcfcfcf8fffff8cf6f8fcffcfcffffcfcf8cfffffffcfffccfccfccfccccfccfccfcccccfccccfcfcfcfccfccfccfcccfccfccfccfcfccfc
                fcfee4b24e24242e2424e2e42b2eefcfefcfefee2b2e42b2eefccfcfccfcffcfcfcccfcceee32b2b2242e242eeefe2ae22eaeeeea2eebeeeeccccececccefecceefeea2a2e22e2ae2aeeeeeeaeeeeeeae2eea2ceaee2caee2a2e2b242b22e224e2a2eeeaffcffff8cf8cf8cffcf8ffcfccfff8fccf8f8fff8fcffcf8f8ff8fcfcfcfccfccfcfcfccfcccfcfccfcfccccfcccfccfccfccfcfcfccfcfcfcccfccc
                ffef322424b2b24242b2242422beeecefceceeee2424e42beccfcccfcfccccfcfcfcfcfcfe2e22424e2b24e42eeeee24b242e2a2ebeeea2aefefcfcfcefccccefceeeee2eea2ae2eeeea2ae2ee2a2a2eeae2eea2eeaee2eae2e4e2e2e2e2b2b2eeeaeeeeccfcc8fcfcfcfcfcffffcfc8fcf8ffcfccffff8fcfcf8fffffcffffcfcccfccfccfccccccfcccccfccfcfcfccfcfcfccfcfcfccfccfccfcccfcfcfcf
                beb2e4e4e22422b24224242e422eefeceeefeee2e4e242b2eefefefecefefefeecefeceeeee2b2e2b242e2b2b2e2e2b22e2b2eeeeeae2eeeeccecececfceceeceeee2e2e22ee2eeee2e2ee2a2ae2eee2e2eaeeeee2e2cee2ee2e2b2e4e4e2e2ea2e2ea2ccfcfcfcfccfccfcffcfcffcfcfcffcf8fcfcffffcfcffcf8fff8fcfccfcfccfccfccfcceceeeececfccfcfcfccfcccfcfccfcfccfccfccfcfcfcccfc
                242442423242b242b24e42b24e42e2e2e2e42e2b2232b24242b24e4e2e4e2b2e2ee4e2ee2e242424eeeee22e22e2e22e42b2eeeaeeeeaecececececececeeee2e2ee2a2be2b2e2e2a2ee2a2e2e2e22ea2ee2e2a2aeea2eae2eb2e2ee2a2ee2b2eeae2eeeecccf8cfcfcceecfff8fffcfcffcffcfcf8ff8ff8fcf8fffcf8fff8fccfccfccccfcccceeaececccfcfccccfcfccfcfccfccccfccfccfccfcccfcfcc
                e4b2b2b24e42442424242b24242b2442b24a4242b24242e4e424e2b242b24244b242b242e42b2e4a2eeeeee2e4242b24e224e2eeeaeeceeaeeceeceeceecee2ee2a2e2e22e2e2b2e2e2a22e2e2e2b22e2eeaeeeee2eeee2ee2eeae2beee2beee224ea2eecfcfcfccfceeb4efcfffcfeb7bffcf8cfcffcffcfcfcffcfffffcffcfccfcccfcfccfceaeeaeaeecfccfcfccfccfcccfccfcfccfccfcfcfccfccfccf
                3242424242b2b2b2b2b2424e4b242b2424242b2424e4e42b24e23224e242b2e242b224e42b224242beefee2b2e2b22424e4e2aeeeeeceeceeceeceeceaeee2a2e2e2e42b2b2b22e2b2e4e4e4e2b2ee4eb2e2ee2aeea2bea2bea2e2ee2e2e2e2ebe2e2e2eecfccf8fcfe4ebeffcffffee4eeffcfcfcf8ffff8fcf8ff8f8fff8fcfcccfcfcccfcccceceececfccfccfcfccfccfcfcfccfcfccfcfccccfcfcfccfc
                eb4a4b2b242424242424e4242242424e4b2424e4e4242b242b2424e232e42442b224e242b24e4e2b2eeeee2e2e2e4e2e22b2b2eeeeeeeeeeeeeeeeeeeeeeeee2b2b2ee2ee2e2ee4e2e2e2e2a2e2e2e2e2aeeaeeee2eee2eeee2eeb2e2b2ee2e22e2b2eeeefcffcffffeb4e4fffcfcfebebfcffcfc8fff8ffcfcffcffffcf8ffccfcfcccfcfccfccfccfcfccfccfccccfccfccfcccfccccfccfccffccfcccfccf
                cfffee424e42b24e4e4242b2b2b2b242242b24242b2b242b242b2b424e424e2424e42b24224242b2eeeeeeeeeb2e2b2b2e22e2e2a2a2a2a2a2a2a2a2ae2ae2aeee2eb2a2ee2b2ea2ea2be2e2eb2be2a2beeeeeaeeaecaecaecee22b24e2b24b2b242242eecffffcfcfee4becfff8ffee4eeffcfcfcfcfff8fcf8ff8fcfffffcfccfccfccccfccfccfceccfccfccfcfccfccfccfcfccfcfcfccfcccfccfcfcfcc
                fccfeb2b24b242b242b2b242424244e32b242b2b24242b242eeeeeee22b242b242424242b2b2b24242ee2a2e22b2e2e2e4a2e4e2e2ee2ee2eeee2eee2ea2ee2e2ae2eeee2beee2ee2ee2aeeb2ee2eb2eeeeaeeececeeceeeeecea42e24e2422242e2b2e2cefcf8fffce4e4efcfffffeb4effcfcfccfff8ffcfcfcffff8f8fcfcfccfccfcfccfccfcecfcfccfcfccfcfccfccfccfccfcfcccfccfcfcfccfcccfc
                ffcfceb4b224e4242424244e42b24242424e424242b2424e42e2e2eee42b2424e4e42b24242424e3ee2aee2aee2b2b2e2e2e4e2b2e2b2e4a2e2bea2beeee2ae4e2ee2b2ee2e2ae2be2be2e2ee2ae2eeeaeeeeceececeececeeee2e2b2e2b2e4e2b2422b2efffffcfcfeeebeffcfcffebebfeff8fcfcffffcf8fcff8ffffffffccfccfccccfccfccfcfcccfccccfccfcfccfccfccfccccfcfcfccfcccfccfcfcc
                ccececffefb242b4b2b42b242b24e42b24242b24b244e424b2eeefeeea424e42b22b242b2e4ee22e2ae2eee42b22e22b2b2b22a2e4e2b2ee4ae2eeee2a2be2ee2b2be2e2be2b2ee2ee2ee2b2ae2eb2a2e2eeeeeeeeeeeeeeee2e2b224242e242e24e2b2becfcffffffe4e2bfffff8fe4e4ffffcfc8f8fcffcfcf8ffcf8fcf8fcfcfccfcfccfccfccccfcfccfcfcfccccfccfccfccfcfccfcccfccfcfccfcccfc
                eeeaeffffe2b42424242424b24424b244e4b244242b242b22b2cfcfce2b242b242424e424b22bea2e2eee2b2b2e42b242242b24e2b2e2b2b2eececec2b2e2b2b2ee2e2b2e2b2e2b2b2b2b2ee2e4e2e4e2ee2a22a222a222a2e2a224e2b2e42a242e2b2e2ecffcf8fcfee4b2fcfcfffcbebfcfcfcfcffff8fcf8ffcfffff8fffccccfccccfccfccfcfccfccfcccccfcfccfccfccfccfcfccfcfccfcccfccfcfcc
                eeeebfefefe42b24e42b44242b24242b242424e4b242b24442befcefe324e424e4b242b242ee22ebeb2eb2e242b2b2b2bee2e2e242b4242e4aeeceece4b2b242b24b2b2b2b24b24e24e2e4e4b2b2b2e4b2b24e42b2b24b242b24e4e2b242b242b24224e4cffcfffffce2b2effff8ffeebeffffcfcfcf8fff8fccff8f8fffcfcfcfccfcfccfcccfccfcfcfccfcffccfcfccfccfccfccccfccccfccfcfccfcccfc
                ceceefffff4b244232424a42424b2b242b24b24224e424e2b4eeeffee2b242b24242b244a42beb2e2ee2ee2be2e2e2e2e24a24e2b242b2b24eeefefe2e2424e42b242424424e24e4b24b2b22e24e24b2242b24a2424e22b2e242b242e2b22e4e2e2be2eeeefffcfcffee4ebfcfffcffcfefcf8fc8cffffcfcfcfcffffcf8fffcfcfccccfccfcfecfcfcfcfccfecfccccfccfccfccfcfccfcfccfccccfccfcccf
                cfcfcffcfee42b24e42b242b2b24244244242b232424b244242ee4b2e44e4424b24244242b22e2b2b2b24322b24b244e4b244a424b2b2424b22e4a2b232b242b242b24e2b2b242322b2242b2b2b2b22b2b22b242eb24b22b2b2b2eeb2e2eb2e2b2b2e42becfcff8ffcee2e4ffcffffcfffffffcffcfcffffcfcff8fcfffff8fcceaecfcceceeaefcfcfcfcfcccfccfcfccfccfccfcccfccfcfccfcfccfccfcfc
                fffcffffff32b244244242442442b24b2b2b2442b4e424b2b2b42b24b242b24242b42b2b24e2b2e2442b22b244242b24224e242b2b2beeb22b4242442e42b2b24e424e424242b2e424b2beb2b2b2eb24e2b24e2b24a2eb24e4e2b22b2b2b2eb2ee2e4eb2efffcfffffe4e4efcff8ffffcf8fcf8cfcff8f8fcf8fcfff8f8ffffceb2beecececeecfcffcffccfcfccfcccfccfccfccfcfcfccccfccccfccfccccc
                fcffcfcfcf4e442b2b2b2b24b2442424244242b24242b224242424242b2424b2b242424242b2ee4a2b2442442b2b242b2b242b242eceee24424b242beeeb2be4a2b242b2b2e4242b2b2eeeecececeee42b2e4a4eee2ee2ceea2eeb2ee2bee2a2b2b2e2eeecfcffcfcfe4eebffcffcf8fffff8ffcfc8fffff8fcffcfffffcfcffbeb2cccceceeaeffcffcfcfcccfccfcfccfccfccfcccccfcfccfcfccfcccfcfc
                ffffffffff4b2b242424442424b2b4b242b2b4244e42444e42b232b2424b242424e4e4e4b22b2b2e4242b2e424242b24242b242bbeefcfb2b2424b242a2eeeeee42b24242442b2424e4cecefcccfee2b2e4e2e2b2beeaeea2eea2eb2be2e2b2ee2ee4b2becfffff8ffe2b2eefff8fffcf8fcffcfcffcffcfcfccff8f8fff8ffce4beefefceeeeccff8fffccfcfccfccccfccccfccfcfcfcccfcccfcfccfccfcc
                e4b4bfcfcf42424b24b242b4b2242244b2442442b24b2b243244244e4b242b24e424232242b24242b4e42442b2b24244e42442b24aecfe242b2b224aeeeeeb2b2eb24e32b2b24e4b2b2eeefcffffee42b2432324b2e2eb2ebe2e4e2e2e2b2e42b24e2e4eefccc8cfcfb2e4efcffff8fffffcfcfc8cff8fffcf8fcffffcf8ffcfbe2becfcfeaeecfcfff8ffccccfcccfcfccfcfcccccfcccfccfcfccccfccfccf
                424e4ffffea4b242b242b42244b23422442b24a42424242424e2b242424b244242b2424b2442b2b424232b244244e4e232b2b244eeefeebe424244242e2e2e2ee242b224242423224244b2fffcffeeb24b224e4b2eaeeeee2aee32b4323232b22e2b2e2cccfcfccfcf2e4ebffcf8ffcf8f8fc8fcfcffff8fcfcff8fcfffffcffe3e4cfcceeeeaefff8ffcfcfcfccfcccccfccccfcfcccfccfcccccfcfccfccfc
                b4a4bfcfff42b2b42b44232b24242b4b2b24b2424b2b2b2b243244b2324242b2b424b2424e4244242b24424e4b2424442424242b2beeee242b2b2b24e42b42b24b2424e4e4b2b24e4e42ebefcffcfe23244b2424b2ee2a2aee2e2b224e4242e4e424e4aeefcccfccfeee4e2fcfffcffffffcfcfcfcf8ffff8fcfcfff8f8fcffeee4aefcfceceeccfcffcfcfcccfccfcfcfccfcfcccfcfccfccfcfcccccfccccc
                242b2fffcfbb4b2b4b2b244232b2424a4b4a42b4242442442b2424242b2b244242b242b242b42b24424e4e42424e4b2b24b24b2442e2ee4e424242423242b24424e4b2423224242422e42efffcffee4e42242b2b2e2be2ee2eee424b242b2b2e4aee2b2efccfcfcfffe4eebfffcff8f8fcfcfcfcf8ffcfcfcfcf8f8fffffffcfb4e4ccfcfeaeeefff8fff8cfcfccfcccfccccccfcfcccfcccfcccfcfcfccfcfc
                e424befffeeeeffcffeee4a42442b2b2feef2b24b24b24b24244b2b244244a42b244b244b242424b2b424232b244242442442442b24b24232b24b2b24e42442b2b2242b242b24e4a2b2ebefcfffffe32b4b2442444b24b44b43232b24b242eeeeeeeeeeecfcfffcfcfeb24eefcffffffff8fcfc8fcfcffff8fcfffffcf8fcfffbe3ecfeceeeeaecfff8ffcfcccfcccfcccfcfcfccccfcccfcccfcccfcccfcccf
                42b4efcfffcefcffcfcf4244e42324eefefee4b242424242b4224244e4b242442b242b2b24b2b424242b424e44e32b24a42b2b242b244b2e42424424e4a42b24244b242b242b2424e4e4eeffcfcfce242242b2b2b224242242242424242b42eeeeeeb2eeccffcffcfee2eeefffcf8fcf8ffcf8fccfcff8ffcfc8fcf8ffff8fcfeaeeecfeceeeecfcfcffcfccfcccfccfcfcccfccfcfccfccfcfccfcccfcccfcc
                e42b4ffcffeecfcffcfe2b24232442befefee232b42b4b2424b2b42b2242b2b2b4b2b442b24424b2b4242b242b224242424242b4424e24424b2b2b242424b24b2b22b2442b424b2b2eeeaeffffffeeb2b4b2442424b2b2b42b4e4b2b2b24ebeeeaeeebeefefcfcffffeb24bfcfffff8ffcfcfccfcff8fffcf8ffcffff8fffffcfecfeeececeaecff8ff8fcfccfcfccfccccfcccfccccfccfccccfccfccfcfccf
                4b2b4fffcfceeffffcee4232b24e232e2eee2b442b2424232424242432b244242b2fefcf442b242424b2444b244e4b2b4e4b2424b2324b2b2442444b2b42424242442b2b242b24eeeeaeeefcfcfcfe4424242b24b242442b24232244244242eeeeee2e2eccfff8fcfce2ee2ffcf8fcfffff8cfcfc8fffcffcfcfcf8fffcf8fffcfcececeeeeeeecfffcfffcfccccfcccfcfccfcccfcfccccfcfccfccfccccfcc
                244ebefffceeccfcfeeb2b2424232424b24aeeee244b2324e32b4b242424b2b4b2cffffebe444b24b244e24242b24242424232b24244242442b24a24242b2b2b2b2b424442444b2eeeeeccffcfffceb2b2b2b24242b24a4242b24b2b2b2b2b2e2e2e2beefcfcffcfffe4e4bfcfffff8f8fcffcfcfcfcff8fcfcf8ffcf8fffcf8fcfceeeeceaeeaffcfffcfcccfcfccfccccfccfcfccccfcfcccfccfccfcfccfc
                e2b2bffcffceeffffcb2442b4b242b424232eeeee32242b242424232b2b242424befefcf32b224b2442b232b42442b44b2324424b2b2b2b2b2442442b244244244242b24e32e24b2aecccfcfffcff2b2442444b2b2442424b24242424244e4bbb4b2e2eeecffcffcfcee2beffcf8fffffffccfcfcfcfffff8fcffcfffff8fffcfcfececeeeeeeecff8f8fcfcfccccfccfefcccccccfcfccccfcccccfccccfccc
                2b44bfffcfeccfcfcceb2b422423242b2b24efee24e4b2444b24b2424442b42b24effcfee44b2424b2442442b42b4242424e4e4242442442442b2b2444a442b42b2b4242424b42beeecefcffcffcfe44a442b224442b24b242b2b2b2b4b2beefefee34becfcff8ffcfe4e2eeffffcf8fcf8fcf8cf8ff8fcfcf8cfff8fcffcf8fceeceeeceeeaecfcfffffccccfcfcccfccccfcfcfcccccfcfccfcfcccfcfccfc
                e42b2cfcffcfcffffffee4232324e423244eeeeee424244a244242b4e2b424b2beefcffeb24232b244a4b2b242b24b2b2b4232b42b24b24b2b24424b2242b242b24244b2b242b24eecfcffcff8ffce3242b244b22b244242b2442424242b2efefeee2b2cefcfcfcffce2b2bffcf8fffcfffcfcfcfcffffff8fcfcfcfff8fffffeceeeceeeaeeeeffcf8fcfcfccccfcccfcfccccfccfcfcccccfcccfcfcccfccc
                24e4effffcffff8f8ffee32b24b232b242b2242e4232b24242b2b4244242b24423effcff3e4b2444242424442b42b2b4b2b4242b42442b24424b2b244b242b24444b22442b424b4cececfffcffcffe4e4b2b2b2b4232b2b2442b24b2b2b4ecfcfcfeb4befcfcfff8ffe2eeeefffff8ff8ff8fcfccfcf8f8fcfcff8ff8fff8fcfebeeeeeceeeeaecffffffcfccfcfccfccccfcfcccfcccfcfcfccfccccfcccfcf
                4e4a4cfcff8fcffffcffb2b4b24b244b2b24b244b24444b2b42424b232b424b2b2efffef4b244e4a4b2b42b2424b2eefeeeeb2424b2b2442b4242442b24b244b2b2234e3242b2b2cecccfcffcfffeeb2b2b4b2b42b2424242b24424424b2befcfcfe4b2cecffcfcfcfeb24efcf8fcffcffcfcfcf8cffffffcfcfcffffcfcfffcceeaeeeeeeeeecfcf8fcf8cfcccccfccfcccccfcccfcccfccccfccfcfccfcccc
                2b24efffcffff8fcfffceeeeeeeeeeeee2324b242b2b224424b232424424b242b4cfefcee44a4242424244232b42cfffffe24b23242442b242b232b2442442b2424424242b444eeeccfcffcff8fcfe4beeefeeef4424b232b242b2b2324becfcfceee4bfefcff8fffee2bebffffff8ff8ffcfc8fcfcf8fcfcf8fcfcf8fff8fffee2eeeceeaeeeaffffcffcfccfcfcccfccfcfccfcccfcfccfccccfccccfccfcf
                42b2befff8f8ffff8fffceeeeeeeeceeee4b244a4242b42b24244e4b2b242b2b4aeffcff32b2432b2344a42442b4efefcfea4244e4b2b244b24424442b2b24242b2b2b2b424a2beececcfffcffffce4eefecfcfe2b42424424b244242b2beecfcffe3b2cccfcfffcffbe2e4fcfcfcffffcf8fcfcfcffffff8fcfcfffff8ffcfcebebeeeceeeaeecfcff8fccfccccfcfccfcccfccfccccccccfefcecfeccfcccc
                e42befccffffcf8ffcffcececeeceeeee224423244b4244232b24242424b24eeeefeffcf4b24242442b242b2b42beffcffee4b24242444a2442b4e2b244232b4424424424b244eeeccccfcff8fcffeb2cefccfeeb2b2b42b42432b2324b4eefcfcce34befcffcf8ffceeeeccfff8ff8ffffcfccfccf8fcf8fcfcf8f8fcffffffcebeececeaeeccff8fffcfccfcfcccccccfcccfecfcfefcfeccccfeccfecefec
                2e44eefcf8f8fffcffcfb2e2e2b2e2b24b4a424e4242b2324444b232b424b2beecffcffee4b2b4b2b242b4442b42eeffcfee4232b232b2442b2423244a424424a42b2b24242b23ececfeffcffffcfe4befcfccfee32423242b242442b24ebefcfcfefcefccfcfffcffffcfffcf8ffcfcf8fcfcfcf8ffffffcfcfcfffff8fcfcfcbececcececceccffcf8ffcccccfcfcfefccfeccccccfcccfcfececfecefcefc
                24b2bfcfcfffcf8fffffb4b43244324422424b2432b2442b24e2424424b24beecefcfcfee324242444442b2b4b2befcfffea42442442442b244b244a242b2b242442442b2b24b2cececcfffcfcffceb2cccfcfcee44b24e4324b2b244e4beecfcfcccfccfcffcf8ffcfcffcffffcfffffff8fcfccfcfcf8fcf8fcfcf8ffff8ffcffccceacfcfcffcffffcfcfcfccccccfccccfcfcfcfccfeccecfececfececce
                e2e4ecfcff8fffff8fcf42424e42e42b4b2324424244b2444232b42b24232e2cecffffcfe42b432b2b2b23eeeee4cffcfcf4b2b2b2b42b244a242b244442444b2b232b2442324beeccfcfcff8ffcfe4befccfcece3242b2b24b244b2b2b2befcfcfccefecccffffcff8ffcf8f8ff8f8f8fcfcfcfcfcfffffcfcf8ffffcf8ffcfffffcccccffffcffcf8ffccfccfcfcfcccfefcccccfeccccfeceececeecfefec
                2b4beefcfcff8f8ffffcb2b2323243242442b2b2b42b24b2b2442b2432b2b4eefecfcffee32424244232b2eeceebecffcfee4424442b2442324b2442b2b42b242442424b24e4eeececccff8fffcffeb2cfefcfceee3e4b2eeeebeeb2b4ebecfccfcfcfccfcff8fcf8ffcfffffcfffffffffcfc8fc8ff8fcf8fcfcff8ffffcff8fcffcccecfcffffffcfcffcccfccccefccccccfcfeccfcfecececececfececcf
                42e2bfcfcffcfffcfcffb423242b242b232442442b24424244b2444242444ebeccffcfcfb2b4b2b232444befecebefcffcee32b2b2424b2b24244a4242423242b2b2b42442323eeccfccfcffcfffce4eecfcccfeeeeeeeececfefeececeecfcffcfceececfcffffffcff8f8fcf8fcf8fcf8fcfccfcffffffcfcfcfffcf8ff8ffff8fccfccffcfcf8ffffcfcfcccfefccfcfcfccecfccecececeeeeeceecefeec
                e4b4eefcfcff8fff8fff4b24e4424b2442b2b4232442b232b24232b2b4b2b2eeeccffffee42423244e4a2beececeecfcffee2b24232b24244b2b242b4b2b24b2442424b2b24e4eefecfcfffcffcfcebeeccfcfcecb2aeaeffcfcfccccecccefcfcfcceccfcfcf8fcff8ffcfffffcffcffffcfcfcfcf8fcf8fcf8fcf8fffcfffcffffffffffff8ffcfcf8fccccfcccccccecccfcfccfccecececeaececeececee
                2b2becfcff8ffcf8ffcf324b24b24244a4242324e4b2442442b24244242b4b4ceefcfcfce323244b24244beefceccffcfcf3444b24424b232424423224244244232b42424b23eeeccfccfcffcfffce2befefccfeeeceeecfcfcffccceccecfcfcfcfeaecccffffcf8ffcff8f8f8ff8ff8f8fcf8fcfcfffffcfcfcffff8ff8fff8fcfcfcf8f8ffcfff8ffcccfcccfcfefcfcfeccccecfececeeeceeaeeceeeecc
                24e2bfefcffff8ffffff4b242324b232424b24e442432b2b2444b2b2b4b2bebeccffcfcf4e44b24234b232ececccecffcfeee424b2b424424b2b2b24b232b2b2b2424b232442beefccfcffcff8fcfeb2cefcfcfcccccfcfcfcfcfcccc7ccccfcfcfccecefcfcf8fffcff8fffcffcffcffcfcfccfc8ff8f8fcf8fcf8fffcffcfffff8fffffffcffcfcfcfcfcccfececccececcfefcfececeeceaeeceeaeeaeaee
                e4b2bfcfcf8ffffcfcfce4232424242b24424423232242444a242444beeceeceeceffcfee3242b44242b4befcceccfcffcf4b2b2442b4a4b242442442442442444b24242b2b44ecefccfcff8ffffceebefcfcfcffcfcfccfcffcffcffcfcffcfcfcfebecfcffffcf8ffcffcffcff8ff8fffcfcfcfcfffffcfcfcfffcf8ffff8f8ffff8f8fcff8ff8fffcfccfecccfcfefcfceccecccfceccecececeeececeece
                2b2beefcfffcf8ff8fffb4b24b232b444b232b2424b2b42b244b2b2b2eecccecccfcffcfe4b2324b2b42b4ceccccccfcffeb232b2b32b2424b232b42b2b42b232244b232442b2aefcfccfcffcfcffe4eecfcfcfcffcccccfcfcfcffcfcffcfcfcfcfaecccfcf8ffffcff8ff8ff8ffcffcf8fcf8cfcf8fcff8fcf8fcffff8fcfffcf8ffcfff8ffcffcfcfcccccfecececccecfcfcfececcefecececccececfecc
                e2b2ecfccf8fff8fffcf4242424e42423242444b2424232442324242beecfcfeceffcffce3232b2432442befffeccfcfcfee4e44beeeeee4242442b424232424b2b2242b2442beecccfcffcffffcceb2cfecfcfcfcfcccfcfcfcfcfcfcfcfcfcfccececfccfcff8f8ffcfcfcfcfcffcffcfcfcfccfcfff8fcfccfff8fcffff8ff8ffcfff8ffcffcffcffcfcfeccfcfccfefcececccfcfecccfcfcefefcfecece
                ebebeefcffff8fffcfffb32b232432b242b42b242b4b244a4242b4b42ecceccccccfcfcf4b2beeee2b23befefcfcfcffcfceb42b2efcfee32b4b24232b42b442424432b44a4b4eefcfccfcfcf8fffeebeefcfcfcffcccccfcf8ffcf8fcfcccccccceccecfcffcffffcff8fffcffcf8fcf8fcfccfcf8fcfffcf8fcfcfff8f8ffcfffff8fcffcfcff8ffcfcccecfececefecccfcfefececcfecececcecececefcc
                eeeecfcfcf8ffcfff8fee2b244b22442b242b24b24244a242b442423eeecccefecfcfcfceb4beefeb44e4ecfcfccccfcffee4b24befecee24242b424424424a4b232e4242424aeecfcfcffffffcfce4befcfcfcfcffccccffcfcf8fcfccfcfccfececfcfccfff8fcff8ffcf8fcf8ffcfcfcfcf8fccfff8fcfcfcf8ff8ffffcff8fcfcfff8fff8fcfcffcfcfcecefececcefeecececefececfcefefccfecfcece
                fecfecfcfcffff8fffffb4442b24b23244b244244b23244442b23242beecfccfccffcfffbb4befeeeb23befcfcfcfcfcfcfb24b2becfcf4b4b24232b2b2b242424244232b2b24ecfcccfcf8fcfffcee2cefccfcfcfcfcf6fcfcfcfcfcffcfccceceeeefcfccfcff8fffcffcff8ffcfcfcfcf8cfcfcf8ffff8fcfcffffcfcff8ffff8fcfcff8ffffff8ffccececececeeceececececececfececccececcececfe
                cececfcfcff8fcff8fcf4b2b2424242b2324b23223242b2b23242b4b2ecec7fcfccffcfceecccffceeeeeccfcfccccfcffee3e4beefccee24232b24442444b232b42b244244b4ececfcfcffcffcffeb4cfcfcfcfcf8fcffcfcf8fccfccf8ffceceeeaeccfcfff8ffcf8fcf8fcfcffcfcfcfcfcfccfcffcfcfcf8ff8fcfff8fffcfffcf8ffffcfc8fcfcfcceceeeeeeceeceeceeeeecececcefcefcefefcfcecc
                ecefccfcf8ffff8ffffce24232b4b2442423242b424b2442424b2424beeccccfccfcfcfcfcffcfcccececefcfcfcfcffcfee42b2becfcf34b24444e232b2242442b2432b42b2befcfcfcfcffcffcce2beefefcfcfcfcfcfcf8fcfcfcfcfcfcceeea2ecfecfcfcffcffffcffcfffcffcfcf8fccfcf8ffffffcfccfcfff8fcffcff8fcfcffcf8fcffcffcffceaeeceaeeceeceeececeecefefecececcccececfec
                feccefcfcffcf8ffcfff34b24422432b4b244b242b244232b42442b24bececefcfcfcfcfcfcfcfcfccecccffcfccccfcfceeb2b4eefceee24b2b243244234b2b244424242324b2cfcfcfcff8ffcffeb2efecfcfccfcfcfcfcffcfcfcf8ffcfeeeeececcfcfcff8ff8fcff8ffcfcf8fcf8fcfcfcfccfcf8f8fcfcff8fffff8ff8ffff8fcffffffcff8ffccceeceeeeeceeeaeeaeeeaeeecececfefefeefeceece
                cecefcfcff8ffffcfcffb242b234e242423224b2324b2b24232b2324bebe7cccccfcfcfcfcfcfcfcccceccfcfcfcccfcffeeb42beecfcf32b242424e42b242444a232b2b42b2befcfcfcfcfff8ffcee4eefccfcfccfcfcf8fcfcfcfcfcfcfceeaeecfefcfcfcffcfff8fcfcfcf8fcfcfcfcfccf8fcfffffcf8cf8ffcf8fcffcffcfcfcff8fcf8fcffcfffcceceaeceeaeeeeeeeaeeeceeeeceeceeececececec
                efeccfcfcffcf8ffffcf4b2444e43e3e324b4a44e32b42344244244b2eefccfcfccfcfcfcfcfcfcffcccccfcffcfccfcfcfb4be4bcccfee444b2b4232b244b2b24424442b244beefcfcfcffcfffcfeb2b2bfcfcfcfcccfcfcf8fcfc8fcfcffeeebecccccfcff8ff8fcfffcfcfcfcfcfcfcfcfccfccf8fcffcfcfcffffcff8fff8fffcfcffcffcff8fcfcccceceeceeeeeceaeceeeeeeaeceeeeaeaeeceeceece
                ceccefccf8ffffcf8fffb2b2b2bee2e4eb2b2eebeeeee4e2b4a4b2423ecfcfccfcfcffcffcfcfcfcfcfcfcfcfcfcfcfcfcfeceeecefccee322442324244b224232b2b23244b24efcfcfcfcff8fcfce2b2beeffcfccfcfccfcfcff8fcfcfcbeeaeecfeffccfcffcffff8f8ff8fcfcfcfcfcfccfccfcffcf8fcf8fcf8f8ffffcfcff8fcfcfff8ff8ffcffffccceccececeaeeeeeeaeeaeeeeeaeeeeeeceeceecee
                ccefccfcfff8fffffcfce444beeeeceee2b2eeeececeee342424232b4efcccfcccfcfcfcfcfcfcfcfcfcfcfcfcccfcfcfcfcfececccfcf42b4a424e4b24232324244242b242bbbefcfccff8ffffffeb244efefcfcfcccfc8fcfcfcfcfcfbeeeeeaefcfcfccfcff8fcffffcfcfcfcfcfcfcfcf8fcf8fcffff8fccfffcff8f8fff8fffcf8fcffcffcff8fcfcfccfefeceeeeeaeaeeeceeeceeeeeaeeeeceeceece
                cfeccfcfcfcff8f8ffff4a2b2eecececebbbecccfcccee2b4b232442becfefcfcfcfcfc8cfcfcfcfcfcfcfcfccccfcfcfcfcfeccecfcceb42424b232423244e44b232b4232324efcfcfcfcffcfcfce2b2b2eeafcccfcccfcff8fcfcfcfceceaebecfccfcfcff8ffff8fcff8ffcfcfcfcfcfccfcfccff8fcfccfcf8fffcfffcf8ffcf8fcff8ff8ffcfcffcccfeccceeceaeeeeeeceececececeeeeeceeceeceec
                eececfcfcfff8fffcfcfb442beecececeb2becfcccfece4b2442b2b4beefcccccccfcfcfcccccccccfccfcfcfccfccfcfcfcececcecfcf4e32b24424b24e4232242442324e4b2bfccfcf8ffcfffcfee442b4b4cffcfcfccfcfcfcf8fcffceceeecefcfcfcf8ffcf8ffcf8ffcffcfcfcfcfcfcfccfcfffff8ff8fcff8ff8ff8fffcffcffcffcffcf8ff8ffcfccfefceceeececececececcececeaea2ceeaeecec
                eccfecfcfcfffcfff8ff4a4b2ececcecebebceccccccfe4232b444242cccfcfcfcfcfcfccfcfcfcfccfcfcfcfcccfcfcfcfcccececfccee423232b242b232b24b2b2b24b232b4bfcfccfcfff8fffce4b2b243eeefcfccfcf8cfcfcfcfcccceccccfcfcfcfcfcffffcffffcffc8fcfcfcfcfccf8fcf8fcf8ffcfff8ffcffcfffcff8fcfcf8ff8fcffcfffccccfecceceaeceaeececfefefefeeeeeeeaeeeeecef
                cececfcfcf8fff8ffffce42bbecceccecccefcfcfcfeee3e44232b23befecfccccfcfccfccfccfccfcfcfcfcfcccfcfcfcccece7ccfcfeb4b24e44b23244244e444b2b24b2eeecefcfcfcf8ffcfcfee2424e4bfefccfccfcfcf8fcf8fcfcccfecccfffcf8cff8fcff8f8ff8ffcfcfcfcfcfcfccfccff8fffcff8fffcff8ff8ff8fff8ffffcffcfcffcf8fcfcccfcfeceeceececececccccecceaeaeeeaeeceff
                ececcfcfcffcf8ff8fcfbeb2ececceccecccfccfccccce44a42424b24eefccfcffcfcfcffcfcfcfcfcfcfcfcfcccfcfcffccecececcfceee2bee2b2b44b2b4232a42b4b2beeeaefcfcf8fffcffffceb4b23e3eefcfcfcfcfcfcfcfcfcfccceccfecfcffcfcfcff8fffcffcffcfcfcfcfcfcf8fccfcfcffcff8ffcfff8ffcffcffcf8ff8fcf8ff8fcf8fffccfecceccefcefcefcfecfecefceceeeeee2eecfecf
                cefcecfcfcfffffcffffecfccfcccececefecfccfcfcfeb2b4b2324b4cccfccfccfcfcfccfcfcfcfcfcfcfcfcccfcfcfcfccececcfccfcebeeebe2b2eee42b4eeeceeee3eececccfccfccfcff8fcfe2e4b2eecfcfcfcfcf8f8fcfcffcfccfececcfcfcfcfcff8ffcf8ff8ffcfcfcfccfcfcccfcfc8ffcff8ffcff8fcffcf8ff8ff8ffcff8ffcffffcffcfcccfefcefecececcececcecfececfececeaeaeecfef
                ececfcfcff8f8fff8fcfcfcfcfceccebcecccfcfcccfeebbee232b24aeefccccfcfccfcfcfcf8cfccfccfcfcfcccfcfcfccecec7ecfccfbeebeebeeceeea42beecececeeecececfcfccffff8ffffcee324efcefcfcfccfcfcfcfffcfcfececfccccfff8fccfcfff8ffcfff8ff8fccfcfcfcfcfccfcfff8ffcff8ffff8ffffcffcffcff8ffcff8fcf8fffcfcfcecececefcfefecfecfeccefecceceeecececcff
                ccceccfccffffcf8ffffcfccfcfcfccfeceecefccfccfcefeee4444b2ecefcfcfcfcfccfcf8cfcfcfccccfcfccccfcfcffcccceccccfcfcccfececcfcee4b4aeecefececececcecfcfcccfcfcfcffe42b2cecfcfcfcfcfcffcfcceb2becccececfcccfccf8ff8fcffff8fcffcfcffcfcfcfcfcf8fcf8ffcff8fffcf8ff8fcf8ff8ff8ffcff8fcf8ffcf8fffceceeececeeecececceccefcccefeccceceffffcf
                ececfcfcffcff8fffcffccfcfccfccfccebccfccfcfccfccfeb2b232beefcccfcfcfccfcfcfcfccf8fccccfcfccfcfcfccccec7cccf7fcfcfccfcfccecea2b2ececcceccccccccfccfcff8fffffcfeb24beecececcecfcfcffcfeb2b4eefeccfceffcfcfcfcffff8f8ffff8ffff8ffcfccfccfccfcfcff8fffcf8fffcffcfffcffcffcff8ffcfffcf8fffcffceeaeeeeececececefececeefeccfeefccfcffff
                cefeccfccff8fffcff8ffcfccfccfccfccceccfccfcfccfccee43244beccfcccfccccfccfccfcf8fcfcecfcfccccfcfcffcfcfcfcfcccfcccccccccfcceececceccccccffffececfcfccffcf8fcfcee4b2eececceccccfcf8fcfe2b4bececfecccfcfff8fff8fcffffcf8ffcf8ffcffccfcf8cfccf8ffcff8ffffcf8ff8ff8ff8ff8ff8ffcff8fcfffcf8ffceaeeeeceeeeececececfecfececeeccecefffcff
                cceccfcff8fff8ff8fffcfcfcfcfcfcfccfcfcfcfccfcfcfcf324b2b2eefccfccffcfccfcf8fccfccfcbecfcfcccfcfcfcfcfcfcfcfccf6cccfccfccffccecefcccceccccfccccfcfcfcfffcfffffeb24b2cececececcfcfcfcfeb42beefecccfcffcfcffcffcf8fcffffcffffcff8fcccccfcfcfcfcff8ffcf8ffffcffcffcffcffcffcff8fcf8fcffffcffceeeeeeaeaeeeeecefeeceecefefefecfcfcffff
                ceccecfccffcfffffcffcccccfccfcfccc6ccfcfcf8cfcccfee32b43eecccfccfcccccfcfcfcfcfcceececfcfcccfcfcfcfcfcfcfc6fcfcffccccccccffcffccccccccccfcfceccfccfc8f8ff8fcfe2b22eeeececccccffcfcfcee4b2ececcfcccfcfff8ff8ffffcf8f8ff8f8ff8ffcfcfcfcfcf8cff8ffcff8ff8fcff8ff8ff8ff8fcff8ffcfffcf8f8fffcceaeaecefeeaeceeeeecececeeceeeceecffffcf
                ccecfcfcffcff8f8ff8fcccfccfccf8fcfcfccf6cfcfcfcfceeeeeeebecfeccfcfcfecfccfccfccccceeccfcfcccfcfcf8f8f8fcfcfc6ffcffccfccfccfcfcffcccccccfcffcccfcfcfcfffcffcfceb2b432befeceeccfcf8fffeb24befcfeccfcff8fcffcfcf8ffffcfcffffcffcfccccfccf8cfcfcffcf8ffcffcf8ffcffcffcfff8fcfcff8fcfcfcffcffceeeecfeceeeeeaeeaeeeeeeceecececcecfcfff
                ceccefcfcff8ffffcfffcccecccfcccf6cc6fccfccccccceeceaeeeeeeecfcccfcfccfcfcfcfcfcceceaecfcfcecfcf8fcfcfcf8fccfcfcfcf6cc6fccffcffcffffffffcfcfccecfcfcfcfcfcffffe2b24e4eececccccfcffccfe2b4beeeccceffcffff8fff8ffcf8ffff8fcff8ff8fcfccfccfcfcff8ffffcff8ffffcff8ff8ff8fcfff8f8fcf8ff8ff8ffcceccececececeeeeeeeaeeceeceeeeeeccffff8f
                ccefccfcfcfffcf8ffcfcececefccfccfcfccfcccfecfeebee4eecceaecfccfccfecfccfccf8ccccefececcfcccfcfcfcfcfcfcfcfcccfcffccfccccfcfcf8fc8fcfccffcfcccccfccfcf8fff8fcfeb2b2b2befeceeccffcffcfeb232efcfecccffcf8ffcf8ffcfcfcf8ffcf8ffcffcfccfcfcfccf8ffcf8ff8ffcf8ff8ffcffcffcf8fcfffcfffcffcfffcfccecccfcfeceaeeaeeeeeaececcccccceccfcfff
                eccecfccff8ff8fff8ffcecececccccccccccccecccececebea4cecebeeccfccfcfcecfcfccffcceccccccecfcccfcfcf8f8fcfcf8cf6ffcff6ccf6f6fcfcfcffcf8ffcf8ffceccfcfccffcfcfffce244e4b2cfecceccfcfcfcfe2b4beececccfcff8fcff8ffcf8cf8cfcffffcff8ffccfcc8cfcfcfcf8ffcffcff8fcffcff8ff8fffcff8fcfcf8fcff8ffffcfccfececcececeeeceaeeefcfefececcecfcfcf
                ceccecfcfcffcffcfffccceecececfecfecfecfcefecceebee2beceeebeecccfccfccccfcfccfccefecefccfcfccccf8fcfcf8fcfccccfcfcfccccfcfcf8ff8fcfcfcf8ffcfccecfccfcfcfffcfcfebe432beefeeccecfcf8ffcee42befecfeccffcfff8ffcffccfccfff8fcff8ffcfccccfcfc8cfcfffcf8fcf8ffff8ff8ffcffc8ff8ffcff8ffcf8ffcf8fccceccefccfecefceeeeeecececcfcfccfcfcfcf
                cfecfcfcfff8ffff8fffcecececececceccccecccecfeceeeeb2ceccbbbbfcfcfcfeffccfcfcfcecccccecccfccffcfcfcfcfcf8ffcfcf8ffcccccfcfcfcfcffcfffcffcfcfceccfcfcf8ff8ffffcee42e24eecececccfcfcfcfeb4b2eececccfcff8fcffcff8fc8fc8fcff8fcffcfcfcfccfcfcfcf8fcfffcffcfc8ffcffcf8f8ffcffcff8ffcf8ffcffffcfcefefccececfcececececeececccfcefccfcfff
                cececfcccffff8fcffcfcccecececceccfecefcefcececeaeebeeeeeebebccccfcccccfcfccfcccecefecfcfffcfcfcfcf8fcfcfccc6cffcf8fc6fcf8fcf8fcffcfcfcffcfcccccfcfccffcfcf8ffe2b2b4aeeeceaeccfcfcffcf4234cfefecccffcfffcff8ffcfccfcff8ffff8fff8fccfccfcfc8fcff8cf8f8ffffcf8f8ffcffcff8ff8ffcf8ffcff8f8ffcccccecfefcceccececeeeaececefcfccfcfccfc
                ccefccffcf8fffff8fffcceceeaeeccececcceccecececeeea2becccecccfcfccecceccfcfccfcecceccc7fcfcf8fcf8fcfcf8fcf8fccfcfcfcccfcfcfcfcfcfcccccfcccfcececcfcfcf8fffcfcfeb2b242beeaeececfcff8fceb2b2ececcecfcff8f8fcffcfc8cfc8fcfcfcfcf8fccfc8fc8ccfcff8fffcfffcf8ffcfffcf8fcf8fcfcfcf8ffcf8fcfffcfcfefecceccefcefcefecceeeececcccfcccffcff
                ceccefccfffcf8fcff8fccececececefcecefcecefeeeccccebeececcefccccfccfcccfccfcfcccecceccccfcfcfcfcfcfcfcfcfcfcccfcffcccccfcfcfcfcfccccecceccceccefccfccffcf8fffcee42b2b2ceececccfcfcfcfe2b4befeccccff8ffcfff8ff8cfcccfcfcf8cf8cfcfcfcfcfcfccf6fcf8f8fcf8fcf8fcf8fffcffcff8ff8ffcf8ffcfcfcffccecccecccceccecccceeceaeeccfcfcfcfcfcff
                ccefccfccff8ffff8ffcccecececcececcececceceabeecceceaeecfcccfcfccfcececcfcfcfccecece7c7ccfcfc8cfc8cf8fcf8fccf6ffcf8f6fcf8fcf8fcfcccecefcfefcecbcfccfcfcfffcfcfe2b42b4bececceccfcf8fcfee44beecfecccffcff8fcffcfccc8ccf8cfcfcfcfcfc8fcccfcf6cfcfcfcff8ffcfffcfcfcf8fcff8ffcffcf8ffcf8ff8fcfcccccccfcecfcfcfeefceceecececfcccfcfcfcf
                ceccefcfcffff8fffcffcececececfccecfccecfece4aecfcee2cccecfccfcfcfececefcfccfcccececcccccf6fcfccfcfcfcfcfcfcccfcfcfccccfcf8fcfcfffcffcfccfcfcecfcfcfcff8fcfffceb2b24e2cfcfcfcfcfcfcffe4b24ececcecfcff8ffff8fffc8cfccfcfcf8cfccf8fccfcf6fcfcff8fff8ffcff8fcf8ff8fff8fcfcf8fcffcfcfcfcfcfcfccecfcfccfccececccecceceecefccfcfcccfcfc
                ccefccfcf8fcffcf8fffccecefecececececececceebbeccecbeeccfccfccfefecececccfcfcfcececce7cfccfcfcf8cc8fcf8fcf8cfcf8ffccccccfcfcfcf8cfcfcfcfcfcfcceccfccfcfcff8fcfee42b2bbefecccfcfcfcfcfe2b4aefecfcccf8ffcf8ffcf8cfcccccfc8cfccf8cfcfcfccfcccc8ffcf8fcf8fcfcfffcffcfcff8ff8ff8fcf8f8ff8fcfccceccfccfccfccfecefecfeececccfccfccfcfcfc
                cfecefccffff8fffffcfceeeececfecefceccfceceebeccfceaeececceceececececcecfcfcfccecec7fcfcfccc8ccfcfccfcfc8fccccfcfcfc6fcfcfcfcfcfcfccfcfcfcfcecccfcfccf8ffcfffcee4b242eeecececcfcffcfcf3234ecececeffcfcfcfcf8ffccc6f6fcfcfcfcfcfcfcfcfc8fcfcfcf8fcffcff8ff8cf8fcf8f8ffcffcffcffcffcfcfc8cccecefffcfffcfcececceefecececfcfccccfcfcf
                ceccccfccf8fff8f8ffcceaeecececcececececceceb2cceceebecfcfcfeceececeececfccccfcececcccfccfcfcfccfccf8cfcfcfcccfcf8fcccccfcf8fcfcfcfcfccfcccccecefccfcffcffcfcfee24b2b4ceccecccfcf8ffceebebefceccccff8fff8ffcfcccfccfcf6fccf8cfcfcf8cfcfccccfcffcfcf8fcfcfffcff8ffcfcf8fcf8ff8ff8f8ffccfcfececfcffcfcfccefcefccecececfcfcfcfcfcfcc
                cecefcfcfffcfffffcffebeeaeecececcecceccefceabecccea2ceccececeeceeecececefcfcfbecececcfcfcfcfcf8fcfcfcf8fcfcf6fcfcfcffcfcfccf8fcf8fccfcfcfcceccccfccfcff8ff8ffeb2b24eeececccccfcfcfcffeeeececfcecfcffcf8fcffcfc8ccc6fcfcf8cfcfc8fcfccccf6fccfcf8ff8ffcff8cf8fcfcff8fffcffcfcfcfcffcf8ccccecccffcff8fccfecececfececfcfcffccccfc8ff
                ccecccfccfff8f8fff8fceaeeececececcefccfceceebefcceeeccefeceeeceeceeeececceccecececcccfcf6fccfcfcf8fcfcfcf8cccfcfcfccfcfc8fcfcfccfcfcfccfcfcecefccfcfcfcfcffcfe4b2b232cececcccffcfcfcfcecccfcecfccf8ff8fffcf8fccf6fccfc8cfcfc8fccccf6fcfcf6ff8ffcfcfcf8fffcff8ff8ffc8ff8ff8ff8ff8fcfcfcfceeecfcf8fffcfeccfececeeaecfcfcf8cfcfcfcf
                cefefccffcf8fffcf8ffeeeeecececcefccccecccecbecceccecefeceeceeeaeeaeceeceececfceccec7fcfcfcf8fcf8cfcf8fcfcfcccfcfcfcfc8fcfcfcfcfcfcfccfccccecccefcfccf8fffcffcee244e4eeccccefcfcfcffcfcccfecccccccffcffcfcf8fcccccccfcfcfcfcfcfcf6fccccfcfccfcfcf8ff8fcfcf8fcfcfcfcffcfcfcfcffcfcffcfccccccecffffcfcfcceeccfecceecfcff8fccccfcfcf
                ceccefccfffffcffffcfaceaeecececcecfefcfcfceebcefcceceeaeeaeeaeeeeeeeceeceaecccece6eccfcfcfcfccfcfcfccf8cfccfccfcfcccccfcfcfcf8fcfccfccfcfccececcfcfcffcf8ffcfee3e23eeecccccccfcffcfcfccecccccfcfcfcf8fcf8fcffccccccf6fcfcf8fcfcfcccf6f6fccf8fcfcfcfcff8fcfcf8ff8f8fcf8f8ff8f8fcfccfccfcc7cccfccff8fccfcfeeccfeccccfcfcfcfcfcfcfc
                ccecccfccf8fcf8f8fffceeecececcecfccccccccfccefcccfceceeeeeeeeecececeeaeeecccfccccfcccf6f8cf8f8fcfc8fcfcfcfc8fccccccccfcfcfcfcfcfcfccfccfcfececcfcccfcffcffcffe42b24b2cfefcfccfcf8fcfcccffccfccffcf8fcffcfcfcf8cf6f6fccf8fcffcf8f6f6cfcfcf6fcff8ff8ff8fcf8ffcfcfcffcfcffcfcfcfccc8cfcf6fcceccfff8ffcfcececfeccccfcfcfcfcfcccf8cff
                cefecfcfcffffffffcfccceceececfcccccccfcfccccccccececeeeaeeaeeaeeceaeeeecececfcffececcfcfcfcfcfcf6cfcfcfcf8fcfcccccffcfcfcf8cfcccfcfccfccccceccecfcfcfcffcffcfcb24b2beecfcccccfcfcfcffcccccccccfcfcffcf8fcfcfccc6ccccfccfcfcf8fcfccfcccccfccfcfcfcfcfcf8ffcf8f8ff8fcf8fcf8ff8fcfcccfccfcfffffcfcfcffcfcccecccefcecfcf8ffccfccfcfc
                ceccefcfcfcf8f8fffffceaeaeececfefccccccccfececfecfeceeeeeeeeeeceaeececeaeccfcfccfccccfcfc8fccfccfcccccf8cfcfcfcccccfc8fcfcfcfcfc8ccfccfcfeccecfccfccfcf8fcffcee4a2b2beecfccf6ffcfcfcccfcccfccfcff8fcfcfcf8cc8cfcf6fcf8fcfcfcffcfccccccf6ccf8f8f8f8f8fcfcf8fcffcfcf8ffcfcfcffcfccfcfcfcccfcfcf8ff8fcccfefcfeffcfcfcfcfcf8ccfcfcff
                cececcfcfffffffcf8fcceeeeeafeccfccc6cccfcccccecceceeeaeeaeeaeececceceeeececcfcfccceccf6fcfcf8cfccccf8fcfcfccfccfefcfcfcf8cfccf8fcfccfccccfececcfccfcffcfff8ffeb24b24eecfccccccccfcfffcccccccccfcfcfcf8fccccfcc6ccccf6fcf8fcfcf8ff6f6f6cfcccfcfcfcfcfcfcfcfcfcf8f8ffcf8ff8fcf8cccccfccfcfffcfffcffcffccfcfefcfcfcfcf8fcfcfccfcf8f
                cecfcfcccf8f8fcfffffbeaeeaeecfccccbcccccfceccfeceeeeeeeeeeeeeaefefcfececccfcccfcceccfcfcf8cfcfcf6fccfccfccfccfceccfcfc8fcfcfcfccfcfccfcfeccececefccfcffcfcfcfcebe4bbbecefcfccfcccfc8fcccfccf6fcf8fcfcfcfc8cccfcccf6cfccfcff8fcfccccccfccf6fcffcffcff8ff8f8f8fcfcfcf8fcfcff8ffcfcccfcf6f6fcf8fcf8ffccfccfecfcfcfcf8fcff8fcfcf8cfc
                ecececfcfffffff8fcfcceeea2eceefefecececcecceeceeeeae2aea2ceaeecccfeceeaeecccfcfcccecfccfcfcfcfcccccccfccfcfcfccbccfc8fcfccfcccfcfccfccfccfeccccfcfccfcf8fff8fcfcefefeffcfccccccfcffcfcffcffcfcfcfcf8fcf8fccf6c6f6ccfcfcfcfcfcfcffcfcccf6ccfcf8fcf8fcfcfcffcfcf8fcfcfcf8fcfcfcfccf6fccfccffcfcfcfcffcfcfecfcfcf8fcfcfccfcfcfcfcff
                cecefcfccf8fcf8fff8feaeeeeeeeceeaececcececececea2e2aee2eeeeeecefecfeceececfccfcfeccccfcf6fccfcfcccfcfcfcfccfcfcecfcfcfccfccffccfccfcfccefccececcccfcf8ffcfcffcfffcfffcfccccf6f6cfcfcfcfcfcfcffcfcfcfc8fcccc6cfccccf6fc8f8f8fcf8fc6ccf6cfcccfcfcfcfcf8f8fcf8ffcfcf8fcfcfcf8f8fc8cccfc1ccfcf8ff8ff8f8cfccfccfcfcfcfcf8fccccccfcfcf
                cefccccfffff8fffcfffceea2aeaeeaeeeecececececeeeebeb2bebeaeaececcfccfcececccfcccccecefcfcfcf8fccfccccfccf8fcfcccecccfccfcfcfccfccfccccefccecceccfcfccffcf8ff8fcfcffcfcfcffcccffffcf8fcf8f8f8fcf8fcf8cfccfcf6fccccf6cfccfcfcfcfcfcfcf6cfccccfcfcf8f8fcfcfcfcfcf8ffcfcf8ff8fcffcfccfccf6fccfcfcffcfcffccfecfccfcf8fcfcfcfcfcfcfcfcf
                cececfcccfcfffcff8fcebeeeee2b2ebeececececeeeee2a2e2b2eeeeeeeececcfeccccbcecccfcfecccfccf8cfccfccccfccfccfccfcfbcefcfcfccfccfccfccfcccccefcceccecfcfcfcfcfcfcf8f8f8f8f8fcccfcccfcfcfcf8fcfcfcfcfcfcfcfcccccfccf6c6cccfccfcff8ff8fc8cfcccf6f6fcfcfcfcf8ff8f8f8fcf8fcfcfcfcffcf8cfcccfcccfcff8fcf8ff8fcfcfcefcfcfcf8ccfccfccccfccfc
                ccecfeffcff8fff8ffffceeaeebeeae2aeeececcecea2ae2b2beb2a2beeaececfccfcccccfcfccccceccfcfcfcf8fcfcccccfcfccfcfccceccfcccfccfccfccfcccfecfccfeccccfcccfcf8ff8ffcffcfcfcfcffccccff8f8fcfcfcfcf8fcf8fcf8fcfccf6ccccfcfccf6fcf8fcfcfcfcfcc6f6cccfcf8fcff8ffcfcffcfcfcfcf8f8f8fcf8fcfccccfcfccfcfcff8fcfcfcfccfccfcf8fccfccfcccfccfcf8f
                ececefccfcffcf8ffcfcceeeea2ae4aeeeeceeeceeeeb2bebee2aebeeaeebeccefcccfcfccfccfcf7cccfccfccfccfcfccfccfcfcfccfcececcfcfcfccfccfccfceccecfeccececcfcfcfcfcffcf8fcf8f8fcfcf8cccfcfcfcf8fcf8fcff8fcf8fcfc8cccfcff6cc6ccfcf8fcfcf8fcfcc6fccfcf6cfcff8fcfcf8fcf8fcf8fcfcfcfcff8fcfcfccfccf6fccfcf8ffcff8fccfecfefcfcfccccccfcccfcfcfcf
                cecfccfcff8fffffcfffaea2beeeeceeeae2aeeceaeeeaeeeaeeeeeeeeececefccfcecfcfcccccfccccfcfccf8cf6cfccccfcccf8cfcfccecfecfcccfccfccfccfcfcfecceccccfccccfcff8fcf8ff8fcffcf8fcfcccfcfcf8fcf8fcff8fcfcfcfcccfcc6cfcffccfc6fcfcfcf8fcf8fcfccccccccfcfcfcf8fcfcf8fcf8fcf8f8ffcfcfcf8fcfccccfccfcfcfcfcff8ffcfccfeccfcf8fcfcfcfcfccccfcfcf
                cecefccfcfff8fcff8fceeeeececececeeaeeaeeeeaeeeea2eeaeeaeaecececcfecfcfccccccfccfcfcfccfcfcfcfcfcccfcfcfcfcfcfcececfccfcccfccfccfccecfececcececccfcfcfcfcf8ffcfcffcf8fcfcccfccf8fcfcfcfcf8cfcfcfcfc8cc6cfccffcfc6cccfcfcf8fcfcfcf8cfcfccff6cfcf8fcfcf8fcfcfcfcfcfcfcf8f8fcfcf8fcfcfcfccccff8ff8fcfcfcfcccfccfcfc8cc6ccccfcfcfc8fc
                cecccfccf8fffff8ffffccbeaeecececee4a4eeaeeeea2eeeaeeeeeeeeccecececcecccfcccccfcfcfccfcf8cf6ccfcccccccfcccccccceccccfccfcfccccfccefcfecfceccccecfcccfcf8fcfcf8fcf8fcfcfcfccccfcfcfcf8fcfcfcfcf8f8cfccfcc6f6fcffcfcccfcf8fcfcf8fcfcfccfcf6cccf8fcfcf8fcf8fcf8fcf8fcf8fcfcf8ffcfcf8fcf6fcfcfcfcfcffcffcfcfecfcfcffccfcfcfcccccfcfcf
                ecefecfcffcf8fcffcfccecececeeceeeceeeaeeeeeeeeaeeeeea2ceececececcececcfccc7fcccfccfcfccfcfcfccfcccfcfcfcfccececcefccfccfccfcfccfeceeceeccececcccfcfcfcfcf8fcfcfcfcfcfccfccccfcf8cfcfc8f8fcf8cfcfcfc6ccfcccffcf8fcf6ffcfcfcfcfcfccccccfcfcfcfcfcf8fcfcfcf8fcf8fcfcfcfcf8fcfcf8fcfcfcccf6fcff8ff8f8fcfcccfecfcfcf8fcfcccfcfcfcfcff
                cecefccfcffff8ffff8fcccceeeeeeeceeeaeeeeeaea2a2ea2a2eeeaeececcececececcfccccfcfcfcfc8fcfcfccfcfccccfcccfccccccfcfcfccfcccfcccececeaeececcfcccefccfccfcf8ffcf8f8fcf8fcfcfccccf8cfcf8cfcfcf8cffcf8fccfc6ccccf8fcfc6ccf8fcf8f8fcf8fcfcf6cfccc6fcf8fcfcf8fcfcfcfcfcf8fcf8fcfcf8fcfcfcfcfccfcfcfcfcfcff8fcfccfcfcf8fcfcfcfccccccfcfcf
                cecccfccf8f8fff8fcffccfeceaeea2eaeeeeeeeee2eeeb2eeebeb2eecefceceeececfccfccccfccfccfcfc8fcccccfcccfccfccceccfccccccfccfcfccfefcceb2beeaefcfecccfcefcfcffcf8ffcfcfcfcf8cfccfccffcfcfcfcfcfcfc8fcfcfc6fccf6cfcffcfcccfcf8fcfcf8fcfccccfcfcfccfcfcfcf8fcf8fcf8fcf8fcf8fcfcf8fcfcf8fcfcfcfccf8ff8ff8fcfcfcfcfcfcfcfcf8fccfcfcfccfcfc
                cecefcfcffffcfffffffcceceeee2eae2eeeeeaea2aeb2ebe3e2eeaececccecebeccecfececfccfccfcfccfccfcfccfcceccccceccfcefcfcfccfceccefececfeeaeeeeccfccc7fccfccf8fcfcfcfcf8fcf8cfcfccccfccf8fcf8f8fcf8fcfc8fcccccc6fcffcf8fcccfcfcfcf8fcfcfccfcccfccccf8fcf8fcfcfcf8fcf8fcfcfcfcf8fcfcf8fcf8fcccccfcfcffcfcffcfcfcfcfcf8f8fcfcfccccccfcfcff
                cecccfcfcfcff8fcf8fcccceceaeae2eaea2ae2eee4e2ae2e2aeb2ececfefceebececececcecfccfccfcfccfcf6cccfceccfecfccccfcccccefcecfcfeaecececeeeaeccfcfeccccfccfcfcf8fcf8fcfcfcfcfccfccccfcfcf8fcfccfcfcf8fcf8fcccfccccf8fcf8ff8fcf8fcfcf8cccccccfcf6f6fcfcfccf8fcfcfcfcfcfcf8fcfcfcf8fcfcfcfcfcfcf6ffcf8fcf8fcfcfcfcfcfcfcf8fccfcfcfccfcfc8
                ecefeccfcff8fff8ffffcefeceeeeebee2eeeea2b2aeeebeaeeeececececeecebecfecececcccfcccccccfcfccccfcccceccfcccfcfccfcfccccfcceceeeaefeceaeeeecefcccefcccccfcfcfcfcfcfcf8fcfcfcccccfcfcfcfcfcf8fcf8fcfcfccf6f6ccf6ffcfcfcfcf8fcfcf8fcfccfccccfccccfcf8cf8fcf8f8fcf8fcf8fcf8fcf8fcfcf8fcfcfccfccfcfcfcfcfcf8fcfcf8fcf8fcfcfccccccccfccff
                ececfcfcf8fff8fffcffcceceeceea2ebea4a2beebeeb2e2b2beececcfeceeaeecfeceeeceecfecfeccfccfcfcfcccfeccfeccfcccecfcecefecececfceeeeceeeeeececcfcecccfeccfcfcf8fcf8fcfcfcfcfcfcccccfcf8cfc8fcfc8fcfcf8fcfcfcfcccfcf8ff8fcfcfcf8fcfcfcccccfcfcfcfccfcfcfcfcfccfcfcfcfcfcfcfcfcfcfcfcfcf8fcfccfcf8ff8fcf8fcff8f8fcf8fcf8ffcfcfcfcfcfcfcf
                cececfccffcfffcff8fcceeeeeeeeeea2eeeeee2aeeeeaeaebecececeecebebececcecceeccecfccccecfccfcccccccfececcfccfcfccccfeccececececaeeeceaebeeccfcfcceccfc7cfcfcfcfcfcf8fcfcfcccfcccccfcfcfcfcf8fcfcfccfcfcfcfcf6cf8fcfcfcf8ff8fcfcf8cfccf6cccfcf6cfcf8fcf8fcf8fc8fcf8fcf8fcfccccccccccfcfcfcccfcfcfcf8ffcfcfcfcffcfcfcfcf8ccccccccfcfcf
                ceccfcfccff8fff8ffffeeaeaeaeaeeebe2a2aeeeeaeeeeeeeeceeceeceeee2cecfeceeaeecccecceccccfccfccccef7ccccccfeccccefeccecfececeeeececeeeeeececcfcecccfcccfcf8fcf8fcfcfcfc8fcfcccccfcc8fcf8fcfcfcf8cfcfccfcccccccfcfcf8fcfcfcfcf8fcfcfcccccfccfcccf8cfcfcfc8fcfcfcfcfcfcfcfcccccccccfccffcfcf6cff8fcffcfcf8fcff8fcf8ff8fcffcfcfcfecfcfc
                cececccfcfffcf8ffcfcceeeeeeeeea2eae4aeeaeeececececeeceeaeeeaeaebeecfcceecbecfcfcccefccfccfcfcccce7cefcccfefcccceeceececeaeceecececaeecececfcc7ccfcccfcfcfcfcf8fcf8fccfcfccccccfccfcfcf8fcfcfcfccfcccccccc6fcf8fcf8fcf8fcfcfcf8ccccfccfccfccfcfcf8fcfcfcf8fc8fcf8fcfcfccfcfcfcccfcf8cccfcfcfcfcf8f8fcf8fcfcfcfcfcf8fccccceccfcfcf
                ceceffcfcf8fffffffffaeeaeeaeaeebeebe2beeeceeeeaeeeaeeeeeeceeeeececcececceccecccfefcccfccfcfcfcfccccccefecccfefeceeaeeeaeeeecececeeeaececfcfeccfcce6cfcf8fcf8fccfccfcfcfcfcccfccfccfc8fccf8cfccfccfcfccccfcf8fcfcffcfcfcf8fc8fcfcccccccfcf6fcfcfcfc8fcf8fcfcfcfccfccfcccccccccccf8ffcfcccf8ff8fcfcfcfcfcf8f8fcf8fcfcfcfcfcfcfccfc
                ceccccfcfffcf8f8f8fcceeeecefecefceeaeeeeeeeaeaeeeeea2aeccecccceccefcfcefcfcfcfeccccfeccfcccccfecfececccccfececececececeecececeececeeececcfcccbcfcccfcfcfcfcfcfcfcfcfcfccccccccfcf8cfcfcfcfccfccfccfcccf6cccfcfcfcf8f8fccfcfcfcccfcccfcfccfccf8cf8fcf8fcfc8fcccfcccfcfccfccccfcccfcfccfcfcfcfcf8fcff8fcfcfcfcfcfcfcfcccccccccfcff
                ccecfcfccf8fffffcfffceaeaefefcfcceceeeaeea2eeeeeea2ebeefecfeeceeecbeeccccecccccfcfeccfcccfcfccfccfccececececcececeeceececeaeecefeceaceccfecceccfcfcfcf8cf8fccfc8fccfc8fcfccfcfcccfcfcf8fcf8fcfccfccfcccfcfcfcf8f8fcfccf8fc8fcfcccccfcfcfccf8cfcfcfcfcfccfcfcfccccccfcccccfccccfcfcfcfcc8fcf8fcfcf8fcfcf8fcf8fcf8f8fccfcfccfcfcfc
                cfefcfccfffcf8fff8fceeeeececceccfffeaee2eeeaeeeeeeceeececeeaeececeaeaefcfcfcfcceceaeeccfcccefecefececcefecfeeceeececececeeececececcfecfecccccfccfcfccfcfcfcfc8fccfccfcfcfcfcccfcfccf8cfc8fccfcfcfcfcccccc6f8fcfccfc8fcfccfcfccfcccccfcccfccfcfcf8cfcf8fcfcf8fccccfccfccfcccfcfccfcfc8cfcfcfcfcffcfcfcfcfcfcfcfcfcfcccccccccfcfcf
                ceccfcfccf8fff8fffffccececececceccfceeeaea2eeeaeeeaeaeeecceeaeeaeeeeececcccecfeceeeeceecefecccfeccecefececeeaebeaeeeeeeeeceececefecefcccccefccfccfcfcfcfccfcfcfcfcfcfccfcfccfcfccf8cfcfcfcfccccccfcfccfcfccfc8fcf8fcf8fcfcfcf8cccfcfccfccfccfcfcfcf8cfcf8cfcfcccccfcfcccecfccccfcf8fccccf8ffcf8fcf8fcf8fcf8fcf8fcfccfcfcfecfccfc
                ccfcccfcffff8ffcf8fcceaeeaeececccfceceeeeeeaeeeeaeeeeeceefeceeeececcecfcfefcccceaeaeeaececceeeceeecececeeeaeeeeeeeaeaeaeaeeceecececfccfcefcccccfccfc8fc8fcf8cfcfccfccfcccccccfcccccfcfcfccfcfccfccfccccf6cfcfcfccfcfcfc8fc8fcfcfccecfccfccfccfc8fcfcfccfcfcfcfccccfccccfcccfcfcf8fcffffcfcfcfcfcfcfcfcfcfcfcfcfcfcccccceccfcffcf
                cecefcfc8fcffcffffcfeeeceecccccefcfceceaeeaeeaeceeceecececeea2aecefefccecccfefeceebeeeececeeceeaeaeeeeeeaeeecefeeeeeee2beeeececeecccceccccecfcfcfccfccfcfccfccccfc8fccffccccccfccccfc8f8f8ccccceccfcccfcfccfc8f8fc8fc8fcfcfccfcccccfcfccfcccc8fcfc8fcf8fc8fcfcccefcfcfeccfcfcffcffcfccf8ff8f8fcf8fcf8fcf8fcf8fcf8fccfccfcccff8ff
                cccfcfccfff8fff8ffffaececfcfefccffcccececeeceececeeceeeeeeea4beeeccccefcfccccceceeeececefeaeea2eeeececeeeeaeeeaeaeeaeaeeeceaeeeaecefcfcecec7ccccfcfcfcfcfcfcfcfcfcfcfcccfccccfcfccfcfcccfcfcfcccefcfcccccfc8fcfcfcfcfcfccfccfcfcceccccfccfccfccfcfcfccfcfcfc8fccccccfccccccfcf8fcf8ff8fcfcfcfcfcfcfcfcfcfcfcfcfcfcfcccccfcfcfffc
                cfccfcfccfcff8ffcf8fcececcecccfccffcffcffccecceeeaeeeaeeaeee3ebecfecfccceceeeceececeeeeabeeeeeaececeeaecceececeeeeaeeeeceeeeeceececececcecccccfccc8fcfcfc8fccfcccfcccfcfccccccfccfcccffccfccccecccecccfcfcfcfcfccf8cfccfccfccccfcccfcfccccfcccccfcf8fcf8cfcfcfcfefcfecfcfecfcfcf8ffcfcff8fcfcf8fcf8fcf8fcfcfcf8fcfcccfcccccffcff
                ccfccfcfcff8fff8ffffccccefcfefefcfcfcfffcfcfeecaeeeaeeaeeeaeeeeaecefecefcfaeaeaeefeececeefeeaeeeececeeceecceceececeececececececececececfcfcfcfcfcfccfc8cfccfccfcfccfccfccccecfccfccfc8cf8fcfcccecccecccfcfcfccf8fcfc8fcfcfcfcfccccecfccfcfcccccfcccfccfcfc8fcccccfccfcfccccfcffcfcf8fcfcfcf8fcfcfcfcfcfcfc8ccccff8fffccfcfcccccf
                cfcfccfc8ffffcfffcfcccecceeceaeecefcffcffccfceeeeaeeeeeeaeeeeeeecececefeeeeeeeebeeeeeeeeeeeeeeeaeecececececececeeeceeeceecececececeecececfcfccccfcfccfcfcfccfccfccfcfccfccecccfccfccfcfccfccfcfcfecccecfcc8cfcfccfcfcfc8ccccfcfccccfccfcccccccccfcfcf8fcfcfcffcfecfccfccfccfcf8fcfcfcf8fcfcfcfcf8fcf8fcf8fcccccfffcfcfcccccfcf8f
                ccfcfccfcfcf8ff8ffffcfcfeceaeeeaefcfcffffcfeceaeeeecceceeeeececeeeeeeeeaeeceea4aeeeea2b2aeaeeeaeeaeececececeeeeeceeeaeeceeceaececeaeececeececfcfcccfccfcccfccfcccfccccfcfccccfcfccfccfcfccfcccecefcfcccfcfcfcfcf8cfc8fcfcffcccfcceccfcccfcfeccfcccccfccf8fcfccccfcfcfcfcefcfcfcf8f8f8fcf8ffcf8fcfcfcfcfcfcfceccfcff8f8fffffc8ccf
                cfecfcfcffffffcff8ffccecceceeaeecfcfcffffcccfeeeccfcfcfeeaeeaeececea2a2eeeea2be2ca2a4b2beeeeaee2aeeecececeaeaeaeeaeaeeaececeecfeceeceaeececcccfccfccfccfcfcfccfcccccfccccececcccfccfccccfccfcfeccfccfcccfcfcc8cfcfcfccfccccfcfcccccccfcfeccccecccfccfcfccfccfcfecffffcfccccf8f8ffcfcfcfcfcf8fcfcf8fcf8fcfccccccff8ffffcf8fcfcfcf
                ebeecfcc8f8f8fffcfcfccfefecececccfcfcffcfceeeaeceeffffceceeeeaeeee2be4beaeeeeaeceeee2bb2beeeeeeceeaeececeeecececcecececfeccccecccceceeeececcfcccfccfcfccfcccfcccfcfcccfcfbeccfcfcfccfcfccfccccceccfecefccccfcfcfcc8fcfccfcfcccfccecfceccfccfccccccccf8cfccfccccfccfcfccfcfccfcfcfcffcf8ff8fcfcf8fcfccfccfcfcfcfccfcccffffffccccf
                b2becffffffffcf8ffffceecececccefefcfcffffcceeeeeaefcfffeeeea2eeceaeeaeeaeececeeeeceea2eb2ceeeceeeeeecececccececfecfcfceccfecfccfecfeceaeeaeccfcccfccccfcccfcccfccccccecececcccfcccfccccfccfcfceaefcfcccfcfccfccfcfccfccfcccfcfcccccecfcccfceccfecccccfcfcfccfcecfcfcffcccccfcfcf8f8f8ffccccccfcccccfcfcf8cfccfcfccf8ff8fcf8fcfcc
                ebeecfcfcf8fcffffcfccececefcfecccfcfcffcfcececececffcffceee2aeeeeea2eee2ceeceeeceea2ebeeaeeceeaeaeaeeaeecececfceccececfececcefeccececeeceecfecfcfccfccccceccececcfecfcfcfcecefccfccfcfcccfcccececcecceccfcfccfccfcfcccfccfccccfcecccccfcfccccecfceccfcfcccccecfccfcfcfcfcccfcf8ffcfcfcfcfcfcfccfcfcf8f8fcfcfccf8fcfcfcff8ffcf6fc
                e4aecffcffcff8fcffffcececececccfcfcfcffffceceaececffffcea2a4b2a2a2eeaeaeeeeeee2a2b2eeea2eeeeaeeeeeeceecececceccfcecccecccceccccecceceaeeaececcecccccccfecfecceccecccecececcefccfcfcccccfcccfcceaefcfcccfcccfccfccfcfcfccccfcfccccecefccccccecccfecccfccfcceececffcff8fcccfccffcfcffcff8fccc8ccccc8cfcfcfcfcf8fcccfccff8fffffcfff
                bebefcff8ff8ffffcf8fcececcecfececfcfcffcfccececceccfcffeb4b2b2beebeeeeeeaeee2a4b4a4aeeeececeeeaeaecccfccccefcfecefceccececcececcececeeceecececcececececceccecceccfefccfcfeccecfcccfcfcccfccecececcfececccfccfccfcccccccfcfcccfcfcecccfcfcfeccceccccccfcfcceaecfcff8ffccccecfcf8fcf8fcfcfcfcfcf8fcfcfcfcfcf8fccfcfc8fcfffcf8fff8f
                4ebeffcffcfffcfc8cccccecefcecccfcfcfcffffccccfcccfffffceeaeea4eeeeaeceaeeeaeeeee2beeececea2a2aeeecfcceccfecceccfcecceccecefeccececceccecceccececefecfecefececececccceccecceecccfcfcccfcccfccfceaefeccccfccfccfccfcfcfcfccccfcccececececcecccefcfeeccfcfccececccfcfcfcfccccccfcfcfcfcf8fcf8ccccccfccf8fcf8fcfcfcf8fccf8f8fffcfcff
                b2becffcff8ff8fccfcccfcfceccececefcfcff8fccfecfffcfcffffcfeeeaeaeeeeaeeeeee23b2aececceceeeebeeccfcecfcceccfcfececcefecfeccecefecfecfeececefecfeccececececcfeccccefecfefcfeaececcccfcccfcecececeecccfecccfccfccfccfccccccfcccefcecececfefceeceeeecceccfcfcccececff8ff8fccfccfcf8fcf8ccfccfcfffffcfcfcfcfcfcfccf8ccfcfcffff8ffff8f
                b2befcff8ffcfffccccfcffcceecececcfcfcffffcfccfcfffff8fcfccceeeeeeeaeeeeaeeaeeeaeecececececeaecececfcecfeceeececeececeeeceecececeeeeececeeceeeaeeececeeceececfecfcccecccecececcfcfcccfcccceccfeaecefccecccfccfccfcccfcfccccfecececebececececeeaeceeccfcfcfccccfcfcfcfcfccceccfcfcfcfcccc8fcfc8cfc8fcfcccccccfccfcfccff8fcffcf8fff
                b2beffcffcff8ffccfcccfcfeceecececfccffcffcccfcffcf8fff8ffcceaeeaeeeeeeeeeeeeaeeececeeeaeeeeeecfcccecccececcececececececececeeceeaeceaeececeaeececeaeceaecececcecefecfececceccececefcecececceceececececcfccccccccfccccccfececceceeaeeceaeeceaeeeececccfcfcccfeccff8ff8fccccccfcf8fcf8cfcfcccfcfcfcfc8fcfccfc8fcfccfc8ffff8ffffcfc
                ebebfcf8ff8ffcfcc6cccfffceceecececfcfcfffcfcccfffffcfffcfcfeee2eeeeeaeeaeeaeeeeceeecebebeaeaececfccfecceaeececececeeaeaeeaeceaececeaeeceaececcececececececececfecccecececefcfcfefcecceccecececeaecfccceccfefcfccccfcfecccfceceeceeeceeececeececececefcfcfccccfcfcfcfcfccecccf8fcf8fcfccfcfcfcf8cfcfcfcccc6cfcf8fcfcfccccfcc8ffff
                bebecffcfcffff8fffffffcfcbecececcfcfcffcfcccfcfcf8ff8fffcfceeaea2a2b2a2ea2eeeeeeeceeeeeeeceecfccefecfefececececececcececcecceccecceccccececcfecccfcecfecceaececcefeceaeaecceecececaeecefceceaeeececefefcecccccfcfcceccfeecececeeeceececececeecececccfcfcfccfcccf8f8ffccccccfcfcfcfcfcf8fcf8fccfcfcfcffcfcccfccfcf8cfcf8ccfcff8fc
                cfcffcffcfcf8fffcffcfffceeeecececfcfcffffccfccffff8ffcfccceeeeeebbb2bebe4aeeaeaeeeecececceccecefeceebeecefcefcfefcfefcfefcfecfecfccfefefccecccfceccfcccceccecceccccecececfecfececeeeaececcececececfceccefcfefececefcececececeeceeeaeeeceecececececcccfcfcfcfcfcfcfcfcfccfcccfcf8fcfcfcfcfcfcf8fc8fcccfc6cfccfcf8cfcf8cfcfccfcfff
                cfcfcf8fcfcfffcff8ffcfcfccececececfcfcf8fcfcccfcf8ffffffceeaeaee2eeeeeeaeeeeeeeeaeaeeecececfececebebebeeceeceeeceeceeeccecccecccecececccecfcececfcececfefcfcecfefeccfccfececeeeaeeaeeececfecfeccfecefcececececcfececcececececeecaeeeaeecececececcccfcfcf8fcfcf8fcf8f8fcfcffccccfcc8fcf8fc8fcfccfcfcfccfccccfcfcfcfcfcfcccfcfff8f
                cccffffcfcffcff8fff8ffffcebecececfcfcffffcccfcfffffcf8fccceee2eaeeaeae2eeeaeeaeeee4bececefeeeceebebeeebececececebececeecefecfececefecfecfcccfccccccfccccceccfcccccececeeceeeaeeeeeeeaececececcfeccccecececececeececeecececeeeceeeeaeecececececccccccfcfcfcf8fcfcfcfcfcfcfccfcfcccfccfccfcfcfcfcfcfcccccccf6cfc8fcfccfcfcfcc8fcff
                cfcfcfcf8fcff8fffcfffcfcceceecececfcfcfffccfccf8fcff8fffceaeaeeeaeeeeeaeceeeeeeeeaeeeeeeeeceeebeeeebebebeeecebececebecbeccececececececccecececfecfecefecfececeecefecececeaeeeaeaeaececcecfecfeccefefececeeceeeeeeefeeaeeeececeeaeeeecececececcccfccfc8f8fcfcfcf8f8fcfcf8fcf8fc8ccccf8fcfcfc8fcf8cfccfccf6ecfcfcfc8fcfccccfcfffff
                cccff8ffcff8fffcff8ff8ffcebecececfccfffcfcccfcfff8fffcfcceeeeeaeeeeaeeeceeaecececececececeeceeebebebebeeecebeeeeeecececefececececececececcfececcececceceeceeeceeeeeeeeceeeeaeeeeeecececceccececececececeaeeceaeaeeeeebeeceeeeaeeeaecececcccfccccfcfcfcfccf8fcf8fcfcf8fcfcfcfcfcfcc8fcfcf8cfccfccfccccccccf6fcfccfcfc8fcfccfcf8fc
                ccfcffcffcffcf8ff8ffcffceceecececcfcfcfffcfcccfcffcffffffcceceececeececeeceeeeeceeeeeeecebeebeceeee7eb7beeceeccebcecececccececeeceecececececccececcececeeaeeeeeceaeaeeaeeaeeeeaeecefccefcecceceeaeaeaeecececeee2eeeea4eeeeaeeeeceececccfefccccfccf8f8fcf8fccfccccccccccf8cf8cfcccfccfcfcfccfcccfccfcfcfcf7cfccfcfcfcfcfcf8cfffff
                cccfcff8fc8ffffcfff8ffffcebeececefcfcff8fccfccff8ff8f8fcfcecececeeceececeecececeececebebeeeceebebeceeeeeceeceeeceececccececeeeceeceececececececcceccececeeeaeaeeeeeeceeeaeeeaeeecececececcefececeeeeecececeeceab2aeeeaeaeceeccecececececccecfcccfcfccf8fccf8fcfcfcfcfcfcfcfcfcf8cccfcf8fcfcccfcccccccccccfccfcfcf8cfcff8ffff8f8f
                cfcff8ffcffcf8ff8ffffcfcceeceececfccfcfffcccfcfcffffffffffcecececececeeeceeeeeeeeeebeeeeebebebee7ebebeceece7ecbeccecefecfecececececececcecececececececeeea2eeeaececceceaeeeaeeeaececefcececececececcecececceee2ebeeeeeeeeeaeeecececefeccfffcfcfcf8cfcfccf8fcf8cccccfcc8fcf8fcfcfcccccccccccfcccfcfcfcfcfccfcfcf8cfcf8ffffcfffcff
                cccfffcfcfcfffcffcf8ffffccececececfcfffcffccccfff8fcf8fcfcfececeeceeeceeeaecbebebeceebcbeceebe7eceeceeeceececeececfecececececeecececececececececefcecfeceecceeeececececeeceeeceecececececfececececececececececceeeaea2aeaeeeaeeececcecceccfcfcf8cfcf8fcfcfcfcfcfcfc8cfcfcfccf8fccfc8cccfccfccfccccccfccfcfcccccfcfcfcfcf8ff8fff8
                ecfcfcff8fcf8ff8ffffcfcfcccccccccfcfcfff8cfcfcfcfff8fffffcceceeceececeeaeeeeeeececececeececececececececececeececeecececececececeecececececececefececeececeeececcececececececceccecefececececcececececececececeeceeeeebeeeeceeaeaeececcfccfcf8fcfcf8fcf8fcfcf8fcc8cfccccf8cf8fccfc8fcfcfccfcccccfcfcccfccf6fccccfcf8cffffffcff8ff
                cccfff8fcfcffcffcf8ff8fffffffffffffff8ffffcffcff8ffffcf8fccecececeecebeebebebebeececececececceccecceccecececcececfececececeeecececececececeeceeceececeececececeececececefeceecececececececeecececececececcececeeeceeeececceceecececceccccfccfccfcfcfccfcf8fccfcffccffcfcfcfcfcf8fcfcfcf8fccfcfccccfcfccfccfcfcfcfcfcf8f8f8ffffff
                cfcfcffcfcf8ff8ff8ffcffcfcfcfcfcfcfcffcfcffcff8ffcf8fffffceceeececeeeeceeebeebebeececfefccfefcfecfececcccccececeeeceeceeeeeceecececececeeeceeeceeeeeeceecececeaeeceecefeceececeececececececeeeeeeeceececececeeaeeaecceccecceccececccfcfccfcfcf8cccccfcc8ccfcfcfccfcfcfcfcfcfcfcfcfccfccfcfcccccfeccccfccfcfccfc8fccfcfffffcf8f8f
                cccff8ffcfcffcffcffcff8fff8fff8fff8ff8fff8ff8fffffffcf8ffcececeeeecebcececececececeeececeeceeecececccfefefcfcfecceeceeeceaeecececececececeeeaeebeaebeaecececeeeeaeeceeceeceeceeeeeeeceeceecececeaeeaecececeece2a2eeeececceccecccccefccfcfcf8fccfccfc8cfccfcf8cf8fcf8cfc8fcf8fcfccfcf8fcfcfccfcccfcfcccfcfccfccfcfcf8fcf8ff8fffff
                cccfcff8fcf8ff8fff8ffcff8fff8fff8ffcffcfcffffcfcf8f8fffcfcceecececebecececececeececceceecececececececcccccececceeceeeceaeeeaeececececeeeeeceeeeeceeceeececeececeeceeceeceeaeeeaececeecececececeeeceeeceeceeaeaeeaececececccfccfeccccfccccfccfccccccccccccccfcfcfcccccccccccccccf8fccfcf8cfcccfcccccfcfcfcfcf8fcfcfccffffcfff8fcf
                cccffcffffffcfff8fff8ffcffcffcfcffff8ffff8fcfff8fffffcfffceceeceecececececcefececeecececeeecececeaecefecfecfcececeaeaeeeb2aeececececcceaebebeccecececcceccceccececececeeceeeaeeeeaeececccccececceececeeceaeeeeeeeececcecfcfecfccfcccccfccfcfcfcf8fcfcfcffcfcf8cfc8cfccfccccccccfccfcfccfcfcfccfefcccccfccfccfcfccfcfcf8ff8fffff8
                cfcfff8fcf8ff8fcffcfff8ff8ff8fff8fcffcf8ffff8fffcf8fff8ffccece7cebcecccfecfecceccceceeeeceaeeaeecececccceccccfecceceeceaeceecececcccecceceeceecececcceccceccecececececceeaeeeeeaeeececceccccccececeeaeea2eeeececcecececccecfccfccfcfcccfccf8fc8cfccfcfcccf8cfcfcfccccccccfccfcccfcf8fcfcfccccccccfcfccccc8fcfccf8fc8fffcffcf8fcf
                fcfcf8fff8ffcfff8ff8fcffffcfff8fff8fff8ffcf8fcf8fffcf8ffcfec7ecececfefeccecccefcecceceab2beeeeceececccfecfcececcfcefceceececececceffffffceceaeeccffffcfffffccececececeeceeeaeceeececcccfccfcfecececeeeeececeeeaeecececcfcfccfccfccccfccccfcccfccccfccccfccfccfccfcfcfccccccccccf8fcfcf8fcfcfcfcfccccfccccfcfcf8fccfcfc8fc8ffffff
                cfffffcfcff8ff8ffcffffcf8ffcfcfcfcfcf8ffcfcfffffcffffffcfcceceecbececccefccfecccfececeebebeeaeeceaecececccefccfececcececceccecccfcfcfcfccceeecececfcffcfcffcccececececececeececceccececcf6fccfceceeceaeaeea2aeeecececccefccfccfccfeccfcfccccccccfcccccccccccccf8fcfcfccfeccccccfccfccfccfccccccccfcccf7c6cfcfcfcfcfcfcfccfcf8f8f
                cccf8ffff8fffcffcff8cf8fccf8fcfcf8fcfccfcf8cc8fcff8f8fcffcceecbeeccfefccececcfececcecea4b2aeeeeaeececfccfeccecccefceccfeccefcefeccffcfffcccccccccfffcffffcffecececececececceceecececcccf6f7fcccececeaeeeeaeebeaeececcfcccfccfccfeccfccccccfccccccccccf6fccccfccfccfcccccccfcfcfcfcf8ccfccfcfcfcfccfcfccccfcf8cfcfcf8fccfcfffffff
                cfcffcf8ffcf8ff8ffcfcfccfcfccf8fcfcf8fcf8cfffcff8ffffff8fcccececcececececeeeeececececeececeeeceececcecececcefececcececececececccfcfcf8fcfffcfffffcfcf8f8ffcfcceccececececeececececececccfcccfcecececeececeeceeecececcecececcececccccefcfcccccffcfcfcf6eccfcfcfcccccccfccfccfcfccf8cfcccfcccccccefcfcfcccccfcfcfc8fcfcfccc8f8fcf8
                fcfcff8fcffffcffcfff8fcfcf8fcfccfc8cfcfcfcfc8fcfffcf8fffffecfefccfefccfeececececececececeeeceaecececfcecececececececcececececefecfcfffcfcfcffcfcff8fffcccccccececcececececececececececfccf6fcfceccecececececccececcefcccccecccccecfccceccfcccccfcccf6ecf6cccfccfcccfccccccfcfcfccfccfccccfcfccfccfcfcf6cccfcfcfcfcfcfcf8fcffcfff
                ccff8ffff8fcff8ff8fcfcf8fcfcf8fcfcffcf8fcf8cfcff8ffffcfcfcccecececcceeeceeeaeeaeecececececeeeececfececececececececececececececcccffcf8fff8ffcfcfcffcf8fcccccfccfeccececececececeececfecf7fcfcccecececcecececececececcececececececcccfccfeccfccfcf6fcfcccccfccfcccfcccccfccfccfcf8cfccfcfcccccfecccf6fccccf6fcf8fcf8fc8cfccfff8fc
                fccffcf8fff8fcffcfff8cfccf6cccf6cf6ccccf6fcfcf8ffcf8ff8ffcfecfecfeefeceeaeeeceeececeeceecececeeceecececececececececececfeccccefeccff8ff8ffcf8ff8f8ff8fffffffcffcfcfeceeceeceeececeeeececf6fcccececececececececececcefccceccceccccfeccefccfcccfcccfcccccf6ccfccfcfccfcfccccfcfc8cfcfccccccfcfecccfcfccfffcfcfccfcfccfcfccfcf8ffff
                ccfcffcfcfcfff8ff8fcfccf6cfcf6cfccfcf6fcfcfccfcfffffcffffccceeceecebeeceeeaeeaeceececececeeeeaeececeeceeeceeceeceeecececcfefcccfcfcffcffcffffcffffcffcf8fcfcfcfcffcceceeceeeceeeecececcfcccfcceeceeceececeecececcecccececceccececccfccccccfcccfcfcfccf6cefccfccfccfcccccfccfcfcfcfcfcfcfccecccfccfcfcfccfcfcf8fc8fcfcfcf6cffcf8f
                cfcf8ffff8ff8ffcffffc8fcfcccfcfccccccf6fc8fcf6ff8f8fff8ffcceceeceeeeaeeeaeeeceeeceeceeceececeeeceeeceececeeceeceeceeecceccccefccccfcffcff8f8ff8fcff8ffcff8ffffcfcfceceaeeaeeececeeeeeeccf6f6feceeceeceeeeaeeeccfecececcceccecc7f7fcccfccfccfcfcccccc6cccccfccfccfccfcfcccfcfc8fccfccccccefccfcccfccfccf8cf8cfccfcfcf8fccfcffffff
                ccfffcf8ffcffcff8fcfcccccf6fcffff8f6fccfcfccfcfffffcfffcfcececeeceea4eaeeeeceeceeceeceeceeeeceeeeceeceeeeceeeceeeeeceecfcefcccccfcffcf8fcffcfcff8fcfcff8ffcf8ffffcfccceebeebeeeeecececcccfccccecececececeecbceececcccececfecfeccccc7c7c7cfccccfcfccfccfcfccfccfccfccfccfcccfcfcf8cfcfccfccccccfccfccf8cfccfcfcfcfcfcfcfccfcf8fcf
                c8cf8ffcfff8ff8fff8fcf6f6fcff8fcffcccccfccf6fcfcfcff8f8ffcceececeeeeeb2eebeebeeceeeeeeeeeceeeaecebeeebeceebeebeebecebccecccccfecccccfcfff8ff8fcffcff8fcfcf8ff8f8fffffcceebeeceaeeceecccfcfcfcececeeeebeeccececfccececccfecccccfcccccccccccfcfccccf6cc6ecfcfcfccfccfccccccfccfccfcfccccfcccfefccccfcfcfcfcfcfcfcfcfcfccfcfcfffcff
                cfcffcff8fcffcffcfff8cfccccfcfffcffcf6fcf8fcf8ff8ffffffffceeceeeceea4eebeeaeecbebeaeececeeaeeeebeecbeecebeeceececebececcfccfcccfcfecffcf8fcfff8fcf8ffcff8ffcffcfcf8cffcceecebeececfcfcfcf6fff7ceeeceebececfefcececccececcecef7cfcc7c7c6ecccfccfcfcccfcfccfcccfcccfccfcfcfccccfccfcfcfccecfcccecfcf6fccfccccccccccccccccfffcf8ff8
                ccffcf8ffcfcff8ff8fcfccfcfcfff8fff8ccf6fccfccfcfff8f8fcffcebeeceeceeeaeeaeeeceeeeeeeeeaeeeeeebeecececceccccececeecececcccccceccceccccffcfff8fcfff8fcff8ffcff8ff8fcffccceceeeeeecefeefcffcffcfcebcbebeebecceccecccececceccccccfccefcccc7ccf6ecfcccfcfcccfcccfcccfccccccccccfcfccfccfccccfceccfcccfcfcfccfcfcfceeceeaececcf8ffffcf
                cccffffcfff8fffcffcfccccccfcffff8ffccccfcf6fccfcfcfffff8fce2aeeeeeeae4a4eececfeceaecbeeeaebeaeccefcfecfefeccccecceccccfccfccfccfcfccfcffcfcff8fcffff8ffcff8fcfcfffcfcffcececebeeeeeccfcfcfcffceeeebececcfecceccececfeccfecefeccfcc7c7ccc7ccccccfcccccfcccfcccfcccfcfcfcfcfccccfcccccfcccccfeccfccfcccfcfccccecbebeebebcfffcfcfff
                ccfcf8ff8fcfcf8fcff8fcf6fcff8fcfffcf6fccfcfcfcffff8fcf8ffebb2beeeceeececcecececececefcccefecececfecefceccfefecceccccfeccccecccccfcfcfcf8ff8fcff8fc8fcfcf8fcff8f8f8fcfccecebeeecebeaecfccfcfccecbcbeeccecececcecfececceececc7ccec7ccccc7ccc7cccfccfcfccccc7ccccccccccfccccccfccccfcfcccfefcccfccfccfcfcfccccfccfcfcffcfcfcfff8fcf
                ccffcfcffcfff8fff8ffc8cfc6ffffff8fccf6fccccccf8f8ffff8ffcceeb2eaeeeeeececececeececcccfcfccfcecececececececccfcccfcfcfcccfccfcefcffcffcffcffcfcffcffcff8ffcf8fffcfffcfcfeceeebeeeceeeececccccececefcecececfecfececcececcccfecce6ecccccccccccececccceccfeccfcecccccfcfccfcfcfccfccccccfccccefcccccfcfccfccfcccefffffcffffff8fcfff8
                eccffff8ff8fcffcffcfcfccfcf8fcfcfff6cccfcfcf6fcffcf8fffcfeea2ce2a2aeeeececececeaccfcfccfcfecefeeeceeceeceeeccfcfcfcfccccccccccccfcfcf8ccc8cc8cf8fcff8ffcffcfcf8fcfcfcfcceecececeeececececececcfefeccecfecececececefecfeecec7cecc7cec7fcc7cccccfecfcceccececcceccccccccccccccfccfcfcfccefccccfefccfcfccfccfccfcfcffffcfcfcfff8fff
                cccfc8ffcffff8ff8ff8ccf6ccfccf8fc8cfcf6fccfcfcffcffffcfffceebebbebe2aeeececeeeceeccccfccfcceceeeeeeceeceecececccfcfcfcfccf7fcccfcfcfcfcfccfcfccff8fcfcf8f8ff8ffcff8fccfccceceececeececceccecececcfceceececececececececceccecc7cecccfcccccecececcecefcef7cccec7f7fcfcfcfefcfecefccccccfcccfecccccfecccccfecefcfffcfcfff8ff8fffcfc
                cecfffcff8f8ffcffcffcf6fcf6fccfcfcf6ccfccf6ccfcff8fcff8ffcbeaeeaeebeb2aeeeecececcccfccfccfeceeaeeaeeeeeebecececccfccfccfcfccceccff8fcfc8cfccc8fcffcff8ffcfcffcff8fcfffffcfccceceececfffffffffffffffeeeeeeeeeeeeeececececececececec7cc7fcfccfeceececececcecefccecececefccefecfccefcfeccefeccfefececbeeeececcecfcff8f8fcffcffcff8f
                bccffcf8ffcfcff8ff8fccccccf6f6cc8ccfcc8f6cfcccfcffff8ffcfccecefefeeea4eaeeceeeeeecccfcfcfceeeeeeeeeebeceecebececfcfcf8fcfcfcfccfcfcf8fccf6cfccff8ff8ffcff8fcf8fcfff8fc8ffffccceeceecffcfffcffffffcfcea2ea2eeeeeeecececefececececcfcfcfcfccfceeceeceeceecefe7ceccecfeceecceccecececececcecceccecfeeeeceeeceecbffcffcfff8ffcff8fff
                ccffcfffcfff8fcfcffcf8fcf6ccfcfcfcf6fcccfccf6fff8fcffffffffffcffcfcebeaeeeeeeaeececccccccfecbe4aeebeecebebecccccfcfcfcfccfcccc7fcfcfcfcccfc6cccfcfcfcf8fcff8ffcf8fcfcffcfcfcfceceeaeffffcfff8f8ffffbe4a2eb2a2beaeecececececececececffcfccfceceeceeecececececefeeceececceccecceccceccecececeececececeebeaeaebecffcffc8ffcff8ffcfc
                ffcff8fcf8fcfffff8ffcccccfcf6ccc6f6ccf6fccf6fc8ffff8f8f8fcfcffffffcea4eeeae3e4b3becfecf7fceb4ee4eeeeceeccfceccfccfccfc8fccfccfccfcfcf8cf6ccfcf8ff8ff8ffcfcffcff8fcff8fcf8ffcffeeeeeefcfff8fffffffffeee4b2ee4ee2beeecececececececccfcfffcf6efcceececeeeceececeececececeecefecefecefecececeecceceeceeeeceeeececfcff8fffcff8ffcffff
                8fffcffffcff8f8fcfcf8cf6f6fccfcfccfcccf6f6cfccffcfcfffffff8ff8fcfffcffaeeeeb323e3eecc7ccceeeb4bbeebeebefccfcfcfcfcf8cfcf8fcfceccfcf8fcfccfccccfcffcffcff8fcf8fcfff8ffcfffcffcf3b432bfffffff8f8ffcfceb2aeeb2bebeaeececececececefeccffcf8fccfccecceeececececeececeeceecefececececececeeecececececeeeebefcfcfcfcfcfcfcf8fcffcff8f8f
                ff8fff8f8fcffcff8ffcfccfccccf6ccf6cf6fccfcfccfcff8ffcf8f8fffffff8ffffceceeeeeceeeccecfcccccb4a24a2eebcecfcfcfccfccfcfcfcfcfcccccfcfcfcccf6cf6cfcfcfcff8fff8ffcfcfcfcff8fcf8ffcb4a4b4ffcf8fffffffccee2be2b2ee2a2eeceeeeeeeeeeecececcfcffccfccfccecceceececececeececececeececececfecececeecefeecefeebecefcfcfcfcff8ffcfffcfcfcfffc
                fffcf8fffff8ff8fff8fcf6fcfcfcffcfcfcf6fcfccf6ff8ffffffffff8f8f8ffcf8ffcecaeceececcfcfcffcfeeb4b4eebcecccfccfcfcfcfcfcf8cfccf7cecfcfcf8f6cfccfccf8ff8fcfcfcfcff8f8ff8fcfcfcfcffb44343ffffff8ff8ffceb2ae4a2bebeeebeececeeaeeceeeeeccffcfcf6cfccefeceeeceecefeecececeeceeceeeeceeeeeeeeeeeceeeceeeeeeb2cfcfcfcfcfcfcfcfcc8fcf8fccfc
                f8ffffcf8fffffffcffffffcfcfffcffcff6cfcf8ffffcfffcf8f8fcfcffffff8ffffccceececcecefffffcfffee4b2beeececfccfccfccfc8fc8cfccfcccccfcfcfcfcccccc6fcffcfcff8f8ff8fcfffcffcff8ff8fcfea44b4fcffcfffffcfeeeb2ee4ee2b2beeeeeeea2eeeeeebebeccffcfcfccfcceceeeeeeeeeeeeeceefececeeceeeeeeececeeaeeeeceeeebeb2bbeffcfcfcfccfccf8fcfcfccfcfcf
                8ff8fffffcf8f8fff8fcf8fcfcccffcffcfccccffcfc8ffcffffffff8ffcf8ffff8fffccececececcfcfcfffffceb4a4ecefccefccfccfccfccffcfcfcfcccccfcf8fccfcf6fccfcf8ff8fcffcffcfcf8fcf8fcfcffcffeb4b23fffffcccceeeea2eb2b2e4e4e2eeeee2e2eee2b2eeeeecfcff8fccfcefeeee2a2b2b2beeceeceeceefeeeea4a4aeeebeeeeeeeeee324b42becfcfccfcfccfccfcfccfcfcfc8f
                ffcfcf8f8fffffcf8fccffccccfcfcfccfcfcccfcfcfccf8fc8cc8cffcf8ffccfcfcfcceccececcecfcfffcfcffb4b2beececccccccfcf8fcfcccfcfccfcfccfcfcfcfcc6cfcccf8ffcfcffcf8fcf8fcfcf8fcf8f8ffcfc4b23bffcfffbb4be32434434b43432343234b34b4343b4beecefcfcffccebe4be4b4b2b2be32eeeee2aeee2aeee2eeeeb2b2eb2a4b2b2b4b24b4befcfcfccfcfccfccfcfc8fcc8fcc
                fcfff8ffff8fcffffcfcccfcf6ccc6ccf6cccf6ccc6cccfcffffffc8fcfcfcf8fcf8fcccececceccccfccfffffcebbbbeccccfecfcccfccfccffccfcfccfcfccfccccccfcfccccfcfcf8f8f8fcf8fcf8ff8fcffcffcfcfcb4b43ffffcfb4a432b44b24b232b2b44b4b242b232b24b2eeeccfff8ffcb4d44b22b2bebebeb2b232b2423e4b2bebeb2eeeaeee4e4b2b42b4b2bbeffcfcf8cccccfcfcccfccfcfcfc
                f8fcfcfccfcf8f8cfcccccc6ccfccfccccfccccf6fccccfcfc8cf8fcf8fcf8fcf8fcfcfcfcfcfcfcfcff8ff8ffcceeeecfefeccccccccfccfcc8fc8cfcfcccfccfcfccf6cccf6fcfcfcfcfcfcfcff8ffcfcff8fcfcf8fffcfcceffcfffcfe2ee2b2ea2eee24342b24323444b4432b2bebefcf8fcfbe34b44b2b2b2cfeee44b2b2b4b2324b2be2eaebee2b232b244b42b2b2bcfcfcccfcfcccfccf8fcfcfccfcc
                fcf8fcff8fcfcfcfcf8fcfcfcfcfccfcfccfcfcfccfcfcfcfcffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfffcffcfcfcfcccccccccfcfcfccfcfcfcfcccfcfcfcfccccccfcccccf8fcf8fcf8ff8fcfcf8ff8fcf8ffcfcfcfcffcfcffcffeecebeee2eb2b2b42b4432b44b2324b24b4b2bbcfffcfcfeb4434e42b4cefcfeb24b2442b24b2bb2eaeee2bee2b4b23e42b44b4fffcfcfcfcfccccfcfcfccfccfccfc
                fcfcfcfcfcf8fcf8fccfccfcfcccfcfccfcfccfcfccfcfcf8fcf8fcfcf8fcff8ffcf8ff8fcf8fcfcfcf8ff8fffcfccfcccfccfccfccccccfccfccfccfcfccfccf6fc7cfcccf6fccfcfcff8ffcfcf8fcfcfcfcfcfcf8ffcfcfcfcfff8ffffee2e2a2be2eee2b4432b42324b4b44342b4b4bfcfcffcfc4344b2b4ebecfece2324b2b234b232eeeee4aee2b42b2444b432b2befcffcfcfccceccfcfcfcfcfccfcfc
                f8fcf8f8fcfcf8ffcfccf6cccf6f6ccf6fccf6cccfcccfcfcfcfcfcf8fcff8fcf8fcfcfcf8fcfcf8f8fcffff8ffccfccfccfcccceccfcfcf8fcf8cfcfccfccfccfecceccf6ccccfcfcfcfcfcf8fcff8ff8fcf8ff8ffcccff8fccfcfcfccfeaebeeeebe4eb2b4a44234b4b23232b4bb2baeefcffcfceb434442b2b2fefee4b2b234b2e4b2b4ae4aee2b2b4b44b2b2bebbbbfffcffccfcfceccfcf8cfc8cfcf6fc
                fcffcfcfcf8fcfcfcff8ffff8fcfffcfcfcfcfffcfcfcfcfcff8fcfcffcfcfcfcfcf8fcfcfcfcfcfcfcfcf8ffcf8fcfcffcfcfffcfcfff8fffcfffff8fffffcfceeecccccfcfccccccfcff8fcff8fcfcfcfcffcfcfccccfcffffcccceceeeee2b2b2e2a2e4232434e2e4b2e4e44beffeffcbbbbcceee4eeb2b442b432b2b244b2423e2ebeeeeee4b4b4b24b234b4eefefefcffc8cccccee4efcfcfcfcfccfccc
                fcf8fcfcfcffcfcf8fcfccfcfcfccf8fcfcfcf6fcffcfcfcfcffcfff8ff8fcf8fcfcfcf8fcf8f8fcfcf8fffcff8ff8ff8fcffccffcfcfcffcff8fcfcffcf8ffccbebecfcccccf7cebcfcfcfcfcfcfcccccccfcf8fcfcccff8fcfaececeecea2aeeeb2b4e4a4b4b234eeeeebee32bfefffcebebeefeb2b24232b232b244324b24b2b4eae2eb2beeee34b3b43b4bebecffcfff8fffccfcc44eeefcfccfcfff8fff
                8fcfff8ffff8ffffffffff8fcfcffcfcf8fcfcfcffcfffffff8fff8fffff8fcfcf8fcfcfcfcfcfcf8fcfcf8f8ffcffcfcff8ff8fcf8ffff8fffffffff8fffcfcececcecfcf6fccebecfcccfcff8fcfcccccfcfcffcfccc8fcffccceceeceeebee2a4b2b432432432b2a2a2eeeb4befffffcbcbcfeeeb2b2b2b4b244b2b24b232432b2bebeeaeb2aeefeffffff2beebeffcffffcfcfcefc4444ecf8fcff8fffff
                cff8cffcf8fff8f8f8f8ffff8ff8fcfcfcfcf8ff8fff8f8f8fff8fff8f8ffcf8fcff8fcf8ffcff8fcffcf8fffcff8ff8fcfcfcfcfcfcf8ffcf8fcf8fcffcccccececcfffcffcffffcfcccccfcfcffcfcccccf8fcffccccfffcffcececeaeeaeeaee3234a4b4b43e34eeeeebe2b3effcfcfffffffffe4e2b2b42432b2324b24b4b2b4ee2a2be2ebebeffffcfefeb3ebecfcf8f8fcfc444ff744eeefcf8ffff8ff
                8fcff8f8fff8fffffffff8fcfcfcf8fcfcfcfcfcff8fffffff8fff8fffffcfcfcfcfcf8fcf8fcfcffc8fcffcff8ffcffcf8f8f8f8ff8fcfcfcfcfcfcfcffcccecccecfcffcffcfcfcfcecccfcfcfcfcccccfcfcfcf8fffcfcfcfcceceeeceeeeeeeeeeee2ee2ee2eeebebeeaee2eeeeeeccfffcffebe32e4234e44444b243242324b2aebeebeaeeecffcfffffbebbecfcffffff8c44445efe444eefcffcfffcf
                fcfcfcfcf8ffff8ff8fcfff8fcf8fcfcf8fcfcfcffff8ff8fffffffff8ff8f8fcf8fcfcffcfcf8fcfcfcff8f8ffcf8fcffcffcfffcfcff8ff8ff8f8ff8fcccecfefffcfcffcffcffcfccceccfccccccccecccfccfcfcccfcfcfcceaeccececcecececeeeceeee2ceea2eeeee2beb32bbbbffcffffce2ee4a42b4a4a2b232b4beeeeaeeeeeeeeeebecfffffcffccefeefcf8f8ffe44474447fc444ecf6ff8fff8
                fcf8fcffcfff8ffffffff8ffcfcfcfcfcfcf8f8fcf8ffffff8f8f8f8fffffcfcfcfcf8fcf8fcfcf8fcf8fcfffcff8fff8ff8ffcf8fcfcfcfcfcfcffcfcffcccecffcfff8fcfcffcffcfcccccccccccececceccccccccccccccccececeeaeceecececeaeeeea2aee2b2ebea2beea2bb2be3efffcfffbb2b24b4b2434434e4b23eeeeeeeecececececefcf8ffffcfce444fcfffce444eeee444ff7effffffff8ff
                f8ffcf8fcff8fff8f8f8fffcf8fcfcf8fcfcfcfcffff8f8fffffffffff8f8fcf8f8fcfcfcfcf8fcfcfcfcff8ff8ffcfcffcff8ffffff8ff8ff8ff8fcffcfcececfcff8ffffcfcf8fcffccecececececcceccecececeecececececcececececcececeeecec2eeebeaeeeeeebea2beeeeeeefcfcfcceeeeeeeee2beeeeeeeeeeeeeeeececeecececefcfffff8ffcfcfcecff8fc444ee4e2e4444efff8ff8f8fff8
                fcfcfcfcfffff8fffffff8ffcfcf8fcfcfcfcfcfcf8fffff8ff8ff8ff8fffcfcfcfcf8fcf8fcfcfcf8fcf8ffcffcff8ff8fffff8f8fffcfcfcfcfcf8fcfcccefcffcffcc8fcfcfcfcfcfcfccccccfcceccecececececececececececcecececececececeaecaeeeeecea2beeeeeeecfececeecefefececcececeecececececececcfeefececefececffcfffffcccccfcfcfe44e4eee4ee4447ffcffffffff8ff
                fcf8ff8fcf8ffff8ff8ffff8f8fcfcfcfcf8fcf8fffff8fff8fffffffff8fcf8fcf8fcf8fcfcfcf8fcf8ffcff8ff8fff8ff8f8fffff8ff8f8f8f8fcfcfcfcfececffcffcfccccccccccccccefecececfecfececececceccecceccecececcecececececeeceeeeceaeeaeeeaeeeecfeefefefcfefecfefefeecececeeceeececefeeececefefeecefcfff8ff8fcffcfcffce44e4ee4e2e444efffff8f8f8fffff
                8fcfcfcf8fff8ffff8ff8fffffffffffcffffffff8ff8ff8fff8f8f8f8fffffffffffffcff8f8fcfcfcfcff8ffcfff8fffffffff8fff8fcffcffcff8f8ffcccecfcff8fc6cf6fcfcfc8fccfccceccecececcececaececececececececececececececeaeececeaeeceeeaeeeaecefecefcefeefecfecefefecececfeefecfeefecefefecececefeccfffffcffcccfcfcce44e4ee2eee444fcf8f8fffffff8ff8
                ffcfcf8fff8fff8fffffff8f8f8f8f8fff8f8f8ffffffffff8fffffffff8f8f8f8f8f8ff8cfcffcfcfcff8ffcff8fcffcf8ff8ffff8fffcf8fcfcfcfcfcfceccfcfcffffffcfccccfffffffceccecceccececcecececececececececececececececeececeaeeeceeceeeeeeecfecfefcefcfcefecefececcececeececeeefeecefececefecfececffcf8ffffcfccfce4444ee2ee4e444fcfffffff8ff8fffff
                cf8ffcfcfcffffff8f8f8fffffffffff8fffffff8f8f8f8fffff8ff8fffffffffffffffcffcfcf8f8ff8fcff8ffcff8fffff8ff8ffff8f8fcf8f8f8fffcfcfcecfcff8f8fffcccccfcfcfcfccececececcececccececeaececececececececececeeaeceaeecceeceaeceaecceffcfccfccecfccfcfcfcfececeefefefefececefeecefeeceecefecfffff8ffcfcfce4444ee4e4e244efcfcfcf8fffffff8f8f
                fcfcf8fcfff8f8ffffffff8ff8ff8f8fff8ff8ffffffffff8f8fffff8f8ff8ff8ff8ff8fcf8f8fcfcfcfcf8ffcff8fff8f8fffff8f8fffcffcffcffc8ffcfcfcfccfffffcf8fccfcff8ffffcceccececeaecfffffccecececeaeceaeaeeaeeceaeceeceeeceeaeceeececececcffffffffffffffffffffffcecececeecececfececefececfecfecccff8ffff8fc8cfc447e4eeee444fcfcf8e4fff8f8f8fffff
                8ff8ffcf8fffff8f8ff8ffff8fffffff8fffff8f8ff8ff8fffff8f8fffff8fffff8ffff8fcffcffcf8f8fffcff8fff8fffff8f8fffffcf8fcfcf8fcffcfccccccfcf8fcfffffcccccfff8ffcccececcececccfcfffcaeceaecececeeeceeceaeeeceaecaeeaeeecaeceaeceaecfcfcfcfffcffcfcfcfcffccececefecfecfeecefececefeeceecefcffff8fffffe44fce44e2e444efcfcfce447effffffff8ff
                f8ffcf8ffcf8ffffff8ff8ffff8f8fffff8f8fffffff8fff8fffffff8ff8ff8f8fff8fffff8fff8ffffff8fff8ff8fff8f8ffffff8fff8fcf8fcfcfcf8fffcffcfcffff8f8fcfccff8ffffcfececececcfcffffcfccececeeceeaececececeecececeeeeceecceeeccffcfcfffffffff8f8ff8fffffff8ffcfefefcfecfeefcfefcfefccfcffcfefcff8fff8f8ee444cf7444444efcf6fcce74eef8ff8f8fff8
                fcfcfcfcffff8f8f8fffff8f8fffff8f8ffffff8f8ffff8fff8f8f8ffffffffffffff8ff8fff8ffff8fffff8ffffff8ffffff8f8fff8ffcfcff8ff8fcfcf8fffffff8fffffff8ff8fffcfffcccfecefeccffcfffffccececceceececeaececcecececcceccececccecfcffffcf8f8f8ffffffff8f8f8ffffccfefcefcfefcfefcefefcfecfeefefcfffff8fffff2e445efe4444cfcfcfcfffe4ffffffffff8ff
                fcf8ff8fcf8fffffff8f8fffff8ff8fffff8f8fffff8ffff8fffffff8f8f8ff8f8f8fff8ffffff8ffff8f8fff8f8ffffcf8ffffff8fffcf8fcfcfcfcf8ffffcf8f8fff8f8f8ffffffcff8ffcfecefeccfcfff8f8ffcfefcfefececeaeeececfefcfcefecefecfecefcfff8ffffffffff8f8f8ffffffff8ffcfeccfcefecfecfefcefcefefefccfeccfcffff8ffee4ee444ff74ffcf6ff8fccfcff8f8f8fffff8
                ffffffffffff8ff8fffffff8ffff8fff8ffffff8ff8ff8ffff8ff8fffffffffffffff8fff8f8ffff8ffffff8fffff8ffffff8ff8fff8f8ffcf8f8fcfcfcf8fffffff8ffffffff8ff8fffffcfccfecfefecfcfffffcfccefecececeeeccececffcfefcfcfcfcfefcfcffcfff8f8f8f8fffffff8f8f8f8fffcfcfcfefcfcfefcefcfcefcfecfefecffcff8f8fffce4e2e4e44cfff8fcfcfcfcffff8ffffff8f8ff
                f8f8f8f8f8fffffff8ff8ffff8ffff8fff8ff8fffffffff8ffff8ff8f8ff8f8f8ff8fffffffff8fff8f8f8ffff8fff8f8f8fff8fffffffcf8ffcff8ff8ffff8f8fffff8ff8f8ffffff8f8ffccecfeeccfcfff8f8ffccfecfefececcececececefefefefefefecfefeffff8ffffffff8f8f8ffffffffff8ffccfecfefecfcefccefefcefcfecfcfecfffffffcfe2e4e4e4e4ff8ffcfcf8fcfcf8ffff8f8fffff8
                fffffffffff8f8f8fff8ff8fff8f8fff8fff8fff8f8f8fff8f8ffffffff8ffffff8fff8f8f8fff8fffffffff8fff8fffffff8fff8f8f8fcffcfcfcfcfcf8ffffff8f8ffffffff8f8fffffffcfcfecfefecfcffffffcfefececfefecfecfefefcfecfcecfecfefecfccfcfff8f8f8fffffff8f8f8f8f8ffffcfefecfcfecfcfefcfcefcfecfcefefccff8ff8fee4e2eeefeffcffcf8fcfcf8fffff8fffff8f8ff
                ff8ff8ff8ffffffff8fffff8ffffff8fff8fff8ffffff8ffffff8f8f8ffff8ff8fff8fffffff8fff8f8ff8ffff8fff8ff8ffff8ffffffcf8fcf8f8ff8fcff8f8ffffff8f8f8ffffff8f8fcfcceefececfcfff8f8ffccecfefecfecfefeecfcfecfecfefefecfcfecffff8ffffffff8f8f8fffffffffff8ffccfcfcefcfefecfcfefcfecfcfefccfcfffff8ffee2eeffffffcfff8fcff8fcfcf8ffff8ffffffff
                8fffffffff8f8f8ffff8f8fff8f8ffff8fff8fff8f8ffff8f8ffffffff8ffff8ffffff8ff8ffff8fffff8ff8ffff8fff8ff8ffff8ff8ffcfcfcfffcfcff8fffff8f8ffffffff8f8ffffffffcffcefefcefcffffffcfcfefcefecfeecefcfeefefefefcfccfefecfecfcfff8ff8ff8ffffff8ff8ff8ffff8ffcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcfcf8fffffffffffcfcfff8ffff8ffffcffff8ffff8f8ff8f
                ff8f8f8f8fffffff8ffffff8fffff8ffff8fff8fffff8ffffff8f8ff8fff8ffff8f8fff8fff8ffff8f8fffff8f8fff8fffff8f8fff8ff8fffff8ff8fff8ff8f8fffff8f8f8fffff8f8f8f8fcccfefcfefcff8f8fffcfcfefcfcfefcfcfeefcfcefcfecefefcefcfcfcff8fff8fffff8ff8fffff8fff8ffffcffffffffffffffffffffffffffffffffffff8f8fcfcf8ffff8ffff8fffcf8ff8f8ff8f8ffff8fff
                8fffffffff8ff8fff8f8f8fff8f8fff8ffff8fff8ff8ff8f8ffffff8ff8ff8f8ffff8ffff8ff8f8fffff8f8fffff8fff8f8fffff8ffffff8f8fff8ff8ffffffff8f8ffffff8f8fffffffffffcfefcefccfcffff8ffccfecfecfecfefefcfefefcfecffefcefcfefefcffff8fff8f8ffffff8f8fff8ff8f8fff8fcfcfcf8fcf8fcf8fcf8fcf8fcf8f8f8ffffffffffff8fff8f8fff8fffffffffffffff8ffff8f
                ff8f8f8f8fff8ff8fffffff8fffff8fff8ffffffff8fffffff8f8ffffffffffff8ffff8fffffffff8f8fffff8f8fff8fffff8f8fff8f8ffffff8ffffff8f8ff8fffff8f8fffff8f8f8f8ffcfcfcefcefcffcf8fffcfcefcefecfefcefefccfcefefcecfefcfecfecfcff8fff8fffff8f8ffffff8ffffffff8fffff8fffff8ffffffffffffffffffffff8f8f8f8f8f8fff8fffff8fff8f8f8f8f8f8f8fff8ffff
                8fffffffff8ffffff8f8f8fff8fffff8fff8f8f8ffff8f8f8ffff8f8f8f8f8f8fff8fff8f8f8f8ffffff8f8fffff8fff8f8fffff8fffff8f8ffff8f8fffffcfff8fcfffff8f8fffffffff8fcfcfefcfcfcfffff8ffcfcfefcfefccfccfefecfecfcfcfecfecfecfcfcffff8ffff8fffff8f8f8fff8f8f8ffff8f8fff8f8fff8f8f8f8f8f8f8f8f8f8ffffffffffffff8fff8fffff8fffffffffffffff8ff8f8f
                ff8ff8ff8fff8f8ffffffff8fff8f8fff8ffffff8f8fffffff8ffffffffffffff8fff8ffffffff8f8f8fffff8f8fff8fffff8ff8fff8fffff8f8fffff8f8ff8fffff8f8ffffff8ff8f8ffffccfccfecfefcf8fffffccfefccfccfecfecccfecfccefecfcfcfcfcfccff8ffff8ffff8f8fffffff8fffffff8ffffff8fffff8ffffffffffffffffffff8f8f8f8f8f8f8fff8fff8f8fff8ff8f8ff8ff8fffffffff
                8fffff8fff8fffff8f8ff8fff8fffff8fff8f8ffffff8ff8fff8f8ff8f8f8f8ffff8fff8f8f8ffffffff8f8fffff8fff8ff8fffff8ffcf8ffffff8f8fffffff8f8fffff8f8f8fff8ffff8fffcfcfcfcfcffff8f8ffcfcfcfcfcfcffcfffcffcfffcffcfcfcfcfcfffcfff8ffff8ffffff8ff8ffff8ff8fff8f8f8fff8f8fff8f8f8f8f8f8f8f8f8ffffffffffffffff8fff8fffff8fff8ffff8ffff8f8f8f8ff
                ff8f8fff8ffff8fffff8fff8fff8f8fff8fffff8f8ffff8ff8fffff8ffffffff8ffff8ffffff8f8f8f8fffff8ff8fffff8fff8f8ffff8ff8f8f8fffff8f8f8ffff8f8ffffffff8fffcfff8ffffffffffff8fffff8fffffcffffffcffcfffcffcfffcffffffcfffcfff8fff8f8ff8f8f8fff8ff8fff8fff8fffffff8fffff8ffffffffffffffffff8f8f8f8f8ff8ff8fff8fff8f8fff8ffff8fff8ffffffffff8
                """))
        if player1.y <= 2000:
            if tiles.tile_at_location_equals(tiles.get_tile_location(player1.tilemap_location().column, 64),
                assets.tile("""
                    myTile15
                    """)) or tiles.tile_at_location_equals(tiles.get_tile_location(player1.tilemap_location().column, 64),
                assets.tile("""
                    myTile1
                    """)):
                scene.set_background_image(img("""
                    666a666666a66666a66666a66666a6666a66666a6666a6666a6666a6666a6666b666a666b6666a666b666b66966b669666b6696a6696a6966b66966b66966b6966b6966b6966b6966b6966b696b696b6966b6966b6966b696b6966b6966b6966b696b696b696b6966b6966b66966b66966b6696a6696a66966b666b666b666b666b6666a66666a66666a6666a6666666a66666a66666a6666666a66666a6666a
                    6a666a6a6a66a6a666a6a666a6a696a6966a9a669a6966a9669a6966a9669a6a66a966b66a9a696a989a669a6a669a6a9a69a6696a6696a6a96a6a96a98a96a6a96a6a96a6a96a6a96a6a96a6a698b66a9a698b69a6a96a6a698b69a6a96a6a96a666a6a66a66a6a96a6a96a98a96a98a96a6a696a6696a6a66a9a66b66a966a98989a696a9a696a9a696a9669a6a9a669a6a666a6a666a6a6a666a6a666a666
                    666a666666666698966696a966986a66a66666a666a6a66a6a66a6a96a6a66966966a66a96666a6666669a6669a66666666a66a696a98969666966a69696a696669696a696669696a9696a96969a69a96669a69a6696a69696a96a6696a9696a969a96969a969696a6966696a96696a966a9696a69a6a6969a96669a69a66a666a6a666a66666a66666a666a68966666a66696a96696a6966698966669a66a6a
                    6a669a6a9a6a98a6a6a6a666a6a666666a6a6669a666696666696666666698a6a6a696966a6a969a9a9a666a6669a9d9a966969a66989a6a6a9a69698a6966a9a6a6a696a9a6a6a966a6966a6a6698989a669a669a696989a666969a6966a6966a666a6a666a6a696989a98966a6a666a9666a69666966a6666a6a666669669a69669a669a6a696a6a666a66986a6a6666a6a666a68666a6a6a6a6a6a6666669
                    666a666666666666666666a66666a9a69669a6a666a98a6a9a6a6a6a6a98a9669666a6a669666a6666666a969a69d1dd19b6a666b6a989669666a6a696a6b966969696a966969666a966a969696a96a9669a669a696a6a98969a6a696a696a6a969a96969a96969a6a966a989a96969a669a966a69a6a969a696969a6b6a6a666a6a669866966a66969a696a6a96669a696666a6669a66666666666666a6a6a6
                    a6666a6a66a6a6a9a6a9a666a69a666a6a666666a966696666669669666966a66a96666a6a69a696a9a6966a69d1d9111d696b9a6966a6b6a9a96969a96986a989a6a966a989a9a9669a96a6a9698966a9a69a696a696969a6a9696a969a69696a696a69a696a98966a9696a966a6a696a666a96989698989a6a6a6696a6966b696698a9a6a666986a666a669689a666a6a66966a666a9a6a69a6a6a98966666
                    66a666666a669666666666a966a6666666a6a9a666a6a6a6a9a6a6a6a9a6a696a66a9a9696a666a66669a696b91d11d969a6b6669a6969a96666a9a666a9696a966966a9669a6696a966696966a9a69a9696696a969a6a669696a96989896a98969a696a966a96a9a966a696a699919a696b966a6b6a69a66696696a6696a696a6a6a9666966b6a966696698a66a66a66669a89896a6666698666696898a6a6a
                    669a6a9a6698a6a6a6a6a966a666a9a6b6966669a669669666696696666696a69696666a66969696b9a66a66111191119a696a9a669a6666a9a96669a966a96989a6b9669a6969a696a9a6a9a9669a696a69a6966a96969a9a696a6a9a96969a9a696a9669a9696696a969a6119bdd919b66a9696969a669a6a96a696a6698a69696666a66a96666a9a6a6a966966966a98666a6a669a6a66a6a98a66a666966
                    6a6666666a666669669666a669a666666a6a69a6698a6a66a986a66a96a98966a6a6a9696a6a6a6a666969a9d1911d1d191a96696a69a9a96696a9a696a96a9a969a669a696a9896a969696696b9696a969a96a9966a9a9669a6969696a9a6a9696a9669a696a69a999b6a999d11911d11996a6a6a6696a69698966a969a6966a66a9a969a66a9a666669666a6a6a6a966a9a69669866698966666698966a66a
                    666a6a6a669a69a6a66a66698669a6b696698666a696969a669a9696a666a6a9696966a66969696969a6a661911d19119d999a9a969669669a6969698969a966a9696b69a969a96969a6b6b9a69a6a969a69696a6b96966a969a9a9a69669696a69669a969a999a6939d199dd9d1d91916bb9696969a6969a6a989a66a669a6969a6666a66966669a9a6a6a966966666a66666a6a6a9a66a6a6a9a6a66a666a6
                    9a6966966a666a6666a69a6a69a6666a6a66b6a966a6a6669a666a6696b69666a66a696a9a6a6a6a6a9999d11d1111d119d9b9966b6a9a9a69a6a96a9a966696989a96b69a696a9a96969a969a69696a969a6a9969a6a996a9669669a9a9a9a969a9a96a9691d19911d191d11191d1d1d996a9a6a969a6a69669a696969a669a66969a696a6a9a69669669666a6a9a6966b6a96669666a69669686666a69a666
                    666a66a66989a666a96666698666a969669a6966a96696a9896a969a6a96a9a969a96a9666969696966b19d191d91d191d99b9a969a9666969696a9696a9a9a9a966a96b69a69696a9a696a9696a9a969a69969a96996a969a9a69a966969669a9696a969a191d1d9d91d1919d191919d9d999699a989696a9a696a9a6696a669a6a696a6969696a9a69a66a966666a6a98966a6a66a6986a6a69a69a66666b6
                    a666a669a66a669a66a9a6a69a696a6a6a666a6966a9896a66966a6696669896a666966a9a6a96a96a96d9d111111911d9b9a696a9669a9a6a9a969a696966966b9a969a969a9a69669a9696a969696b696a9a69a6a969a96969a969a9a9a9a966a9696b619d9b9b9d191d1d1d1d9dd9dd1dd9d9b969a9a96696a96669a6969a66966a696a66a69669a66a966a96a96666a6a696698966a9666666a6669a66a6
                    69a696a666a698669666696a66a66966969a966a696a6a696a6a969a6a9a698969a98b966969896a966b6b91d91d11d1116a96a9669a966996966969a9a69a9a96696b696a96969a9a969a9a96b9a9a96b969696996b969a9a9696a969669696b969a9a999d6b696a96b99b99d9d9d919d99d9dd9b9b6666b6a966a9a69a6a696a6b9698969a96a6b669666a966a669a969696a6a698a966a69a6966a666a696
                    a666a666a9666b6a6a9a6a696969a6a6a6666a96a696969896966a6969669a6a966696a9a69a9a9669b969d111d9191196969696b9a96b9a6b6b9a69669a96969a9a969a969a9a96969a96969a9696969a96b9a9a69a6b6969a9a969a9a9a9a96b9a9696a9b969a969a96a96a969a9b9a9b9dd99d999a9a96966b9696966969a999a69a989898969a69a9a966a969866a6a66a6966a966a666a66a669a669866
                    66a9669a66a96a969666966a6a66696969a969896a6a6a69a6a9696a6a9a696989a9a69669a66669a99a9a11911111d91d9a9a69a969a96969a969a9a9696a9a96969a969a96969a9a969a9a969a9a9a969a96969a9969a9a96996b969696969a96969a9696a9a96b96a969a96a96966969a96d9d9b99969a9b96a989a9a6b666a696a66b6b69a669a96d989666a69a96696a966a966a6696966989a666a69a6
                    a966a666966a666a66a6a96969a9a6a6a66a6a969696969a696a6a9696696a69a69669a69b969b9a9696911d1d191d11dd1199b969a9619a9696a96969a969696a9a969a969a9a96969a96969a9696969a996b6b969a969699ddd19a9a9a9a9696b6b969a9a96969a96969a96996b6b9a9696a9a9b9a6b9a969a9669a66969a9696a96969a6989a661919d9a9a9698989a66666966a6966a6a6a6a666a96a666
                    98989a9a6a969a969a9666a6a66669696969698a6a69a6696a969699a116a96696a9a696d9a99a966ba9d1911911d1911191d119a969d911b6a996b6b96b9a9a99696b969a96969a9a969a9a969a9a9a969b99b9a969a9a9a19191d1996969a9a99a96a96969a9a969a9a969a9a99a969a9a969696a996a69a696a9a969a966b9a996a9a696a9669d9ddd196666a69a669a9a9a6a696a6966969696a966666a6
                    a6a96666966a666a6669a96969a9a6a6a6a9a69969a69a9a696a96a9111119a9a96969a99b9d9699a96d111d111d111d91d9d9d9d99d9dd9119b69a96b96b9696a9a96b9a969a9696969b96969a9696969d939199a969696191d1d91d19b9b9696969b9b9a996969a96969a9696a969a96969a9a9696a996969a96966b6989a99d6d96696a966a99dd19d9b9a9696a69a666666966a698a9a6a6a6666a6a9696
                    9666a69a6a69696969a666a6a66696969696698a969669896a96696a919191199939d119b969b939999d191191d19191191d19d19dd9d91111119b99a969a96b9969b9a969a99b9a9b9a969a9b969a9b9bdd1dd9d9b9a9b99d191d191dd999a9b9a9a96969a9a9b9969a9b969a9969a969a96969a9a969a9a9696a9a969a9696d9a96b9a9669a9b9d9d19166989a6966969a9a6a9696a966669669a96696a6a6
                    a69a96a6966a6a6a6a69a96969a96a69a6a9a696a989a96a969a9a9696d1d1d11d1d191d11dd9d9b9b11d1d9d1911111dd9919d119d9d9dd19d1119b96b969a96a9696969b969a9969a969a9969a9969a919d9d9d969b96bd1d191d1919d9a969a9969a9a969969a9a9969a9b969a969a969a9a96969a9669a9a96969a96b9b9d99b966669a96919d19dd9a9a9896a9a6a6669666a66989a9a6a666a6a669666
                    96a66696a6969696969669a6966a969a69669a9696a96a969a69666a9a96d19d11911d11911dd16d9b91191d9d91d1d191d1d9d919d9b9a9699b9d969a9a969b99a9a9b9a969a969a9969b9b9a99b9a999d9d9dd9a9a9699a9191d91dd9d99b9696b9b999b9a9a9699a9a9969a969b969b9a96969a96969a96696a9a9669a9d9a9b6a9a99d69dd91d9d919966d9b96696969a69a969a698989696a96969a6a98
                    a969a6a696a989a6a989a696a9696a6969a9669a696a969a9696a996969a99d91d11911d1d19119d911d1d9119d9199119d91d9dd9d99a969a969a9a9969b9a9699b969a99a9969b969b9a9699a9699b9b99b199b9699a9b99d1d1d1919d9b99a99a99a69a99699a969969a969b9a9a9a96969a9a96b9a969a9a96969a96969a9696969a99a191d9dd1d9361d91d919a6a9896a69a696a966a66a96a6a666669
                    66a69696a966a96966b696a96a9a969a696a9a69a96969a969a969a9a6966a91d1911d1911911d1dd1d1911d919d9d9a99d19d91d99a969b969a9969b9a9969b9a969a99699b9b99a9b9b99a9b969a9dd91d9d9a99a999b961919191d9d9d9d99b99a999b969b9a99b9a9b99a969969969a9b969969a969a96969a9a969a9a969a96a969a99d9d919d9d91d9dd9ddd9d969a6969896a6989a9696669669a9a6a
                    9696a6a966a966a69a96a96696669a69a696969699b9a969a696a9669a9a9969911d191119d191d1191119111d9d9d9d9b9b19d9b9b969a96b99a9b96996b9a969b9b9b9b9a969a99b969a9969b9b911d1d1dd99b99dd9ddd1d1d1d1d9dd19dd99a996b969b9a9969a99b9699b9a9b9a99969a9a9a996b969a9b96969a96969a69699b996d9d1dddd91dd9dd91d919d99a696a96a9696a9666a6a9a66a666966
                    a6a969669a969a96a9696a9a9a9a696969a9a6a9d1d99b9696a969a969696a9a69d1111d19d9d9911d99d1d9119dd99b9999a969a969a99699b96969a9a99a99b969a969a99b9b969a9b9969b9a99dd919191d119dd91d9191919d1919d9d19dd99b99a9b9a9969b99b969a9a9969a996a9a9969b96b99a9b969a96b969a9a969a9a9da99dd9d9191d919191d9d19ddd996a96a966a6966a96969669a969a6a9
                    6966a9a9669a696969a6969669696b6a96969999d1ddd9da999a969a9a9a9699a99d91d19d9d9dd999dd91d1d1d99b99a9a969a996b99b9bdd91ddd9969b99699a9999a99699a99a9999a9b9b999b11d1d1d919dd91d1d1d1d1d191d9d91d19d9d9b9b99b9969b9a9a96b99b96b9b96999b96b9b969a96969a96969a9a96969a9696999dd91d919d9dd9ddd9d9d9d99d9d969696a969a696a9a6a9a666a69666
                    a9a966989a696a9a989a9a69a9a9a9969a9a6a9d1d191119d169a969696969a969a9d1919d9d9a99ba99b999d9d9d9a969b9b996b99a969d911d191dd9b969a9b9b6b99b9b9a9699b9a99b999a9d1919191d1dd91d19191919d191d19d1d9d9d9d9999a99a9b9b9999b99a99a99a99bbb969b9a969d9b9a9b969a9b96969a9696b6ba9a91d9d1ddd191d9191d9dd9dd9d9db6a9696a969a966969669a96989a9
                    66969a69a96a9696a96969a9696966a9a9696961d9111d1119d969a9a9a9a969a96969b9d9d999b96969a9b999b9a969b96969a99a969a111d191d1919b9a99b9699b9a99a999b9b9b9699a99d91d1d1d191919d9d91dd1d1d191d9d9d911d9d9dd9399b999b99a9b99a99b99d99b9996b9a999b9391999b96b99a969a9a96b9a99969619d19d99d9d91d9d9dd919d9d9d99a96a6966a6669a6a69a6696a9666
                    9a6a69a966969a6969a9a969a9a69b9696a9a9a9111d191919da9696969696b969a9a99a9b9a9a969a9b969a9a969b9a99a9b99a99b999d91d11d91dd99b9b99a9b9a99699b9b9b9969b9b9d9d1d91919d1d19d9d9d91919d91d1d19d9dd91d9d9d9d9d9b9a9b99b9a99b99a99d99b9a99b9b969b91ddd99b99a969a969969a969a69a9d9d9dd1d91d9d9d1d919dd9d9d9b96699a9a9969a969698969a6989a9
                    a96969669a9a969a969696a96969a96b6996969d11911111dd999a9a9b9a99a9a9969a96996969b9a9969a9699b9b969b999a99d996b9d1119191119d9b999a999b99b9b9b99699a9b9b99d9d1911d1d1919dd9d9d9d1dd11d19191d19d91d9d9d9d9d9d99999a9999b99b99b9a9d9b9b99b9a9b19d9193d1d99b9969b9a9b969a99b9191dd9199d9d9dd9d9d9d9d9d9d9a69a696696a9a96a9a96a9669a6966
                    69a9a69a96969a96a9a9a969a9a969a99a9a9a99d11d19d191d9b99696969a96969a9969a9a9b969969a999b9a969a996b699b9ddd19b19d11d1d1d19d9b9a99b99a999a99a9b9b999b9b9d1d1d19191d1d191d1d19d9191919d1dd91d1d9119d9d9d9d9b9a9b9b9a99a99d9a999a9999b1999b91d1dd9d9d91d9b9a969969a9696a99dd9d91ddd9d9d9dd9d9dd9d9d9d999a96a9a9696669669896a9a696a6b
                    966969a96a9a96969696969a9696b969a96996d99d191111d1119d9d9a9a9699b9b969b99b969a9b9a99b9a9699a99b99b9a9911911d1d11d191191d99b9b969b9a99a99b999b99b9a999d1d9191d1d919ddd19191d1d1dd1d1d911d919d19dd9dd9dd9d999b999b9b99b9a999b99b9a99b1dd919d919d191d9d99b99a9bd969a999d9d91d9d99dd9b99d9d9d9d9d9d9d93999d9696a9a9a9a96b969696a969a
                    6b9a9a969696a9a9a9a9a9a969a969a969a9b9dd1d111d911919d9d9d999b9a969a9b9a969a99969b9b9699b9b99b96b99b99d1d11d19119111d119d199a999b999b99b99b9b9b9b99b9a91d1d19191d1d9b91dd1919d919191d19d1d1d9dd91d9d9d9d9db99a9b999a9999b19b9d99b9b999d1dd19dd9d19d9d9b9699b99d9d9b9d9d1d9d9ddd91d9a969b99d9dd9d9d9d9dd9d9a969699999a96a9a6966a96
                    9a69696a9a99696969696969a969a969a9699d91191d911d1d19d9d9d9b9699a9b96969b9b96b9a9969a9b969a969b9939dd1d1191911d1d919191d9d9b99b9b9a99b99b99a999a99b999d19191dd1d91d9bd9d91dd11d1dd191d1919d119d919d9d919d9d9b999b9b99b9b9b99b9dd999b9b19d9d19d19dd9d9d9a9a969a9d9d99b9d9d9d9999d99b96b9a9a969a9b9d9b9d9d9d99d9d9b9b96a9669a69a96a
                    969a9a9696a9a9a9a9a9a9b969a9969a99a9a91d1111111911d9dd9d9d9b9a99699a99a99699b99b9a9996b9b99b99a911191d91111d19191dd119d9d99b9b99b99b9b99a999a999b9db9d1d1d191911d9bdbd91d19d919191d91d19d99d9d9dd9d9d9d9d9d9b9b999b9d9999a99dd1dd9d9d91d19d19d9d9d9d99969b9a99d9d9b9d9d99b9b9a9a969b969696a9696b9a9d9b9d9d9d9d9dd9a969a969a96696
                    9a96969a996969696996969a9696b9a969999111d91d1911d1919d9dd9d99b969a99b996b9a99a9699b9a99b9b99a99d9d911911d91191d19d99dd9d9d99b9a99b999a999b9b99b9999b91919191d1d9ddb9dbb91911d1d1d91d19d1d19d9dd9d919d9dd9d9d999b9a99b1ddd9b999d91dd9dd91919d91d9d9d9db9b99a999d99b999b9a99a9b9699a96b9a9a9969a96969a969a9b9b9d9b9696b696a969a9a6
                    969a9a969a9a9a9b9a9a9b969b9b9699b9a1d1d9111911d1911d9d9d9d9d99b9b9b96b99b99a99b9a9999b9969a99b9d9d91dd9d11d1191d191d9d91d939999b99a999b9b999b99bdb9d1d1d1d1d91d19b9b9b9bb1d919191d191d1919d9d9d9d9d9dd9d9d9ddd9b99b99b919d9ddd91d9d191dddd1dd91d9d9d999a9699b9a9a9b9a969b96969a969a9696996b9a99a9a996b9696a96a96a9a969a969a69696
                    b9696969a9699696969969a9b9a969a9696919111d11d1111191d919d9d9399b9969b9a99a99699b9b9a99a9b99b999d9d9d9d9d9119119d19d9d9d9d99b9a99b99b9b999b9d1dd999b191919191d19dbddb9db9c6d1d1dd191d9d91dd9d9d919d9d9d9d9d9d99d9b99b99ddd9d9d1d91d9d191919d91d9d9d9ddd999b9a9699969a99b969a9a996b9969a9a9a969696996a99a9a996969a9696b969a9696a9a
                    9a9a9a9b969a9b9a9b9a9b969699a999a9b9d1d191191191d1d9d9dd9d9d9d99a9b9b99b9969b9a99969b9999b99a9d9d9dd9d911d11d1d1919d19d9ddd999b99b99b9b9b9dd919d9391d1d1dd1d911d9b9db9db8c89d9191dd19dd9d9d9d9d9d9dd9d919d9d9d9d9d9d9b9911d19d91d91ddd9dd91d91d19dd99ddd9b9969b9a99969a9a996969b96b9a9969969a9a9a9969a9696b9a9a969a96a9696b69696
                    969696969a9969a99a96969a9b9a9b99999b19111d11d1d1919d911d9d9d9d9d99a99a969a99b99b9a999a9a99dd99d9dd919d9d19191d11d11d91d9d99db99b99a999b99dd11d1d1d11919d9191dd9bdb9bdb9d66c6b9d1d9191d9d9d9dd9dd9d9d919d9dd9dd9d9dd9d1ddd91d191dd19191d1919d19d9d9d9d999b9b9b9a99a9a996996b9b9a9b9a9969a9a9b996969a96969a9696969b96999a9a969a9a9
                    a9a9b9a9b96b9a969969b9b99a9969a9393919d191d19119119dd19191d99d9b9b96999b99b99a9999b9b999b111d9d9d9d91d19111d19191d11d919d19d9b9d9b9db99bdd9191919191dd11d1d191b9b9db9db9bbd6cb6d1d1d19d9d9d9d9d9d9d9d9d9d9d919d9d9d9dd9119d91dd919ddd919dd19dd91d9d9d9399b969b969969b9a9b99a996969969a9969969a9b9a99a9b969a9a9b969a9a6969a9a9696
                    9696969b69b9699b9a9b9a969969b99b99dd19d111911d19dd9d91d9d9d9319a999b9a99a99a99b9a99a99b99d191dd19d9d91d11d9111d119191d9d9d1d99d9d9d99b99d11d1d1d1d19d99d9d9d19dbdb9db9bdb9b6b6b689d911d9d19d919d9d9d9d9d9d9d9d9dd9d9191d91d19d19d1d91d91d9dd91d9d9d9d9d9b9b9a99b9a99a9969a9969a9b9a9b969b9a969969969969a99b9969a9a9699a969696b6b
                    9a9b9a99a99a9b9699b9699b9a9b9a99a999dd9d1d11919d9d919d919d9d99b9b9a999b99b99b99b9b99b9b91d1d19111d919d19111d91191d1d91d9d919d9b9d9d9d939d9191919191d9dd9d919dd9b9db9bd9b9bb6b6b6cb119d19d9d9d9d9dd19d9dd9d9d9dd919ddd191dd91d91d191d91d91d91d9d19d9d9d99b9999b9699b9969b9969a999a9969b9a969b9a9a9a9a9a99696b9a96969a969a9a9a99a9
                    699a99a99699b9a9a969b9a999b969b969a961d91191d9d919dd19ddd9d9d999699b9a9b99b99a9999b999b1d19111d911d9d11d19111d1d1919d9d9dd9dd99d9d9b199d11d1d1d1d1d91d911d19db9db9db9bdbd9b6b6b6b69d191d9d9d9d9d99d9dd9d9dd9d9d1d9d91dd911d91d919d91d91d91d91d9dddd9d9b99a9a99a9b969a9b9a9b99b69969a99699a9969969969996b9a96969b9a996b9696969696
                    9a9696969a9a96999b9a9996a99a999a99b9d9d1d1d19d9d9d919d9919d99a9b9b99b999a99a99b9a99a9b99d11d9111d911191911d91919119d1d9d9d9d9d9d9b99b1dd1919191919d1911d91919bdb9bd9bd9b9b6b6b6b6c9d1d191dd9dd9dd9dd9d9d9d9d9d9d91d9191d9d91d1ddd1d91d9dd91d9d19191ddd9b99b96999a9b999a9969a99a9a999a9b9a969a9a9b9b9a99a99b9a9b96969a969a9b9a9a9
                    b99a9b9a99b999a969b96b999b99b969b999dd1911919dd9d9d1d9ddd99399b9b9a99b9b99b99b999b9999a99d911d9111d1d11d1d11119dd19d9d919d9d9dd9d9dd9d91d1d1d1d1d19d1d911dd1b9b9db9bd9bd7d6b6b6b8c9d9191d19119d9d9d919d9d9d9d9d91d1d91d191d19d919d9d9d191d9d19dd9d9d999b9b99b9a9999a96969b9969999a96996999b99b9969a969a969699969a9b99b9a99696969
                    6b9969b9b996a99b9a999b9a99a99a999b939111d11d19d91d9d91991d99b99b999b99a99b9b99b9b9b9a99b9911d111919191d19191d9d9d9d9d9d9d9d9d9d9dd191d1919191919191d91d91919bddb9dbd9bd9bd6c6b6b6c9d1d1d91d191d91d9d9d9d9d919d9d19d91d9d19d91d9d191dd9dd9d19dd919d9d9d9a99a99b9b9a99b9b9b9b9a9a969b9a9b9a99a996b9b99b9969a9b939a996b69696b9a9a9a
                    99a9b9969a999b9699b9a999a99699b9a999d1919191191d9d9d9ddd9dd9b9a9b9b9b999b999b99b999b99b99d9d91911d111d91111d19d9d9dd919dd9dd9d19d9d1d191d1d1d1d1dd91d1d1d1db9b9db9b9bdb9b9c6c6cb6bb919d1d91dd91d191d9dd9d9d9d9d9d191d191d1d191d91d919191d9dd91d9dd9d9d9d999b999999b9699a99699969b99b99699a996b99a969a9b9b9d9d9996b99a9b99a969969
                    b9699a9b99a9b9a9b99b9b9b99b9b99b99b9d1d11d1d1d19d9d9191919d99b999b999a9b9b9b9b99b9b99d9b9d99d11d191d11119d1919dd9d9d9dd9d9d9d9d19d9191d191919d19d91d191919d9dbd9bddb9d9bdb6b6b6c6b6dd19191d911d91dd1d19d919dd9d19d1d9d19d9d9dd91d9dddd19d191d9d19d19dd9dd9b9dd939b9939b969b9a9b99a996b9a9969b9a999a9969b9d9d9d9a99a999a9699a9a96
                    9b9a999a99969999b9a999a969b99a99b99dd19111911919d9d9d9d9d9d9b9b9b9b9b99999b9993d999399b99b9391d19119191d1191d191d9d19d9d9d9d9d9dd91d1d191d1d191d11d91d91d1bdb9bd9b9dbbd79bb6b6b6c6c9191d191d9d1d91919d119dd9d9d9d191d91d191d191d919d919d9dd9d19dd9dd9dd9dd9d9d9d9d9d9999b9b99b9a996b99b9b9b99b969b99b9b99dd9d9d9b996b969a9b9699a
                    99b96b99b69b9a9b999d9999b99a99b99a999d1d911d11d9d91d9d9d9d9d999999b99b9b9d9b9d91db99d9939d99d1911d1d119191d11d1d9191d9d9d9d919d19d91d91d19191d19d91d911d9d9b9db9bdb9d9b9d6b6b6c6b6bb9d19dd191d91d9d1d9d9d9d9d9d9ddd91d9d91d9d19d1d9d9dd1d91d9d9d919dd919191d9dd9d9d9bd9399a96999b999a99969b9a99b99a9969d9d9d9b969a99a99b9969b9a9
                    699a99a999b9b9969b11ddd99a99b99a99ddd9111d191d1d1d9d9dd9dd9ddddd939b99b99399dd19d9d9dd99d9d9d11d191191d1d11919111d19d9d9d919dd99dd1911d91d1dd91d1d911d911b9db9bd9b9bb9dbb6b6b6b6cb66d91d191d191d91d911d1d19d9d9d191d91d1d91d9d19d9d919d91d91d9d9d9d9d19ddd9dd9d9dd9d9d99d999b9a99b9a99a9b9969b99a9969bd9d9d9d99b99a996d9a9a9699b
                    9a99b99b9d9a9b9b91d111dd99b99b99b999d1d91911191919d9d919d919d99d99d9b911d9bd911d9d9d9dd9d9d9d99d11d1d1d191d1d1d9191d9d1919d9d9d9d91dd911d91911d911d9191d9db9bd9bdb7d9bd9c6b6b6cb66b6dd919d19d191d919d9d99d9d9dd91d91d9191d91d9dd9dd9d19d9dd9d9d9d9d9d9d9d9d919d9d9d9d9dd939b9b99b999b99b9a9b99a9969b99d9d9d9939b9b99b99b999b9a96
                    99b99a99b99999b9d1919119d99b99a99b93191d9d9d911d1d19d9d9d9d9dd9ddd9111d1d9911d19d9d9d9d9d9d9d9d99d919191d9d91d11d1d91d1dd9d9d9d9d919d9d91d1d191d9191d19db9bd9bdb9d9bdb9c6b6c6b66bcb6b91d19d19d19d9dd919dd9d9d91d91d91d9d91d91d91d91d9ddd91919d9d9d9d9d9dd9dd9dd9d9d9d9d99d99b9b99b9a9b99999b969b9b9b939d9d9399d999a99a999b99b99a
                    9b9a99b99b9b9a999d11d1d19d9b9b99b9d1d19d9dd91d19199d9dd9dd9119199d19d191d1d1d911d19d9d9d9dd9d9dd91d11d1911119191d911d919d9d9d9d91d9d9d9d91919d1d19d9dd9d9bdbd9b9bbdb96b6b6c6b6cb66b6bd91d191d19d9d9d19d919d9d191d91d91d1d91d91d91d91d919dd9ddd9dd9d9d9d9d9d9d9d9d9d9d9d939d99b9b9a9999a9b9b9b999d9d99d9dd9d9dd939b9699b69d9d69a9
                    9999b99a99b199b9b1d19191dd99b9b99b991d9d919d9d111dd919d9d91d1d9dd9d91d1191d111d19d9d9d9d9d9d9d9d91191911d9d1d1d111d911d191d919d19d9d919d9dd9d919d9dd91d9bd9db9db9b9d6cb6c6c6cb66bc6b6dd919d19d1d19d9d91d9d9d1dd91d91d919d19dd91d91d9dd9d91d9d919dddd9d9d9d919d9d9d9d9d9d99b9b99999b9a9999b999a9b9d9a9dd9d9d9d9d999d9b99b9a9d999b
                    9a9b9b99b99b9b99991d111111d9999b99b911d9d9d9d19d19d9d9d9191d9d9d9d1d99d1d191919d19d9d9d9d9dd19dd1d1dd1d91d9191919111d9191d1dd9dd19d91d9dd91d19d19d9d19dd9bd9bdb9b6bbb6b6b6c66c6c6b6a6b91d1d91d919d9d9d9dd9d19d91d91d91dd9dd91d9dd9d191d9d9dd9ddd919dd9d9d9d9d9d9d9d9d9d9d9b9d9a9a9999b9a99dd9d99d9d919d9dd9d9ddd9399b9a9999d9b99
                    b999969b9a99d9b9b9d191d919d9bb99b99b9d111d9d19d9119d91d9d1d9d9d9d919dd99d111d119d9d9d9d9d9d9d1191919191d9d91d11d19d911d119191d9d19ddd9d9d191dd91d9d9d1b9bdb9b9db6c66b66b6c6cb8b6b8b6b819d91d91dd19d9d9d9b19d191d91d91d91d91d91d91d9d9d91dd919d919d9d91dd9d9d9d9d9d9d9b9d9b9d9d999b9b99b9b96d9d9b9dd9dd919dd9d9d9d9b9d99d9b99b9d9
                    9a9a9b9999b9a9dddd11d111dd9d99b9b9b9999d9119d9d19d9dd9d91d11919d9d9d9d9d99d919119d9d9d9d9d9d99d11d191d99d9d919d19111d919d1d1d9d99d919d919d191d1919d9d9db9b9bdb9c6f8c6c6cb6b66c6b6c6c6c61d191d919d9d9d9db9b19dd91d91d9dd91d91d91d9d191dd9d9d91d9dd919d9d91d9d9d9d99399d9d99d9d99b999d9d999b99d9dd9d9d9dd9d9d9dd9d9d9d9b9939a99b9b
                    9999b9b9a99911191191191919d9b99b99b9b939d91d9d9d91d9d9d911911d1d919d9191dd91d19d9d9dd9d9d9d9d9d99d9dd19d9d9d91d1d19d11d1d919119dd1d91dd1d19d191d9d9d9db9dbd9b9b6c6c6c6c66b6cc6c6c6c6b8c99dd91dd9d9d9d9b9dbd191d91d9dd91d91d9dd919d9d9d9191dd9dd91d9ddd9d9d9d9d9d939d9d9dd9a99399b9a9d99b9d9b9d9d9dd9d9dd9d9d99d9b9d9d9b9999b99d9
                    b9b99b9b9b931911d1d191d1d9d9d9b9b9d9d99d9d9d9d9dd9d9d9dd1d1d1911d1d19d9d91d91d1d9d9d9d919d9d9d9d9d9d9d9d9dd9dd9191d19199d9d1d91991d1d919191dd1919d9d9b9bd9bddb78c8c66b8bc6c6c6c6c6c6c6c6d91d919d9d9d939bd9b9d91d9d19d9d919dd919dd91dd9ddd99dd919d9d9191d9dd9d9d9d99d9d9d9b9d99b9b9999bd99d9d9bd9d9dd9d919d9dd9d9d99b9d9b9b9b9a99
                    9b9b99b999d11d191911d119d9d99b9d99b9939d9d9d9d9d9d91d9d9191911d91d91d91d9d9d9d91d9d919d9dd919d9d9d9d9d91d919d91d1919d1d1919d1ddd191911d91dd919dd9d9db9db9b9b9d6c8ccc6c66b6b68c8c6c6b8c8c9d9d9d19d9d9dbd9bdb9dd91d9d9d91dd9191d9d19d91d919dd919dd9dd9dd9d9d9dd9d9d939939d9d99399b9bd9399b939d9d9dd9d9d9d9d9d9dd9d9dd9d9d9d9b999d9
                    bd99a99b9b19191111d9119d9d9d9d9939d9d99b9dd9dd919d9d1111d111d111911d9d9d9d919d1911d9d9dd919dd9d9d9d919d1d9d19d9d9d9d9d9dd1d9d9191dd19d1d911d91d19d9d8c6bdbd9bd6c6f6c6c6c6c6cc6c8c8c6c6f66d91d9dd9d9b9b9b9b9bd9d91d9d9d9d9ddd9d19dd9d9d9dd919dd9d9d919d9d9d9d9d939d9d9d9d9d999b99b99b9d99d9d9d9d9d919dd9d9dd9d9dd9d9d9d99b99b9a99
                    d9dd9b99b111d11d9111d19dd91d9b9d99d9dd9dd9d9d9d9d9d9d9191d919191dd919d9dd9ddd9d1d919d9d9d9d191d9d9d9d9d91d9d9d1d19d9d9d99d1911d1919d19d1d9d1d919dd9b8c66b6db9bb6c6c8c6cc6c6c6f6c6c8cc68c6b9d9d9d9ddbd9bdbdd9bdb199d9dd19191919d9d91d91d9d9d9d9d91d9dd9d9d9d9dd9d9d9dd9d9dddd9d9b9b9999399d9dd9dd9dd9d9d9d9d9dd9d9d9d9939d9d9b9b9
                    9d9999b99d9119111d9191d9d9d9d9b9d9d9ddd9119d919d9d91d91d11d1d1d1911dd1919d99d99d11d9d9d9d9d91d9d9d9dd9d919d9d991d9d9d9d9d191d919d1d91d91919191dd9b18c8c6b9b6db6c8cc6f6c8c6c6c8c8f6f6cc6c6c8c99d9d9b9bd9b9b9b9b6b9d9d9d9ddd9dd9d19d9dd9d91d9d9d9d9dd9d9d9ddd9d9d9dd9d9d9d999d939d99b9b9d939d9d9d919dd9d9bd9dd9d9dd9d9399d9d9d999b
                    9dd9b9b9b11d1d191d1d19d9d9d9d99d9d9dd91191d9d9d9d1d91d919919191d19d919d1d9d19dd9d91d91d91d91d9d9d9d91d9d9d9d9d9d9191d9d9d9d191d1d91d91d1d1d91d9bd88c6f6bbb9bd9b6c6f6c8c6f6c666c6c68c6f8c6c6c8cb99c9b9bdb9dbdb9b6b9d9d91919dd919ddd19d9dd9dd9d9d9d9d9d9dd99dd9dd9d9d9d9dddd9d99d9d9b9b9d99d9d9d9dd9d9d9b9bd9d9dd9d9d9939d9d99b9a9
                    999dd99b9191911d1919d9d9d9d9d939d9d9111d1d11d9d9d91d11d1d1d1d9d9d911d9d919d1d9d991d11d191d19dd9d9d9d919d9d9d9d9d9d9d19d9dd191d9d1d91d19d9d91d1b9db6f68c66db9bdb6f68c6f6c6c6cc6c8cc6f6c6c86b8c88d6cc9bd9bd9b9d6b6b6d9dd9d9d91d9d9d9d9d9d9d9d91d9d9d9d9d9ddd9d9d9d9d9d9d9d9939b9d9d9d9d9dd9d9dd9d9d9d9d9bd9b9d99d91d9dd99d9bd9b99b
                    9a99dd99d1111d919d9d19d91119d99d9dd1d191919119d911d191919199d9d9d9d9d9d9d919119dd19191d191d191119d9d9d19d919d9b9d9d9d9d99d91dd19191d9191d1d91b9bb8c6c8cc8d9bd9b6c8cc6c8f68c66c6c6c6c8cc6c6c6c6c6c86c6bd9bdb9b6b8c8c99d9d9dd9d9dd919d9d9d919d9d9dd9d9d9d99d9d9d919d9d9d9d9d99d9d9b9d9d9d9d9399d9d9d9d9b9bb9b939dd9d9d9dd9d99b9b99
                    b9b9d9d9dd91d11d19d9d9dd9d1d1dd9d9d191d111d19dd1d191d1dd1d9d9d919d9d919dddd1d1d191d1d91d191d19d1d9d9d9dd9ddd6b8d9d9d9d9dd91d9191dd91d91d91919db9b6c8c6f6f9bd9b9b6c6f6c6c6c6cc6c8ccc6f6ccc6c66cc86c8c6bb9b9dbd8c6c68cc9d9d9d9d9d9d9dd9d9dd9d9d9d9d9d9d9dd9d9d9d9d9d9d9dd9d939d9d9d9d9d9d9d9d9d9d9d9d9bdb9db9bd9d9d9d9d9d9d9b9a69b
                    999b9d9d911d1919d9d9d9d9d9d9191d9d191d191d91199191d191999d9d9d1d9d9dd9d19999191d19191d191d91d1919d9d9d9d1968bb6b9d9d9d9d919d19dd91d91d919d1db9bb8cc6f66c9bd9bdbd8c6c8f68f6c66c6f66f68c6cc6c6c66f6f6c66dbdb9b6c6c8c8c6c9d9d9d9d9d9d9d9dd9d9dd9dd9d9dd9d99d9d9d9d9d9b9d9d9d9d9d9b9d99b9d9dd9d9d939d9db9b9b9bd9bb9b9d9dd9dd9b966b69
                    b9b99bd1d1d911d9d9dd9d9d9d91d1919d9d191d1119d9d1d191d9dd9dd9d9d1d119d9d9d9dd9d191d1d191d91191d1d9d9d9d99b8cc8b6c99d9d9d9ddd91d19191d91dd19d9bd66c6f6c8f6bd9bd979c6f6c6c6c6c6c66c6c8c6f66cc876c6c86c8cb9b9db6c8c6c6f68c88b99d9d9dd919d9d9d9d9d9d99d99d9d9d9d9d9d9d9d9d9d9d9d9d9d9d939dd9d9d9d9d99a69b9bdb9b9b9c6c6d9d9d99b9ba66a6
                    9b9b999d1911191d9d9d19d9d9d99dd9d91d9d919d19dd1d191d19d9d9d9d9d919dd1d9d9d9d9d1919191d911dd1919d9d9d99dd8c6866b6b9d9d9d9d91d9191dd91d9d9dd9d9b6c8c68c6c6b9bd7bdb66c6c8f6c6c6c8c6f6c6f66c6cc8c6c6cc8c66db9b6b8c6f686c86cc6c6d9d9d9dd9d9d9dd9d9d9d9d939d9d9d9d9d9d99d9d9dd9d9d9d9d9d6d9d9d9d9d9b9b9bb9b9b9bdb9c6c6a6b9d9399d96b96a
                    999d9b99d1191d111d9d9119d9d9d9d9dd91d1d1191d9191d1191d19d9d9d9d191d91919d19d91d1d1d191d19191d9d9d99dd9bb68ccc6bbb9d9d9d9d191b6b9d919d9d999bdbd8cc6f6f687bd9b9d9ddd8cc6c6c686c6c6c8c86c6c6686c6c68f6cc6bdb9bd6c66cc6ccc6c8c88b9d9d9dd9dd9d9d99d9d9b999d9b9d9d9d9b939d9d9d9dd9d9d9b9a6d9d9d9d9d9d9b9db9b9b9b9c8c866b6a6d9b9b9b6a69
                    b9b9b9b9dd1d119191191d19d9d9d9d9d9d99199d1d1d1d191d1d911d9d9d99dd91d91d9d91d191919d91d91dd191d9d9d9d939b8c6f6b6b6b9d9d9d91d99b6a91d9d99ddd9b9c86f68c6cc6b9bdb9b9bb6c6f6c6cc6c6c66c6f6c66cc6c6c6c6c6c6c6d9d9b66cc6c6c66c6c6c8c6b9d9d9d9d99d9d9d9d9d939d9d99399b9d999d9b9d99d9dd9d99b69d9d9d9b9b9b9b9bdb9bd9b86c8c8c6b6a99b99996b6
                    9b99b99d9191d1d11d11d9d19d19dd19d9dd91dd91919191d91911d919d19dd9191d19191d191d1dd11d191d919dd99d9d9bdb9b6c866bb6b69d9d1d19d9d999d99d9d9d9bb9b6c8c6c8c8c6cb9b9bdb96cc86f8c686c86c6f6c6c6c66cc66c6c6f6f6b9bbd9bb78c8c6c6c6f6c6c6bb6b9d9d9d9d9939d9d99d9b9d9399399d939b9d9d939d9d9b9b9b9d9d9d9d9d9b9bd9b9b9bb8c86c6c6c6b6b99bdba69a
                    99b9939d9d11919191919d91d919d91d9d9d919d9d1d1d19d9d1d911d99d99d19dd91d9d9dd1919d99d91d191d1919d9bdb9b9bb8c6fc666bb69dd919d9b9bb69d9d9d99b9db6c8c6f6f6c6f6db9db9bd8c6f66c6c6c6c6c68c8c6c6c6c6cc66c68c68bb9d7b9bb68c6f6c86c6c8c6b6bbb9d9dd993999d9b9399d99b99d9d9d99d9d99d99d9d9d9b99a69d9d939b9b9b9b9b9bd96c6c6c8666c66bb99969a66
                    9b93999d9d91d11d1d1d19d91dd1919119d9dd9dd9d9191d19d9d1d91d9dd9d9d91d9d9dd9191d19d91d9191d91d9d9b9b9bdb96c6f66cbb86bb919db6b9d9a6b9d99dbdbd9b6c6f6c68c6f66b9bd9b9b6f6c8c6c6c6c6c6f6c6c6c86c68c6c6c6c6c6b9b9b9d96c6c6c86c6c6c6c6b6b6b9d9d9d99d9399d99b9d939d99b9d9b9d9939939d9d9b9db69a9d9d99b9b9bdb9b9b9bb66c8c6c6cb6b66cb9ba669a
                    9999bd9dd9d191d91191d1dd9191dd1dd1119d919d919d191d919191d9d9d9d1dd9d19d91d1dd9d9d9d91ddd91d9d9bdd9bd9bb6c86c86b6bb6b61d9b69b9b696d9399b9db9db8c68cc6f68cb9bdb9bd6c8c6c66c66c6cc6c86c68c6c6cc8c6c6c68c87bbd9bbb6c66c6cc6c6c6f6c6b9b6b9d9d9dd9d9b9d9b9b9999d9399b9d99399399d9d9d9b99b66b9b939b9bd9b9bb9bd9bb86c6c6b66b6a6b6b99b6b6
                    9bd99dd9d1d1d11191d19191d91d1991919d1d9d9d9dd191d1d1dd1d19d91d9191191d1d9191919d9d9dd9191d91939b9bd9b68c8cc8c6b6b6b6cb999a6a996a699939db9bb9c68cc6f68c6c9bd9bd9bc6c6f6c66c6c66c68cc678cc6c86f6c66c6c6f66db9d9bd8c6c6666c6c66c6b6b6b6b9b9d9d99d9d9b9b9bd93999d9d99399399b9d939b99bb9b96a696b9b9bb9b9bd9bb96c68c6c6b6b6b66a6b99a96
                    d9b9b9d191919191d191d1d111d9d9d91d191d191d9d91dd919191919d9199d1d91d9191d19dd9d9d9d91d1d919d9bdbd9bb6c8c6c6f6c6b6b6b6b9b96966a96ba9d9b9b9d9b8c6f6c6cc6f87d9b9bd6ccc6c66bc6b6c6c6b76b6c6c66c86c6c6c6c86c6d9bbd9b7b6b6bcb66c6c66b66b6a69b6b9d9399b99b99a699bd9b9d939b99b9b9d9b99bb996a6969a9b9b9b9b9b9bb9b6bb86f68c66c66b66b6b966a
                    999b99d1d11d1d1d1d1d1919d91919d9d91d191d191d1911d1dd191d19d9319d19d1d91d9d9d91d99d99d99d19d9d9b9bb9c8c6cc6f6c6b6b6bb6b99bd9396b696d9db9bdb9b6c86f68cc86c9bbdb9b666c8c6c6b6c6b6c6d9db6c8c6c8c6c66c6c6c8cb9bd9bb9d9c6c6b6b6b6c8c6bb6b86c69a69d9b9d9b9b96ba999b9d999b9b6a96a99b6a969a969a96b9b9bb9b9b9b9b9bb96c68c68b6cb6a6b66a6b96
                    9b9d9bd9191d919191911d11119dd9d9d1d91d91d1d91d91919191d9d19d91d91d9191d9119d99d9d9d9d1d99d99d9b9d9c86c86f6868c6b6b6b66ab99b69a96a969b939bb6c8cc68cc6ccc6bd9b9b7b6b8c6c66c6b6c6c9bb9b6c6f6c66c6c6c686c666b9bb9db9b6c6c686b6b66c6b6b6b6cb69a999d9b99b9b969639d9939b999b9696a69b96a96b96b6d9b9b9b9bb9bdb9b9b68c86c6c6666b686a666a6b
                    1dd9b9111d1111d11d191919dd19d1dd9d1d9119d91d191d191ddd1d91d1d91191d1d91d99d9ddd9dd9d99d9d9d9b9bdb9c8c6f6c8cc6f66b6b9b6b6b8b9a6969a9b9bdb9c8c6f6f68cc6c6f9b9bd9dbb876c6cb6b6c66bb9db9c6c686c6c6c68c6c6f6bbd9b9b9b6c8c8c6c8c6b6c66b9b6b66a696399b9b9d9a6b6a99939b99ba96a9a99b69696b96a9b9bb9bb9bd9b9b9b9b98c68c6c86c6b6a6c66c8b666
                    1191d19d1919d919191d1dd191919d91919119d91d9191d91dd919191d9191d91d9d91d9d9d9999d9d99d9d99d9d939b9c8c6f686c6f66b6b6b6b8c66b66c6ba696db9b9b68c686c8c6f6f6cdbd9bb99bb6b6b96b6c6c6db9b9b66c6c6c6c68c66c6c6c6bb9bdb9b6c686cc6c686b6b6a66b6b696a69b99b9a6969a969a69b9a696b9696b69a9a69a969b9b9b9b9b9b9b9b9b9bb68c66f6c6c6c66b6c6c686a6
                    1d1d91d191d111d1d1d19191d1dd11d1d1d91d19d91d1d1d9191d19d191dd91d91d1d9d99d9d939d9d9d9d9d9b99d9b9bb6c68ccc6c6c8c6b6b6b66cc6b6b6969a9b9db9b6c6f6c8c6f686c669bd9dbd9bdb9bdb6b6b6b9bdbdb6c6c6c6c6c66c6c668c66db9b9bd66c6c6c8ccc6b6b6b6b6a6b6b9b69b99b9b9a6969a9b69b99b99a9a969a969b969a8b9b9b9b9b9bb9bb9b666c66c8668c686a66b6b68c6c6
                    1911d191d1919d1919191d1d91919d919191d9d9d9d999d91d19191d91d91d91d9191d9d9d9d9d9d9d9d99399d939b9bd9b6c6c6cc8c8c6c6c6c6bb686c6a68b66bb9b9bdc8c6c8c6f6c6c8cc6b9b79bd9b9b9b9c6b6bdb9b99b66c6c686c6c6c66cc68c6b9b9b9bb6b6c8c6c686c6b6b6b6b6b6a69a69b999b99b9a9699b99b99b96969a969b69a68666b9b9bb9bb9b9b9b9bc86c86c8c68c6c6c66a66c68c6
                    d1d911d191d1d191d1d1d911d1d1d191dd1911d9d9d9b9b9d91d9dd91d9191d91d9d9d9d9d9d9d9dd9d9399d9d999bd9bb9b8c6f68c6f66c6b6b6b6c6c6b6c68b8c6dbd9b66c8c6f66c8c6f686cb9b9b9b9bdb9db9bb9b9b9bb9c6c68c6c686c6c686c8c6db9bdb9b9c6c6c6f6c6c66c6b6b6b6b6b69b9b9b99b9696b9b6a9b9b99b9b9b969a99668c8cb6bb9b6d9b9b9b9bb66c86c86c6c6c8686c66b66c686
                    1d119191dd9191d1919d119d919191d19191d91d19b9d98b6b191d1d91ddd91d91d19d919d9d9d9199d99d9939d9d9bb9db6c6c6c6f66c6c66c66c68c6c6b6c8c68db9b9b8c6f6c6c86cc68c6b66cdb9bdb9b9bdb9b9b9bdb9bd6c6c6c6c6c6c68c6c86c6b9b9d9b9b666c8c68c66b6b6a66a66b669a99b9b9b9b9a9698b66699b9b99b96b96b88c66c686868b6b9b9b9bb966c68c6c6c68c6c6c66c86a66c6c
                    9191d1d1911d1d91d91d9d11d191d9191ddd919d9d9d9bb666a919d919d91d9dd9d919dd9d99d9d9dd9d993999b9db9db96c8f68f66c8c66cb6b68c6b86b6b6c6c879bdb9bc68c6f6cc6f6c6fb6c6b9b9b9bd79b9bdb9bd9bd9b6c66c86c6c66c6c8c6c6b9bdb9b7b9cb6c6c6c6f6b6a6b6b6b66a6c96a999b99b99b6c866a6a9b99a99b99a686c6c86c6c6c689b9bb9b9b9b8686c6868c6c68c6c86c6c6b68c
                    11d19191d1919119db9d191919d1d1dd9191dd1d19b9b96ba966b91d1d9d9b9d91d9d9d9d939d9dd9d9d9399399d9b9b9b8c66c6c8c6f6c666a6cc8dbdb6b6b68c6bd9b9b78c6f68c6f68c6c68c66db9bdb9b9bdb9b9b9b9b9bb66c66c86c68c6c66c6c6db9b9b9b9b66c68cc6c66c66b6b6b6a66c66b99b99a99a9986c8b6b686b99b998c86c6868c6868c68c6b9b9b9b98c6cc68c6c6c68c686c6c686c6c66
                    191d1d1d91dd19d999d9b1ddd1919d91d1d91919d99d9d9666a6b669b9d9b6a9191dd9d9d99d9d9d19dd9d9d9d999bb9b6c6f68c6c6c68c6bc6b66c9b9b9b6b6c66db9bd6b68c6c6c68c6c8c8c6fd9bd9b9db9d9b9bd9bdb9b9b6c6c86c686c66c6c86c9b9b9bdb9bdd66c686f68c6b66b66b66b66a66b9b9b9b99b8c86c6b6b6c86b98c686c86c6c68c6c686c66b9b6b9b9b68686c6868c66c6c6666c86b6b6
                    1d19191d19191d93b9b9969d91dd1919d91d91d9b9b9b9b9a696a6a69b9b999d9d9d9d9d9d9d9dd9dd9d9dd9993939bd9c86c8c6f6c8c6c66b66b8b9b9bd9c6b6cb9b9b6b8c6c8c6f6c6f6c6c6c66b9bb9b9bdb9bd9bb9b9bdb66c68c68c6c6c6866c8c79b9b979b9b9b6c6c86c86c6a68c6a66a6c6b6869b999b9886c8666b6b6868868c6c686c8686c686c68c89b9b9bb9b9c6c68c6c66c86c68c6c66c668b
                    91d1d191d1d1d9d99d9bda6619191d1d9191d9d9d9b9d9b99a6b696b69d9b6a61d19199d9d993919d91919d93999b9b9b8c86c6c68c6f68c6c6b8c9bdb9b9b6b68b9bd6c686f6c6c8c6c68cc6f6c6cd9b9b79b9b9bb9db9b9b9b86c6c8c6c6c6c6c6c68b9bdb9bdb9bb6b6c6c86c66c6b6666b66b66a6b886b9a88c6c6c6b6a666b6c6c68686c686c6c68c68c666b9b9b96b9b6b686c68c68c68c6686a686a66
                    1d919d191919d9b9b9b996b6a19d91919d99dd9d9b9d9b9d6b696a69a69b9b96d9d9dd9d99399d9d9d9dd9d99d9d9b9b6c6cc6f6c8c68c6c6b6c66b9b9b9b6b6b8db9b68c6c68cc6c6f68c6f68c8d88b7d6c6dbb9b9b9b9bd9b6c8c86c6c6686c6c68c79b9b9b9b9b9b9c666c6c6c66c6cc6c6a6b6a66c6c88866c686866a66bb8b68c6c6c6c86c68c686c6686cb9b9b9b9b9b668c686c6c66c66c6c66c6c66a
                    91d1d91dd1919b9d9b9b9a696b191d9dd9d99d9b99b9b9b996a6b698b6b966a661919dd9d99dd9dd19d9d9d9d9b9bb9d8c6c6c86c6f6c6c86c68cb9bdb9bb6b6b66db9c86f68c6c6f68c6f66c68c7d8b9b86c9b9b97b9bd9bb6c686c86f68c6c686c66b9bdb9b9bb9b9b6b6c6c68c6b6686c86b66a66b686c6cc68c6c6c86b666b6866868c686c6c686c66b6c86b9b6b9b9b69b866c6c686c86c8686c6866a66
                    d9d91d1919d9b9d9b9d966b6a69d9dd9d9d9d9b9b9d99d9b9a966a696a6a96b9a9d9d9d9dd9d9d99d9dd9d9d99d9b9bb68c8c6c8c66c8c6c8c8c6bb9b9b9b66b6b6b9c8c68c6f68c68c686c8c8c69b6b6b6c86b66b6bd9b79b66c6c6f68c6c66c6c6c6bb9b9b9b96bb6b66c668c66c6a6c66c66a66b86c6c6868c668c86c6b6b66a6c6c6c68c68686c68c6b9b9b9b9b9b6b9b98b6c686c686c686c6c86c6c68c
                    6b91191d91b9d9b99b9ba69696a6d99d9d9d9b9d9b9b9b99b66a96b6b969a9666b6dd91d9d9d9ddd9d9d919939b9bd96c86c6f6c6f686f686c686b9b9bd76b6b6c66c6c6f6c68c6c8c6f6c86c66bd9b9bb66c86cc6c6bb9b66c6c68c6c6c68c686c66b86b9b9bdbb69b6b6a6b6c8c666c6c68c66b66b68c68c6c68c66c6866b6a6666a686c66c6c6c68b9b96b9b6b9b9b9b9b9b6866c686c686c6c66c6868666
                    b6b9d191d99d9b9b99b9b6a6a696a9d99d99b9d9b99b99b9b696b69a66a69bb9a96a9d9d9d9d9d99d9a9b9d99b9b9bb6c6c6c686c6c8c6c6f6c6c9b9b9b9c6b6b6b6b66c68c8c6f66c68c6cc6f6db9b6b6c68c68c86c9b9b6c668c66c686c68c6c68b6d6c9bb9b9b6c66866b86c686c66a66c6c6b6a6c6686c686c68c68c66a66a6a666c686868686c9b6b9b9b9b96b96b9b6b9bb6b866c68c6868c686c6c6c8
                    69869b19d9b9b99d9bdb996b69a696d9d9d9d9b99b9d9b9b9a69a6969a96d9b96b6969b919dd99d9b96b6b9b99b9b9b66c8c6c8c68c6c68c68c6b7db9b9b66a66a6c6c6c86c6c68c8c6c6f68c66b9bd668c6c6c68c6866bb66cc66c66c6c8c6c66c6db9b6b9b9b9b66c6bc66b68c6c86b86c68686b666b8c686c68c686c6c66b6666b6c68c6c6c6c6b69b9b6b96b9b9a9b9b9b969b96b66c66c6c6686c666a66
                    a6b6a6b9b9b99b9bb9b9bb69a66b6b9b99db9b9b9d9b9b99b9a696a6b66db9bb9b6a9a69b999b9b99b9969a9a9b9b9db66c68c6f6c6c8c6c6c6c9b9b9bd9c6b6b6b6b6b6c6c6c8c6c6f686c6c86cb96cc68c8c8c6c8cc686c668c66c86c6c686c86b9b69b9b9b9b9b6b8b9b66b686c6c6c686c6c86a6a666c6c86c66c6868c66a6a66a6666c686c6b9b9b69b9b9b96b9b96b96b9a6bb6b6868686c6c686c8686
                    b69a9666a99bd9b9b9b9b9c669a96a66ba99b99b9b99b9d9b696b96969b9b9b9b969696b6ba9b99b99ba96696b9bdb9bdb9c6c668c86c6f68c6bb9b9b9bb6c6b6b66b6b68c8c6c6c6c6c8c6c6c6876c68c686c6c6c668c6c6a6c6c66c6686cc86c68b9cb9b9b9b9b9b96b6b6a6c6c86866b8c686c6666b6c686c686c86c666a6666b668b8686c6869b969b9b69a9b9b96b9a9b9b9666b6a6c6c668686c686c6c
                    6b666b9a99b9b9b9b9b9bb6a866b696b969b9b99b9b99b9b9b9a6a9a6b9b9b9b9b6a9a9696969b9b9b996b9a9b9b9b9b9b9bb6bc66cc6c68c66b9b9bdb9b66b66a6b6b66c6c6f68c6c86c6c8c6c6d86c68c6f68c6f6c6c866c668c8c6c6c86c6c8bb666b9bb9c6b6b9bb9d9a66686c6c6c666c6c68b6a6b68c686c686c68c666b6a68b66b86c686b9b6b9b69b96b9a96b9b969a9bb9866686686c6c6c66c6866
                    a96b9869b99b8b9bdb9b986b6b69a696a6999b9b99b9b9b999b96969b9b9b9bb9b96b69ab9a6b9b9b9b9a96b69b9b9b9b9b9b9b9b86c68c6c6d9b9b9b9b9b66a6b66a6b6686c68c6f66c6f686f6bb6c8c6f66c6c68c6f6c6c66c66c6886c686f6b99bb9b9b6b686c6d9b9b69b6c6c686c68b86c68b666b6b66c6c686c6866c6a666b66a66b668bb9b9b9a9b9a9b969b9a96b9a969b98a66a6c6c686866a68b86
                    66a96b9a9b9d9b9b9b9cb6b66a6a69a69b9b9d99b99b999b9a96b6b69b9bb9b9b6b969a9669b9a999b996b96b9bb9b9b9bb9b9b6b6c6f66c6bb9bb9b9b9bb6b6b6b6b66a6c66c6c66c6c86c6c689b686c66c86c8c686c6866c6a6c86c6c6c8c669bb9bb9b9868c66c9b9c9bb6b868c6c66c68686b66a6668686868c66c6c6666a6b6a66b66a66896b69b96b96b9a9b69b69a96b9a6b6686686866c66c686686c
                    9b66a98699b9b9b9b9c868c6b66b66b69a9b9b9b9b99bd9b996b969a9bb9b9bb6b6a96969a96996b99b9b9a9b9b9b9bb9b96b966c68c6c86c9b9b9b9b9b9b6b66a66b6a6b6c68c6c8db6c68c6c6b6c6c8c86c86c6c6c86c6c6c686c6c686866c6c9b9b9b9c8c66c86c9b9b6666c6c6866a66c6c66a66a6a6c6c6c66c8666b8b666666b66a66b6bb69a96b9b9b969b69a9b9b69b696686a6c66c686a6866c6c68
                    b69a969b6a9bb9bb9b86c68c6b6b6b6a669b99b99b9b9b99b9a96a9b9b9b9b98b9b6bb6b96b9a69a9b99a969bb9b9b9b96c66cc86c6868c66b9b9b9bb9b9b6b6b6b6a66b6b8c68c6b9668c6c8c6b66c86c6c6c6c6f68c6c66c66c6686c6c6c86c666b9b6b866c86c8686b9a6a68686c6c6866c68b6666686868668666c6a666a6a6a66a96b66a99a96b9b69a69a69b96b969b9b9b6a66686a66a6686c6a686c6
                    9a696a69a9b9b9b9b86c8c6866b6b6b6b6a69b9a99b99b9b99b969b9b9b9b9c666b69a96a96969b969a969a9b9b6b9b9c8c6c86c68c6c6c8b9bb9bb9b9bb9c96c66b6b66b666c66b9b6c68c6c6b9c68c68c6c8c686c6c68c66c68c6c86c66c6c86bd9b666c686c866c6c96b66b6c6c6866c6a6868b6a6b6c6c6c6c6c8666b66666b6966b96b996b69b9a9b69b9b9b6b96b9a96b9a668a666868686c66866c668
                    b69a69b69b9b9b9b9c686c6c8b6a66b698b6a66b6d9b99b9b96b9a9b9b9bb98c8b6a66b6b9a9a96b9a96b96b9b9b9b96c68686c68c68c6c67b9b9b9b9b9b98c66a666b6a66b86c66bb68c6c686b9c6c6c6c686c6c6868c66c68b68c6c66c6868c6d686b6c68c686c868c6b9b66a6686c6c686c6c666b6686868686866c6a6a6a6a66a69a9a9b6b9b9a96969a96b69a9a9a96b9a966a668a66a66c66a66a686a6
                    6969b69a9b9bb9b9b9b6c686c666b66a66b66b6a6b9b9b99b9b9b9b6b9b9b986c66b9b6b669b969a969b9686b69b9b6c86c6c68c68c66c6c9b9b9b9b9b97b66c66ba66b6b6b6c6c66b6c686cc6b9c686686f6c6c8c6c6c6c66c6c6686c66c6c66d86c68c86c6c6c6c6c68b96a666c6c68686c666a6a66a6b6c6a6c6a68666666666a9b696969a969696bb9a969b9b96969b9696b66668666866a66868668b686
                    ba969a69b9b9b9bb9b9c86c86c6b6a66b6b6b6b6b699a9a68b9a9b9b9bb9b6cb68686b69ab69a9b969b9a6c6bb6b9b866c868c686c6c8686b9b9b9b79bb9b68c8c66b66a66a66b6c66c68c6c6b9b68c6c6c686c6c6c86c66c66a68c6c66c668cb66c6c6686868686868666b66b6868686c6c66a6666a666a6668666866a6a6a6a69696b9a9bb96bb9a969a96b9a696b9a69a9a998a68b6a66a6686a66a668668
                    96b6b969bb9b9b9b9bb66c6c686b69a6b6a66a696a6a666c686b6b9b9b9b989b9b8c68b669a6969b9a96686868b9b86c86c6c6c6c686c6cb9b9b6b9b9b9b98c6688c6a66b66b6666c86c68c687b66c66c66b6c68686c686c6a66866c6bb68b6b66c6868c6c6c6c6c6c6c8c6d68b6b6c6c6898668b6a66a666a6c6a6c6c6666696b9a9a96b966b99a96a6866b969b6b969b696b6b66cc66686686a66686c6ccc6
                    b969a9b9b9b9b9b9b99b6686c686a66b669a666a6666b6b86c6b69b9b9b66bb9b66c68b6a66cbb8666868c6bb69b6686c68686868c6c6c6b9b6d9b9b9b9bb68c6c6666b66a66a6a66c68c66c6b9c66c66c6866c6c6c6c6c666c6c6c66686a69b6686c6c686c68686868666a98b6868686a6b6a66866666b6a66c66866868a68b9a96b969b69cc66686666a668a66a66a66a669a966cf686a66a6668b6668cf66
                    6b9a969b9b6b9bb9bbb6c6c86c686b66a666b66b6ba68686c686a9b69b9b89b98c86c66b66b6696a86c6c689b9b98c6c68c6c6c6c686866b9b9b9b9b6b9b66c686c6a66a668c6b6a66c68c686b9b6c6c66c6c66b66c68c68c6866c68c6a69b686c6c686c6868c6c6c6c6c68b666a6c6b686866a66b6a6a6666bf6cc6a66666b969b96b9a9a6fc6a6b6a6666a666666a6666a6866a6cc66a666668b686a66cc6c
                    9a969bb9b9b9b96b9996c86c68c66b6b6b6b6a66a666c6c686c68b9bb9b9b9bb666868c6b66a6a666c686c6b9b6b9c686c6868c686c6c86b9b9b9b6d9b9b9868c6866c6b6c686666c686c68c6bb6b668c68c6c86c66c6686c6c8686c686b9c6c68686c686c666c6866868666a66668686b66a668b666666a666cc6f668a6a69a9a69a96986ccf666666a6a6666a6a6668a6666a668ffc666a6a668c668ccffcc
                    6969a9b9b9b9bb9bbb6c66c686c6c6b698b6b6b66b6b686c686c6b9b9b69bb99b8c6c66b6b6b6b6b686c68d9b9b9b9bb686c6c68c686c6b9b69b69b9b9b9b8c66c6c66a666c6c6a66a6c686c69b96bb66a6686c68b66c8c6866c6c686c6d8686c6c686c6c68c686c6c6c6c666a6a6a66a686686b689a6c868acff6e8666c9b6969b66ba666cfc66a6a666668a6666686666a66686cccf6b98666a6c6acf6cfcf
                    9b9b9b9b6b9b9b9b99b68686c68686b6a69896a686a66b686c686b96b9b9b96b96868686b6a966b6a6c68b9b69b9b9b9b9b686c66c6c68b9b9b9b9b9b6b9b66c8686c666a68686c66666c6c6b9b6b69b666c6c686c68666c6c8686c6c6986c68686a6c6866c66c66868668a666666686686a66a668b86fc666cfcffe6b6c69a9b69f9966a6fefc668666a66666a686ac6a666a6666cf7c66986a66f66fcfef7f
                    96b9b9b9b9b9b9b9b69c8c6c68c6c66a6b6b6a66b666a6b6a66c69b9b9b69b9bb6c6c6c6a966a6966b866b9b9a9b6b9b9b6b6868686866b69b9bb9b69b9b68686c6c66a66c6c6c6a6ca66866b9b99b69a6b666c6c68c6c8686c6c6866b8c686c6c668686a686a686a6c6a668a6a68b6a6c96c6686666afc66cfcf7fc6b6cc966a6cfc8f66ccf7f666a6668a6a666a66c6666666a6fcffc6b6a666cfc6fef7ffc
                    b9b9b6b9b9b69b69b9b86686c668686696a6669a686a666668b6b9bb969a9b69b986c68666a666a6b668a96b9b69b96b969a6c6c6c6c6c9bb9b96b9b9b9b9c6c68686a66c68686668686c6cb9b6bb9b866a6a6686866c68c6c66b86a6666c6c6868c66a6686686c6666866c6666866866868686a18b8cff66cf7ff7fc9ccf6b666fcccc66ccffc6a666a6666668c666cc68a6a666cf7fc6986668cfccfcff7ff
                    9b9b9b9b9b9bb9b9bb66c6c686c6c6a6a66b6a66b6666a6a6b9b9a96b9b6b9b9b9c686a6a6b6a66b6866bb9b69b9b9b9a9b686868686c669b69b9b9b9b69c686c6c666c668b6a6c6a6c66c69b6996b66c8666a6c6c6c8666868b6666a6a66a66a666a668c6c6c668a6a6c686a6a6a66a66a66a666666cf7c6cff7fcfc6f7f666a6cffcf6e4747f6666666a66a6cf66cfc6666668ccfcfec666a66cf7fcf7fcf7
                    b9b69b9b69b9b9b9b98b66b86c6868666b66a96b6a6a666686b69b69b9b96b9a69b66866666b6866a6a8969b9b9a9a96b9b66c6c6c6c68b69bb9b69b69b686c6868c6a66a6666c66668c68686a6c98a686c866c666866c8c6c66bb9c666a66686c686c8666866a66686686a666666866866c666a68afcffcf6fcfcf7f6efc6a668cf7fc47eeee4c66a6a666666cc66cfcc66a6666c6fcff66666afcfcf7f7fcf
                    9b9b9bb9b9a96b9a9b9b9b9b8686c6c868b6686666668c6a686b96db9a9a9b69b9b6a6c86a666a668666b9b9a96b96b9b96868668668666c89b69b9b9b98b86c6c66666a66a6a68a6b668b6c6686a668c66c686a6a6c68666686b66a6b666a6b686c6c6c6a6a6686a6f66c6686a66a66a666a66866c6f7ff7fef7fcfcf7fcc666cfcfc7e4e74eee669696c6a6cffc6fcf66666a6cfef7f7ccbbecf7f7ffcfefc
                    79b9b969b9b9b9b69b69b969b6c6686c666a66a6a6a66686c66a9a69696b969b9a998666c66a66b86b86bb696b9b69b96b8b86c6c6c6c866c9b9b9a9b6b68668668c6a6686666b66b9a668686c6c68c66c686c68666b86c6a6c686a666a6666866ac6f66866686a666cc6fc66a6866a668a6686c6afccfcfccf7ff7f7fcf7f66acff7fe7edb7e7fb6a96ac9668ccf6ec7f6a6666cfcffcffce47b7fffcf7cf7f
                    9b6b9bb9a96b9b9b9b9b9a9b69b86c66a6a66686666a6a666a66b66abb9b9a9b698c68c68666b666a66b69a6b969b9a9b9666c6866866a66b69b69b69b6a6c6c6c66866a6c6b9b9b966c6c6c6868666c686a6686c6a666a68686a666a66a6a6b866fcf6c66a666686cfcfcc66666a6686666a66c6ccf7f7ff7ffcffcfcf7fc666f7ffffddb9bdce6696a6f69ccf7fc7ffc666a66ccf7f7fcf94bbdf7ef7f7ffc
                    79b9b9b96b9b69a96b96b9b9bb66a6868666a66a8686668c686866b68696b96b9a66666a6a686a6666a68666a9a9a96b9b6a66a6a66a6b9b9b9a9b9b9a66686686a6c6666a6b9a96b6a666a66a6c6c866a668c6a686b68666c6668686666b666a66cfec66868a68b6cfcfcf68a666866a6a666cfbcf7fff74e7f7f7f7f6fcfc66fcfcef9ddb9b7fc6b9cfcc6ccffcf7fcf666666cf7ffe7efd9b9be47eef7cfc
                    6b9b69b69bb9b96b9b9b96b696a6686c6b666a666c6c6c666a66a66668b69a66686c8a66686b66a6a6666a686b696b9b698686686866b96b69a696b9696a66a6c6866a8c666b96b9b686a6686866866a686c66666c66a66c686a66a66a6a66a66ccfefc66cc666686fcf7fc6666a66a66666b9fccf7fcf7e4e4eefcffcf7f7f6ccfef7fdd9b79cf76c8f7fc6f6f7f7f7f7fb6a6ccffcfdbfcdd97d7b47ef7f7f
                    9b9b9b9b866b6b9b96b9a9b9a66866a6686a666a686686a6866c686a666a698a6666668686b66866686a6686666b9b69b98b6a666a689b9b9a96a96a9b66b686686c66668a69a9b96a668686c6c6a6866c668b6a68666a686a6686686666966a6cfcf7f666cc6a66ccfcffec66866a66a69a96cfcffcf74e47e47eef7fcfcfc6cfcfffc7dd9bb7fc6fcfcff6ccffcf7fcfc6666cc77e77b77d9bbb9bbb7c7e7f
                    9b96b9a66a686a96b9a96b986866a6686a666a666a6a66866a6866a686a68966a6a68b6a6b98b6a6866686b6a6a6969a9868668c666b6b6969b66866b9a66a66a66868a666b969b6a6686c6a668666c6868668666a6a666a6686a6c6a6a6a6666cf7fcfe68cf668b8f7fcf7f66a686669cc66cfef7f7ffb4e47be7fcf7e7f7fc7ef7f7f19db9bcfe6fe7f7c7f77777e77777e7777efffcfce7bb9b77cc777777
                    b9b9b666a66669b9a96b96b6b6a6686c66868686866686a66866a66668666c6b66866866b96a6966a6a66a686669a9b69c66a666a68b99a9a6986c6a969b66986c6a6668c69a9b96686a666686a6866a66a6a6a666866a6666a6666666666a6acffcf7fc66fc6666cffcf7fc666cc69a6fc66cfcfcff7f797b9b7df7e4eeefcc7befffcdd9bb977e7777777777e7e777e7e77e7ef7c7c777c7c777e7777e7c7e
                    6b9b9b9a668a6a6b669b9a99b966c666a66a66a66a66a666a66a6686a66a68969a6b6a696a966a66666a66866a9a969a66a66868666b6b969b6b6668b9a9b6b668668b866a69b6a66a6686a66666a6866c666668a66a666a66686a86a6a66696cf7fcf7f6ccfe6a6fef7ffcfc66cf966ccf6cfef7f7fcfddddb9bbff7b7df7fc7d65e77bddb9b7e7e7e7ee7e7e77e7e77e7e77ccfef7f7e77e77c77c7e77e77c
                    9b6986896b6666866a6b69b69a9b68a66866a666668666a6686686a668666a6a969669ab96b666a6a66666a666b69a6966686a66a689b69a9b96a9b696969a98b6a6666a669b98668666a668a6866c6a66868a666b668666a66a6666866a6a68fcff7fcfccf7f666f6f7fcf7f66fcf6afcfef6cffcfcfcdd9b9b9b7c7db9ec7f7cf7be7d9b97db777e7e77c7e7c77c7c777c7ef7c777777e77f7e7e77c7f7fff
                    9b9c6c6866a686a66699a96b96b666686a66686a86a6a6866a66a666a66a6666b9a9a96969a6a69669a6a666a696b9b98a66a66666a69a96b6a9969a9ab9a66686686a668b9a66a66a6666a666a6866686a6668b66b66a6b686668a66a66666ccf7ffcf7f7ffc68bc6efcf7fc6bcfc66cf7fcf7f7f774fd9ddbdb777bd9b7774747dbb7dddbb6ffe77e7c7e77c7e77e7e7c77c7ff7f7ec7c7e777c7e77effcfe
                    6986866a6866a668b9a69b9a969a98b6666a66666666666a6666668666a668a696b96b9a6969866a666666a6686a669a666a66a6a69896b9696b6b96b96b66a66a66a68666b96666a66a6866a666a6a66a66c6689a96a6666a6a6666666a66a6ffcf7fcfcfcf7c6cfef7f7ffc6fcfc6cfcffefcfff4ed77dd9b96b4b7ddbe74be749db7e79bcfecf7e777e7c77e7c77c7c7ef7f777e777e7f77c7e77c7fffcfc
                    76c66a66c668668b89b96b69a9b9686a6866a6a6a6a68a6686a6a6a6a666a669a96a66969a96a666a6a6a666a6666a666a66666666b6b96b9a99a9a9696966686686666a68686a686666a666686a66686666c86a69b696a686666a6a6a6669fcf7ffcf7f7f7ffc6cf7f7ffcfe6fef66cf7fcf7c7777db7b7cfffef74bd7e7e74eeedb947c77fcf777e7c77c7e77f7e7e77e7fc7ce7c7f7c77e7e7c7f7efcff7f
                    666a68686a66a6698b69a9b96b698b668b86666668666666a6666666668666866a966a6a96b666a9666666a6698a666a668686a689a96b9a696b9696a9a6a86a6a6a6866a66a666a66a666a6a6666a66a6a6f669b69a69866a66866666c86a6fefcf7fcfcf6cf7c6fccf7feffef6fefc7f77777477b77e77cf7fc7e747474b4e47e49b77e7e7777e7c7e7f77f7e77c7f7ff7f7e7f77e7e7f77f7e77e7fff7fff
                    6a6866c66686686b69b9696a969a6686666a6a686a6a66a66686a686a66a66a666986666a969a66689a66696a6666a6666a66a96a6969a969a96b6b96b66666666666a6666666a666a66866666a6666a666ccc9a969b66a6666a66a686cf66cffcf7ff7f7fcf7fcfef7f7f7f7fc77777747747e77e7e77e7ef77e7e7d47d7474e47eb9e77e77ec7e77e777e77e7c7f77f7c77e777ec7f777e7cff7f7ffcfffcf
                    6666c66a68b6a6a66a96a9b96b966a6a6a66666a66666a6686a666a66666a666a66a6a6696a9866a6666a6a666a66666a669896969a9696b96b969a96986a6a6a66a666a6a6a666a6686a6a6a6686a6666afcf96b9a98666a6666a66a6fc66cf7fcf7eeff7fccf7fc7f7fcf7e77e7e7477e77e774777e77e77e77ecf7c74b7bd7bd9b77c7e7c77e7c7f7ec7f7c7f77fec7f7f7f7f77f7ec7f7fcfffffffcfcfc
                    c6c86a6666866666b969b696b6b98666666a68666a66a666a666a666a6a6668666a6666a69696a666a6666666666a668666a66a6a96b6a96a96a9696a98666666866866866666a666666666666a6666a666cfc696b6698a666a6666668cfc6feff7e4e74fcf7fcfcfcf7c7e77e77e77e777e77e77e7e77e7777ecf7fef77e7edb9bb9b7e7c77e7f7e77e77e7e777ef7f77e7e7c7e7f77c7f7fffffcfcff7ffff
                    7f666686a66a689a96a969a969a66a66a6666a6a6666666a66986666666686a6a66698666a6a6666666a6a6a6a9666a66a666666669a969a9696b6a966a6a66a66a66a66a68a6666a6a6a66a6666a6666acf7fb696986666a666a66a6ccfccfc7ffd74b9f7cfcf77777f7e7c77e77e77e7e7e77e7ec7e77e7ee7f7f777e7e77ddb9bd6e7c7e7f777c7f7f7c7f7fef7c7ef7c7f7e7f7e7f77ecffcffff7fffcff
                    666a66a668666a69696b9a69a9696666998a666666a66a66986a66a6a66a6666666a96b666666a6a6a666696666a6666666a6a66a6696b696a969a969a6666666666a666666666a6666666666a666a6866cffc69a9a6a6a6666866666cf7f6fffcfd9db7cfc7777e7e747e77e77e77e77e777e7ef77e7e77e7fc7f7f7e7e7e7c7bcc7e7c77f77ec7f77e7e7f7e7f7c7f77c7f7c7f7c7f7ec7ffff7ffffffff7f
                    66c66866a6a6669a9a96a9696b6a9a68a66666a6666a66968966666666666a66a66669a9a66a66666666a6869a666a6a6a66666669a69a9696b6969a6666a6a6a6a666a6a6a6a6668a66a6a6666a666a66cf7fc6966666686a6c6a6a6cffcf7f7fcddb9b7e7e7e77e77777e77e77c77e77e7eec7e7e7f7fefc7fcf7e7c77c7e7e7fff77e7e7e7c7e7e7c7f77fcf7c7f7e7f77e7f7c7f7c7f7ff7fffcffcf7fff
                    6668b6686666a6b696b969a69a96966666a6a666a6666a66a6a6a9898a66666666a6b6969666666a66a66698666a966666666a6a669a966a9a9a9a696a666666666666666666666a66666666a6666a6668cffcf9b69a66ac668c66668fc7fcfcfe7e7cf7ec7f77e7747ee77e7e7e7e77e7ec7f77c77c7f7c7fc7f777e7e7e77c7fc7f7c7f7c7f7e7f7f7e7fc7f77f77c7f7cf7f7c7f7ef7c7ffffffff7ffffff
                    6a6668a66a66669a696a969a6969a6a6a696668666a66666666666a6666a6a6a66666a66a9a66a6666666a66a66666a666a666669a6969a96696696a666a66a686a6a66a66a66a6666a6a68666a66666a6fef7f69a66a6cf66cfc66a6ccff7f77777777e7f7e7e747e777e77e777e7e7ec7f77e77e7fcefcf7f77e7e7c7f7c7e77e77e7f77e77e7f77e7f7f7f7c7ecef7c7e7f7c7f7c77f7ffffcfcffffffcfc
                    666a666666a6a669b6969a6969a6966666866a66a666a6a6a96a6666a98666666a66669a96666666a66a666666a66666a666a66a6696a6969a69a69966666666a66666666666666a666666a6a666a6666cf7ffcc699698cf66cfc666cf7777747ee7e7fe7e77777e77e7e7e77e7e777f7f77e7c7e7fc7f77e77e7c7c77e77e7f7f7c7f77ec7f7f77ce7f7fcf7c7f7f77f7f7f7c7f7ef7f7fcfcfffff7ffcffff
                    6666a9a6a66666a69a9a6969a696a69a66a666666666666968666a96666a666a666a6a6666a6a6a6666666a6a666a6a66666666966a696a9696696a6a6a6a6666666a6a6a66a6a666a66a666666666a6ccffcf7696a666fcc6fcf69677e7e7e7e7f7fe7777e7e7e7e77e777e7cf7f7fc77e7c77eff77e7f77c7c7e77f77f7c77e77f77ec7f7c7ec7f7fcf7f7cef7c7f7c7f7c7f7cf7c7fcfffffcf7ffffff7ff
                    cc698966666a669a69696b6b96a966666666a66a9a6a66a666a9666a66666a6696666666666666666a69a66666696666989a6a686666a966a69a9696966666a66a6666666666666666666666a6a6a6666cf7fcfc6b96acfcfcc77e7e7477747ef7f7777e7e77e7777e77e7e7f7c7fc7e7c7e7ef7c7ffc77e7e7e7f7e7c7e7e7f7c7e7f7f77e7f7f77f7f7fc7f77f7e7f7f7cf7cf7e7f7f7ef7fffffffcfcffff
                    ffffc69a6a6689696a96a986c9698a6a6a66666666666666a6666a666a6696668a66a66a6a66989a6666666a698a666a66666696a98666969a6989a98989a66666a66a66a68a66a6a6a6a6a6666666a6ccffcf76c9698cf7777e7747e77e7ef7c77e7e7e77e77ee7e7e7c7cf7fef77e7f7e7f7ff7fc77f7c77f777c7f7e7f7c7e7f7c7e7cf7f77efcfcfc7f7c7f7f7f7c7f7ef7ef7f7fcfcfffcf7ffffffffcf
                    cfcffff66666a9a696a9696cc6a96666666a6a6a66a66a66666a6666666a66a696666966696a666666a66a666a666a666a66a66a696a96a9696a9669a698966a6666666666c66666666666666a6a66c66fc7fffcf9a66e77e7e77e777e7eef777e77e777e7e7e77e77c7ef7fec77e7f7ef7f7f7fc7e7f7e7f77ec7f77c7c77f7f77c7f7f77e7cf7f7f7f7f7f7f7c7f7cf7cf77f7c7fcf7ffcffffffcfcf7ffff
                    ffffcfcf66a69696a9696a6cc696a96a666666696666666a666986a66a66666686a66a66a6666a66a966666989666669898966696866696a66966b66986b6a666a6a6a6a6af6a66a666a6c6a66c666c6bfff7fcfc67b777e777e77e7e777777e7e7e7e7e77e77c77c7ef7f7f77f77c7f7f7fcfc7f7f777c77e7c7e7c7e7f7e7e7cef7e7c7f7f7f7fcf7f7c7ec7f7f7c7f7f7fc7f7f7f7f7ff7ff7ffffffffcf7
                    ff7fffff6a666a69696a966cc6b696966a698986a66a6a666a666c696666a6a696666666666a6666666a698666a66a66669a69a66a96a9696a9a96b6a9696666696666666ccc66666a666c666cf69cfc6c7ffc77e77e7e77e7e7e77e77e7e7e77e777e77e77fe7e7ef7f7fc7e77e7fef7fc7f7e77e7c7c7f7c7f7f7e7f77f7f7f777f7f7f7cef7f7f7f7f7f7f7f7ef7f7ce7cf7f7f7ffcfffffcff7fcf7fffff
                    ffffcfcfc669a96a98966a6ccc698a6a666a66a66666696666a6ac68a6a66966a66a989a66666c6a66666a6a6666696a6a69666666696a669666696966a69a9a6866a9666cfc66a66c6c6cf69cfc6cfc6ffc77e77e7777e77e777e77e7e77e7e77e7e7e7c7fcf7f7f7f7f77e7c7fc7f7f7fc7c7f77c7e7c7e7f777c7f7c7c7c7c7fc7c7e7f7f7fcfec7cec7f7cef7cf7f7fc7f7cf7ffcffcf7ffcfffffffcf7f
                    cffffffffe6696966a6a96ccfc6c9c6698966666ac6a686a6cc6ccc69669866666666a666a96ac696a66666966a986669666a9a969a6969a6b9a98a9a969666669a6666acfcf6666ac6fcfc6cfcf6cfcc777ee7e77e7e77e77e7e7e77e7e777c7e7c77c7fef7f7fc7fce7e7c7f7ff7fc7f77e777e7f7f77c7f7ece7f7e7f7f7f7f7ef7f7fcfcfcf7f7f7f7f7f7f7f7cecf7f7f7f7fcffcfffffcffcf7fffffff
                    fcf7ff7ffc6b6a6c6cc669fc7feccfb666a66a66ccc69c66ccc6c7c666c6a66a6a666666666a6cc6666a96a666666a66a9666666a696a66966666966696a69a668666a66cf7f66966fcfccf6ccfcfc7e77e7f7e7e77e7e77e77e777e777e7e77e777e77f7c7f7f7fc777c7e7f7f7fc7fc7e77e7f7c7e7ce7f77c7f77c7f7e7c7f7c77f7fcf7f7f7f7f7c7f7cce7f7f7f7c7f7fc7f7ffff7fcfff7fffffcf7fcf
                    fffffffff76c666cccccc6ccf7cf7ccc666a66ccc7e66cc6c7f7fcc66ac6c666696a96a6989ccfc66a968666a66a669666a96a9696a969a69a96a969a6696a9669a66666cffcc689cfcf7fccf7f7e777e7fe7f777e77e7e7e7e7e7e7ee77c7e7c7f7efef7fcf7fec7f7e7ef7fef7fef77e7c7677e7f7e7f77ce7f7cf7f7c7f7f7ef7fcf7f7fcf7f7c7f7f7f7f7f7cc7f7f7fc7fceffcffffff7fff7ffffffff7
                    ff7ffcffcfccec6cccf7c7c7ec7cc7e7cc6cccc7eb16bcd6eccce7fe6cccc6c6a6666666a68cc7f6666696a6696696a669669896a9666696666966a696a69666a6666a6cf7fffc6bfcf7fcf7fc777e7e7f7fc77e7e7e777e777e77e777f7e7c77e77f7f7f7f7fc77e7e7f7f7f7fc7c7e7f7e7e7c7c7c7f7ce7f77f77c7f7f7cef7cf7fcfcf7f7fcf7f7f7fcef7fc7f7f7fc7f7c7f7fffcff7fffcfffcf7ff7ff
                    cfffffffff77fcfef7f7c7e77f777b7eccf7f7e77bd7b77e777777f6cf77c7c666a66a6669ccfcccc66a6669c6a68696a66a66666669a66a9a989a96696986a6666a966cfcf7f766cfcfcf7e77e7e7efcf7c7e7e77e77e77e7e7e77f7e77e77f7e7fc7fcfcef7e7f7c7c7f7fc7f7e7f7c7e7c76e7f7f77c7f7c7f7cef7e7cef7ff7ff7f7f7fcf7c7f7fce7f7cc7fcf7fc7f7fcf7fffcffffffffffcfffffffff
                    7fcff7ff7f7e77c7f7fcf7f7e7e7e7e777fccf77e7b7b7e7e77e77ef7fcf777e777b7bcb686e6f7fc6986986c66c96a696969a9a96a6969666698966a66a96666a6666cfc7fcfc6b6fef7777e77e7f7f7777e777f77f7e7f777c7f77e7e77f77efcf7f7f7f7f7c77e7f7fcf77e7c7f77f7f7f7f7f77e7f7f7c7f7c7f7c7f7f7f7fcf7fcfcf7c7f7f7ce7f7cf7f7f7cf7ce7f7f7f7fcf7fcffcffcfff7ffcffcf
                    fcf7fffffff77e7f7f7f7f7f77f77f7c7e77f7fc77e7e77ed7e77e77f7f7f777e7e7777777777ecc5c6c6a66cc6c6a666a66666669666a69a96a966969666a69669866cff7f7fc6cf7777e7e7e77f7f77e7e7f7e77e777e77e77777e777c77e7f7f7fcf7fc77e7f7c77f7c7ec7f7e7c7e77c7c7e7ce7f7c7c7f7c7f7c7f7fcfcf7f7fcf7f7f7f7f7f7f7fc7f7f7f7f7f7fccf7fffffffffffffff7ffffffffff
                    7ffcffcffff7e777cf7fccf7fc7e77e7f7e7cf7f7e7e7e77e777e777ef7fccf77e7e7e7e7e7e77777ccc669cccccc6c6969a69a96c6b9666666989a6a69cc668986a6cccf7fcff777e7e77e777fcf777e77c7777e77e7c77e7f7e7e7c7e7e7cf7f7fc7fc77f7c77e7f7fe7f77f77f7e7f7f7f7f7f7f7c7f7f7c7f7c7f7cf7f7fcfcfcf7f7ccf7ccf7fcc7f7f7fc7f7f7f7f7fffcfcf7ffcf7fcfffffcfcf7fff
                    f7ff7fffcffc7f7e77f7f7fc7ff7f7c777f77cf7c77f77e77e7e77e777cc7f7fe777e7e77e77e7e7eb7ccccf7ccf7ccff6669866cc9869a96a98989696acf966a6c66cf7fef777e7e7e7e77f7fe7e7e7e7e77ee7c7e7e7e7c777e77c7e7c7f7fecf7ff7e7e7e7f7f7cf7c77f77ec7c7f7c7e7c7c7c7f7f7e7f7f7f7f7f7fcfcf7f7f7f7fc7f7f7f7c7f7f7fcc7fccecc7f7ffffff7fffffffff7ffcfffffffcf
                    cfcfffcfffff77e7f7cf7f7fc7fc7f7ef77e777e7f77fcffc777e77e7fefffccfef77e7e77e77e7e77e7f7f7f777fffcfc6a696cccc9666696698966a66cf66666cfcfcf7f7e7e7e77c77f77fcf77c777c7e77c77e7c77f77e7c7f77e7f7f7f7f7fcf77c7f77c77ef7f7ef7e7f7c7f77f7f7f7f7f7e7f7c7f7c7ec7f7cf7f7f7fcf7f7f7f7f7ce7fef7fcc7f7f7f7f7fcfcfcfcfcffcf7ffcfffffff7ffcffff
                    7ff7fcff7ffff77e77e7f6f7fc7fcf7f7e7f7f7f77e7777f7fe77e7e7ff7ff7f7c7fe7e7e7e7e7e7f7e77f7c7f7ffcffcf696cccccf69a6a66a69896966ccc6a98ef6cf7777e77c7c77e77fec77c7e7c77e7f77e7f77f77e7f77e7e7f77f7fec7f7f77e7f7e7f7fcf7e777c7f7c7f7c7c7c7c7e7cf7f7c7f7cf7f7f7fefcffcf7fcf7fc7f7cf7fc7f7f7f7f7fcc7f7f7f7fffff7ffcfffffff7ffcffffff7fff
                    fcfcf7ffffcffef7f7f7cecf7fc7f7f77f7c7f7ec7f7fe77f77f7f7fffffff77fcf7f7f7f7e7f7f7ef7e77e7effcffcffcf6ccccf7c666989696a6a66cfefc668cf7f77e7e7e7e77e7f7efcf7f7e77c77c777e77e7777e77e7e77c7c7fefce7f7e77e7f77e7c7fe77f7f7f7e7c7f7e7f7f7f7fcf77c7f7f7c7c7fcfcf7f7f7fcf7f7f7cf7f7f7f7f7f7f7fcf7f7fcf7f7fcf7ffffcfcfcf7ffffff7ffcffffcf
                    7fcf7fcffff7f77f7c7f7f7f7f7f7f7fc7f7f7c7f7ce7cf7ecf7e7fffcffcfe777fcf7c77f7f7e7f7ff7fc7ff7ffcff7ffc7e7c7cfcc6c6c6a669698bcf77ffe6f7e7e77e7c7c7f7e77f7f7f77e7f77e7e7e77c77e7e7e7f77c7ff7f7f7f77c77f7c7c7e7c7fcf7f7e7c7e7f7f7e7f76e7cec77c7f7f7ec7fcf7fc7fcfcfcf7fcf7f7f7cf7f7f7fcccf7f7c7f7f7f7f7f7ffff7ffff7ffffffcfcfffff7fffff
                    fcffff7f7fffff7c7f7c77f7f6fcf7fcfc7f7f7f7f7f77ef7f7fcfcffffcfff7f77f7ffcf7e7f7fcffcfffc7ffcff7ffcfff7f7f77efcc6cc696a66c6fcfccff77e77e7e7e77e777e7fcfc77e77e7e7f77f7e7e7e7c7e7c7e7f7f7fce7f7c7f7e7c7f7e7f7f7f77c7f7c7f7c7e7f7c7cf7f7f7f7f7f7cf7f77ff7ff7f7f7f7fcf7f7ccf7cecccf7f7f7fcf7fcf7f7fcccf7ffcffcfffcf7fffffffcfcfffcf7f
                    cf7f7fffcfffcffef7f7fe7c7f7c7fc7f7fcc7f7ce7fcf7ffffcfff7fcff7fffcf7ecc7f7fcf7fffcffcffff7ffcffcff7fffff7cf77f7fec6c669cfcf7e7f77e7c7e7e7c7f77f7e7fc7f7e7c7f777e7e777e77e777e7f77c7fcfc7f77c7f77c7f77c7f7cf7f7ce7f7c7f7e7f7f7cef77c7f7f7f7cec7c7fcf7fcfcfcfcfcfcf7f7fc7f7f7f7f7f7f7f7c7f7f7fcc7f7f7ffffcff7ffffffcf7fffffffcfffff
                    f7ffcf7ff7fffffffc7f7fcf7fcfc7fc7f7f7fcf7fc7f7ffcf7ff7fffffffffffffcfffcf7f7fcf7fcff7f7fffcfcff7fffcf7fffffc7fc7f7cc66fc7fcf77e7c7e7c77f777e7e7ffcff7e7f7e7e7f77c7e7c7e7f7e777e7ff7f7e77c7f77e7f77c7e7c77f7c7f7f7e7f7cf7c7ce7f7cf7f7c7cef7f7f7f7fcfcf7f7f7f7f7f7f7ccf7fcf7f7f7fccf7fcfcf7f7fcf7f7fcfcff7ffcf7fcfffffcf7fffff7ffc
                    ffcffcfcff7fcf7fffffc7f7f7c7fc7fffccf7f7f7f7ffffffffffffcf7ffcf7fffff7ffff7f7fffff7fffffcff7fcfffcfcffcfcfcffcfcf7fcfecfcf77e7c7e7e7f7e7e7f7c7fc7f7c77c77e7c77e7e7f77f77777f7cfcf7f7e7f7e7e7c7f7e7c76f7fe7c7e7c7c7f7c7e7f7f7f7c7e7cef7f7c7f7f7ff7f7f7ffcffcfcf7f7fc7f7f7f7fccf7f7fc7f7f7fcc7f7fcf7fff7fffffffff7ffcfffff7fcfffff
                    7ff7ff7f7ffcffffffcfff7f7ffff7f7ffff7fccf7fcffcf7fcfcfcffffffffffcf7fffcfcfffcfcffffcfcff7ffff7fcff7fffcf7ffcff7f7fefcf777e7f7e7f77f77e7c77e7fcff7f7e7f7e7f7e7c7f77e7e7f7f77e7f7f7e7c77c7f7c7f7e7f7c7e77f7f7f7f7f7c7f7f7f7c7c7f7f7f77f7f7f7ccf7ffcfcfc7f7f7f7fcfc7fcf7f7fc7f7f7f7f7fc7fc7f7fcf7f7fcfffffcf7fcffffff7ffcffffffcff
                    fcffcffffcf7f7ff7fff7ffcffcffffffcfffff7fc7fffffffffffff7ffcf7ffffffffff7ffcffff7ffffff7fffcfffff7fffcffffcff7ff7fcf7f7e7f7e7c7f7e77e7f77c7ffc7f7c77f77e777c7f777e7f7c7e7e7ffcf7c7c7f7f7e7f7e7e7c7c7f7f7c7e7c7e7c7f7c7f7cef7f7c7f7cf7fc7f7f7fcfc7f7f7ffcfcf7f7f7fc7f7fcc7fcf7fccf7fcf7f7fcf7f7f7fcf7ffcffffff7fcf7fffffffcfcfffc
                    f7fcf7f7fcffcfcfffcfffff7ff7fffcfff7fcff7fcfcf7ffcf7f7fffffffffcfcffcfcffcff7fcfffcf7ffffcff7fcfcffcf7f7fff7ffcfc7fc77c7f77e77e77f7e7c7c7f7f7ffcf7e77e7c7f7e77ee7f77e7e7c7fcef7c7f7e7e7c7c7e7f7f7f7e7c7c7f7f7f7f7f7fe7ce7f7f7f7f7f7cf7fcceff7f7ffcffcf7f7f7fcc7f7fcf7f7ff7f7f7f7fcf7fcfcf7f7fccfcf7fffff7ffcffffffffcfcfffff7fff
                    fff7ffffcf7ff7fcfff7fcffffcffcfffcffff7ffffffffff7ffffffcfcffcfffffffff7ff7fffffcfffffcfff7ffff7fcffffffcfcffcffcf77f7f77e7f7f7c77ef7e7f7fcfcf7f77ce7f7e7e7f7e7f77e7c7f7ffcf77c7e7c7f7c7f7f7f7c7c7f7f7f7f7c7ec7ec7e7f7f7f7c7f7f7cef7fcf7f7fcfcfcf7f7fcfcfcf7f7fcf7f7f7f7fccfcf7f7f7f7f7f7fcf7f7f7ffffcfffffffcf7ffcffff7ff7fffcf
                    7fffcf7ffcfcffcf7ffffffcfffcfff7fffcfffffcf7ffcffffcffcffff7fff7ff7ff7fffffcfcfff7fcfff7ffffcfcfff7fcfcff7fcff7f77f7e7e7f7c77e7ef777f7f7fcf7f7c7e7f77e7f7c77e777c7c7f77f7f7f7f7f7f77c7f77e7c7c7f7e7c7e7f7ef7f7f7f7f7f7cf7f7f7cec7f7c7f7fff7f7f7f7ffcf7f7f7f7fcf7f7fcfcfc7f7f7fcfcf7fc7f7f7f7fcfffcffffcfcf7fffffffffcfffffffffff
                    fcf7ffcf7ff7fcf7fc7ffcfff7fff7ffffff7fcffffffff7fcffcff7fffffcfffffffffcf7ffff7fffff7ffffcfcfffcfffff7fcffff7fffc7e7f7f7e7f7f7777fe7cf7ff7ff7c7f7e7c7f77e7f7c7f7e7f77fcfcfc7c7e777f7e77f7f7f7e7c7f7f7f7c7c7f7c7f7c7f7f7c7f7fcf7f7f7f7ffc7ffcffcffcf7fcf7f7fcc7f7fc7f7f7fcf7fc7f7f7f7ffcfcf7fff7f7ffcffffffff7ffcff7fff7ffcffcff7
                    ffcfcffcfcfff7fffffcf7ffffcfffffcf7ffffcf7ffcfffffcff7fffcfffffcffcfcfcfffcf7fffcf7fffcfffff7f7ffcf7ffff7fcfffcf7f7f7e7c7f7e7ef7e7f7fcfcfcf7e7f77f7e77c7f77e7f7e7f7ef7f7f7e7f7c7f7e7f7f7e7c7f7f7f7c7c7f7f7f7c7f7cf7ce7f7f7ce7f7f7cf7f7fcfcf7f7f7f7ff7f7fcf7f7fcf7ff7f7f7f7fcfcf7fcfc7f7f7fcfcfffffff7fcf7fffffff7ffffffffffff7ff
                    fcff7f7ff7f7ffcf7f7fff7f7ffcffcffffffcfffffff7ffcff7ffffff7fcfff7ffffff7ffffffcffffffffcf7fffffffffffcfcfff7fcffc7e7c7f7e7e7f77fcfcfcf7f7f7c7e7e77c7f7f77ec7f77c77ef7fef7f7c7e7f7e7f7c7c7f7e7c7f7e7f7f7ec7ef7f7f7ef7f7f7cf7f7cc7f7f7cfcf7f7ffcffcf7f7fc7f7fcf7f7f7fcfcfcfcf7f7f6f7f7fcf7f7f7ffcfcfcfffffffcffcfffffcfcffcf7fffff
                    cf7ffffcffffcf7ffcfc7ffcfcf7ffff7ffcfff7ffcffffff7fffcfcfffff7ffffcf7ffffcf7fcff7ffcfcfffffcffcf7fcfcf7ff7ffffcff7f7f7ef7f7f7cef7f7f7ffcf77e777c7e77e7e7f7e77ec7fcf7fcf7c7e7f7f7cc7c7f7f7ec7f7f7c7f7cec7f7f7c7f7c7f7cf7f7ec7f7fcf7cfcf7ffcfcf7f7fcfcf7ff7fc7fcfcfcf7f7f7f7fcf7f7fcfcf7fcffcffcffffffcfcfcff7ff7ffcfffff7fffffcf7
                    fffcfcff7fcf7ffcff7ffcf7ffffc7fffffff7fffff7ffcffffcfffff7fffffcffffffcfffffffcfffffff7ffcff7ffffffffffcfffcf7fcf7c7ce77f7c7f7f7fffcf7f77f77f7e77f7f7c7f7e7f7f7ef7fcf7c7f7f7c7c7f7f7f7e7f7f7c7e7f7cf7f7f7f7f7f7ef7cf7c7cf7f7fc7f7f7f7ff7f7f7ffcfc7f7fc7fcf7fc7f7f7f7fcffcf7f7fcf7f7f7fcf7f7fff7fcf7ffffff7fffffffffcf7fffffcf7ff
                    cfcff7fcff7ffcff7ffcf7ffc7f7ff7f7cc7ffcf7f7fcf7f7f7f7f7f7fcf7f7f7f7fcff7ff7ffcffcf7f7fffff7fffcfcf7fcf7ffcffffffcf7f7f7f7ef7efcfc7f7ff7f7ece7c7e7777e7f7e6f7c7f7fcf7f7f7e7c7f7f7e7c7ecf7c7c7f7f7cf7e7f7cf7c7f7f7cf7c7fc7f7f7cf7f7fcff7ffcfff7f7ff7fc7ff7f7fcfcf7fcfcf7f7f7fcf7f7fcfcfcf7ffff7fffffffcf7ffffffcfcfcffffffcff7ff7f
                    f7fcffff7ffcff7ffcf7ffcfffffcffcffff7f7fcffcf7fcfcfcf7fcfc7fcfcfcf7f7c7f7ffcff7ffffffffcfffffffffffffffcff7fcf7ff7f7c7f7c7e7f7f7ffff7c7ce7f7f77f7e7e7f7c7e7f7fcfcf7f7c7f7f7f7e7c7f7f77c7f7f7ce7f7e7f7cf7f7fe7f7f7c7fc7f7f7cf7f7f7fcf7fcf7f7fcff7fcf7fc7fcf7f7f7fc7f7ffcfcf7f7fcf7f7f7fcfcf7ffffcfcffffffcffcffffff7ffcffff7fccf7
                    ffff7fcffcff7ffcf7ffcfc7f7fcf7f7f7f7ffcf7f7f7fcf7f7f7fc7ffc7f7f7f7fcff7fcc7f7fc7f7fffcfff7ffcf7fcfcf7fff7fffcffcfc7f7f7ef7fffcffc7f7f7f7f7c7f7f7c7f7c7e7ff7fcf7f7ff7ce7e7c7e7f7f7c7fef7f7cef7f7cf7f7fcf7ce7fc7fecf7f7f7fef7f7fcefc7ffcf7ffcfcf7f7f7fcff7fcf7fcf7ffcf7f7f7ffcf7fcfcfff7f7fffffcffff7fcf7ffffff7ff7ffffffcf7fcf7fc
                    fcfffff7ff7ffcff7ffcf7ffffffcffcfcffcf7ffcfcfcf7fcfcfcff7f7fcf7f7fc7f7fcf7fcf7ff7f7c7fcfffffffffffffffcfffcff7fff7f7e7f7c7f7ffcfff7cec7f7f7f7e7f7f7c7f7f7ffcf7ffcf7c7f7f7f7f7c7cef77c7f7f77c7f7f7f7fc7f7f7f7f7c7f7f7fcc7f7f7f7fcfff7fcffcf7f7fcfcfcf7f7f7f7fcf7fc7ffcffcf7f7fcf7f7f7ffcfcffcfff7fffffffff7fffffffffcf7f7fcf7ff7f
                    ff7fcf7ffcffcf7fccf7ffcfcf7ff7ff7f7f7ff7f7f7f7ff7f7f7f7f7ff7f7fcf7ff7fc7fcf7f7f7fcff7f767c7cffcf7fcfcfffcff7fffcfc7f7f7f7ffcfff7fcf7f7f7c7f7f7f7e7f7f7cfcf7f7fcf7c7f7c7f7c7c7f7f77f7f7c7ef7f7c7c7fcf7f7c7f7f7fcf7f7f7f7f7fcccf7f7f7ff7f7fcffcf7f7f7fcf7fcff7f7fcff7f7f7f7fcf7f7fcfcfcf7f7ffff7fffcfcfcfcfffcffcffcffffcf7f7f7fcf
                    7fff7fffcfcffcfff6f6fcf7fffcffcffcffcfcffcffff7fcfcff7fcf7fcff7fcf7fcf7fc7f7fcfcf7cf7fcccf767f7ffffff7fff7fffcff7fc7f7fefcff7fffff7c7f7fef7cec7fcc7f7ff7fcfcfcf7f7f7f7f7c7f7f7e7f7c7ce7f7c7f7f7ffc7f7cf7f7f7cc7f7cccf7fcf7f7fcffcffcffcf7f7f7f7fcf7f7fcf7f7fcfcf7ffcf7fcfcf7fcfcf7f7fcfff7fcfffffffffffffcfff7fffff7f7fcfcfcfcf7
                    ffcfffcfff7f7fcf7ffeffcfcf7fcff7ff7fcf7fcf7f7ffcf7f7ffcf7fcf7fcf7fcf7ff7ffcf7f7f7f7fcf7f7fcfc7f7c77cfffcfffcff7fff7f7ccf7f7fffcfcff7f7f7c7f7f7f7f7fefcfcf7f7f7fc7f7e7f7ef7ec7f7c7cf7f7f7f7f7cffc7f7cf7cf7fccf7f7f7f7f7f7cf7ff7f7f7f7f7fffcfcf7fc7fcfcf7fcfcf7f7ff7f7ffcf7f7fcf7f7ffcf7f7ffffffcfcf7f7fcffff7fffcf7fcf7f7f7f7f7ff
                    cffcfcfcfcffffcffcff7ff7fcff7fffcfff7fff7ffcfcf7fffcfcf7fcf7fcf7fc7fc7ff7f7fcfcfcfcf7f7f67c7ff7ffff7f7c7f7ff7fffcfffff7ffffffff7ffffcf7fcf7f7f7f7fcf7f7fcffcff7f7cef7c7f7f7f7c7fc7c7f7c7f7cfef7f7f7f7f7ce7f7f7fcf7fc7fcf7fcfcffcffcffcf7f7f7ffcff7f7f7fcf7f7fffcfcfcf7f7fcfcfffffcf7ffcffcfcfffffffffff7fcffffff7f7f7ffcfcffcf7f
                    f7ff7ff7ffcf7ff7ff7ffcff7c6ffcf7fcfcfcfcfcf7f7ffccf7ff7fff7fcf7fcff7ff7fcfcf7f7f7f7fcfcefffc7fc7c7f7f7fcf7f7ffcff7fcfffcfffcfcffffcf7cf7e7f7fcecf7fcfcf7f7f7f7f7f7f7cf7e7c7cef7c7f7f7f7f7f7f7f7f7ce7f7f7fc7f7f7c7f7fcf7f7ff7f7fcf7f7f7ffcfcf7f7f7fcfcf7f7fcfc7f7f7f7fffffff7fcf7ffffcf7fffff7ff7ffcffcfffffcfcf7ffcfcf7f7f7cf7fc
                    ffcfffcff7fffcffcffcf7fcff7ffcffff7fff7fffffffcff7ffcffcfcff7ffcf7fcf7fcf7f7fcfcf7f7f7f7f7cfcf7ff7fcfc7f7fcf7c7fcfffcfcfcfffffffcff7f7f7fcf7f7f7ffcf7ffcffcf7cce7f7c7ef7f7f7f7c7f7f7cec7fcff7f7cf7fc7f7f7fc7fcf7fcf7f7fcf7ffcfcf7ffcffcf7f7fcfcfcf7f7ffcf7fcffcfcfcf7fcf7fffffffcf7fffffcf7ffffffff7ffffcfff7f7fc7f7f7fcf6c6cfcf
                    cffcfcfcffcfcf7c6cf7ffcfcffcf7fcfcfcfcfcf7fccf7fffcff7ff7fcffcf7fcf7fcf7fcfcf7f7ffcfcf7fcf7f7fcf7fc7f7fcf7f7fcf7f7cff7fff7ff7fff7fff7fcf7f7fcfcfcf7ff7f7f7f7f7f7f7f7f7c7f7f7c7f7f7cef7ffcf7cc7f7ce7f7fecf7fc7f7fc7fcf7f7ffcf7f7ffcf7fcf7fcf7f7f7f7fff7f7ffcf7f7f7f7fffcffcf7f7fffffcfcfffffffcff7ffffcfff7f7fcf7ffcfcfcf7fcf7f7f
                    f7ff7fff7fff7fffcf7ffcf7f7fcfff7ff7fcf7f6fcffcfcf7fcffcfff7fcfcff7ff7fcf7f7f7fcf7f7f7ff7f7fcf7f7fef7fcf7f7fc7f7f7f7c7ffcffffffcfffcfc7f7f7fcf7f7f7fcfcfcf7f7f7f7ce7f7f7f7cef7f7f7cf77f7f7f7f7fcef7f7f7c7f7f7fcf7fcf7fcffcf7ffcfcf7ffcf7fcf7fcf6fcfc7fcff7f7fcffcfcf7fff7ffffffcf7fffff7ffcfffffffffcfff7ff7fcf7fc7f7f7f7fcf7ffcf
                    cfcffcfffcfffcfc7fcfcf6fcff7f7ff7fff7f6c7c7f7ff7fff7fcf7fcff7ff7ffcff7fcfcfcf7fcfcfffcffffc7fcfcf7fcf7f7fc7fcf7fcf7fc7f7ffcfffff7ffffcf7fcf7ffcfffcf7f7f7f7f7ccf7f7f7cf7f7f7c7f7c7cfcfcff7f7f7c7f7fccf7f7fcf7f7fc7f7f7f7fcf7ff7fcfcf7fcf7ff7f7fcf7ffcf7ffcfcf7f7f7fff7ffcf7fcffffcf7fffffff7ff7ffcfff7ff7fcf7ff7ffcfcfcfcf7fcf7f
                    fff7ff7fff7fff7ffcfcf7ffcfcfffcffcfcfcfcfcfffcffcfcfcf7fcf7ffcffcf7fcf7f7f7fcf7f7f7cf7f7f7ff7f7f7f7f7fcf7ff7f7f7f7f7fc7f7cff7fcfffcff7fcf7ffcf7f7f7f7f7f7fccf7f7f7f7f7ec7f7f7f7fef7f7f7f7f7ccf7f7f7f7f7fc7f7fcf7ff7fcfcf7ffcf7ff7f7ff7f7f7fcff7f7fc7f7fcf7f7fcfcff7cfffffffff7fcfffffcfcf7fffffffff7ffccf7fcf7ffcf7ff7f7fcfcf7fc
                    f7fffcfcfcfcfcffcf7fffcf7ff7fcf7ff7ff7ff7fcf7f7ff7fcf7ff7ffcf7f7fffcfffcfcf7fcfcfcf7ffcfffcffcf7fcfcf7f7f7fcf7fcef7f7fcf7f7cffffcff7ffffffcf7ffcfcf7f7f7f7f7cf7cecccef7f7ce7f7c7c7fffcf7fccf7f7fc7f7f7f7ff7fc7fc7fcf7ffcfcf7ffcffcfcfcffcfcf7fcff7ffcfcf7fffcf7f7fffffcf7fcfcfff7f7fffffffffcffcf7ffc7f7fcf7ffcffcfcf6fc6f7fcff7
                    ffcfcfff7fff7fcffffcf7fffcffcfffcff7ffcffcf7fffcffcf7fcffcf7ffcfcf7f7f7f7fcf7f7f7fcf7f7f7fcf7ffcf7f7fcfcfce7fcef7fcfc7f7f7f7c77fffffffcf7ff7fcf7f7fcfccf7f7f7f7f7f7f7c7fc7fc7fef7fc7f7fc7f7ef7c7fccf7fcf7fcf7fcff7fcf7f7f7ffcf7f7fcf7f7f7f7fcf7fcfcf7f7ffcf7f7fcf7cf7ffffff7ff7fffff7fcf7fffffffffcf7ffcf7ff7fcf7ff7fc7fcffcf7ff
                    cfff7f7fff7ffff7f7ffffcf7fcf7f7fcfcfcf7f7fffccf7f7fffcf7f7ff7f7ff7ffcfcff7fcffcff7fcfcfcf7fff7fcfcfcf7f7f7ff7f7f7f7f7fcf7fcf7fc7cf7ffcfffffff7ff7f7f7f7fccf7f7fcf7f7f7f7f7f7f7cffcffc7c7f7f7cf7f7f7fc7f7fc7fcf7f7fcfcfffffcf7ffcff7fcfcfcfcf7ff7f7f7fffcf7ffcfcf7ffffffcfcffcfffcfcfffffffcfcf7f7f7ff7f7ff7fcf7ffcfffffc7f7ffcf7
                    fcfcffffcfffcfcfffcf7ffcff7ffffcf7ff7ffffc7ff7ffffc7ff7fff7ffcfcffcff7f7ffcf7f7fcf7f7f7fcf7cffcf7f7f7fcf7fcf7fcfcf7fc7f7f7c7f7fc7f7ffffcf7fcff7fcfcf7f7f7f7fec7f7f7f7f7f7f7fef7f7f7cf7f7cc7f7fcf7fc7fcfcefcf7fcfcf7f7f7f7f7ff7ff7fcf7f7f7f7fcf7fcfcfc7f7ff7f7f7ffc7ffcffff7ffcfcfffcf7ffcffffffcf7fccfcf7fcf7ffcf7fcf7f6f6fcf7ff
                    ff7fcfcff7fcfffcfcfffcf7fffcf7ffff7ffcf7fffcffcf7fffcffccffcf7f7f7fcffcfcf7fcff7fcffcff7fff7f7ffffffcf7ff7f7fcf7f7f7ff7fcf7fcf7f7fc7cfffffff7fcc7f7f7fcf7fc7fcf7f7fccf7fcef7cffcff7f7f7f7fc7f7f7f7fcf7f7f7f7fc7f7ffffcfcfffcff7ff7f7fcfcfcf7f7ff7f7fffcfcfcffcfcf7fffff7ffffcfff7ff7fffffcf7f7c7ffcf7fcfcf7ffcf7ffcf7fcc7ff7ffcf
                    7ffff7fcffff7f7fff7f7fffcf7fffc7fcfcffcfcf7fcf7ffcf7f7ff7f7fcfffcfcf7ff7f7ff7fcf7f7f7fcf7fcfcf7f7f7f7ff7fcfcf7f7fcfc7fc7f7f7f7f7f7fc777fcf7ffcf7fcf7fc7fc7fcf7f7fc7f7cf7f7fcf7ff7cf7ccf7f7fcf7fccf7f7fcf7fffcff7fcf7fcf7f7f7fcfcfcffcf7f7fcfcfcfcff7f7fcf7f7f7f7ffcfcffffcfff7fffffffcf7ff7fcfff7f7ff7ff7ffcfcff7f7ffcfffcffcf7f
                    ffcfffff7fcffffcfcfffcf7fffcf7ffffcf7ff7fffcfffcf7ffffcffcff7f7fcf7ff7ffcfcff7ffcffcfcf7fcf7fcfcfcfffcfcf7f7fcfcf7f7fcfcf7fcef7fcc7fffc7fffcf7ff7f7ffff7ff7f7f7f7fecf7ef7ff7ff7fc7f7f7cf7f7e7f7f7fcfcf7ffccf7fcff7ffcf7ffcffcf7f7f7f7ffcf7f7f7f7f7ffcfcf7fcfcfcf7f7fff7fff7fffffcf7fffffcfcf7f7fcfc7ff7ffcff7f7ffcfcf7f7f7fcf7fc
                    fcf7fcfcfff7fcff7fcfcfffcf7fffcf7ffcfcffcf7f7f7fffcf7fc7ff7ffcff7ffcffcf7fc7ff7fcf7f7fcfcf7fcf7f7f7f7ff7ffcf7f7f7fcf7f7f7fcf7fc7f7f77c7f7cfffc7fcfffcffff7fcf7fcf7f7f7f7fcffcfc7f7fc7f7f7cfcf7fcf7f7f7fcf7fff7fcff7f7ffcfcf7fcfcfcfcf7f7ffcfcffcff7fcf7ffcf7f7fcffffcfffcfffcfcffffff7f7f7f7fcf7f7ff7fcfcf7ffcfcf7fcffcfffcf7fff
                    cffff7ffcfffff7ffff7f7fcfffcfcfff7ff7fcf7ffffcfcf7fcfcff7ffcfcf7fcf7f7fcffff7ffcf7fff7fcf7ff7ffcfcfcf7ffcf7ffcf7fcf7fcf7fc7f7f7fcf7ff7fcf77ffff7fcf7fcfcfff7fcc7fcf7fcf7ff7f7f7fcf7fcf7fef7f7fc7fcf7ff7fff7fcfcf7ffcfcf7f7ffcf7f7f7fcfcf7f7fc7f7fcfcf7fc7ffffff7f7ffffcfffcffff7ffcf7fcfcf7fcf7fcf7ffcf7fffcf7f7ffcf7f7f7cfcfcf7
                    fcf7fff7fcf7fffcf7ffffff7fcf7fcfcfcfff7ffcf7ffcfcffcf7fffcf7f7ffcfcffcf7f7fcfcf7ffc7ffcf7fcff7f7f7f7ffcf7ff7f7ffc7fcf7fcf7fcf7f7f7f7cf7f7fc77ffffffffffffcfff7ff7f7f7f7fcffcf7f7f7f7f7f7f7f7f7ff7f7fcff7fcf7f7fcfcf7f7ffffcf7ffcfcf7f7fcffcfffcfcf7fcfcffffcffffcffcffff7fff7ffff7f7fcf7f7ff7ffcf7fccf7fcf7fcfffc6f7fff6c6ff7fff
                    ffcffcffffffcfcfffcfcf7ffcffff7ff7fcfcfcffcfcf7ff7f7ffccf7ffffcf7ff7f7fffcf7fcff7fffcf7ffcf7fcffcffcf7f7fcfcfcf7ff7fcf7f7fc7fcfcf7fcf7f7f7fcf77fcf7fcf7ffffcff7fccf7fcffcf7f7fcf7f7f7fccf7fcfc7fcfcf7fcfcf7fffcf7fffffcc7f7ff7f7f7ffcfcf7f7f7f7f7ffcf7f7fcfff7ffffff7fffffcfffc7fcfcf7fcff7fcf767fcf7ffcfcff7f7f6fcfcf7ff7fffcf7
                    fcfcff7fcf7ff7fcfcfffcfcff7f7ffcfff7ff7fcf7ffff7ffffcff7ffcf7fcff7ffcfcf7fffcf7ff7f7fcf7fcfcf7f7f7f7fcffcf7f7fcf7fff7ffcf7ff7f7f7fc7f7fcec7f7fc7fcffffff7ffffffc7f7fcf7f7fcfc7f7fccfc7f7fcf7ffcf7f7ffcf7fffccf7ff7f7f7fffcfcfcffcfcf7f7ffcfcfcfffcf7ffcffff7fffcf7ffffcfcfff7fff7f7f7fcf7fcf7f676cf7fcf7f7fcfffcf7ff7ffcffcf7fff
                    ff7fcffff7ffffff7fcf7fff7ffffcff7fffcfff7ffcf7ffcf7ff7ffcf7ffcf7ffcf7ff7fccf7ff7ffcff7ffcf7ffcffcfcfcf7f7ffffcf7fcfcfcf7fcf7fcf7f7fcf7f7f7f7f7f7f7cf7fcfff7fcffffffcf7f7f7f7fcf7f7f7fcfcf7fc7f7fcff7f7ff7f7ff7fcffcfcfc7ff7f7f7f7f7ffcf7f7f7f7f7f7ff7f7ff7ffffffffcffffff7f7f7cfcfcff7f7fcf7f7ccfcffcf7fffcf7fcfffcffcffcf7ffcf7
                    fffff7fcfffcf7fffffcfcfcffcfcf7ffcf7fcfcfcf7ffcffcfcffcf7ffcf7ffcf7ffcffcf7ffcffcf7fcfcf7ff7fcf7fcf7fcfcf7f7ff7fff7ff7fff7fcf7fcfcf7fcef7fcf7ccf7f7fcffcfffff7fcf7ff7fcfcf7f7f7fcf7fc7f7fcf7fcf7f7ffffcffcfcffcf7fcf7fff7ffcfcffcff7f7ffcfcfcffcff7ffcffffffcfcf7fff7fc7fcfcff7f7f7f7ffcf7ffcffcf7f7fcfccf7fffcf7ff7ff7ffcfcffff
                    cf7fffff7fcfffcf7fcfff7fcff7fffcffcff7ff7fffcff7fff7fcfffcffcfcf7ffcf7fcfff7f7f7fcff7fcff7ffcf7fcf7ff7f7ffcf7ffcfcfcffcf7fc7fc7f7f7f7f7fc7f7fc7f7f7c77fffcffffffffffff7f7fcfcfcf7fcf7fcf7f7ff7ffcfcc7fcf7fcf7f7ffcf7fcf7fcf7f7f7f7ffcfcf7f7f7f7fcfcf7f7fcfffffffffcffcff7f7f7fcfcfcff7f7f676f7f7ffcfcf7f7ffcf7fffcffcff7ff7fcf7f
                    fffcf7fcfff7fcfffff7fffff7ffcfff7ffcffcffcf7fcffcf7fff7fcf7ff7fffcf7fff7f7ffffffcf7ffcf7ffcf7ffcf7fcffcfcf7ffcff7ff7fcfcfffcf7fcf7fcf7f7fcf7f7f7fcf7fc77f7ffcfcfcfcfcfffc7f7f7f7fc7ffcf7ffcf7fcf7ffffcf7ff7ffffcf7ffcf7ff7ffcfcfcfcf7f7ffcfffcfcf7fcffffff7ff7fcf7f7f7f7fcfcf7f7f7f7fcffc7c6fcc6cf7f7ffffcf7ffcf7fcf7fcfcffffcfc
                    f7ffffffcfcfff7fcfcfcf7fffcff7fffcff7ff7ffcff7fcf7ffcfff7ffcffcf7fffcf7fffccf7f7fffcf7ffcf7ffcf7ffcf7f7f7ffcf7f7fcfff7ff7f7ffcf7fcf7fcfc7f7fcf7f7c7f7ff7fc77f7ffffffffc7ffcf7fcf7ff7f7ff7f7ffcf7fcf7f7ffcffc7f7ffcf7fcfcfcf7f7fcf7fcfff7fcf7fcf7ff7f7fcfcffffff7fcfcfcfcf7f7ffcfcfcf7f7ffc6fe67c7ffffc7f7fffcffcff7fffcff7f7ff7f
                    ffcf7fcf7ffcfcffcfff7ffcfcfcffcf7fcffcffcff7fff7ffcfcf7ffcff7ffffcf7fffcf7ff7fffc7f7ffcf7ffcf7ffcf7ffcfffc76fcffcf7fffcffcfcf7fff7fc7f7ff7f7f7fcfefcf7cf7fcf7f7c7ff7ffff7f7fcf7ff7fcfcf7fcfcf7fff7ffcfcf7f7ffff7f7ff7fcf7f7ffcf7ff7fc7ffcf7ff7ff7ffcfffffff7f7fcf7f7f7f7ffcf7f7f7f7ffcfcffeff7c6fc7f7ffffcf7fcf7fcfcf7f7ffffcffc
                    fcffffcffcff7ffcf7ffffcfff7fcffffff7ffcf7fcfcfcfcff7fffcff7ffcf7ff7fcf7fcfcffccfffffcf7ffcf7ffcf7ff76c76f7c67f7f7ffc7ff7ff7fffcfcfcfcf7f7fcf7fc7f7f7cf7f7f7f7fcf7c7ffcfffcf7f7fcfcf7f7ffcf7f7fcfcfcf7ff7fffcf7ffcfcff7f7ffcf7fcf7ffcffcf7ffcffcffcfffcf7f7fcfcf7ff7ffcfcf7fcfcffcff7fcf7f7fcf6cffffcffcfcf7ff7fffcf7ffffcf7fcf7f
                    ff7fcff7ff7ffcffffcf7ff7fffff7f7fcffcffffff7fff7fcffcf7f7ffcff7fcffffcff7ff7ff7f7f7fcffcf7ffcf7ffcfc6c6effcf6cfffcfff7ff7ffcf7fcf7ff7fcfcf7fc7fcf7f7f7f7f7f7f7c7ffc7f7fcf7ffcfcf7fcfcf7f7ffcffcf7f7ffcffcf7fcfcf7f7fcfffcf7ff7fcfcf7f7fff7fc7f7f7f7f7fcfcf7f7f7f7ff7f7f7fcf7f7f7f7ffcffffff7fff7f7ffcf7ffffcffcf7fffcf7ffcff7ffc
                    fcfff7fffcffcf7f7ffffcffcf7fffffff7ff7f7f7ffcf7fff7ff7fffcff7ffff7fcf7fffcff7ffffcff7f7fffcf7ffcf7ffefff7fcfef7f7f7f7fcfcfcfcff7ffcfff7f7fc7c67cf7fccf7fccfccf7f7cf7f7f7ffcf7f7fcf7f7ffcf7ff7f7ffffcf7f7fcff7fcffcf7f7f7f7fcff7f7f7fff7fcfcffffcfcfcf7f7f7fcfcfcfcfcfcff7f7fffcfcfcff7f7fcffcfcfffcffcfcf7ff7ffcfcf7fffcf7fffcff
                    7fcfcffcffcffffffcf7ffcffffcf7fcfcfcffffffcffffcfcfcffcfcf7ffcf7fffcffcf7f7ffcf7ff7ffffc7f7ffcf7ff7ff7fcfcf7fcfcfcfcfcf7f7ff7fffcf7f7fffcf7fc6c76f7f76c7f7f7f7fcf7fcf7fc7f7f7ff7f7fff7fcff7ffffc7f7fffcff7fcff7f7fcfcfcfcfcf7ffcffcf7fcf7ff7f7f7f7f7ffcfcfcf7f7f7f7f7f7ffcfc7f7ffcf7ffcff7fcf7fcf7f7fff7ffcffcf7ffffc7ffcfcf7fcf
                    fff7fcff7ff7fcf7ffffcff7f7ffffcf7fff7fcfcff7cfcfcff7fcf7fffcf7ffcf7fcf7ffffcffffcffcf7fffffcf7ffcff7ff7fcf7f6f7fcf7fcf7fff7ffcf7ffcffcf7ffcf7fccfcf7cccf7fcf7fc7fc7f7f7fc7f7fc7fcf7cfcf7fcfcc7fffff7f7fcffcf7ffcf7f7fcf7f7fcf7fc7f7ffcfcf7fcfcfcfcff7f7f7f7ffcfcfcfcfcf7fcfffcfcf7ffcff7fffffff7ffffc7ffcf7fcf7ff7f7ffcf7ffcff7f
                    cfffff7ffcfff7fff7fcf7ffffcf7ffffcfffff7fcf6c7ff7fffffffcf7fffcffcff7ffcfcff7fcf7fcfcfcf7fcfffcf7fcfcffcf7fcc7cf7ffcf7fccfcfcf7fcf7f7fffcf7ffcf7f7fcf7f7fc7fcf7f7fcf7fcf7fcf7fcf7fcf7f7fcf7fffcf7fcfcff7f7ffcf7fcfff7fcffcf7ffcffcfcf7f7fcf7f7f7f7f7fcfcfcf7f7fcf7fcf7ffcf7f7fcf7fcff7ffcf7f7fcfcf7fffcf7fff7fffcfffcffcfcff7fff
                    f7fcfcffcfcffffcffffffcfcffcfcf7ff7fcfcfffff7f6ffcf7f7fcfcfcf7fcf7fffcff7fcffcffff7ff7fffcf7f7fffcf7fcf7ffcfff6ff7f7ffcf7f7f7fffcf7ffccf7ffcf7fcf7c7cf7fcfc7f7fcf7f7fc7fcf7fcf7fc7f7fcf7f7fc7f7ff7ff7fcfff7f7ff7f7fcfcf7f7ff7f7f7f7f7ffcf7ff7ffcff7fcf7f7fcfcfcf7ff7ffcff7ffcf7fffcf7ffcfffcffcf7ffcf7fffcfcffcffcfcf7ff7f7ffcf7
                    fff7ffcff7fcf7ffcf7fcff7fcff7fffcfffcff7f7fffffcffffffff7ff7fff7ffcf7fcfff7fcf7f7ffcffc7ffcfffcf7fffcf7fcf7f7fcf7fffcf7ffcfffccf7ff7f7fffcf7ffcf76c667cf7f767cf7fcfcf7fc7fcf7fc7ffcf7f7fcf7ffcf7fccfcf7f7ffcfcffcf7f7f7ffcf7fcfcfcfcf7cf7fcfcf7f7ffcf7ffcf7fcf7ff7ffcf7fffcf7ffc7f7ffcff7fcf7f7ffcf7ffcf7fcf7ff7ff7fffcffffcffcf
                    fcffcff7ffffffcffcfff7ffff7ffcfcfcf7f7ffffcf7fcf7f7fcf7ffcf6ccffcffcff7fcfff7ffffcff7fffcf7fcf7ffcf7fffcfffcff7ffcf7fcfcf7f7f7f7fcfcff7f7fffcf7ffc67cf6fcfcccf7fc7f7fcff7f7fc7ff7f7fcfcf7ff7f7fcf7f7f7fcf7f7f7f7fcfcf76b7f7ff7f7f7f7f67cfcf7f7fcf7f7ffcf7ff7f7fcffcf7ff7f7fffcfffffcff7ffcfcfffcf7ffcf7fff7ffcffcffcfcf7fcff7ff7
                    ffcff7fffcf7fcf7ff7fffcf7ffcff7ff7fffffcfcffffcfffffcf6cffcf76fcf7ff7fff7f7ffcfcff7ffcfcffff7fffcfcfcf7f7f7fcffcf7ffcf7fcfcfcfffcf7f7fcfcf7ffffc7ffcfcf7f7f7ffcf7fcf7f7fcfcf7fcfcfcf7f7fcf7fcf7f7fcfcfcf7fcfcfcf7f7f76b6fcfcfcffcfcfcf6f7f7ffcf7ffcfcf7ff7ffcfcf7f7ff7ffcfc7f7f7f7fcfcfcff7fcf7fffcffcfcfcfcff7ffcff7ffffcf7ffcf
                    fcf7fffcffcfffffcffcfcfffcff7ffcfffcfcff7fcf7ffcfcf7ffc7fcff6c7fffcffcfcfffcff7f7ffcff7f7f7ffcfcf7ff7ffffffcf7f7ffcf7ff7fcf7fc7f7ffcfcf7f7fc7f7ff7fcf7fcf7ff7fffcf7fcfcf7f7ff7f7f7f7fcf7f7fcf7fcfcf7f7f7fcf7f7f7ffcffcfcf7f7f7f7f7fcf7feffcf7fffcf7f7ff7ffcf7ff7ffcfcfcfcffffcffcff7ff7f7ffcf7fcf7f7ff7fcf7fcffcff7ffcf7ffffcff7
                    fffffcff7ff7f7fcfcff7fcfcf7fffcfcfcfcf7ffffffcff7fffcfff7f7fffc6f7fcf7ff7fcf7ffffcff7ffffffcff7fffcffcf7fcf7ffffcf7ffcffcf7ffffcfc7f7fcfcfcffcf7fcf7fcf7ff7fcf7ff7fcf7f7fcf7fcfcf7ff7fcfcfcf7fcf7f7fcfcfcf7ffcff7f7f7fcf7ffcffcf7676fcfcf7fcfc7f7ffcfcfcf7fcf7ffcf7f7fcf7f7f7fcf7fffcffffcf7fffcffffcfff7fffcf7fcffcffcfc7f6f7ff
                    cf7fcf7ffcffffff7fcffff7ffffcff7ff7ffffcf7f7ff7ffcfcf7fffffcfcfffff7ffcffcfffcf7ff7ffcfcf7ff7ffcf7fcf7ffcfffcf7fcffcf7f7fffc7f7fcfffcf7f7f7f7fcfcfcff7ff7fcf7ffcfff7fcfcf7fcf7f7ff7fcf7f7f7ffcf7ffcf7f7f7ff7fc7fcffcfcf7fcf7f7f76bccf7f7ff7ffffcfcf7f7fcfcf7ffcf7ffcff7ffcfcff7ffcf7f7fcf7ffcf7fcf7ff7fcfcf7fffff7ff7ff7ffccffcf
                    fffffffcf7fcfcfcfff7fcffcfcff7ffcffcf7ffffffcfffcf7fffcc6ffcff7fcfffcff7ff7fcfcfcffcf7fcffcffcfffff7ffcff7fcfcff7f7fffcfc7fffcfcf7f7fcfffcfcf7f7f7fcffcfcfcfcf7fcfcf7f7f7fcf7fcf7fcf7ff7ffcf7f7fcf7ffcfcf7f676cf7f7f7f7ff7ffcfcfcff7ffcfcffc7f7fcf7fffcf7fffcf7ffcf7fcfcf7ff7ffcffcfffcfcfcffcff7ffcffcff7ffcf7fffcffcffcfcf7ff7
                    f7fcf7fcff6ff7ff7fffff7ff7fcffcff7ffffcf7fcff7fcfffcf7ff7c6f7fffc7fcf7ffcffcf7ff7fcffff7fcf7ff7f7fcffcf7fff7ff7ffffc7ff7ffc7fcf7ffcfcf7cf7ffcfcffff7fcf7ff7ffcff7ffffcfcfcf7fcf7fcfcf7ffc7f7fffcf7fcf7f7ffc7cf7cfcffcffcff7f7ff7fcffcf7ff7ffffff7ffccf7ff7f7fffcf7ffcf7fff7ffcff7ff7fcf7fff7ff7ffcf7fcf7ffcffffcf7fcf7fcf7fffcff
                    fffcfff7fcfcffcffcf7fcffcfff7ffcffcf7ffcffcfcfff7fcfffcff6f7fcfcf6cfffcff7ffffcfff7f7fcff7ffcffffcfcf7ffcfcfcffcf7fffcffcfffcf7fcf7f7ff7ff7f7ff7c7fff7ffcffcf7fffc7fcf7f7f7ff7ffcf7fffc7ffcfc7f7ffcf7ffcf7ffcffcf7f7f7f7fcfcfcffcf7f7ffcff7f7f7ffcff7ff7ffcfcf7fff7ff7f67cfcf7fcf7f6c7ffc7ffcffcffffcfffcff7f7ffcff7fcf6ffcfcfcf
                    cfcf7fcfcfcf7ffcffcfff7ffcfcffcf7ffffcff7ff7fcfcff7f7ff7ffccfcffff767ff7ffcf7ff7fcfffcf7ffcff7fcff7fffcff7ff7fcfcfcf7f7fc7f7fcff7ffff7ffcfcffcffffc7ffcff7ff7ff7fffcffffcff7ff7f7ff7f7ffcf7fffcfcf7ffcf7ffcff7f7ffffcffcf7ff7f7ff7fffcf7fcffcffcf7fcf7ffcfcf7ffc7ffcffc7c667fffcffccf6c6ffcf7fcf7f7ff7f7fcffffcff7fffcfcfff7fff7
                    ff7fffffcffffcff7ffcfcffcf7fcffffcf7ff7ffcfff7ff7ffffcffcfff7fc7fcffccffcffcfcffff7fcfffcff7ffcf7ffcf7fcffcfff7ffcffffffffff7fcffc7fcfcf7ff7f7f7fcffcff7ffcffcffcf7f7f7ff7fcfcfcf7fcfcfcfffcf7ff7ffcf7ffcfcf7fffcf7ff7ff7fcffcf7ffcf7fffcf7ff7fcff7fffcf7ff7fcfffcf7f7fc6cc6fcf7fcf7fc7fcf7ffffffffcfffff7fcfcf7fffcfcf7f7fff7ff
                    cfffcf7ff7f7ff7ffcf7ffcffffff7f7ffffcffcff7fffcffcf7c6fcf7fcffffffcfff7ff7ff7fcf7fffcf7ff7ffcffcfcf7fff7fcf7fcfcf7f7fccf7f7ffcf7fffcf7fcf7ffcfffcf7f7f7ffcf7ffcf7ffcfcfcffcf7f7fcfcf7fcf7f7fffcffcf7ffcff7fffcfcfcfcffcffcf7f7ffcf7ffc7f7ff7ffcf7ffc7fcff7fffcf7ff7fffcfffefcf7ff7ffcfff7ffcf7f7fcff7fcfcfff7fffcfcff7fffffcfcf6
                    fcfcfffcffffcfffcfffcff7f7f7ffffcf7ff7ff7ffcf7fcfffcfcffffcfcf7f7ff7fffcffcffffcfcf7fffcffcff7ff7fffcfcff7ffcf7fffffcf7ffffcff7fcf7fff7ffcf7fc7ffcfffcfcf7ffcf7ffcf7ff7fcf7ffcff7f7ffcf7ffcf7f7fcfffcff7ffc7fcf7f7ff7ff7ff7fffcf7ffcfffffcffcf7ffcfffcf7ffcf7fffcffcf7fcf7ff7ffcffcff7fcfcffcfffcf7fffcff7fffcfcfff7ffcc6cfff6fc
                    fff7fcff7fcf6f7ff7fff7ffffffcfcffcffcffffcffffff7fcf7f7f7ff7fffffcffcf7fcff7fcf7ffffcf7fcff7ffcffcf7fcf7ffcf7ffcf7fcfffcf7ff7fffcff7fcfcf7ffcff7f7fcff7fcfcffffcf7ffcfff7ffcf7fcfffcf7ffcf7ffcff7f7ff7ffcfffcf7fff7ffcff7ffccf7ffcf7f7f7f7fcf7fcf7f7f7ffcf7ffcf7fcffcf6fcfcf6ccf7ff7ffcff7fcfcfcfffcfcf7ffcfcff7f7fffcfcfcf7ffff
                    7fffff7fffff7fcfffcf7ffcf7fff7fcff7ffcf7ffcf7fcfff7ffffffcffcf7fcf7c6ffff7fffcffcf7ffcff7fcfcff7ffcff7ffcffcfcf7ffcf7f7fffcffcf7f7ffcf7fffcf7fcfffcf7fff7ff7f7f7ffcf7f7ffcffff7fc7f7ffcf7ffcf7fcfcf7ffcf7f7f7ffc7ffcf7f7cf7ff7fcf7ffcfcfffcf7ffcffcfffcf7ffcffcfff7ff7c76f7c7c6cfcffcf7fcfff7ff7fcfff7ffcff7fcfffffcff7fffffcf7f
                    fcf7fffcf7ffffccfcfffcffcfcfcfff7ffcffffcfffff7fcffcfcf7ff7ffcffcfcfcf7fcfcf7fcffcfcff7ffffcf7ffcf7fffcff7ff7fffcff7fffcf7fcf7ffffcf7ffc7f7ffcf7f7fcfcfcfcfcffffcf7ffcfcff7f7ffcffffcf7ff7f7ffcf7ffcf7fffcfffcfffcf7ffc6c6fcffcfcfcf7ff7fcf7ffcf7ff7fcf7ffcf7ff7fcfcf6cc6cfff6ff7fcf7ffff7fffcffff7fffcff7ffff7fcfcf7fff7fcffffc
                    ffffcfcfffcfcfff7fcf7fcffff7ff7ffcff7f7ff7f7fffff7ff7fffcffcff7ff7ff7ffcfffcfff7fff7fffcf7ffcfcf7ffcf7fcff7ffcf7f7ffcfcfcff7fffcfcfffcfffffcf7ffcff7f7ff7ff7f7fcf7fcff7fcffcfcf7f7f7fff7ffcfcf7ff7ff7fcf7fcf7f7f7fcfcffffcf7fcf7ff7ffcffcf7fcf7ff7ffcf7ffcfffcfffcf7f7c6c7fcfcfcff7ffcf7ffcfcf7fcffcf7fcfffcfcfff7ffffcffff7f7ff
                    7fcff7fcfcf7fcffff7ffff7f7ffcffcff7ffffcffffcf7fcfcffcf7fcff7ffcffcffcff7f7fcf7fcf7ff7ffcfcf7ffffcf7fff7fcfcffcfffcff7fff7ffcfcf7f7fcf7f7fcf7fcf7fcfff7ffcffcfcf7ffc7fff7f7ff7fffcffc7ffcff7fffcff7fff7ffcf7ffcffcf7f7f7f7ffcf7fcffcf7f7ffffcffcffcf7ffcff7fcf7fcffffcf7fff7ff7fcffcffcffcff7ffff7ffffff7fcf7fcfcffcfcfcf7ffffcf
                    fff7ffff7fffff7f7fffcfcfffcffcff7fffcfcfcfcffffffff7fffffcf7ffcfcff7ff7fffffcffffcfcffcff7fffc7fcfffcfcffcff7ff7fcf7ffcf7ffcfcfffffcffcffcf7ffcffcf7fcfcff7ff7fffcfffccffcfcffc7ff7fffcff7ffc7f7fcfccffcf7ffcf7fcf7fffcfffcf7fff7f7fffcfc7fcf7ff7fcffcff7ffcffff7f7fcfffcfcfcffcf7ff7ffcf7fffcf7ffcf7fcfffcffff7fcf7f6ffcfcfcffc
                    f7ffcf7fffcf7ffffcfcff7fcff7ff7fffcfcf7ff7fcf7fcf7fff7fcf7fffcff7fffcffcf7fcf7fcf7ffcff7ffcf7fff7f7ff7fcf7fcfcffcfffcff7ffcff7f7fcf7f7fcf7ffcf7fcf7ffcf7fcf7ffc7fcf7ff7f7fcf7fffcff7f7f7ffcfffffcf7ff7f7ffcf7fff7ffcf7fcf7fffcfcfffc7ff7fff7ffcffcf7ff7ffcf7f7fcfffcf7fcffff7ff7ffcffcf7ffcf7fffcff7ffcf7ff7fcfff7fcfcf7fff7fcf7
                    ffcffffcfcfffcfcff7fcffff7ffcfffcff7fffcffff7fffcffcffcfffcfcf7ffcf7fcffcff7fff7ffcf7fcfcf7ffcfffffcfff7fff7ff7ff7fcf7fffcf7ffffcffffff7ffcf7fff7ffcf7ffcfcfcfffcf7fcffffcf7fcf7f7ffcfffcf7f7f7ff7fcffcfcf7ffcf7fcf7ffcf7fcf7f7fcf7ffcffcfcfcf7f7fff7ffcf7ffffcfcf7fffff7f7ffcfffcfcffffcf7ffcfcf7ffcff7ffcffcf7ffcfcfffcfffffff
                    fcfcf7fff7fcff7fcffff7fcfffcfcf7fcffcf7fcf7fffcff7ffcff7fcff7ffffcfff7f7fcffcfcffcffff7ffffcff7fccf7fcffcfcfcffcffcf7ffcfcffcf7ff7f7fcffcf7ffcfcfcf7ffcf7ff7f7f7fffcf7f7f7fff7ffcfcfcf7fcffffffcfffcf7ff7ffcf7fffcffcf7fffcfffff7ffcff7ff7fffcfffc7ffcf7ffcf7ff7fffcf7fcfffcff7fcff7f7fcfffcff7fffcff7fffcfcf7ffcffcf7fcf7fcf7fc
                    ff7fffcfcfff7ffff7fcffff7fcff7ffff7ffffffcffcff7ffcff7ffff7fffcf7fcfcfffff7ff7fcff7f7ffcf7ff7ffcfffff7fcf7fff7ff7ff7ffcf7fcffcfcffffcf7ffffcfcf7ffcfcf7ff7ffffcfc7f7ffffcfcfcfcf7ff7fcfcf7fccf7fcf7fff7ffcf7ffcf7fcf7ffcf7fcf7fcfcff7ffcffcf7fcf7ffcf7ffcf7ffcffcf7fffff7fcf7ffff7fffff7f7ff7ffcf7fcffcfcf7fffcffcf7fffffff7fff7
                    """))
            elif tiles.tile_at_location_equals(tiles.get_tile_location(player1.tilemap_location().column, 64),
                assets.tile("""
                    myTile65
                    """)) or tiles.tile_at_location_equals(tiles.get_tile_location(player1.tilemap_location().column, 64),
                assets.tile("""
                    myTile64
                    """)):
                scene.set_background_image(img("""
                    cfc3ccc3cc8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c6c86c86c68c66c66c66c666c6666c666b66b66b66b66b66b66b66b6b6b69b6b69b69b69b69b9b69b9b9b9b9b9b9b9b9b9b9b9b9b9b9b69b9b69b69b69b69b6b69b6b6b6b6b6b6b66b6b6b6b6b6b6b6b66b6b6b6666c66b9b9ddddb9bb6b6b6b66c66c66c68c66c68c68c68c68c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c88c88f8c8c8f8c
                    3c3f8f3c33fc38f38f838f8383883838c386836c86c8c86c86c86c68c8686c868c668b8b66a66c66a66a66b66b66b69a696969b669b96b9b69b69b6b9b6b69b696b696b696b696b696b69b69b6b69b69b69b69b6b96b6b969b969b69b6b6b66b66b66b666b6a6b9b66a6ab9b6ddddd9b9bb9b9b6b66c66c68c68c66c86c86c68c68c86c6836868386838388383883838838f838f838f83f8f8f38fc838f8f6f8
                    fcfcfc3cce3cfc88c38c8c8c8c8c8c8c8c8cc8c8386c6c86c86c86c66c6c68b6c6c6c668b66c6a6b66b66b6b69a69a66b6bb6b69a66b69c9b69bb9b69b99b69bb99bb99bb99bb99bb9b9b69b9b9b69bb9b6b9a69b69b96bb69bb69b669b69a66b66b66a6b669ddd9db6b9ddb9d9d9bd9b9b6b6b6b6c6c68c66c66c86c86c8c86c86c38c8c8c83c8c8c8c8c8c8c838c8fc8c8c8c83c8c8c8c38c8f838fc83c8c8
                    3fc3c3e3c3cc3c3c8c8f8383883838838c3838c8c6c838c836c86c8c8686c68668b66a668b666666a66b69898b6b669b696b69a69b9b9a69b6b96b9b69a69bb96b69b6b96b69b6b969b69b6b69b9b69b69b96b9b69a6b69b6b69a6b6b6b668b6b6b6a66b6bb9d9ddd9db9dd9ddbdb9bbdb9b9b6b6b6a6c66c86c86c68c68686c838c86836c8c8c83838c838388c8c8c8383838fc88f838f8c8f8c8c88f8f8f8f
                    c3cfc8fc3c3cc3cc38c838c8c8c8c8c8c86c86c68c86c6c68c86c866c6c68c6c6c6866cb66ca6a6b6b66a6a6b669a6b6b69a6b69b6b669b69b69b6969a9b696b99b9b96b99b9b96b9b9b69b9b6969b69b69a96b69b69b6b9b9a69b69a69a6b66b6969b9d9b9ddd1ddd9dddddd9d9ddd9b9bd6b9b6b866c6c6c68c68c66cc6c386c68cc8c8c3868c8c8c838c8c38f838c8c8c8c83c8c8fc83883c83f8f68c83c8
                    3c3c3c3cfcc3cc3fcf838c8f838f83c838c8c838c36c8c86c86c6c686c68b668b66a6c66b9b66b6666a666696b66696b698969b6b69b9a69a9b69a9a96b9b9b9a69b69b9bb9b69b9b69b9a969bbb69a9b9a6b96b69a69b69669b66b6b6b6b6b69a6a6dddddd1d1d9dddd9d9ddddd9b9dbd6d6b6b96c6c686c68b6c66c868386c86c8686c686c836c86838c838c86c88388f838c88f38c8c8fc8f8c8c8f83c8cc
                    3fe3c3cfc3c3cfc3c3c8c8c38c86c88c8c838c868c8686c86c6868c6c86c68c66866c6a66cb6b66a6b669a6a69a6b6a69a6b6b6969a669b6969a9696b969b69b9b69b9b6969b9b9b9b69b69bb969b9b66b969b69a69b69a6bb6b9b69b696b96b66b6b91d19dd1ddd9d9dddd9b9dbd9dd9bd6db9bb66c6c6c6a6866c86c868686c86c38c838c8c8c83c8cc8c8c8c83c8c838c88fc8c8838fc838c838f6c8f8c8c
                    3ecc3c3cf3cc3cc3ccc8388c883c83c836c86c8c68c8c386c86cc66c66c6666c6a6c666a666b86a666b6a6696a69696b669b69a6b69b9a9b6b69b6b9b6b9b9a69b9b9a9b9a9b69a69b9a9b6969a96b6996b96b9b9b69b69b969a66b69a6b6b6b6b69b1d1dd1d9d9dddb9d9bddb9d9db9bd6d6b66bb668b6866c6c86c68c6c6c86c886c68c686c86c86c8838c838c8838c8c83c83838c8c838c83c8c8f83c83c6
                    f3e3cfc3cc3c3e3c3c3c8c383c8c8c86c8c8c36c86c386c86c8686c86868c6c6a666a666a666b66b6a6669a6b66a6a69a6b69a69b9a6696b9b9b69b69b9b69b9b69b6969b969b69b96969b9a9b6b9b9a69a69b66b69b6b69a6b69b9a6b969a969a6b9dd1d1dddddd9ddbdb9b9bdbdb9bb9b9b6db66a6c68b86866c68c66c868c86368c86c8c8368c8c83c8c38c83c8c83838c8c8c88f838c88c8f83c8c8c8c8c
                    3ecc3e3cf3cc3ec8fc8838c8c8c838c8c83688c86c86686c866c6c66c6c66c6668b66a666a666a66669a6b66696966966969a696b69b9b6969a9b9b9b969b69b9b69b9bb69a9b9b9a9a9b696b969a696b96b69b969a69b69696b6b69b6bb66bb69b6d1d1d9d9dd9db9d9b9dbd9b9b9bd6d6bb9b6b96c66c66c6c68c668c68c66c86c86c83686c8c386c86c868c88c838c8c8838838c38c8c3c8c8c8838383c8c
                    3f3c3cfc3cfe3e3c3c3c8c8838c8c8386c8c6c86c86c8c6c6c86c86c668b86a6c668b66a66b6a66b6a66b66bb6a6bb6a9a6b69b69a66b69ab696696b69a9b9b69b9b9a969b9b69b696b69bb96b9b96b9b69b9a69a69b69abb69a96b6b696b969a6b9dd1d1ddd9ddddbdd9bd9bddb9bb9bdb96b6b6bb9b686c68c668c6c686c8686c868368c8c8686c838c86c836c8c8c883c8c8f8c8c83c8c83c83c8c8c8c83c
                    cfc3e3e3cc3cc3c6c8c8c83c8c386c8c838c86c836c86c8686c866c86c66c6686a6668b666a666b669a669a6696b696b669696b6969b9b6969b9a9b9b69b69b969a6969b9b69b9b9b99b696b9b69a969b9a669b69b6b6b699b96b9b69b69a6b6b96b19d1d9dddb9d9d9bddbd9b9bb79b6d6bb6bb6b6bbb6c68b86c66868c66c86c86c86c86c68c8c86c86c838c883838c8c838c83838c8c838c8c8838fc83c8c
                    3f3fef3fcfe37ccc38c38c8c8c8c838c6c68c8368c86c6c86c66c66686c66a6b66ca6b66a666b669a666b669a6b698969a6bb69a6b96b69a9b69b6969b9b9a9b9a99b9b69b9b6969a6b9b9b969a69b6b6969b69a69b969b1d1db6b69a6b69b9b6b6d1d1ddd9d9ddddbd9b9b9bd6d6b6bd6b6bd6b9b696b66c666c68c6c66c86c86c86c86c8836c36c86c838c8c8c8c8c388c8838c8c838c8c8c38c3c8c3c8c6c
                    ffec3cfc3c3ec3c38c8c838c38c38c6c88c686c8686c8686c86c86c6c68a66868b6666866b6a66a666b69a66696a6b6a69b69a6969a69b69b69a9b6b9a696969696b69b9a969b9a96969b69a9b969b99a69a9b69b66b9a911d9b69a69b9a6b69b69dd1d9dddbd9d9d9dddddb9bd6d9b6b6d6d6b6b6bbb9bb68c686c6868c6686c68368686c68c86886838c686836c8388c38c8c8c838c838c388c8c888c8c6c8
                    3cf3ec3cff3e3e7cc3c8c8c88c86c8c86c83c86c8c686c6c66c66c686c666c6a666a6a6b6666b66b6a6b669a6a6969a96b69696b9a96b9b69b6969b969b9b6b9a9b9b9b69b9a969b9b9b9b696b69a6b69b6969b69b96b9d1d1d9b69b66b969a6b6bd1d1d9d9dddbddd9d96dd6d6d6bb6d6b6b6b6b6b6b6b9c66c6c68b6c68c6c686c8c6c838686c86c8c68c8c6c886c8c8c83c838c8c8c8c8c8c3883c38c6c8c
                    f3cc3cce3ec3e7e7cc38c386c6c8c86c83686c86c6c6c868c868686c66a68b666c666666a6a6698696669a6696b6a666969a6b6966b9669a69b6b96b9b69b9b96b969b9b96b96b9b69b6969a969b969b69b6b69a66b69d1d11d9b6b6b9b9bb6b9b9d91ddddd9d9d9dbdbdb9b9bd6d6bb6b9b6b6b6b6b6b6b9b6a6866868668686c686c86c86c8c86c386c836c883c8c6836c88c8c38c38c38838c8c8c8c838c6
                    fb3cfe7b7c3ee77e7ccc3c3e3c836c8368c8686c868c66c666c6c6c68b6666a6a6a6a6a666698a6b6a9a66b6a6969b9a6b669b9a69b69a69b699b69b69b969b69b9b6969a969b9b9b69b9a96b9b69b69b69b9a69699b1d1111dd9b99b9dd9d9bb9bdd1d19dbdbddd9d9d9bb9b79bbb96bb6bb9b6b6b6b9b9b9b66c6c6c6c6c6c6c86c6c866c8636c86c86c86c6c6c838c8c86c3868c8c88c8c8c83c838c8c6cc
                    3cf3e7b7c3e77cbe7b7c6c6c6c6c86c8c86c8c866c686c86c6866c66c68b86666666666b6b6a66698666b6696b6a666969a966b69a96b9b69b6b9b99a969a969b969b9a969b9b6969b969b69b69b69b969a6969b9a9d11d1d111d9dd1d1d1dd9dd91d1ddd9d9d9d9dddbdd6b9bb6b6bbd6b6b6b6b6b9b6b6b9b9c68a6868686c86c68686c86c8688c686c66c6c86c86c68c8388cc83863863838c88c8c3c838c
                    fcc3e6b3ec3e7e7b7e7c6c8c83c868c686c8636c86c6866c86c6c68a6666a6a6a6a6a6b66666b6a6b69a69a6b6969a96a696b969b69b6969b9969a69b69a9b9a9b9a969b9b69b9b9a9b9a9b969a9b969a969b696b61d111d19d1dddd1d1d9ddd9d1d19d9dddddd9db9d96ddbd6db9b766b9b6bb6bb6b6b9b9b9b98666c6c6c66c86c6c6c66866c6c66c66c6666c86c88c8368c6838c8c8c8c8c83c83c88c8c86
                    f7ec3ccf3c3cc7b7b7b3c8386c68c83868368c86c86c6c866c668b666a6866666666666a6a6989669a666669698b66b696b69a6969a969a69a6b969a9b969b6969b96b9b69b969a9696b969b9b969a69b69a9b69b9d1d1d1d11d9d11d1d1d191ddd9ddddb9d9d9dbddbbd6d6db96b6b9bbbdd6db9b9bdbb9bbd9b6a686a686c866c686868c6c86c66c6b6b6c8c6c86c3686c8c8c86c838c838c88c8c83c836c8
                    3b3e3c3efcc3ec7b6bdb6c8c68c86c86c86c66c866c6866c668c668c66c6b6a6a6a6b666698b66a666b69a6a6a969b69a69a69b69a69a69b6996b9b6969b69b9b69b9b969b9b9b96b9b969a696b969b69b6969a69b1111191d1d1d1d91d1ddddd9ddd9d9dd9dbdb9d9d9bd6d6d6bdb9bd99d9d9bd9dd99dd9d6db66c6c66c666c686c6c66c86c666c6b686c6c86868868c8c86c86c8c868c8c6c3838c8c8c8c8
                    ce3ccfc3f3fc3c3cbd6d6c68c38686c86c86c866c68c6c668c66c6a66a66a66666666a69a666a669a6698696966b669669696b69a6969b69b6b9b69b9b9b9b9b9b969b9b9b69a969b969a969b96b9a9b69b69a96b1d1d1d1d1d1d1d1d1d9d9d9ddd9dbdb9dbd9d9dbb9bb9bdb9bb9bd9ddddddd9dd1ddd9dd9d9b686a6686a68686c686c86668c6b6b68c68686c83c6c86836836c838c83868388c8c838683c3
                    c3c3e3cfe3fc3ec3b7dbd6c6868c386c86c6b6c66bb9b6bc66c6a666866a66a6a6a6b66a66a669a669a6b6b6a6969a69a6b6969a969b69b699a69b969a69b6969b9a969a969b96b9b9a969b96b9b6969b69b696d911d11d1d1d1d9d1dd1dddddd9db9d9dbd9dbdbd9bb9bb9b9bb79bddd9d9d9dd1d9d9d1d9db9b6a668b686c6c6c66c666c8c66b6b6c66c6c6c86868838c8c88c8c86c8cc8c8c86c86c83c88c
                    3cc3ee3c3ef3b7b7bc7b9b6c6c868686c6b9d9bdd9d91d9dbb6b668b6a6666666666698666696666b66969696b6a69a6969a9a696b69b69b6969b69a969b9b9a969b6b969b9b99b96969b69b9b69b9b69b69b69b1d111d11d1d9d1dd9dd9dd9ddb9db9b9d9bd9b9bdd6d79bbb9b9b9b9dd1d1d1d9dddd1d9dd9b9866c668b66a66a6868c6666c66b686c868686c6c86c86686c6836c8368386c86c838c8c8c88
                    fe3e3e7ef3eee7e7e7cc7bb6c6c6c6c66b6ddd191d11d11d91d98b66666a6a6a6b6a6a6b69a6a69a698b6a6a69696696b966969b69b69b69a9b69b969b969b69b9a999b9b9b9a9b9b9b9b9b6969a969b69b969a9d11d11d1d1d1dd1dd1dd9dd9b9bd9bdb9bd6d9b96db9bb9b9bdbdd9d1d9ddd9dd9d9d9dbdbdbb6a66a6686868668b6686c8686c68b86c6c6c8686c86c8c838c868c86c86c838c8c8c838c3cc
                    3c7e3ec3e3e37ec7b3b7c3b7d6c6b6b6b6d6d9ddddd1d1d1111d9b6a6a66666666666666a6666b666b6966969a6b9a696a9b69a69b9b69b6969b969b9b9b999b9b96b9b9b9b969b969a969b9a9b969a99a96b9b9d111d11d19d1d1d9d9dddddbdbd6bd6dbd6dbbdbb9bd9bd9b9b979dddddd9dd9dddddd9d9b9b6668668b6c6c6c6686c6c6c6c686c686868686c8c68386868686c868c8c8c86c83868c8c8888
                    3ec7e3bc3e3e7c7e7b7bb7c7b9b9b6bbb9bb9bb9d9d91d1d1d1dd666666a6a6b6a69a69669a6969a66989a6b669669b69669a6969669b69b69a96b9b69b9a69b99b99b9b9b9b9b9b9b96b9696969a96b69b9b96dd1d11d11d1d1d9dddd1d9d9d9b9bd6d69bd6d6d6db9bb9bddd9dddd9d9d9b9bd9b9d9ddb9b9b6a6b6c66a66a68c6c68b866a66c686c6c6c6c68686c86c86c86c838c68386c886cc838683c3c
                    c3cccc3fe3e7c7c3e7e3bb7bdbd6bd69b6b9b9bd9dddd9d1d1911da6a666666666a666a6a666a6669a6b66969a69a696a9b6969b69a969a96969b969b9699b99b99b9b969b99b969b699b9b9b9a96b99b96969b9d11d11d1d1d1d1d1d1ddddd9bdb9b9bbb6b9b9bd6d79dd9b9ddd9ddd9bbdbd6bd9dbd9b9b9b9b666a66a668666a66a666a668686c686868686c6c86686c836c86c868c68c83c8838cc8c888c
                    3ec3c3c3e3ece3ee3e3e7cb7c79b6b6b6bb6bd9bdb9ddd1d91d119d666a6a6a6a6669866696969a666969a6b696b696966969a69b6969a969a9b69a9b9b9b9b9b9b9b9b9b9b969b99b9a969a969b99b69b9a9b6b1d11d111d1d1d1d9d9d9d9dbd6db7b9bd6d6bb6d6db9bdd9bd9dd9d9dd9b9bd9bd9d9ddb9b6b9b9866a666a6c66686686686c6a686c68b6c868686c8c836886c86c838c86c86c86c8683c6c8
                    3c3fc3ef3e3e6e3ec7e3e7bc7b6b6b9bb9b9b9b9b9b9d9ddd1d1d1d6a666669669a6a69a66a6a669a66a669698969a6b9a69a96969a9b69b969b9b969b9b9b9b9b9b969b969b9b9a96969b969b9b9b99b6969b99d1d11d1d191d19dddd1dddd9bdd69bb6d6bd6db9b9bd9bdb9dd9dddd9bb9b6b9b9dddb9db6d6b9b6c6668b666a6a66c6a6c66866c68b68686c6c6c86668c6c868c686686868c86c8c38c8838
                    e3e3efe3e3e3c3e3ec7c3b7c7b6b9b6b6b6bdb9bdd9bdd9d9d1d19d666b9bd9da666666696696698969696a69a69669669b6969a9b696969a9b6969b9b69b9b99b99b9b9b9b9b9b96b9b9b9b9b969b69b9b9b9b9111d11191dd1dd1d1dd9d9dd9b9bbd6d6bd6b9bbbb9bd96db9bd9d9bb9bb79bb9db9d9db9b6b9b66a66a666a66666c66686a6c6a6a686c6c686c866c8c6686c86838c8c38c386c83868c6c8c
                    34e3c3cfc3e3e3e73ec3ee7c7b6b6bb6b6d69bd6d6db9ddddd9ddddbd6b911d19b69a69a6a6b69a66b69a696b69a69a9b696b69669b69a96969b9b9b699b969b9b9a9b969b696969b9b9b69b9b9b969a969a69b1d1d11d1d1d1d1d9d9d1dddddb9bd6b9b6b6d6b796d6d6dd9bd9dbdb9bb9b9b9bb9bb9bb6b6b9b6b666a66a666a6a66a6a6666a66666686868b866868668c686c6c686c686868c868c8c88386
                    c3e7cf3e3e3e3ee3e7ee3c3bcb6bb6b9b6bbb9b9bd9bd9d9ddddd7b7d11d1d1d19a66b666966986969a6696969696966969a96b9b69b969a9b6969a99b9b9b9b9b969b9b999a9b9b9b9699a969b69b969b969b911d11d1d1d1d19ddd1dd19d9ddb9b9b6bd6d6db9bbdb9bddb9bd6d9bdd6bd6bb6d6d9bd9b9b6b6b6b6a6666b6b666a6666a6c66a6ba6c6a6c6668c6c6c868c6c8c86c868c8c6c68c86c6386c8
                    3e3e7ec3e3ec3e7cc3c7c3e73bbc7b6b6b96bbd6d6bd9bb7bc7d9dddbd91d1d9d196b669a69a6b6b66696b6a69a6b69a69a6996969a69a96b969a969b6969b9b969b99b69a969b9b969a9b969b9b9b9b9b69dd1d11d111d1d1ddd1d1d9ddddd9b9bb7bd6bd6b9b6b96db9b9b9b9bd6d6b9b6d6d6bd6bb6b6b6b9b69a666b9b696a666b6a6666a9d19d9b666868c6686866c668866c86c866c6886c3688c8c8c6
                    c3e3c3ce3ef3ecc6cc3e7e3cc37bc7cbb6bb76bdbd9bb7be73bdb77cd9dd9d9dd9db698b666696969a69a6969a6969a969696a9a9696969b969b969b99a9b969b9b9b699b9b9b969b9b969b9b6969a69b9b9d111d111d1d1d191d1d9dd1d9ddddd9b9bd6dd9bbdbd6bd6d9b9bd79bd6db79b9bb9b6d6d6b9b6b6bb669b9a69a6b69a66666a6b9d9ddd9bbb6b6c68c6c68c68c6c868686c8386c8388c6868688c
                    3ecc3e3e3ee3e33c3c3c3cc3cec77c77c7b7c7c7b6b7ce73eed7b7e7bdd9ddb9dd998b669a96a6a66966969a6969a6969a69b6969a9b9b6969a9b9b969b969b9b9b99b9a969b99b96969b9699b9b99b9b9bd9d1d11d1d19d1dd1d9dd1dd1d9d9d7ddb9b9b9b9b69bb9b9bdbd9bdb9bd69bbbb96bb9b6b9b6b6b96b6bb6b6b69b6b66b6a666b9dd1dd9d99b6986c6686866866866c6c68668686c8668c838c638
                    c3e3ee3e3e3e3e3e3e3ec3ee33ec3be7c3e7e3b7b7c7c3e7b7bbbb7b777bd9dd9bd9b69666696969a69a696696b6969a696969b696969b9b9b969b96b969b9b9699a9699b9b969a9b9a969bb9b9d9b9b9b9d1111d11d1d1d11d1d1d1d19ddddd9b9b9b9b9bb79bb6d6bd6d9b79b9b79bb9b96bbd6b6b9b6b6b6bb69a696b9b6b66b6666b6bd1d1d9dd9bb6bbb66a68b6c6c68c68686c86c8c6c86c8686c68c86
                    fc3e3e3e3e3e3ec3e3e3ec3ecc3ec3c3ee7c7e7c7c7c3b7b7b7bbdbd7b7b7b9b9d9b698b69a6a69896b69a69a969696969b69a969a9b696969b969b99b9b9b9b9a969b9b969b9b969b9b9b969ddddd9d9d1d1d1d1d111d1d1d1d1d1d9ddd19ddd9bd79bdb9b9b6d6bdd6db9b9bd6d9bb9bd6dd66b6bb6b6b6b6b6b6b6bb6b6b9b698b698b9d1d9dd9db9b666b66686686868b66c6c86c866c86686c86c8c86c8
                    3ee7e3e3e3e3e3e3ee3e3e3c3e37ee3e3e3ec3e7ec7ce7e7ec7779d9bbbbd6bdb9b9b696986969896b696696669a69a69a9b6969b969b69a969a9b69a969b969b96d9b969b9b969b9699b9b9bd1911ddd9d911d111d1d1d1d19d1d9d1dd9dd9d9bd9bb9b9b7b9b6d6d6d9b9bd9bd6b9bb96d6b9b6b6b6bb6b6b6b6b6b6b6b69c9a6b6a6b9dd9dd9dd9bb6bb6b9a6c68b8b668686866866c86c8c686c86868386
                    c3cc7fcfcc3ee3ee3ce3be3e3cfc3ec7be73e7e3e3e3e3ee7e7bbb9bd9d9bd9b9b9698b6a96b6b6b69669a69b969b696966969a969a969b9b969699b969b9b9b969b969b9b969b9b9ddd9d9b91d1d19d1d1d1d11d11d191d1d1d1d1dd1dd1dddbd6db9bd79b9b6bbd6d6bd6d6dd6db9bd6db9b6bb6d6b69b6b6b6b69a69a6b6b69b6969ad9dd9ddd9db6b66a6a668b6668686c68c6c6c86c8668c6c86c83686c
                    3ec3fc3f3ff3ee3e3e3e3ee3c3cf3f3e3ec3e3e3e3e3e7e737e3b7d7d7d67bdb9b9a6696669669696a96b69669a6969a9b9b969b6969b9696b9a9b69b9b969b69b9b9b9b9b9b9b969d9d9d9dd91d1d1d9d91d11d1d11d1d19d1d19d1d9d9d9d9ddd6db79b9b6bd6d6b9b9bddb9b9b9bd6db9bb6b6b6b6b6b6b6b6b6a6b66b6b6b6b6a9b9dd1db9d9b9b6b6b666b668686c6c68666868668668c66c86c6c86c88
                    ff3cfffcfccf3e3ee3e347c3fe3efcfec3e3ecfece3e3e7cec7c7b9c6b3e7c9b96b696a69a69a69896696969a6969a966969a969b9b69a9a96969b9b699b9b99b99b99b9b969b9b9ddd9d9dd1d19d1911dd1d1d119d1d1dd1d19ddd1dddddddd6d6d9b9bbb9b6b6b96bd6d69b79bd6d6d6d6b9b6d6b6b6b6b6b66b66b6b6b6b69a69b9d1dd9b9bbdd9b9a6b6bb6a66a686a66a6c68b8c86c86b9b66c868686c6
                    f7cc3cf3ff3ecff3e7ee3e3eefcf3f3c3c3fc3e37cc3ecc3b7c7bd6bc3e3e77b6d66b696696696a969a69a6969696969b69669a96969b96969b9b9699a9999a969b9b9b99b9b9d1d9d9db9d1d1d1d1d1d19d191d1d1d1d1d1ddd1d9d9d9d9d9dd9bd6bb96bb9b9b6bbd6b9bb9bb9bd6d9b9bb6b6b6b9b6b6b66a6b6b6b6b6b6a66b9ddd9d9db9b99b9b66b6b66b66a66c6686686a66666c66b9ddd96c6c8c868
                    fff3f3cffcff3cfefc3e7c3c3c3cfecffcfefc3ef3ef3c3e7c7c7bb97e7e7c76b69696a96a69a696a696696b69a69a6969a9b969b9a969b9b9b969b9b9d1dd99b9b99b9b9b9dd9d9d9d9dd9d9d9d9d19dd1d1d1d11d19d19d19dddddd1ddddd9bdd6d9bb9bd6b6bd6d6d6b9bd9b9b9b9bb9b9b9b6b6b6b6b6b6b66a6b66c66b6b6bb69dd9db6b6b9bbb6b6a6b6b6b6866a668b68668c6866bddd9dbb68666c86
                    f3ffcffe3f3ecf3f3fe3ce3feffc3c3c3e3c3fcfcf3cfc3cfcccc66bcc67c7b69b69896696966966969a96969a9696969b6969b696969b696969a969d1d1d9b9b99b99b99d9dd1dddddd9ddd1d1dd9dd9d9dd9d1d11d1d1d1dd19d19dd9d9ddd9b9bd6d6bd6bd6d6b69b9bb9b79bd6db9bb79b6b6d6b6b66b66b6b6b6c6b6a6b6b66bb9bb9b9b6bb9b6b6b66b66986b6b68b68668c6686cb9d9ddd69b6c8c66c
                    ffcff3c3fcff3cfcf3fc3eee3f3fffcfcfffcff3ffff3ffcf3c3bb79b7bc7b7b6b6a6b69a6b69a69a69669a9669b69b9a969b6969a9b969b9a9b969dd19d1d1d9d9b9b9b9dd9d9d9d91dd9d19d9ddd9dddd9d1d19d1d1d1d9d1dd1dd1dddd9b9bdd9b9bd696d6b69bb6bb9b79bb9b9b9b9b9b6b9b6b6b6b66a6b6c66b6a6b666b6b6b6b9b9c6b6b6b6b6a6b6b6a6b69a66668b86b6c6c6b9dddd9dbb9c668c86
                    3f3fcfcfcf3fcf3c3e3fc3c7cecfcfff3fcff3ffcf3fcfcf3fc73b6b969bc7eb969696989696b69696b9b6969b6969b99b919d9b96969b969969b9bd1d19d191d9b9b99b99d9d9dd1dd91d1dd1d9d9dd9d9ddd91d119d19dd1d9d9d9d9d9dddd9b9b9b6d6bb69b6b6d9b9b9b9b9bdb9bb79b6d6b6b6b6b6b6b66b6b6c66b6cb68b6b6b69bb6b6b9b6b666b6a66b6b6b69a6a666a9b96a9ddddddd9b9b6b6666b
                    bcf3e7c3fecff3fefcccfcf3e3c3cf3fcfffffffffcff3fc3cfc7cb6bbb97b777bb669a669a6969a6966969a6969b991d11111d9b9b969b9a9b9699d19d1d9dddd9d9dd9db9b9d99d91dd1d9d9dd9d9d9ddd9d1d1d1d1dd1dd1dd1dddddd9d9bd9bbd79bd6d6bb9b6b6b9bb9bd9b9bdd9b9bb9b6b6b6b66b6b6b6b6c6b66c66b6b6b69ab69b6b6b6b6bb66b6b6b6b69a6b696a6d9bb9bd9d9d9ddb9bd96bc6b6
                    3cce3fcfe3c3cfe3c3e3efcff3fe3fcfff3ffcfcff3fee3ef3e3c3ccc6d6d6be7b79b669b6969a6969a969a969b69dd1d1d1d11d9b969a969699b9d11d19ddd9d91d111d1d9d9b9d9dd19d91d9d9ddd9d9ddd1d1d1d1d1d19d1d1d9d19d9ddd9bd9d9bb9b9b96b6b9b9b79bd9bd9b96d6b9b6b6d6b96b6a6b6c6b6a6b6cb6a66c6b6a669b6b6b6b6b666a666c66a6b6b66b6b69bd9dd9dddbdb9b9bd6bb6b66a
                    fc7fccf3fffff3fccfecf3ffffcfecfffffffff3ffff3e7e3efcfc3f3cc79b7e7b7b6969696a696696969a69699b99b11d19dd11d9b9b969b9b991d19d9d9d9d9dd9dd9d91d9d9dbd9d9dddd9d9d9d9ddd9d9dd91d191d1d1d19d1d1ddddd9bd9db9b9bb6b6bb9b6b6b9b9b9b9bd9bd9d9b9b9b6b6b6b6b6b6b66b66b66a66b6b6b66bb6b6b6b6b6b6a6b6b6a6b669b6b6b66b6b6d9b1d9d9b9b9bd6b66b6b6b
                    3fc3c3fff3e3ec3f3e3cfff3fffcffff3ffcf3ffffcfff3e7e33c3efff6bbb77b7e7b9a9a696969b69a696969a6969b9d9dd9d9d199b969b969bd1d1dddd9d9dd9dd9dd1d9ddd999d9ddd9d9d9bdddd9d9dd1d1d1d1d191d11d11d1d9d9d9d9dd9bd9b9d9b9b6bd6d9bd6d9bdb9bd9bd6bb6b6b9b9b6b6b66b6b6b6b6a66b66c6b6b6b6b6b6b6b6b6a6b6c6c6b6bb69a696a6b69b9bddddb9bb6bd6b6b6b6bb6
                    cfffcfc3cfcf3fee3e3e3fcffffff3fffffffffffff3ffcf3ee3fe3cc3e3c7b74d6bb99699b9b969a969b69b6969a99b9b99d9dd1d99b9b99b99d1d9d99d9bd9d9d9d9d9dd9dddd9b99d9d9d9b99d9d9dddd11d1191d1d11d11d119dd1ddddd9bd9b9db79b6d696b6b69b9bd69b9b9b9d9b9b9b6b6b6b6b6b6b6b6b66b6b6b6b6b6b69b6b6b6b66a6666c6a66b69bb66b6a669bb9dd9d9d9b9b9b6b6b6b6b6bb
                    f3cf3f3fff3fee3cec3fcffffcf3fffffcffffcf3fcfcfcfe33cfcfffcfc3c7b9d97dbd9b9b969a9696969699b969b9b99b9b9d9ddddd9d9b9b91d9d9dd9d9b9d9dd9d9d9dd919d99bd9d9db9d9bd9dd9d11d11d1d11d1d11911d1d19d9d9d9b9dd9b9d9bb9bbb9b9b9bbd69bd9b9b9bbd6d6b9b6b6b9b6b6b6b6b6a6b6b66c6b6b6b6b6b66a6b66b6b6b66b66a69b9a666bbb9dd9ddddbdb6b6b6b6b6b6bb96
                    cffffcfe3cfc3bc76c3ffff3fffffffcffffcfffcfffff3c3befff3c3f3ce7bdd9dd9d9d9b991b9d9b9a9b696969b6969b99b99d9d9d1d1d19dd1ddd9d9bd9d9dd9dd9dd9dd1dd11d9b9db99b9b9d9bdd1d11d191d1d111d1d1d19ddddddd9bddd7dd79b9b696d6b6b6d69bd9bd6db7969b9bd6d9b9b66b96b6b66b66b66b6a69a69a6b66a66b6a66a668b66a6cc8c66bb6969d9bdb9d9d9bb6b6b6b6b6a6b6b
                    e3cf3fcffc3fe3c3cfcfcffffffffcfffffff3fff3ff3fcffc7f3ffcc3c7bdd9d9d11d9d99ddd19d6969699a69a969b96969b9b9d9d9d919d1d9d9d9ddd9b9db9d9d9d9dd9d9d9ddd9d999bd9d9d9b9d111d11d1d111d111d111d1d19d9d9dd9b99b9b9b9bdb9b69b9b9bb96b9b9b9b9bb9b69b6b6b6b9b6b6b6b6b6b6b6a66b66b66b6a6b6b666b66bc6b6c6b8c38c696abbdbd9d9bdbb6b6b6b6b6b6b6b6b6
                    e3cff3c3efee3cfc3ff3ffcffffcffffff3fffcfffcfff3fcfeccf3ffcfcc79d9d19d1d1dd91dd199a969a696969b6969a969b9b9d9b9d91d191d1d9d9d9db9dd9dbddd9dd9dd1dd1d9bd99d9b9b99d9d1d119111d111d1d1d1d1d1dd1d9dddd9db9d9bdb96d6b9b6b6b9bb9b6dd6d6b9bb9bb9b9b9b9b6b9b69a69b6b6b6b6bb6bb6b66b666cb68b66b66cc6c38cc8cbc9d9d9dbbbd9b9b6b6b6b6c6c66c6b6
                    c3e3cfce3e3c3e3cfe3ffffff3ffffff3ffcfff3fcf3fcff3c33c3ec3e3c3cd9b9d19d9d9ddd19d9b969d9699a96969b969b9699b9b99b91d1ddd9d9d9bd9d9b9d9d9d9d9dd9d9d9d9b9bd9d9d9d9bd11d11d1d1d1d1d111911d19d9d9dd9d9dd9ddbd9b9b9b9b6b9b9b69b6d96d9b9b9b9b96b9b9b9b9b9b6b69b6b6b66b6b66b66b6b66b6c66a6b6c6cb6cccc8383c6c6bd9d9b9b9b6b6b6b6c6c6b6c8b68b
                    3e3ef3ffc3e3efef3cffcff3ffffff3ffffff3ffffffcf3ffcfc3cf3e7c7cfbd9dd1d1d1d9d1d1d9b991d19a6969b969dd9b9b699b9b9d91d191dd9d9d9b9b9d9dd9d9d9d9ddd9d9d9d99b9bd9d9d91d11d1111d111119d1d1d1d1dd9dd9dd9b9bd99b9b9bb9b9b9b6b9bd6d6bd6b9b9b9b6db9bd9b9b9b6b9b6b6b6b6b6b66b6b9b6b6b6c6a6b66c6b66c68838cfc8cf8c79bddb9bb9bbb6b6c6b6c68c66c6c
                    cff3cfefffcff3f3ffcfffffffffffffffcfffcf3fcf3fcfc3f3efc3cfbbc3bbd9d9d9d91d1d9d199bd11d199b9696b1d1d999b96969b9dd1dd9d9dd9d9d9d9bd9d9dd9dd9d9dd9d9b9b9d999b9bdd1d1d191d11d1d911d11d191d9dd9dd9dd9dd9bd9b9b9b6d6b6d9bd69b9b9b9b9bdbd6d9b9d9bdd9b9b6b6b6b69a69a6b6b6b66b66a66b666c6b66a6b8ccc3c83c83c8cb9d9bd9b6b6b66c66c68c66c8c6c
                    3c3feff3fff3ffffcfff3ffcffcf3ffcffff3fffff3ffff3ffcff3fc3c3c7c3bd9dd11111d11d1dd9d1d11d1d9b96991111d1d9b9b99dd1191d9dd9ddb9b9bd9d9bd9bd9dd9d9dd9d99d9b9db9d9d191d1d1d1d1911d1d1d11d1d1d9ddd9db9bd9b9bdd6dd9b9b9b6b96b9b6d6d9dd9d9d9dd9ddd9d9bb69b9b69b6b6b66b6b69a6b6a66b66cb6b66c66a6c3c8c83cfc83c3cc9b9b6b6b96c66c68c66c6c6b6c
                    f3ef3fcfffffffcffffffcffffffffffffffffcf3fffcfcfcf3fcc3ffff3ccc37bd1d1dd11d11911d191d111199b9a9dd111d19d99a99d1d19dd9dd99d9db9b9bd9dd9d9bd9dd9d9db9b99b99b9d9d1d1911111d1d1d11d1d1d19ddd9d9db9d9bd9b9b9d69b9b9b9d6b9b6d9b9dd9d9d9dd9dd9b9db9b9bb6b69a69b66b6b69a66b6b66b6c666a66a6b66bc8c3c8c8c3cf8c8cc6b9b6b6b6c6c6c66c6c86c6c6
                    fffcfcffcfcfcffffcfcfffff3ffcffff3fcfffffcfff3ff3fcff3efe3cc3e3ee7b19111d1111d1d1d1d91d91dd9b9d191d19dd9b99b1191d19dd9d9db9d9d9d9d9d9d9d9d9d9d9d99b9d9d9b9d9d1d1d1d1dd11d11d1d119d1d1d9dddd9dbd9b9bd9b9b9b9bd6d6b9b9b9bd9d9dd9dd9d9d9dd9d9b9bd69b6b6bb6b6b696b66b6b66b66a6b6a66b666c6cc38c3cf38c8c83c38c6b6b6b6c6c6c6c6c86c6c6cc
                    3fcf3f3ffffff3ffffffff3fffcffff3fffff3fffff3ffcffff3cff3cf3fe3e7c77ddd9d19d111191d9dd911d11d9d1d1d1d11ddd9b9d1d19dd9d9bd99b9b9b9b9d9bd9d9db9dbd9d9d9dd9b9d9dd9d191d119d191d191d1d19d9dd9d9db9d9b9b9b9b9bdd69b9b9b9bd9d9ddd19dd9dd9bdb9db9bd696b69b9b69b69a6a6b6b6b6b66a6666a66b66c6b6c6cc8c8c8c83fc8cfc8c6b6c6c6c6c6c6c6c6cc6c3c
                    ffffcffcf3f3ffcf3f3f3fffcffff3ffffcffffc3fffcff3fcfff3cf3cfc3ee7ce7b9dd9d1d1d11d11d9dd9d1d111191d919d919d99b19ddd19d9d9b9d9d9b9d9dbd9d9bd9db9d9d9d9d9dd9d9d9dd1d1d19111d1d11d1d1d1b6b6dd9d9d9b9bd9b9bd7969bd6d9bd9b9bdd9d9dd9dd9bd9d9b9db9bdb9b9b6b6b6b6b69b6b6b66b6b66b6a66b66c6a66c6c83c83c3cfc83c8c3c6b8c8c6c6c6c6c86c8c6cc8c
                    3c3fffcffcfffffffffcffcffffffffcfffffcffffcffffff3fc3fcfcf3cc3e3e7b7d9dd9d9d9d11111d9d9d11d1d11d9dd1dd9d9d99dd919dd9db9d9b9b9db9b99d9bd9db9d9d9bd9d9d9d9d9ddd9d191d1dd11d1d1d19d19c66b6d9bd9bd9b9b9b9d9bdb9b9bd9bd9d9d9dd9d9d9b9d9b9b9b9b9969b6b69b69b6b6b66b696b6698b66b6b666a6b6c6cc6cc83c8c838c8f38c8c3c3c3ccc6ccc6cc83fc383c
                    ffffcff3fffcfcffcffffffff3fffcfffffff3ffcff3ff3fcff3fcf3c3e3c3ec3e7ebd9dd9dd9d9d91d1d9ddd1111d1dd9d9d9d9d9b99d9dd9d9d9d9bd9db99b9db9d9d99d9d9bd9d9bd9d9dddd91d1dd1d1191d191d1d19dd6b6c6db9b9b9b9b9dd79b99b9b9d6d9d9dd9d9dd9ddd9db9b9b9b9b9bb6b9b6b6b6b696b6b6b6a6b6a66a6666b6c66c66c83c83cc83c8c3c38c83fc8c8cc67c3c3c3c3cc83cfcc
                    f3fffffff3ffff3ff3fc3f3ffffcffffffcfffc3fffffcffffcff3fcfe3ecc3e7e77bb9d9d9b9d9dd119dd9d191d1919d9d9d99b9dd9b9dd1d9d9b9d9d9b9db9d99b9b9bd9b9d9d9bd9d9d9d9d9dd9d919d9d1d1d1d19d1d9d66b66b9b9d9b9ddb99b9bd9bd9b9d9d9dd9dd9d9d9b9b9b9b9bb9b6b99b96b969b69a6b696b6666b66b66b6a68b66c6c83c8c38c8c83c8c8cc83c83c3c3c3cfc3cc3c3c3c8c83c
                    fcff3fffffff3ffffffffcfffcffffffcfff3ffff3fcfff3f3f3cfcf3cc3f3e3bb7c77d9b9b9d9b9d91d1dd1d1d11dd9dd9d9b99b99d9b119ddd9d9b9b9d9b9b9bd9d9d9b9db9b9d9d9db9d9ddd9dd1ddd1d1d9d91d91d9bb6b6c6b6b9bdb9b9b9bd9b9b9d9b9dbd9d9dd9d9dd9dd9b9b9bb96b9b9b6b6b6bb6b6b666a6a66bb669a66b666b668b6c6c8c6c8c3c3c8c38c38cc8cc8c6c3cf3cc3cc3cc83cf3cc
                    3fcfffcfffcfffcf3fcf3fffffff3fffff3ffcfcfffff3ffcffcff3c3c3e3e3bbdd7b7bd9b9b9b9d9dd1d919111d919d99d99b9b99b9b9d1d9d9d9dd9d9b9d9d9b9b9b9d9d99d9d9b9d99dbd99dd9d9d9d9d9d1d1d9dd9d66b6b6b66c6d99b9b9b9d9b9d9b9dd9d9dbd9b9db9db9b9b9bb9b9b96b6b969b969b696b6b6669a669a66b66a6c6c6b6c86c636c6c86c86c6c6c6c3c36c3c3fcc83fcfc8f3fc3c83c
                    fffff3ff3fff3fffff3fffcf3fffffcf3ffffffffcf3ffffffcf3cfccfc3eee77b9b7bb9b9b9b9b9b9d91d11d1d1dd9d9b9b9969b9999d9d91dd9db9db9d9b9b9d9d9d9b9bdb9b9d9d9bd99d9d9dd9dd9dd9dd9d9dd9dd9b6b66c6c6b6b6d6d9b9bd6d9bd9b9bd9d9d9b9d9d9b9b9b9b9b96b6b9b96b6b6b6b6b6a696a6b666a666a66a666c666c6c6c6c6c6c6c6c6c6c6c6c66cc6cccc3cfcf83f3fc8c8fcfc
                    f3fcffcfffffffcf3fcfcfffff3fffffffcfcff3ffffffcf3cf3ff3f3fce73e7e7d9b9b9d9b99b9b9b9dd1d11919d9d999b9b9b969a9dd9ddd9dd9d9b9d9b9d9b9b9b9b9d99d9db9b9d9bd9bd9d9d9d9d9dd9dd9d9dd9b6b66b6b6b6b6b9b6b6b9799b9b9b9d9dd9d9b9db9b9b9b9bb9b6b9b9b69b69b9b696b696b6a66b6c66b6b66b66c66cb66c6c6c6c6c6c6c6c6c6c6c6c66c3c3c3fc3f8fcfcfc3f3c3c3
                    fff3fcffff3fcfffcfff3f3fcfffcffcffffffffffffcffff3fcc3ccfc3e7b7e7ebd9b9d9b9db9d9b9d9d9d9ddd9dd9b9b9699699b99d9d19dd9d9d9d9db9db9b9d9b9d9b9b9b99d9b9d9b9d9b9bd9d9dd9d9d9dd9d9db6b6b6c66a66b66b666b9b9b9d9b9dbd9d9db9d9b9d9b9b9b969b96b69b6b6b66b6a66b6b666b666b66c66c66c66cb66c6b66c66b66b66c66c66b66b6cc6c7c3cfcfc3f8f83fc8cfc8c
                    fcffff3fffffff3fff3fcffc3fffffffffff3fffcf3fff3fcfcf3fef3fe7e7b7e376dd6dd9d9d9b9d9d9dd1d19d19d9d99b9b99a99b9dd9dd9dddd9d9d99d9b9d9b9d9b9d9d9db9bd9b9d9d9d9d9d9d9d9d9d9d9d9d9b66b66a6b66b66b66b6b6b9b9b9b9d9d9d9db9b9b9db9b9b96bb69b69b69b69b9b666b96a6b6c6b6a66a6b6b68b6c66a6b66b66b6b6b6b66b6b6b6c6c66c3cfcfc3c3f8f3fcf8ff383c3
                    ffff3ffffcff3fffcffcff3fcffcff3fff3ffcfff3fcfffff3fcfe7cf7c3e3477e7b9b9b7dbd9b9d9b9d9d9d9d9dd9dddd9d9b99b99d9dd9dd919dd9db9b9b9d9b9d9b9bb9b9b9d9b9d9b9b9b9d9b9b9d9d9d9d9db9d9b6b6b66b6b6c6b6b666b6b9bb9bd9b9ddb9d9d9b9b9b9b9b969b69b69b69b66b6b6b6a6666a666b6b66b666a66b6b66b6b66b6b66b66c6b6b66b6c6b67c7c383f8f8fccfc3fc3cfcfc8
                    fffffffcf3ffffcfff3ffcffffffffffcffffff3fffff3fcfcf3cf3fc7b7e7cb7bb9bd67c7d6d9b9bd9d9d9dd1d1d1d911d1d1d9d9d9d9dd9d1dd9dd9d9d9d9b9d9b9b69a6b9d9b9d9b9d9d9d9b9d9d9db9d9b9b9d9bb6b666b66c66b66a66b6c6b96b69b9dd99d9b9b9b9d9d9b6b6b9b6b9b69b66b96696b66b6b66b6a666b66a6b66b666b66b6a6b66b66b6b6b66bc6c66c7c3c3cfcfcf3c3c3cc3fc3cf8f3
                    ff3fcffffffcffff3fffffff3fcfffcfffcfcffcfcffffff3f3ffc3c3ecc3e77b9bd97cc3bbdd9b9d9d9ddd9d9d9d91dd9d91d1d9ddddd9d19d91d9d9b9b9b9b9b9b69a669bb6b9bb9b9b9b9b9d9d9d99d9bd9d9a9d9b66b6a6b6b6b6a66b66c66b6b6b6d9b9b9b9d9b9d9b9b9b99b969b96b69a69b6a6a66b66b6b66b66b66a6666b66b6a6b6666b6b66a6b66b6b6c66c6c7ccc3c3c38fcc3c3c3fcc3c3c3cc
                    fffffff3fcff3fffffcf3fcfffff3fff3ffff3fff3f3fcfffcfc3cfe3b77e3bbd9b6bc6cc776dbd9d9bd99dddd1d9dd9d9dd999d9d9d9dd9d1d19d9b9d9b9d9b9d9b6b9b6b69b6b66b99b9d9d9d9b9bd9bd9d9bb9b9b69a666b66b6666b66b6b6b6b666b9b6b9b9b9b9b9b9b9b9b69b6b6b69b69b66b666b669a666a66b66a66b6b6b6b6b66b6a6b666a66b66c66c66c6b6c6c3cccf8fc3c3ccfc8f83cfc3cc3
                    fcfff3ffff3fffffcfffffffcfffffcffff3fff3ffffff3ff3fff3c3ecbc7e7b6d9b63c3cc7e77bd9bd9dd9d9d9dd9d9d9d9db9bd9ddd91d19d9dd9d9b9d9b9d9b9b966b96b69b69a6b69b9d9b9d9d99d9d9d9b9b6b9b66bb66b66b6b6b6b666b666b6b6b66699b9b9b9b9b9b696b69b96b6b6a66b66b6b69a666b66b66b66b66b6b66b66b66b666a66b6c66b6b6b6c7c6c3c3c3c3cfc3ccc3cf3c3c3c3cfc3c
                    fff3ffffffffff3ffffff3ffff3fcfffffffffffcffcfffcffc3cfc3e3b7c3bb6b67bcc7c7c7cb9bd9d9dbd9d9d9d9dd9d9b99d99d9d1d19dddd9d9d9b9b9b9b9b66bb96b69b6b6b69b6b9b9b9d9b9db9d9b9b9b6b66b6b96b6b6a6b6b666a6b6b6b666b69bb6b66b99b9b969b6b9b6b6b66966b66a66b66a66b6b6b66b6b66b6b66b66b66b66a6b6b66c6b66c6c6c6c3c3ccc8c3c83cc3c3c3cc3cccff8fffc
                    f3ffffffcffcfffffff3ffcffffffff3fcffcffff3fffcff3ffcf3e3ec6e3e7c7bd6c3c3c7c777b9b9b99d9d9d9d9d9d9d9d9b9b9b9d9d9dd99d9d9b9d9d9d9b99b966b69a6b69a69b69b9b9d9b9d99d9b9d9b9b69b6696b6b66b666b6b6b66b66a6b6a66b66a6b69b9b96b9b9b96b6b66b6a6b6b66b666b66b66b66b66b6a66b66b69a6b66a66666c6c666c66c6c3c3c8c63c3cfc3c3cc3cfc3cf3cf3f3fc3f
                    ffffcffffffffffffffffffffcfffcfffffff3fcfffcff3ffc3fc3fe3c7cc3c3c66c6cc6c3ccb7c9d9b9b9db9bd9bd9d9b9b9b9b9d9d9d9d9dd9d9d9d9b9b9b9d9a6b9b6b696b69b66b6b9b9d9d9bd9bd9d9b9b6b66bb6b6b6b69a69666a66b66b66b66b66a6696b9b69b9b96b6b69b69a666b666a66b6a66b6b66a66a6666b66a66a6666a66b6b6b66b6c66c6c6fc8cf3cc3c3c3cccc3c3c3cc3cc3fcfcf8fc
                    ffcfffcffff3ffcff3fffffffffcf3ffcf3fcfff3fff3ffff3c3ceccccc7c77e7b7c3c3fcfc6b7b6b9b9b999d9b9d9b9d9b9d9b9d9b9d9d9d99d9b9d9bd99d9b9b69b669b6b69a66b9b96b9b9b9b9b9d9d9b9a69b6966b69669a66b6a6b696b6b66b66b6b66b6b6b6b6b6b6b69b6b66b66b6b66a666b6666b666a669669a698b666b66b66b6b66c66b666b6c6bc6c3c3c83cc3cc63c3c7cc3c3ffffcf83c3fcf
                    fffff3ff3ffffffffffffffff3ffffff3cfc3ffffcfffcf3cffc3f33c3c7b6bc7c6bc8c3c3c3b6d96d69bbbb9b9d9bb9b9d9b9d9b99b9d9d9d9d9d9bd99d9b99b696b69a69b6b69b66b69b99b9b9d9b9b9d9b96b6b6b69a6b6b66b6b696b6a666b66b666b6b66b66b69b6966b669b6b6b66b66b66b66b6b666a6698b6a66a666b6b66a6b6666a6b6b6ca66c6c6c3c83cfcc3cc3ce3c73c3cc3cfc3c3c3cfcf3c
                    fff3ffffffffffffffffcff3ffffffcfcfccfcf3ff3ffffcf3cfc3cfc3cccb67bc6c3c3f8c3b7b6b96db966b9b9b9b6b9b9b9b9b9b9d9d9bd9dbd9d9d9db9b9b9b6b9a69b669b6b69b9a6b69b99b9b99d9b9b6b696b6b6b6b69b696b6b6b669b6b6b6b6b669a66b696a66b6b69b6b66b6b66b66b66b66989a6696c66b66b6b6b666b666b6bb6b66b6c66cb6b6c6c3cc873c7c3c3cc3ce3e3cc3c3cfc3cfc3cc3
                    fffffffffcfffff3ffffffcffffffff3f3f3fffffffcf3f3fcf3fcf3fc3c3c7b6c3c83ccfcc6bd6bb96b6b9b6bbb6b6b9b9d9d99d9d9d9d9d9d9d9d9db9b6b6b69a669b669a69b69a66969b9b6b9b9b9b9b9b69b6b69b969b9b69a69b69b9bb6b9696696b666b96b6b69b69b6b666b966b6b6b66b69a6a666b6a69b66b6966b6b6a69b6b666b6ccc8c8c3c867c3cc3c3c7c3cccc3c3e7c3c3ec3e3c3e3c3e3cc
                    ffffcffcfffff3ffffcffffffcff3ffffffff3ffcff3ffcff3fccf3cfc3c3c6c3cc3ccf863c7c6b66b6b6b6b6b69b6b6b9d9b9b9b9d9b9d9bd9d9d9b99b69696b696b669a69b669b69b6b6b69b969b9b6b69b6b669a66bb69b9b6db9b9b9b969b6b6a6a66b9a66b6696b6b66b69b6b6b696666b6986666b6b6696b6b696a6b66b696c66b6b6bb6c3c83c8f6c3cc3b67cc3cc33c3fce3e3ec3e7e3ec3cc3ec3c3
                    ffcffffffffffffffffff3ffff3ffffcfcfcffcff3fffcf3fcf3fcf3c3ecc7b3cc3c83cccc6c76b6b6b6b6b6b6bc6b6b6b9d9b9d9d9b9d9d99d9dbd9b9b6bb69b69b9b9b6b669a66b69b969b69bb96b6969b696b9b69b99b9b99b99b9b9b9d9b9b69696b69869b69a6b696b96b6b9696b6bb9a66a6b6b69669a6b666b6b6b69b6b6b6b666c6bc38c83c83c3cc3c6cc3c7c7ccf3fc37b3e7c7c3e7c3e3ec3fcfc
                    ffffffffffffcfffcfffffffcfffcffffffffff3ffcff3ffcffc3c3cfc3c6bdc3cc8fc36c3c7cb6b696b69b6b6c6c6bb7bb6b9d9b9d9d9d9d9b9999b96b969a69a66b669b9b9b69b9b66b9a9b696b96b6b9b9b9b69b9b9b9b9b9d9b9b9d9d9dd99bb6b69a6b9c696b69b6b6b69b66bb69a96669b696b6b6a6b666b69a6966b6b66b66b6b6b6b6cc3ccfcc8f83c67c6cc37c3c3cecc3ce7c3e3e3c3ec3cfcf3f3
                    ff3fff3fff3fffffffffffcfffcfff3f3f3fcffcfcffffcf3f3ccfc3c3c3c67bc83c3c8c7b6b6b69b6b6b6b6b6c3c7c76b6bb6bb9d9b9d9b9d9dbb9a69b6b69b69b969a66696b6b6969b6b669bb9b69b99a6b6b9b9b9b9d9d9d9b9d9d9d9dd9db99b9b9b69b69bb96b969b969a69b969b69b9b669c696969669a69a66b6b6b69b6b6b6b6b6bbc38c83c3c3c3cccc6c3c7c3e7c3e33c3c3e3ffcce3c3e3c3fcfc
                    ffffffffffffffffffffcfff3fff3ffffcfff3ff3f3cf3fcffcf36c3eccecc683cc8fc3c6b6b6b6b6b6d6b6b7c6cc76b7b67c7b7b9b9d9b9d9b99b969b696969a696a969b9a69b9b6bb9b99b6969b9b96b999b99b9b9d9b9b9d9d9d9d9db9b9b9b9b969b9b9b99b9b9b9b69b69b969bb9b66b69a696a6a6a6b66b66b69b6b6b6b6b6b66b6b6c6cc3cf8c8fcc83fc3bc7cec3ce3ec3efcfcfcf33fcf3fcfc3cff
                    fcffcffffffffffcfffffffffffcffcfffcffcfffffcff3f3f3cc83cbe3c63c3c83c3cc6c7b676b66b66b6c6c3c3cc7c7cc6c66b79d9b9d9b9b9b9b9b69a9a6969a96b9b6b969696999b96b9b9b9b69b9b6b96b969b969b9d9b9db9b9b9d9d99b9b9b9b9b9d9b9b9b9b9b9b9b69b6b96969b96b96b669669b69b69b696b669b6b6686c6c6c6bc38c83c3c383cc63cc3c737e3e73efc3c3f3fcfcf3ec3c3cf3f3
                    fffffff3ffcfffffff3ffffffcffffff3ff3ff3fcf3f3fcfcfcf3ccc7b7bc6c8fcfc83cc6c7bb6b6c6b6c67ccc6c3c6cc76c67c6bb9d9b9b9b9b96b69b6969b6b96b96b969b6b9a9bb99b999b99b99b69b9b9b9b9b9b9b99b9b9b9d9b9b9b9b9d999b9b99b9b9b99b969b6969b69b96b6b66b69b6b6bb6b66b6b6b6b6b6b6b6b8ccc6c8c6cb6cc3ccfc8fc3c3ccc3c3ec7c3e3c3c3fcffcff3ffef3cf3fc3cfc
                    ff3ff3ffffffff3fffffff3fffff3fcfffffcfff3cffcfff3c3cc83cbbb6c3c3c3c3c83c7b6c6bc6b6b66bc63c3c6cc36cc3cc6c7d6d9b6bb9b9b99b969bb69b9b96b969b9b99b9b99b99bb99b9b9b9b99b9b9b9b969b9b9b99b9b9b9d9b9b9b9b9b99b9b99b99b96b9b9b9a69a66b69b69b9a6c6c68c6b9b6b696b96b66b6b8c6c8c6c8c6b7c6f8383c7cc3c3c3cfc3ce3c3ec3ffcf3fffcfcf3cf3ccc3cfc3
                    fffffffffffffffffffcffffff3fffffcf3fff3fcfcff3cffc3cc3cc6b7b6cc8fc8fcfcc3b67c66b66c6b6cc6c6cc6cc7c6c6cc6c6b7b6b67b99b9b9b9b999b9b9b9b9b9b96b99b9b9b9b99b9b99b99b9b99b99b9b9b99b99b9d99d9b99d99d9b9b9b9b9b9b96b9b99b696b969699b696b66b9c6c8c6c6c6c66b6c6b66b69c6c6c36c86c7dbc3c6cccc7c3cc3cfc3c3b3ccfc3ccfcfffcf3ffffffcff3cfc3cf
                    fcffcffffcff3ffffcfffffcffffffcfffcf3ffff3f3fff3cfcc6cc6cdb7b3c3c3c83c86c6c67bc6b6b67c67c3c63c6c6c7c6c6c7c6b767b6bbb9d9d9d9db99b99b99b9b9b99b9d99b9b9b9b9d9b9b9d9b9b9b99b99b9b9b9b9b9b9b9d9b9b9b99b99b96969b9969b69b9b69b69a69a69b9b6b6c6cc83c6c6cc6b6b6b69a6c6cc86c83c6bd6c6c7c3c3c3c3fcf3cfc3ec3f3ef3e3f3fffffcf3cf3f3cfc3cf3e
                    fffffffcfffffffcffffffffffcfff3ffffffffcfcfccc3cc3c3c63c7b6bc6cc88fcc3cc67cbc66b6bc7b6c3bc77cc3c6c6c3c6c6c76bbc6b6d6ccc6d9d9d9d9b99b99b999b9b9b9b99b99d9d9b9d9d9b9d99b9b9b99b99d99d9d9d9d9b9d9b9b99b969b9d9b9b9b9b96b9696b69b69b6b6b6b6cc836c8c6c6c6cc866a66b7b83c83c6cb7cccc6c3c3cc3fcf3cf3fcc3fcfc3c3cfcffcf3ffffffcffcf3fccf3
                    ff3fcffffffcfffffffffff3ffff3ffcf3fcfcfff3f3fcc3cc6cccccc3c3cc383c3c3c83ccc66b7c676bc6cc63cc7c7cc3cc6c7c7cc7c67b7b6c63c6db9d9b9d9b99b99b9b9b9d9d9d99d9b9b9d9d9b99d9b9d99d9b9d9b9b9b9b9b9b99b99d99b9b9d9b9b9b9b9b96b99b9a99b69b6b6c7c6cc38c6c8c38c83c83ccc6cb6b6c6c6c8c76b8383c3ccf3ccf3cf3cc3c3cf3e3ffe3ffcf3ffcfcffffc3fcfcf3ec
                    ffffff3ffffffffffff3ffffcf3ffcfffffff3f3fcfcf3cc3c3c3c33ccfc6cfcc3c8c6cc383ccc6b7c7c7c3ccc7c67c7c6c7c6c7676b6c6c67bc3c8c9d9b9d9b9d9b9b99b99d99d9b9db9d9d9d9b9d9d9b9d9b9d99d99b9d9d9d9d9d9d9d9b9b9d9b9b9d99b999b9b99b9696b69b69b6c6c7b6c6c8c836c83c86c86836c67c6c3cc3c6bbc7ccc7cf3cff3cc3cfc3e7c3cc3ec3cc3f3ffcffff3fcfffcfff3ffc
                    ffffcfffff3ffcfff3ffffcffffffff3ffcf3fcfcf3fccfcc6c3c3ccf3c3fc3c3cf3c3c3ccc83cc6ccc6ccc3c3c6ec7c7c6c7c3cccc7cc7cc6c7c83b6b9b9b99b9b9d9b9d9d9d9b9d99d9d9d9d9d9d9d9d9d9d9d9b9d9d99b99b99b9d9b9d9d9d9b9d99b9d9b9b9d9b9b9b9b9b69b6bc6c6c6c6c63c6c8cc8cc83ccc8c6c6c3c6c86cc67cc63cc3cffcfcfc7c7c3ec3e3cc3fe3ffcfffffcffcff3fff3ffcfff
                    ffffffffffffffffffffffffffcffcffcfffcff3f3fc3c36c3ccc8fc8c8c83c8c8cc3cc8f83cc6c3c7c7c36c8c3c6c67c7c7c8c83c366c6c6e6c3cc6c7b9d9b9d99b9d9d9b9d9d9d9dd9d9d9d9d9d9d9d9d9d9d9d9d9b9d9d9d9d9d9b9d9b99b99d99b9d9b9d9d9c66b969ad66bbb66c6c6c6c6c8c8c36c6383c8c386c86c6c6c3c36cc7c7c37c3c3cf3f7c7c3ec3e3cc3cc3cfcfffcf8ff3fffffcfffcfffcf
                    3ffffffcfffffff3fffcffff3fff3ff3fff3fcfcfcfc8ccc3c3f3c3c3f3fcf83f3c67c3ccc8c3c67cc6c6cc3c8c3c3cc6c3c3c3c86ccc63c3c6cc83c7b9b9b9b9b9d9b99d9d9d9dd9d9d9d9db9dd9d9d9dd9d9d9d9d9d9b9d9b9d9b9d99d9d9d9b9b9d9b9d9b9b6b6b6d6b96bc676b7c6c6c6c83c836c8c8cc8c386cc3c63c3c6c6cc6c7c7cc3fcfcfcfc3e3e3e3cfcffffff3f3fcff3ffffcf8fff3fffff3ff
                    ffcff3fffffcfffffcffff3ffffffcffcffff3f3c3c3c3c3c8c8cfcfcc83c3cccc3eccc383c38ccc637c3c8c3c3c8c6c3c6c6c8c3c3c3cc8c3c73cc6c6c9b99d9b9b9b9d9d9d9d9d9dd9d9d9dd9bd9d9d9d9d9d9d9b9d9d9b9d9b9d99db9b9b9d9d9d9b9d9b9b6b66769b9b6c76cbc76c6c6c3c8c6c8c6c3838c8cc86c8cc6cc3cc3c3c7c3c3cfc3f83c3c7e7c3e3c3c3cf3fcffcf3fffcfffff3fcffcf3ffcf
                    fffffffffffffffcfffffffcffcfff3ff3fcfcfccc6cc3ccf3fc3c3c38fcfcf383c3c36ccc8cc3c3ccccc3c38c8f3c3cc3cc6c36cc8c83c3cc6cc83c7b6b6b9b9b6b69b9b9b9b9d9d9d9bd9b99b99d9dd9d9d9d9b9d9b99d9d9d9d9bd99d9d9b9b9b9b9d9b9b9b67cb6b6b676bc6c6b6c6c38c86c38c68c8c8c3683c86c36c38c86c8c63cfcf8f3cfc3cc3c3c3ecfcffcf3fcffffffcfff3fcffffffffffcfff
                    cffffffff3fff3fffffffcfffff3fcffcff3ff3f38f6cc63cc83c8f8cfc638c3ccc3bcc3c3c3c6cc63c3c8cc83ccc8c3cc83c6cc6c3cc8c83c6c3cc6c67c6b99b969b9b99b9b9b9b9d9b9b9b9b9b9bd9d9d9db9d9d9d9db9d9b9b9d99b9b9b9d9d99d99b99b9b76b66c6b9b6b6c76c7cc38c6cc38c6c3c38c38cc8c83c8cccc6c3c83cccf83fcf8fcfc3e3cffff3ff3fffffffcf3ffff3fffffcfcf8fcffffcf
                    ff3ffcfffffffffffffcfff3fcfcf3ff3fcfcc8cfc3c3fcc83fcfc3cf3c3cc3cc3fc3c6c3ccc6c3c7cc83c38fc383c38c3cc83c3c6c383cc83cc83cc6cc6b6b9b9b6b9b9b99b9b9b9b9699b9b969b99b9d9bd9dbbb9b99d9b99d9d9b9d99d9d9b9b9b9b9b9d9b9b6b76b6c67c6c6c6c6c6c6c86cc86c88c68cc83c38c6c3663c6c3cc63c3fc3c3c3c7c3cff3fcffcffcfcfcfffffcfcffcfcffffffffffcffff
                    fffffff3ffcfffffcffff3ffff3fccfcfc8ff3c3c3cfc3c3cfc83fc8c3cc7cc3cc3c83c7c83c3cc3cc3cc8c3c8cfc8cf8c83ccc6c7c8cc83cc3c3c83c63c7bb96b9b969b9b9b9bbd69b9a99b99b99b9d9bd9d9b99b99d9b99d9b9b9b9db9b9b99b9d9b9d99bd67b6b6b6c67b67b67cb768c86c386c38c6cc66c6c8c6c3c6ccc3ccc3cc3cc6c3ccc7c3e3cfcfff3fffff3fff3fc3f8f3fffff8f3fcff3fff8ffc
                    ffcff3fffffffcffff3fffcfcffcff3fc3cf3ccfffc3cfcfc3c3cc3c3cc3c3cc3ccfcc3cccc3c83cc7c3c3c83c3c3c3c3c8c3c6c6c7c67c63c8cc83cccc6c6b6d696bb6b9699b6b7b9b9d6b6b99b9d9d9d9cb6b6b6d9b9d9d9b9d99d99d9d99b9d9b99b9b996b66b6c67c6c6c6ccc79c6c6c38c6b6bd9b79bb9b96b6c67c3c3c63c67cc3c3cfc3c3be6cf3ffcffcf3fcff8ffffcfffcfcf8fffffffcffcfff3f
                    fff3fffcfffcfffffffffffff3f3ffc8fcfcff3fc3fc3c3c3ccc3cc6e63ccc7c3c3c3cc63c3cfcfc3c6cc8fc8f6c8c8c83cc83c3c677c7c3cc3c3cc836c6c6c79bbb6b69b9b9bd6c79d99b969b9d9d9d9db6cc7c7b6d9d9b9d9d9bd9bd9d9b9d9b99b99b9bb6b7b6c7b6c67b67c67bb6c6c8c6c6dd9dd9db9ddd6b67cccc83c83c7cc3c6cfc3cc7c37f3cff3f8fffcffcf3fcfff3fffffff3fcffcffffff3fff
                    cffffcfffcfff3ff3ffcff3ffcffcf3c3c38fcfcffc3cfcc83c3c63c3cf3f3c3ccc6c3cfcc83c3c8c3c73c3c3c8f3cf3c8f3cc8cc3cc3c6cc8c6c83ccc3c6c7b6b6767b67b6b9c76bbbbb69a69d9db9d9d9c6c6c6cb9b9b9d9b9b9d99b9b9d9b99b99b99b96b66c66b6c6b6cc6b6b6c6c836c8cb9b9b9b9bd66bd67c63c3ccfccc3c6c3c3c3c3cc3ec3ff3cff3fcff3fffcf3fcffcf3fc3fffff8ff3fcffcffc
                    ffcfffffff3ffffffcfffffcffcf3cccfc8f3f6f3cfffc33cf8cfccfcfc8cf8c3c3e3cc3c3cfc83c3ccccc8c83cc838c83c8c36c7b6c7c3c3c38c3cc66c3c6c6b6ccc67cc6bb76bc63b67969b9a6b6cbb9cc6c76b76b9b9bb6bb9d9bd9d9d9b9b9d9b9b99b9b97bc76c67c6c76c6b6c6c6c8c666c6b6b6c66c66c7cc7c7c3c673c7c3fc3cc3cc37c3ec3fcffcfc3fcf8f3ffcf3fcffcfffcfcf3ffffff8fffff
                    ffff3ffcffffcffcffff3ffff3fcf3ff3f3ccffcf3fc3fcfc3fc3f83f8f3fcfc3cc7cc3c8fc83cfcc83c3c3c3c83cc83cc83ccc6c3c3cc6c8cc6cc63cc6c6c7c67c6c7cb6b76b77ccc7b6bb6b6b8c666cb6c6c6c6c6b6c6b6c76b7b9d9b9b9b99b9b99b6b6b76b66b6b6c6c6b6cc6c6c8c6c3c8c6c6c6c6cc6cc7c6c7c6cc7cc7ccfc8fc3cc3ccc3e3ccf3cf3cfffff3cfc3fff8f3ff8fffffcffcfcffffcf8f
                    f3fffcff3fffffffff3fffcffff3fcfcfcfff3c3ccf3f83cfc83c8fcf3cfc3c3c3c3c6c3c3c3fc83c3cc3c8fc8fcf6ccfc3c83c3c8cc6cc36c6c6ccc7c3cc36ccc6c6c6b7c7bc6c76bc6b69b6bc6c6cc6b6cc36bc6cc6c6c6c6c7b6db9b9b99b9b96b96b96b6b7b6c6c6c6c6c6c6c6c66c386c86c8c838c838c6c63c7c73c63c3c383c3cc3cc3c7c7c3fcffcff3fcfffcfffcffffcff3fcf3ff8ff3f8f3ffff3
                    ffcfffffffcf3fcfffffcffff3fcff3f3f8f3ffc3cc8fcf3c63ec3c3cf8c8c6ccccc7c3cc8fc83cfcc3c8c3c3c63cc3c38c3cc8c3c3cc638cc6c3c6c6c6c6cc66c6c6c7c6c6c7d6cc79b69b9c6c6c6c6c6c68cc6cc6c6cc6c6cc6bc6b9b9b9b9b9b99b6b6b6b96b67c6c6c6c6c6c6c6c6c8c86c36c36c6c8c6c3c3cc7ccc3ccfc8ccc3c63c3c837c3c3e3cf3ffcff3f8f3f8ffcf3fcffffcfcf3fcfffcffcffc
                    ffffff3fffffffff3fcffff3ffcf3fcfcff3fcf3ff3fc3fc3cc3cc3cc6f3c3f3c3c7c3cc3c3c8fc838c83cc8c3cc3c6cc3cc83c3c8c3c7cc83c8c83c6cc6c3c3c6c3c6c6c6c6c6cc6cc6cc6b7c6c38c6cbc3c68c38c3c6c63c6cc6c6b69b69b69b6b6b66b6b6bc6c6c6c6c6c6c6c66c6c6c6c38c86c8c836c8c67bc7c33cc383cf3fcc7cc3c3cc3c3e3cff3ffff3ffcffcfff3fcfff8fcf3ff8fff8f3ffff3ff
                    fff3fcffcffcfcfffcff3fffffffffc3f8fcf3fcfcfc3fcfcfcc3cc3c3cfcfccfc3c3cc3cf8f3c3cfc3cfc3c3c8cc3c38c6c3cc83c8c6cc3c8c3ccc83c63c6c6c3c8c38cc6c6c6c6c6c6c6b6b6c8c6cc6c68cc38c6c6c6ccc6c3c6c7bd69b9b6b69b9b6b6b6b66c76b6c6c6c6c66c6c6836c8c6c6c86c6c8c367c63c6c8f8fcf83cc63c3cfcfcfc3ecf3cffcf3fcf8f3ff3fcfff8f3ffffcf3fcf3ffffcf8ffc
                    f3fffffff3fffff3ff3fffcffcf3cf8fcf3ffcf8f3f3c8f3c38f8f3cfcfc3cf38c3ccc3c8c3cc8fc83cc6c6c8fc38c8cc3c8c3c3c83cc78c83c8c38c6ccc83c6c6c6c8c38c6c6c6c6c36cc6c6c3cc6c3c6c6c8cc6c8c836c3c6c7c76c79b9b96bb9b9b66c9c6c6c6c6c6c6c6c6c6c6c36c8c6c86c3c6c8c36cc6c7cc3c3c3cfc3cf6c3cfc3c383cc33eff3cf3fcfffcfcfcff8f3fffcf3ff8ff3ffcfcfffff8f
                    ffcfcf3fcfff3fcfccfcffff3fcf83c3ffcf3ff3cfcfc3cf8fc3fcfc83c8fc8fc3cc3c8f3c8f3c83cc83c7c3c6cc3cc38c3c38c8fcc6cc3cc8c38c6c383ccc6cc6c3c38c6c3cc83cc6cc86cc6c683c8c6c6c63c6c3c3ccc6cc3c6bb7b6bd6b6d69bd6c6c6b66c66c6c6c6c6c6c6c6c68c6c683c6c86c36c8c6c7cc3ccfcf8f38fc83cc3c6f6cc3c3ef3ccf3cfcfc3ff3ff8f3ffcffcfffcffcfcf8ffff3fcfff
                    3ffffffffcfcfffc38ff3fcfff3cfcfc3cfcc3cfc3f38c83c3fc3c38fc3c38f3cfc3cf3ccfc3cfc83c3cc3c8c38c838cc8c8c83c83c3c6c36c8cc83c8c6c83c6c3c8c8c3c8c83cc83c83cc3cc3cc8c38cc6cc6c8c8c86c6c86cc6c66bb66b9b6bd6b66b6b6c6c6c6c6c6c66c66c6c6c6c6c6c6c86c6c6c866c6c3c63c3c3c8cfc3cc3cc7c3c3cfcfcc3c3cc3cf3fc3cfc3fcfc3fcff3fcff3fffff3fcff8ff3f
                    fcf3fcfcf3ffffcfcfc3fff3fcf3cf3cff3fcf8f8c8fcfcfcfc8fc8fc3fcfc3cc6c3ccc3c6fc83cfc8c3c8f3c83ccc83c3c3cfc83c8c3cc8c3c83cc8c3c8cc6c6c83c8c8c3cc8c38cc8c68c86c83c8cc6c6c3c83c3cc6c6c3c83c3cc767b6b6b6bd6b6c6b6c66b6c6c6c6c6c6c6c6c6c6c6c86c6c6c6c6c3c63c6c3ccc8c3f3c8c3cc3c3cfcfc3fc3cfc3e3c3cfcffc3fc3c3fff3fcfcffcfcf3cffff8fffcff
                    fffcff3f8fcfcff3fcfcfcfcf3fcfc8f3ff8f3c3c3c3c3c38f3fc3fc3c8fc3cc3cfcf38fc3c83c83cfc8fcc83cc83c38c88c383ccfc6c6c38c8cc83c8c83c83c3cc83c3c8c83c8c6c3c3cc3cc3c8c38c3cc6c8cc8c83cc6c8c3c8c3cccc76bd6bd6c6c66c66c6c6c6c6c6c36c6c6c686c86c6c6c36c86c6c6c7cc7c63c3c8c8f3cc3cc3cc83cfc8fc3ccc3bccf8fc3fc3fcfcfcfcfff3fcff3fff8fcff3ffffc
                    fcff3fcf3fcfffcfc38ff3fffcf3c3ccfcf3fcfc8fc88c8fc8fc8fc3fcfc8f8fcf38cfc3cc6ccfcf83c3c83cc83c8c8c3c3c8ccc6c3c8c8cc836c6c83cc6cc6cc83c8c86c6c6c3c8c8c66c6c66c6c6cc6c38c36c6cc8c36c6c6cc3c6c76b7b6b66b6b6b6bc6b6c66b6b666c6c6c686c66c6c36c68c6c63b7c7c6c67e7c3c3f3cc3c3c6c3fcf83fc38f6c3cc3fcf3fcffcf3f3f3ff3fcff3f8ffcffff3ffcf3ff
                    3f3ffffcfc3fffff8ffcffcf3fcc8fc38fffc383c3c3c3fcf3cf3cf8cf83fc3f83cf38fc8f3cfc83c8c83c83cc83c3c3c6c3c383c8cc3c3c3ccc3cc3c8c3c3c6c3c8f6cc3c6c6c83c36cc8c6cc6ccc83c6cc6cc6c3c36cccc3c8ccc6c7cc6b7b7b6b6c6c66c6c6c6b76cc6c66c6c6c6c6c686c8c6c6cc76c6c3c3ec6c3cfccc3c83cc3c8f3cfc8fccfcfc3cc3c3cf83f3fcfcffcffff8ffffffff3fffcffffcf
                    cffcfcf3fcfcf3fcfc3ff3fcfc3c3c3c3c3cfcc8c8cc8c38cf8cf8cf83fcfcfcfcfc8fc3c8fc83c8f3cfcfcc3ccc8fc8c3cc8cc83c38c6c8c6c8c6c8c6cc6c8c6c83cc3c8c3cc3cc8cc83c3c6cc836cccc8cc6c83c8cc8838cc3683b6c7c7c6b6c3c7c76b6b66c6bb6b66b6c6c66c6c6c6c6c66c6c66c6c3e3ccc73cccc3c3c83cfc8f3c8f83cf3c383c8f37c3cf3fcfcf3fc3ff8fcfffcf3fcfcffcfff8ffff
                    f8fff3ff8f6fcfffcfcffc8f3c8fcfccfc3c3c3c3c3c3cfcfc3fcf3cfcfc38f8383fc3c8f3c8fcf3c8f683c6c3c3c383c8c3c3cccc8ccc83cc83cc83cc36c6c3cccc6c6c67c6c6c3c63cc6ccc36ccc836c386fccc6c8c3cc6c6cccc3c6c76b67c6c6c6b6c6c6c6b76b6bc66c66c6c6c6c6c6c8c6c6c6c6c7cc633cc3c3c83c3cfc83ccf8fc3f8c8fcfcf3cccfc3ccc3cf3cfffcff3ff3fffcffff8fff8ff3fcf
                    3f3fffcff3cfffff3cffcf3c8f3c83f83c8cc8c8c8c8fc838fc83cf8f838fc3cfc8fc83c3cfc3c8cfc3fcc3c3c6c8c3c83c8c83c83c63cc8c3cc83cc8c6c7c3c6c63b77ccc6c3cc86cc6cc6c8cc683ccc8ccc66c3c83c86cc3c83c3bc6ccc7cc6c7c76c7b6b6b6b6b7c66c6c6c6c66c686c66c676c6c6c7c63ecc3b7c38fc8fc83cf83c3c8fc3c3c8f3cfc3c3cc3c3c3cffcfff3fffcf8ffff8ffff3ff3ffff8
                    ffcfcff3cfc3fcfcf8ff3cfc3c8fcfc3cf3c3f3c3c3c3cfcf38fc8fc3fcfcf8fcfc3fccfc83cf83c38c83cfccc3c3c8fcfc3c3c83cf6c6f36c83cc83c8cc6ccc63be6e677c3cc63c3cc63c63c38ccc6f6c386cc8c83cccc6c8c3c8c6c3c63c6c3c6ccc76bc67b7c7b6bcc6c6c666c6c6c66c6c6c67c6c6c677c3cc3c3c3c3c38fc83cccc3c8fc8fc3c8fc3cfc3c3cfcf3cf3f8ffcf8fff3fcff3fcffcffcf8ff
                    fcf3f8ff8f8fcfffffcfc83f8fc383cf8cfccc3cfc8cc838fcfc3c3fc8f83cfc38fc83c3cfc83cf8fcfc3cc383ccc3c3c83c8cc3c8cc8cc8cccc83ccc3c3c67c7e63c7ccc7c6ccc8c63cc8cc8cc36f6cc8ccc3c3ccc8c36c3c86c3c8c6c3c6cc6cc386cc6c7bc67c6c767bc6c6c6c66c6c6c6c67b6c6c67cce3c3c83ccfcfc83c3cfc63cfc3c3c3cf8fc3c3c7cc3c3c3ffcff3ffffff3fffffffffffffffff3c
                    f3cfcf3cf3cffffcffff3fc8c3fcfc8fc3c83cf6c3c3fcfc3838f8f8fc3fcf8fc3c6fc8c3cfcf83cf3c8fc3cfc3c6cc83cc83c8cfc3c36c3c863c8f6c8c6c3c7c7cccc7c6ccc36c3ccc83c3c3c8ccc6f63c36c6c838f6cc8c8cc6c83cc6cc7c6c38cc6c6c76c6cc6c3cc6c7b6c6c6c6c66c6c67c67c7c7c73cc3c3ccc36c3c3cc3c83cfc3ccc8cf8fc3cfcc3c3c3fcffcff3ffcf8f3ffcf8fcfcf3fcf8f3fcfc
                    ff8f3cf3cfc3cffffcfc8fcf3c8fc3c38fc3c3cc3cfc83f8fcfcfc8fcfcf83fcfc83cf3fc838fcfc8c3c3c8fc8c3cf3cc3c3c83c8c8ccc8c6fccfcc83c6ccccc6c3c7c6e73c6c6c86c3cc8c8c83c6c6ccc8cc8c3ccc3c8c3c36c6c3cc63c6c3ccc63c6c3bc67c3c3bc6cc7c7c6c6c66c6c6c67c6cc6c7c6cc3c8cc63ccc6c8c3cc3cc83cb6c3cfc3c3cc3cfc3cccf3cf3fcfcfff3ffcffffff3ffcfff3ffffc3
                    fcf3f8fcfc8fcffcff3fc38cf8f6f8fcfc8fcc3c8fc3fcf3cfc83fc38f83fc838f3fc8cf3fcf3c83fcf8c8f6f3c83c83c8ccc3cc383c86fc6c638c3ccc3c3c3c3cc3cc6cc7c6cc3c3c86c6c63cc8c3c83c38c3c88fc8c36c8cc3cc8c3cc6c3c63cccc3cc6c7ccc6c683c67c3c37c6c6c6c6c6c6c6c7c3c37c6c3c3cc3c3c3cfc38f83cc6bc3cf6c8cc3c83c3e3f3ec3fcff8f3cffcff8fcf3ffcfff8ffcfcf8f
                    f3fcfcf3c3fcff8ffffcfcf3c3cfc3c83fc3c3cf3cfc8fc8f83c8fcfc3fc8fcfcfc8f3fc8cfc8f3cf83f3c3ccf3cc8fc83f86cc8ccc83cc3c3cc83c6c6ccc6cc6c3c6c3c7c67c6c8c6cc3cccc83c6c6cc8c6cc6c3c83cccc36c8c3c6c83ccc6cc8386c6c76c63cc83cc6e7c3ccc77c76c6c67cc7c6c3b6cc3c7c7cc6c6c38f6fc83c8c7ccf8fc3c3c3c3fc3ecfcf3cfcf3f3fffcf3fffff8fcfff8fffff8f3fc
                    8fc8f3cf8fc83fffcf838fc8fc83f8fcfc3c8cfc838f3cf3cfcfc38f8fcfc3f83cfc3c8f3f83cfc8fcccfcf83ccf3c3cfcc3c83c3c3cc838c8c8fc8c3c3c6c36e6ccccc6c6ec3c3ccc38c8383cc8c3c836cc38c8c83c8c86cc83c83c8cc3c6c7c3cc3c6c7c7cc86ccc6c77cc3c3cc3cc6c67c6c67c3c6c3cc3cc3c3c3c3cc83c8fc83bb7c8f6c3cfc3ccc3c3c3fc3c3fcfcfcf8ffcfcfcfffff8ff3fcf3fcfcf
                    3cc3cf8fc8ffcffffffcfc3cf3fc8fc3c8cf3c3fcfcfcfc8f383fcfc3c8f8fcfcf8fcfc8fc3fc8fc38f38fc3cfc3c8c8383cfcc8c8c8c3ccc3c3c83cc6c3c8cc3c3c36c3c7c7c6c836c6cc6cc83c6c6ccc38cc3c3cc836cf6fc6cc8c3c38c3c6cc6c8c3c67b63c3c3c3cc7c3cfcfcc7c6c7cc67c6c67c3c3cc63c8c8cc8f3fcf3c3fcb7cc3cf3cc3cc3c3cc3cfc3fcf3fcf3fff3ff8fff3fcfcf3fcf8fcf8f3f
                    c3fccfc3f3cfffcf3fc838f8c8cfc3cc3c3cfc83c3f838f3cfc8c8f8ffc3c838fc38f83fc8fc8f3cfc8c3c3cf6c83c3cc8c83c6f3c3c8c838c6c83cc3ccc3c3ccc8c8cc6c7c76ccc6c8c38c6c38cc8c3c8cc36c8c83ccc6c36cc3c3c8c6cc6c3c63c6cc7bc7cc7cc6cc7c3e3c3cf3c3c7c377cc7c6e6ccc83c3c83f3f3c8c83c8fc6c7cc8f8fc3cf3cc3cf3c3cfc3cfcf3fcf8ffcfffcfcff8f3fcff3fcf3fcf
                    fcf3c3fc8f83fffffcfcfcf3f3fc3c83cfc83fcf8fc3fcfcf8fcf3cfc8f8ffcf38fc3fcf8fcf3c8fc3fc3cc83c3cc3c8f3cfc83c6c8c3c8cc6c8fcc6c3c6cc6c36f3c3c3bc6b6c68c6c6cc3c6cc3c6cc87c6c83c3c8f83cc6c838c8c6cc3cc6c3cc77c7c77b6e67c77677c3cfcfc8fc3cccc3b7c3c73c3fc3c8fcfcc8cf3cfc8f6cc3cc3cfc3c8fc83cc3cffcf3fcf3fc8f3ffcff8f3fff8f3fcff8fcf8fcf8f
                    3cc3cccf3fcfcfcff8f38fc8c8c8cfcc3cfcc83fc3fc8f38fc38fcf83fc3cf8fcf8fcf8f3c3cf8f6fc83cf3cfcc3c8fcc8383ccc8c3c8f3c83c3c3c3ccc3c3c8cc6c8fcc3c6cc3c3cc3c8c8c838c83c3c83c8c8c8fc6c8f8c3cc83c3c6c6c6e3c3ccc77c7c3c7c3b7ceec3ec3cf3f3fc3c36c6c6c7cc3c6c8f3c3c83f38c83c3c38fccccc38fc3c3fc3cc3cf3cfc3fc83fcfcf3fcffcf8f3fcf8f8f3fcf3f8fc
                    c37e3c3ccf8ffff8ffcfc38f3f3fc3c3cc3c3cfcfc8f3cfc38fc38fcf8f8fc38fc3f8fc8f8f8cfc3cfcfccc3c8fcfc383cfc8f83c8cf6c83cf8c8cc83c8c8c3c3cf3c3c8cc3c3c8c8c8c383c8cc3cc6c6cc3c3c3c83c83c3c883c8c8c3c37c7c7c3c3c37cc3cc7c7e77c3e3cf3cfcfcfc3cc6c67c63c6c3c3cc38f3c8c3cfc8fccfc3cf3cfc8fcfcc3c3ec3cf83fc8ffcf3f83cf8f3ffffcf8ff3fcf8f3fcf3f
                    3ccc3cc3cf3cfcfffc38fcfc8cfc3c8fc3cc3c83cf3cf8f8fcf8fc38f3c3cfcf8fcfc3f3fcff38fc83c3838fc3c3c83cf8c83cc8f3c83cfc8c3cf63cc3c3c8fc83cc8c3c38cc8c83c36c8cc83c8c8c6c3c38c88c3c83cc8c83cc83c38ccc7c7cc3cc7ccc3cc3c3cc3cc3ecf83f8f8f38f83c3c6c67c6ccc6c3cc3c8f3c83c3c63c3c8cc8c3f3c8f3cc3c3cf8fcfcf3cf3cfcff8f3fcfcf8f3fcfcff8fcf8ffcf
                    cf3efc3cfc8ffffcffcf83c3fc3c83c3c8f8f3fcfcf8fc3cf3c3fcfcccc3f8fc3f83f8cf8fc8cf3cfc8fcfc38fc83cfc83cfc83cc83c8c83c8c83cccc83c83cc3c83c8c8c3c3c6cc8c83c83cc83c3c6c3ccc3c38c8cc83c3cc83cf8cc367c7c3cc3cc3c3cf8fcf3ec3ec3c3fcfcf3cff3fc3e7c67c6c777e3c3cc3ccc3cc3cc3cc3cf3c3c8cf8fcc3cfc3cf3cf38fcfcf8f83fcfcf8fff3fc8f8f8f3ff8f3f8f
                    fc3c3ccc3f3cfcfffc3fcf8c3c3cfcfcf3cfcfc838fc3f8fc8fc8f83f3cfc3f8fcfc8f8fc38f3c8f6fc3c8fc3c3cfc83c83c83c83c8fc3c83cfcc83c3cc83cc38cc83c3c3c6c3c38c3c8c6c83cc8c63cc838c8c3c383c8c83c8c8c38c8cc38fc3fc3c3cc3c3c3cc3cc37c3cf8f3f8fc8fc3cc6c3cc73cc7c7cc37cc3cc3cc7cc3cfc3cccff83c3c3fc3cfc3fc3cf3fc3f8ffcf8ff8fcfcfcff3ff3fcfc3fcff3
                    cfcc3f3f8cf8fff3f8fc83fcfc3c3c3cc3c3c8ffcf3cfcf38f3f3cfc3fc3fcfc838fcf3c8f3c8f3cf3cc3c3cf8c83cfcfc83cfc8fc3c8c3c8f683c83c83cc3c6c3cc8fc6cc3cc6c6c8c3c83c8c36c8c83cc83c8c8cc8c3c8c3c3c8c3c3c38c38fc8fcf8f8fcf8f63e3cc3fcf3cfcff3fcfc3c3cc67cc7c3cc3cc37cc3c3c3c3cf3c3cc38c3cc3ccc8fc83cc8ffcfc3cfcf38f8f3ff3f8ff83cfcfcf8ffcf8fcf
                    8f3cccccf3cff3fffc3fcfc38fcc3cf3cfc3fc3c3cf8f8cfcccccf3cfcffc3cf3fcf3c8f3cfc3cfc3cf8ffc83cfc83c383cfc83c38c83c8fc3cfc3cc3cc3cc8ccc83c6c3ccc67ddb76c6cc8c38cc83c3c83c83c3c3c38c83c8c83c8c888c83cfc3c383c3c38cf3ec3cc3ccfcf8f83fcf38fc3c63cc3c3c3c3c3ccc37c3c3cfc3cc3cc3fcfc3cc3c3fc3fcfc3c3c3ccf8f8ff3fcfc8fcff3fcf8f8ff3fcf3f3f8
                    ffcf3c3ccf8fcffcffcf83cfc3fccfcc3c3cfcfcf8fc3f3cf6c6ccbb6f3cff3cfc8c8f3cfc8fcf83cf3c3c3fc83cfc8cfc8c3c8c8f3cf83c8c838c83cc3c83c36c3cc3c6c3ccc6c66b6c83c8c683cc8c83c83c8c8c8cc3cc83cc83c3c3c3cf8c8f8fcfcfcfc3cc3cc3cc3c38f3fcf8f8ff3cc3cc3c3cfcfc3fcf3ccfcfcf3cfc3cfcfcc6c7c3cfc3c3cc3c3ccfcf8f3cf3cfcf67e3f3fcfcf8f3fcfcf3cfcfcf
                    3f3cffcf3c3ffffffc3fcf8fcfc3f3f3fcfc3f3c3c3fc8f8f3cc3b3b7cff3fc8fcf3fcf8c3c3c3cfcfcfcfc8fcfc38f3c3c83cf3cc83cc83c3ccc3c8c38ccc8c838c8c83c83683cc6cc6cc36c3cc83c3cc8cc83c3c38c83cc683c8c83c8fc3c3c3cf83c83cf8fc3c3c37c3fcfcf8f3fc3cf38ff3fcf8f3fcfc3cf3c3f3cff3fcf3c3c7c3c3cc3cfc8fc3ccc3c38f3cf8fff8cb7ec3fcff8fcfcfcf3fc8f8ff3f
                    cfcfc3c3cccfcfcf8fcf3c3c3f3cfcfcfc3fcc8fcfc8ffc3cfccccbcbc3fcff3c3c8fc8ffcfcfc3f3cf6c3c3c3c8c3cc8c3c8f6c83c8f3c8c8383c83cc83c3c3ccc3c3cc8cc8cc6c86cc38cc8c83c6c8c3c3c38c8c8c3c838c3c83ccc3c3c8c8fc83cf8fc3c3c8f3cfcc3cfc3fc3fcff8fcfc3c8f8f3cf83f8fcfcfccf3cfcf3fcfc3c3c7c3cc3c3fc3cc3c3fcfcf3fcfc3b7be3cfcfcffc3f3f6fc3fcf3fcff
                    8ff3cccfc3cffffff3fffcc3fcfcf3f8f3fc3fc3f8f3cf8fccc3b7bb7bcffc3cc8cc7fc3c3f3ffcfcf3ccc8fcf63cc383fc83c8f3cfc8cf3c8cc8cfc83cc86c8838c8c83c383c386c368c66c36c6c83c68c8c6cc383c86cc838c3c67cc7c3c3f6fc3cf3c38fcf3cc3c3cc3cfc8ffcfc3f8f3c83cf3cf8fcfcf3f8f3f3cffcfcf8fc3ccc3cfc3ccfc3cc3c3cccf3cfcf8f3bb7c3ef3fff8fcfc8fc3cfc3fcffcc
                    f3cfc3c3cc3fcff3ffcfc3ccfcf3fff3fcccc3cfc3cfc3fcf3cc3ccbb7cf3ffc3c3cc6cfc8ffc3f3fcc3c3c63ccc3ccfc83cfc3c8c3838c83c3c3c83cc83c83ccc83c83c8ccc8cc3c6cc6cc6cc83cc6cc36c38c8c6c6c383ccc8c8c7c3c8f8fc3c3cc6c3cfc3c8fc8fc3cc38f3c3f8fc3fcf3cfc3cc3c3cf3fcf3cfcffc8f3fcf3fcf3cc7c3c3c3cc3cc3c3f3cfc3cf3cc7bc3e3cfcf3ff38f3c3f3cfcff3c3c
                    ff8fc3fcfccfffcffcf3ff3cf3ffcfcfcff3ccc3cfcc3ac3cc3fcf3ccbecfcfcf3fc3c3c3c3fffccc3c3c7ccc3fc3c3c3cf8c38f38c8f3c3c8c8c3cc83cc8cc838c8c3c8c383c6c6cc6c836c836c6c836cc8c63c6c83c8cc863c3c3c83c3c3c3fc83c7cc63cc3c383ccc3cc3cffcf3cfc38fcf6fc3cc3c3cc8fcf8f3c8f3fcf8fcf8fc3c3ccc3cc3c3c3ccccf83ff8fc3bc7c3cfcf3ffcffcfcfcfc3f3fccc83
                    cf3fccf3cf3fffffc3cffcfe3fcfff3f83cf83cccc6cc3bff8fcfcffc3b3fc3c3cfcffcc3fcf3f3c3c3cfc3c3cc3c8c8fc83c8c8cf3ccc8c83c3c83c3c83c3c8c3cfc8c3c8cc83c6c38c6cc86cc6c3c6cc36ccc83cc8c38c3c8c86c3cc8c3c8c83cc3c3cc3c3fcfcf3c3c3b3c3cfcf3c3c3c3cc7cc6cc3cc3f3c3c3cf3ccf3f3ff3fc3cfc3c3cc3bcccc3c3c3fccfcfcb7c3efc3fcfcffcf3f8f3cccfcfc3cfc
                    fcfcf3ffcffcf8fffcfcffc3cfff3cfcffcfcfc3c3ecccc8fcfc8fc8fcbcffcfcf3fc3fcc3fcfcfcccc3c3cfc3fcfcf3c3c8f3f3c8c783c3cfc83c8c8c3c8c83c8c83c8c83c3cc6c6cc3c86cc6c8c6cc86cc386cc383c6c6c83c3c8c83c3cc3c3fcfcc3c3cfc83c3cc6c3cc3cfc38fcfc3cc87c673e3ccc3cccfcfcfcf3fc8fcccfcfcf3fffcfc3cf3c7cc7ccfcf8f3b7cec3efcff3fcf3cfcfcf7f3fc3cf3fc
                    3f8f3fcff3fffff3fc3ff3cfcf3ffcc3cf3f3cfcfcc3c3cfc3b6fcf3cc3bc3f3cfc3f8f3fccff3f3c3e3fe7bcc3c83c88c3c8cc8f3cfcc8c83c8cf63c38c3cc83c3c83c83cc6c3c3cc68c6c36c836c663c86c63c8c6c6c8c3c6c8c36cc8c683ccc36c3ccc3c3c8fc83c3c3cc3c3cf383fcc6c3c3e7c7b7b6c3c3c3c3fcf8f3ff383c3cfc8fc38ff8fccfccff8f3cf3b7b7c3cf3fc3fcf3ffcf3c7c7ecfcfcfcf
                    cfc3cffcffcff3ffcffcffcffcffcf3cfcfcfc3fc3ccc3c3cc7b7cfcffcc7ccf3fcfcfc8f3cfcc3c3cfcecc3c3cfc83cfc8f383c3cf3c3c3c83c3ccc3ccc863c8c8cc83cc83cc8cc83c6c36c8c6cc6ccc6c3ccc636ccc3c8c8c3c6cc383c3cc36cc6cc3c6c3fc3c3fccfcc3c8fcfc8fcf3c6cccc3cbbccc3cc3cfc3cf3cfcfcfcfffcf3f3fcf3cf3ffc3f83cfcf8fcbc7ccf3cfc3fffcfcf3cc7bec3cf3ff3fc
                    f3ccff3fcff3ffcffcf3fffffffffcfc3fcf3fcf8fc3ccffcccccc3fcc3bc3fcfc3f8cffcfc38fcfc3c3c3cc3cc3cc7bc3c8c8fcfcc8fc3c83c8c383c83c3ccc83c38cc83cc83c3c6b6cc8c6c6c6c36c3c6c683c6cc686c63c6c6c36cc6cc6cc7c73c3c63ccc8f8c383c3c83c3c383f3c83c7c63cb7c63cbc3cc3fcc3cf8ff3f8fc3fc8fcf3cffcfcf8fcfff3fc3c7c7c3ccfc3fcfcf3f3c7e3cf3cf3cfcfcf3
                    cfff8fcff3ffcffff3ffcff3ff3ff3fcfcfcf8fc3fcccfcf3fc3e7cf8fc3ccf3cfccf3c3c83ff3ff3cfcfc3ee3cc63c3cc3c3c383f3c3c83cc8fc83cfc3cc6c3cc8c3c3cc6c3c8c3ccc66c6cc36c6cc66cc6c6c6c86c3c6c767c3ccc3c63cc7c63ccc83ec3c3c3fcfcc83ccfc3cf3ccf8fc3c3ccc7bccc3c3cfcc83cfc3c3cc3f3fcff3cfcfcf8ff8f3fcfc8c6bcc3ecfef3cfcf3f3ffe7eccc3ef3ef3f3f3cf
                    f8cf3ff3fcffffcfffffffffcfffffcf3f3ffcffcf8f3f8fcffccccf3fcfcc3ff3f7cccfcfcfcffcfc3c3c3c3cc3ecfcc3c8f8cfcfcfc3cc83c3c3cc3cc63b3c63c8c8c83c8cc36c836c3cc6c6cc6c6cc683cc6cc3c6c6c7ccc6c636c6cc63c6ec3c3cc3c8fc8f63c3c3c83c3c83cf83c3c7cc3cbd6c3cfcf8f3c3c3c3cfc3ccccc3cccc3c8f3fc3fcfcf3ffcc3c3b3e3c3fc3fefcfe7cc3c3cfe3cfcfcffcfc
                    ff3cfccfcffcffffcfcf3ffffffcff3fcffcf3cf8f3fcf3fcf8ffc7ccf8f7cfcfcfc3c7c83fcffff3fffcfcfc3ec3c3c3cc3c83cf383cc83cc8c8cfc83c3bcc7cc3c3c3c6c3c8cc3c6cc6c86c86c6c6c36c6c6c366c6c67c767c7cc7c73ccc3c3cc6c3ccf3c3c3cfc83cfc8fc3cfc3fcfc7c3cc7d7ccc8cfcfc3ccccec3c3cc3b7bb777cc3fcccfcff8fcfcf3ffcc3efcfcffcf3fe7c7c3efe3cfcfcf3fcff3f
                    7cfe3c3ffcfffcfff3fffcffcffffcffcfcfcf8f3fcf8fcff8f3fcc7fcfccec3fc8fc3c3cfcf3fcfcfcf3f3fcf3cc3cccc3c83cfcfcfc3cc83c3c3c3cfcc3c6c3cc8c8c6ccc3c3c6cc6cc6c66c6c6c36c6cc6c6cc6cc6e6c6cc6c3c6ccc73cc3c3c3cc3c3c8fc83c3cc83c3c8c3cfc83c6fcc3cd6bc3f3c8f3cfc3c7c7cccf7be7ecece3ecc3fc3fcf3f8f8fccfc3ec3f3fc3fcfe7cc3efc3fcf3fc3fcf3fcfc
                    c3e3ffcf3cf3fffcffcfffff3fcf3fcf3f3f8ffcfcffcffcffcf8fccc3fc3b3cc3f3fcfc3cfcff8ffc3cfcfc3cc3eb7c3ccc7fcf3cfc8c83cc83c83fc33cc3c3cc63c3cc76c6c6c6c3c36c6c6c6c6c6c6c6c66c6c6c6c6c7c6c3c6c3c76cc6ccc6cc3cfc8f3c3c8c83c8c3c3fc83c3cc3c37cc7bc38fc8f3cf8cccc3cf8fc3e7c7c3e3e7c3ec3fc83cfcff3fffc3cfcfcfcffc3e3c3ec3c3ef3efcfcf3fcf3cf
                    e7eec3fcf3fffcffcfffcffcfcfffffcfcfcf3ff8fcf3cf8f3fff3fc7cfcfcc3eccfcf8fc3ff8ff3cff8fcf3ffcfc3ec3c3ccc3fcfc3c3cc3c3c3fcc3cfc3fccc3cc8c6c67cc3c6c6c6c6c3c6c6c6c6c6c67c7c6c67c63cc6c3ccc6b7c7c7c763c3cf3c3c3c8fc3fc83cfc8c63ccfc3ccc7cc7b6cffc3cfcfcf3c3cfcfc3ccc3cc3e3c3cc3ecc3fffc8f3fcfcfcc3cf3fff3fe7ccfe3fcfcfcfcf3ffccffcff3
                    be7bcf3fefcfffff3cf3ff3ff3ffcfff3f8ffcfcf3fcffcffcfcfcfcfcfcc3efc3c3fcf3fccff3ff3c3fc3fcfc3c3ec3cff3c3cf83cfcc3cc8cfcc3fcfc8cc3c8cc3c6c3cc36cc7c3cc6c6c6c6c6c6c6c6c6c6c63c67cc6c3c6c677c7c7c3c3ccc3c6c83cc3c3c8c3c8c3c3ccf3c3cc3c6e7c6bfc38fcfccf3cfcff8fc3fc6cf3cfc3cc3fe3c3ccfcffcf8ff8f7cf3fcfcfe3cc3e3cfe3fc3f3fcfcf3fcf3fcf
                    7cb7ecf3f3ffcfcfcf3ffcfcffcff3fcff3fcf8f3fcfcf3cff8ff8f3cfcf3cc3c3ecc3ccf3c3fcfccfc3fcfcffcfe3ccfc3fccf3fc83c3c3c3c3cfcfc3c3c3cc3c6c3ccc6ccc6c6cc6c6c7b6c6c76c6c6c6c6c6cc6cc6c6cc6cc7cb7cc3c7cc3c3cc3c3cfcc3bc3c8c3c8c3c3cc3c3c6c3c3c7ccffcfcb7b6cfc8cf3c8fcf3ccfc3fcffcc3ccc3c3fcf3ffcfffc3cfcfe3c3fcfec3cf3fefccfcf3fffff3ffff
                    cc3ec3ccfeffffff3fccfffffcffcfc3ccc3fcf3cf8f8ff8fff3fcfcfc3fcfccfcc3ccf3ccfcff8f3cfcfcf3cf3c3cc3cfcff3cfcfcc3cc3cfc3c3f6fc3cfc3cc3ccc63cc36c3cc3c6c67c6c6c6c6c6c6c7c6c6c67c6c7c3c6c67bc7c7cc3c6ccc3cc3cc3c3c6cc3cc83c3cc3c3cfc3c3ccc7cc3cf83dbdbc3cff3cfcfc3ccf3cfcfc3cf3cf3fefcf3fcf8f3fc3fcf3c3efcf3f3fcfcfc3f3fcffcfcfcffcf3f
                    3ccce7e3e3fcffcfcbc3ef3fcf3ff3fcf3ccc3fcffcf3fcffcfcf8f8fcfcfcf3f3cfe3cff3c3fcf3fc3c3c3fcfc3cf3cf3fcccf3f3c3cc3cf3ccfc3fc3cc3c83cc7c3cc6ccc6c6c6c6c7c67c67c67c67c66c6c7cc6cc6c6c6c3bc7c67c3cc3c3c3c83c6c83c83c3c83cccc3ec3cfcfcfc3c3ccff8fcb7c6ccf8fcff8f3fcf8ccff8ffcfcfcfe3f3ccfcffcfcfcc3ccfcf3ffcfefcf3feffeff3fff3fff3ffffc
                    fff3cfccccffffff7cecc3cffcfcfcffcff3fcf8fcfcfcf3ff8ff3fcf3f8f3cfcfcc3cf3cfcfcffcf3fcfccf3cfcfcf3cfc3c3cfcc3fc3c3ec3f3cfc3cc3cfcc3c3cc6c3c3cc3c6c3cc6c7c6c6b6b6b6c6b67c66cc67cc6c3cc7c6c3cc63ccc3c83ccc3cccfcb7c67c7c3cc63fc3f383cfcc3fc8f3b7cc3cfcf3fcfcfcf8ff3fcf3fcf3fcf3cfcff3cfcf8f8f3ef3cf3fcf3fcf3fccf3cf3fcfcfcfc3ccfcfff
                    cfcffc3c3cffcf3fcc7c7cecc3fcffc3fc8fc3cff8ff8ffcf8fcfcffcfcfcffcf3fcfefcf3c3f3fcfcfc3f3ccf3cf3ccfcfc3fcf3cfcc3cfcfc3cf6fc3ccc3c3ccc3c7cc6c6cc6cc6c7c6c7b6c6c6b6c67cc6cc67cc6c7cc76c6b7c7c3cc3c8c3cc83cc3c6c3cc6ccc7c6c7ccf3fcfcf3c3cccf3cbbfc8ff3fcf8f8f3f8f3cf8fcf8fcf8fffcfcfcff3fcf3fec3cfe3fcffcffffcf3cffcffff3fc7cbe7e7c7f
                    f3fcf3fcccfffffcc3cccce7cbe3cf3fcf3cfcfcf3fcf3f8fff3ffcf8f8ffcf8fc3fe3f3cfcfcff3ff3cfccf3cfc3cf3f3cccc3fcfc3bfcf3cffc3fc3fcf3cc3c3cc6c3c3c3c6c3c76c67c6c6c7b6c67c6c6c67bc67c6c67cc7cc6ccc7ccc3c3c83cc38c6c3c83c7c3cc3c3c3cfc3cfccfc7f8fccbc8f3cfcf8ff3fcfffcffcf3f8ff8ffc3fff3ff3cf8ffcf3ffe3fcff3fff3ff3fffc3fcf3ce7be3be3c3fcf
                    cf8fcfcff3fcffffccf3c3cc7ccc3fccfcffcf3fcf8fcfcfcfcfcf8f3ffc3fcf3fef3cfcf3f3fcfcfcfcff3fcf3ffcfcfc3e3cfcf3c3c3cfcf3cfcf3cfccc3cfcf63c3cc6cc6c3b6cc6cc6c676c6c7b6b6b6c7c6c6c7b6cc6c6c7c6c6c3c6c8c3cc3cc3c3ccc3ccf3c3cc3cfc3cffc33c3cc3cf7dc3fcff8f3fcfcff8f3fcf8fcffcf3fcffc8fcfcffff3ffcfc3ffcf3cfcfcfcffccf3fffce7b7e3e3fcffcff
                    ffffffffcffffcfc3ccffcfcf3cfbccf3fcf3fcf8ff3f8f3f8ff8f3fcfcff8ffcf3cfef3cfcfff3f3f3fcfcf3cfc3c3fcc3cc3f8c3ccfc3f3cf83fcfc33fc83c3cfccc3cc6c3cc6c6cc67b6cb6b66b6b6b6c6b6b67c6c7c63c7c6c3c3cc3c3c6c3c83cccc83cc3cccfc3cf3c3fc3c3cfcccccc7bcfcf8fcfcff8ff8f3fcf8f3ffcf3fcf8fcffff8ffcfcfcf3fffcfffffff3fffc3f3efcfc3ecc3cfcf3ffcff3
                    fcf3fcf8ffcfffffc3ccfcffcfffc3ccf8fcfcfcffcfcfcfcf3ffcfcfcfcffcf3ffc3c3fcffcfcfccfcf3f3cffcfcfc3fcc3cfcf3cf3cfccf8f3fc3c3ccc3cfc3c3c3fc3bc3c6bb6c76c6c67c6b6b6b6b6b7c6c7cc6cc6cc7cc7ccc3cc3ccc3ccc3cc83c3cc3cc3c3cfcf3cfc3cffcfc33c63bbc3f8f3ff3f8ff3ffcff8ffcfcf8fcf8ff3fcfc3fcf3ffffcf3cff3fcf3fcffcf3eec3cffcc3c3fcf3ffcff3ff
                    ff8ff8ff3fffcffcffc3cfcf3fc3fc7cffff8ff8f3f8f3f8fcfcff8ff3ffcf3fcfcfc3efcff3ff3f3cfcfcffcf3cf3fcf3ec3c3fc3cc3cf3fc3cfcfc3fc3fc3ccfcfc3cc3ccbd7bc6c7b6bc6b6b6b6bd6b6b6b6c6cc76c3c6c6c63cc38c83cc3c8c3c3ccc3c8fc3fcf3c3fc3cf3c3c3cfc7ccb3cfcfcfcf8ff3fcf3f8ff3ff8f3fcf8fcfcf8ffff3ffcf3ffcff3fff3fcfffffffc3cfc3c3efcfcfffcff3fffc
                    fffcfffcffcfff3fc3ffcf3ffffccfcc3cfcf3ffcfcfcfc3c3ffcf3fcfcf3fcfff3ffef3fcffcffccf3f3fcf3fc3cfcfccfcfcfccc3cf3cfc3fcf3c3cfcc3cf3c3c3cc3cc6c66b6c6c6bd79b6b6b796b79b67c7c67c6cc6cc3cccc6ccc3cc86c3c38cc83c83c3cc3ccfcfc3cfc3cc3c3eccfcccf8f8ff8ffcfcff8fff3fcfcfcf8ffcf3f8ff3cfcfcfffcff3ffffcffffff3ffc3fcf3fccf3f3ffcf3ffcffcff
                    fcfffcfffcfffcffccccfccfcfcfc3fecf8ffcf8fff8f3fcfccffcfcf8ffcff8fcfcf3cfff3ff3ff3fcfcf3cfcf3cf3f3f3ccf3f3c3efc3c3cfc8fcfc3cfc3ccfc3c3cc7cc3cc6c67bdd6bbdd9b9bbd6b9bc6b6c7c6b7cc6cc67c7c3c3c83c3cc6cc3c3c3cfc3c3fc3c3cfc3cfc3ecfef3c3c7fc3cf3ffc3f8f3ffcfcfcf8f3f8fc3fcfcfcfff8ff8f3fffcf3fcfffcff3fffcfe3fecf3fcfcfcf3ffcffffff3
                    ff8f3ffcfffffffcffcf3cfcffffccc3cffcffff3cfffcf3ff3fff8fffcf8fcfff3fcffc3fcfcfcfcff3fccff3cffcfcfccfc3cfcfe3c3fcfcf3fc3c3cf3ccf3c3fcc3cc3b6c6c7cc9bd6d96db9b96d9b6b7b67c6c7c63c3c6cc6c7b6cccccc63c3c83cc83cfc3cfcfff3cff3cf3c3cc3fcccc38ffcfcf8fffcfcf3ff8ff3fcfcff8f8f8f38fcf3fffcf8f3fffff3ff3fffcff3cc3fffcf3ffffcfcfff3ff3ff
                    cffffcff8fcfcfffc3fcfcf3fc3fcfececf3fcfcfffcffcfcfc3cfffcf3ffff3fcfcf3cfeff3ff3ff3cfc3fc3ffcf3ff3fcfcfcf3c3cfc3cf3cfc3efc3cc3fc3cfc3cc3ccc7c7cb6b7bdd6bb76b7b76bd6b6bb6bc6c6ec6c7c3c7b6bc36663ccc6c6ec3c3cc3cfc3c3ccf3cfcfc3cf3fecf3cfcfc8f8f3fc83f8f8fcf3fcf8f8f3cff3ffcffcffcf3ffffffcfcfffffffcfffc3cffcf3ffcfcf3fff3fffcffcf
                    ffcfff8fffffffc3cfcfcfcfcfffc3cc3cffcfff8ff3ff3f3ffffcf3f8fcfcfcfc3c3ccf3fcfcfcfcff3ffc3fcf3fcfcfc3c3f3cfcfc3cf3cfc3ccc3ccf3cc3cc3efc3e37c7bbb97bd9b9d9d9d9d99d6dd9dd6b7b7c7c7c7c6bc6bc6c6cccc66c3b76ccccfcfc3cfcf3fcfc3f3cffcfcffcfc3f8ff3fcffffcff3fcfcfcf8fcfcf8fcfcff8f3f8ffcf8f3ff3fff3fcffffff3fe3fcfffcfffffcfcffccff3fff
                    cff8fff3cf3fcfffcf3fcf3cffcffcfe7ecfffcff3fcfcfcfc3cff8fffcff3ff3cc3ef3ccfff3ff3fcfcfefcfcfcff3fcfcfecff3f3fcfcfc3fcf3cf3c3cfc7c3cc3ec3cecc767bb7bb7dddbdbd6bdb9b6d6dd9dd9bdb9bbbb7dbddbdb7b76b7cbbbb7c63c3cfcf3ccc3cffcfc3c3fc3fc3cc8fcfcf8f8fc3fc8fcf3f8f3fcf3fcf3f8f83fcfcf3fff3ffcfff3fffff3ffcfc3fcfffcffff3ffff3fff3fcfcf3
                    fcff3cfcfffffffc3cfcfcfc3ffcf3cfc7cfcff3ffcfcf3fffff3cfcfcf3fcfcc3ecf7cf3fcffcffcf3fc3ef3fc3cfcf3c3ef3cfcfcfc3c3fccfcfcec3cf3cfec3ec3cec37b7bdbdd9dd9b9b9b9bd69b9b9b9b6b6bb79bd79dd9b97d9b9bb7b6b797cc6ecc3c3fcc3cfc3c3fc3fcfcfcfcf83fcf3f8ff3f8fcffc3cfcfcff3fcf8fcfcfffcffffcf8ffcff3fcfffcfffff3cfefffcfff3fcfcfc3fe3fcffffcf
                    cffcfff8fcffcffccecf3fcfecf3cfc3ec7fffcfffff3ffcf3cfcfff3ffcffffcc3cc7bec3f3ff3cf3ffcfc3cfffc3fcffcfcf3ff3fc3ffcf3f3c3c7ebecc3e3c3e3c3c3bc7bdbd9b7dd6db9db9b79b6bd6b6b6b796bb9bd6b6b7dd6b7b76b67b6bb6cc7c6cfc3fcf3c3fcf3fcc3f3c3ff3fcfcfcfcfcfcff8f3ff8ff3f8fcf8fcf8f3fcffccf3fff3fffcfffffffffcfcfcff3fff3ffcffff3fcfccfffcfcff
                    f3ff8fcffff8ff3c3cc3cff3c3cfcfcfccecfff8fc8ffcfffff3ffcffcff8fc3c3c3bcc3ffcfcfcf3fcf3c3efc3c3c3fc3c3ccfccf3fcc3fcfcffcfc7b7ce3ce3ccc3e3e7bddd97dbb6b6b676b76b6b666b666b66b6b6c66b67b6b67b66b6cc6cbb7c3c7cc3cfc3cfcfcc3fcf3fecffcfcfccf8f8f3ff8fcffcfcffcfcffcf8f3fcfcfc3cfcffcf8ffcfff3fff3ff3fffff3fffcfffcfffcffcf3e3e3fff3ff3
                    cf8ffcf3cffffcfcececcccfccfcf3c3c3ec3fffff3cff3f3fcffcfcff8fffffcffe3fffcfff3ffcfcfcfcfe3fcfcfcf3cfcf3cf3fcfc3cfc3fc3c3c3cc3ce3ce3c3eccccbb7bb7b676b676b6b69b66b9b66b66b6c66b6b6c76b66b6bc6b67bc76bc3e7c7ce7c3cf3fc3fc3c3cf3c3cf3fcf3fcf3fcfcfff3ff8f8ff8fcf8ffcf8f3fcfffcfcf3ffcff3fcffcfffcfff3ffffcfffcfffcf3f3fcc3cfcfccfcff
                    fffcf3fcffcfffffc3e3e3ec3eeccfcfececfcfcffff3fcfffffcf3fcff3fcf3c3ccfc3ff3cfcf3ff3c3e3e3e3f3f3fcfe3fcf3fcfc3cfc3cfcffcffc3cc3c7bc3cc3c7bbbbd7bb6c6b6b6b6b6b66b96b66b6bd766b6c6c76b6c6bc6c76cc6c7bb7bcc3bc73ccc3cfcf3cfcfcfcfcf3ccf3cfcfcf8ff8f3fcf8fffcfff3ff3fcffcfffccfeeffcf3ffcf8ff3ffffffffffcfff3cff3cff3fcfe3fef3ffcffffc
                    fcffcfcfcfffcfcf3fcecb3ecc3c3fc3ff3cfff3fcfcffffcf3fffcf3ffffc3ffc3f3fcfcfff3fccffcece3cfeec3ef3c3cf3cfcf3fcccfcfc3cf3c3cf3eccc3ccf3cc7d77c7b7c76c7c76b6966b66b66b66b66b6b6b6766c6b676c76bc7b7db6bb73cc3ece3e3cfc3cc3c3c3c3f3efc3fcfcf3fffcffcff8fffcff3fcfccfcfcf3fc3fe3fe3cf3fcff3ffcffcff3fcfffff3fcf3cffffc3c3fef3fef3fefcff
                    ff8ff8ffffcfffffcfc3cecc3cfcfffffcff3cfcffff3fcffffc3ffcffcf8ffcffefef3cf3cfcfff3c3c3ece3c3cfc3efcfec3fcfccfef3c3c3cfcfc3ccc33cc3cccc7ccbb7b6c6c6b6b6b6b6b6b9b6b6b6b6b6c6c6c6cb6c6c6c6b6c6c6c6db7bcbc3fb737e3efcf3fcf3cfffcfff3ccffcf8fc8ffcffcfffcff3fcff8f3ff3f8fcfffe7ece7ccfcfcfcff3ffffffffcffffcfcfcf3cffefef3fcffcfffcf3f
                    cff3ffcfcfff3fcff3ffc3eccf3ff3ffff3fcf3fcf3ffff3fcfffcf3ff8ff3ff3fc3fcf3fffffc3fcfce7c7c7cc3e3cfc3c3ccf3cf3c3cfcfcf3c3fcf3c3cc3cc3f3c7c7c76bc7c7b676b66b6b96b669b696b6c6b6c6c6c6c6c67c6c6c6c6b6b7b7b7cf7b47b7e7f3cf3ec3e3ef3cffff3fcffcff3f83ff8ffffcfff8fcfc3cfff3fc3e7c7c3e3e3f3fff3ffcfffcfffff3ffff3fffff3fff3cfcfcffefeffcf
                    f3ffcfffff3ffffcfcfcffc3fcffcffcffffffcf3fcfcf8ffff3ffcfcff3ffcfff3fcfcfccfc3fcf3c7cc3e7ee3eccf3ccfc3fcf3efefe3e3e3ccc3cfccc3cc3ccccccc7bbb7b676c6b6b7b696b66b6b6b6b6676c6766c6c76c6c6c67c76c7ccbbd7cc3b7b7c7cc3efe3cfcfc3fffcf3cfcf3ff3fcffcfff3fcfff8fc3c3cffc3fcfe7bcec3bcccccfcfcfcfff3ffff3fffcffcffcf3fffcffff3fcfcfffcff3
                    ffcfffcf3ffcfcf3cfcf3fffffcfffff3ffcf3ffcf3fffffcfffcf3f3fcfcfffcffcf3cf3c3fc3cc7cc3fccc7ce77ecf3f3fef3ec3e77ec3ecf3f3c3c3c3c3cf3c33e37cc76b6bc6b7b6b69b6b6b96b66b66b6b66b6c7666c67c6b6cc6c6c6c7bddbb7ceb7cec3ec3e3ec3e3cc3cf3fcfc3fcfcfffcffcfcfff8ffffffcfcf3ffcfe7ce3c3ec73e3ff3ffff8fffffffffcffffffffffcffffcfcfcfffcff3fcf
                    cfffcff8fffffffcfcfcfcfcf3ff3f3ffffffff3fcfcf3fff3cffffcfcffff3ff3ff3fc3fccf3f3fcffcf3c3c3cc7c3eccef3ec3c7bbe3ec3e3eccfecc3cfe3ec3ec3bc7b7bc7b7b66b76b66b6b6b6b9b6b66b6b6c6b6bc76b6c6c76c6c3c3c6ddd7bce7ccc3cc3e7cbc3ec7e3cfcfcf3cfcf3f8fcffcffffcfffcf3cfc3fcfcff7cc3cc3c3ecfffcfffcf3fffff3fcfffff3fcf3fcfffcfff3ff3cf3fffcfff
                    ffcff8fffcfcfffff3ff3ffffffcffffcf3ff3fff3f3fcfcffff3fcf3cf3fcffcffcfcfcff3fcfcff3fcffccfec3ccc3ef3ecfe3ebd7dc3c3cc3fe3c3cc3e3c3cc3ecc7c7b6bb7b6b76bb6bd6b696b666b69b6b66b66c66b6c6c76c6c76c6c6c7bbbc7cb7c3cc3e7cc7cc3cbccf3fcfcfcf3fcffffcff3f8fff3fffcf3fef3cf3ce3ec3efcff3cf3ffcffffcffcfffff3ffcffffffff3fff3fffcfffffcff3ff
                    cff8ff3ffffffcfcfcfcffcf3ffffcfffffcfffcffcfcf3ffcfcfff3ccecfff3fff3ff3fc3fff3fcfcf8fcf3c3cfcf3e3ecf3e3ec7ddbc3ec3cc3ec7c7ecccce7c7c7b7bb7b76b6b6bb67966b96b6b9b96b66b6b66b67c6c67c6c6c6c6c6c6c6c6767c7cccc3edb7cfc3feb7e3ccf3f3c3fcff8fcf3fcfff3fcffc3fcfefcffcfc3e3cf3c3effecfcff3cfff3ffffcfffcfff3fcf3ffffcfffcf3fcfcff3ffcf
                    f3ff3fcfcffcfffffffffcfffcf3fff3fcffffffcff3f3fc3ffffcfcc3ef3ffffcffcfcf3fcfcfcf3fcf3fcfcfc3ccfeb3c3ec3ec7c3fcc3e7e7c7b7c7b7777c7cb7b7c7bb7bb7b76b79b6bdbdb9ddd6bb6b6b66b67b66b6b66b6c76c6c63c6c67bccc6c7c7bc7ce3c3fec3cc3e3cfcfcfcf3cff3ffff8ffcff8fffcfcf3fc3fe3cff3cfccfc3f3f3fcffc3ffcf3ff3ff3fc3cff3fcfcfffcf3ffcf3f3fcffcf
                    cffcfffffffffcffcf3fff3ffffff3fffff3ff3ff3cffec3ec77c3f3ef3ffcf3ff3f3ffcfeff3f3cfc3cfc3f3cfcf3e7bbee3cc3ccee73ecc3ccc7cc7c7cc67bc77bcbdbbdbdddd6dd6bbbb9d9dbd7bb96b6d6b6b6b6b6b67b6c76c67c6cc6c3ccc63c3cc6cc7c7c3cfe3c3fcfcfc3fc3f3cfcf3ffcf3ff3ffcff3ff3cfcffe3cffc3fc3cf3ccfcffff3c3cfffcffcfcfc3ffcf3cff3ff3f3ffcfffffcffcf3f
                    ffcffcffcf8ffffffffcfffcf3fcfffcf3fffffffffc3cfe3fc3ece7ecfcfcffcffcfe3cf3ccfcffc3cf3fcfef3cccf7b7e7c3ec3e37cec3ec3c3c77c7c77bb7dbbbd7bd7d7b7bbdddddddddd7b7db7dbb976b6b766b666b6c676b6c6c76c6c6c63cc6c63c7cb7cfcc3cfcfc3f3ffcf3fcfc3fcfcff8ffcfcf3fcfccff3fcfcff3cfcfcfc3efefe3fc3fcfcfcffcfff3fcfcf3effcfcfcffcfff3cfcfff3ffff
                    cfffff8fffff3fcffcff8ffffffffcffffcffcffcff3fe3fc3cf3c3c3e3e3ff3fc3f3fcfcff3fe3ecfe7ec3cfef3c3cee7c3ee3eeece77c7c3e7eccc7c7bc7bdbd7d7bd7dbdbd7dddddddddddddb7bb67b7bdd6b6bb6b6b676b6c6c76c6c763c6cc6c6ccccc6c7cc3ffc3c3eccc3cf3fcfcfcf3fc3ffcfff8fcff3ff3cfcf3f3cfff3fc3fffcfcfefccc3ef3fff3cfce3fc3fffc3f3f3ffcffcfff3f3fcffcff
                    f3fcffff3fcffffffffff3fcfcf3fff3fcff3ffff3feffc3fcfe3fe3ec3eeecfc3fefcf3fc3fee7c7e7b7b47b3efcfc3c3ec3ee37c3bec7e7c7c7c7c7c7b7dd7d7bbb7bdbd7ddddddd1ddddd9d7db7bb7bbb7dd9b97b6b7c6b6c76b6c76c6cc6c63c63c63c7c3bb7ebe3ecc3c3cffcfcfc3f3ccf3cf3fc3ff3fcfcfcfcf3ffcfff3fcffcfe3fefc3cf3fe3ecfcffcf3ecfcfcf3ffefefff3f3fcfcfcffcff3ff
                    cfff3fcfffffcfcffffffffffffffcfffffffff3ffff3fffc3cfc3cf3fe3c3e3cfcf3fcc3ece7c7e7bb7b7bec3ef3e7eec3ec3ece7e7b7c7c7c7c7c7c7bbb7dbddd7ddd7dddddddd1dddddddddb7bb7bb76d9bb7b7b6bb9dd7b6b6c76b6c76c7c6c7cc3c7c6ec7bb7bcc7ccc3cfc3c3c3cccfcfccfccf8fcfcf3f8f3ffeffff3ffcff3fcffcff3fefcfe3ec3effcf3c3f3cf3fefc3cfc3fcffcf3ff3cf3cfcf3
                    ffffcfffcfcfffff8ffcfcf3fcfcff3fcf3fffffffcffcf3ffc3fefefe3c3e3e3f3fef3cfe3e7eb7b7b4be3c3e3ec3b77ec34bc7bbbb7e7cec3ec7c7cc77bc7b7bb7b7eb7ddb7c71d97ddd9dd7ddd7d6bb7b7c7b6b6d7d7dbb76c66b6c6c6c6c63cc6c7cc7c63cc7bd7bc3c3cfc8cfcfcf3fc3c3c6c3c3c3c3ccfc3fc3fe3fcffcfffcf3f3fc3ef3fe3ec3ec3fffffccee3efcf3ffc3fcffcf3ffcffffffcfcf
                    fcffffcfffffcfffffffffffffff3ffffffcf3ffcffffffcfcfcf3f3cfcfecfeece3cfe3e7ece7eee7b7e7e3cfc3ee3ec7e7b7b7d7b7db7e77e7c7c7c7b67b7bb7bbbdbbbb7bec7ddddddddddddd9b777b7ce7c7b7eec7eb7b6c7b6c767b67c6e7c7c6c7c63ec6cc7bb7bccc83cf3cf83c8fcfcfc3cc3ccbbb7b7bbcccc3eff3fff3ffcfcfffffcfe3e3ec3ecff3cf3c3fcf3fefcffcffcf3ffefffcfcf3ffff
                    ff3fcfff3fcfffcff3ff3ffcf3ffffcff3ffffffff3f3ffff3ffcfef3c3cf3e3c3ec3e3eec73b7e7e7e7be3cc3e3e3e3e7bd7b7bb7db7ec7ccc77c7b7b7bbdb7bb7d7b7dd7db7dddbddddddddddbd7bbb7e3e3ec3ec3e77bb7c66c7b6bc7c6c76c6c7c7c7c7c7c3cc6c6c3c3cfc3cf3cfcf3c383cf3fcf7b7bb7bbfff3ccf3fcffcfcf3fc3e3cf3ec3efc3efe3ffffcfcc3fef3fcfffcf3ffcff3cff3ffcff3f
                    cfffff3fffffcfffffcfffffffcfcffffffcffcf3fffffcfffc3f3fcfcf3ef3e3e3ee3ee3e347e7ec3ee7ce347ec3ece7e7be7b47ee7e3c3c3ec7be7cc7bb7dbd7b74bd7b47bbd7b3d7bd7dd7d7dddd7dbbe3e3ee3e7ccc77b7bc76cb76b67c7c7c7cddbdcc6c3c63c3ccc3cc3cfc8c3f83cfcfcfccc3cfc3eeecf3fcf3fefcff3ffffcfffffccc3efc3ec3e3ffcfffef3ef3efcf3cf3ffcff3fff3ffcff3fcf
                    ffcffcffcf8fff3fcffffcfcffffffcfcfff3c3fffcffff3fffcfcf3fccfc3efe3e3ee3e7ece7ec7e7e3e3ec3c3ef3c3e7e7ee3ec7e7e7ecfe77e7c7c7b7bbd7bb7be7ee7ce73beee7e77b7e77c77b3cf3c3ece3e7c7c77cbbb7bbdbb7b7cc7c6c67c7db7c7c3ccec7c3c3cc3cf6f3fccfcf6fc3c3cfc3ccc33f3fcf3cfe3ff3ffcf3ff3cfe3f3fcf34e7ce3fcfffcf3cccec3e3cffffcff3ffefcffff3fcff3
                    cffffffffffffffffffcfffffcffcffff3cccecfffff3ffffcff3fcfc3f3fcf3cfec3e3ec3e3e7e7ecece7c3ec3c3fe3ec7c7c7c3e3e7d7f3f7ec7f3b7c7e7dd7be7e33e3c3efe7e3eeeee7cc3ece7eb7ce77e77c3e7ce7b7bdd9bd7d6cc76c7c7cb7cc7c7c7c7c73ccc7c3cc3c3cc3c3c3cf6fcc3c3c83c3efcfcf3fef3fcffcffffcfff3fefec3ee3e3e3eefffffcf3f3c3ecfefcf3fcffcfffffcffcff3ff
                    cf3cf3fcfcffcfcffcfffff3fff3ff3fcc3c3c3cf3fffcffff3ffcf3fcfef3efc3c3ece3ec3ec3ce3e33e3cc3ccfcf3e3c3ef3eb7bc3ebb3ef7e3c3be7bbbb7ece3e3ee7e3ef3c3e3c3e3e3e3e73e77bb7bb7c7e7e7e7ce7e7c7bdbdbd77bc76c7cbdbbddb7cc7c6c7c3cc7c7ccc3ccfccc3c3c3cc3ccfcfcf3f3fcfe3cfcf3ff3f3ff3ccc3fc3fe3ecc3efe3cffcf3ececce3fe3c3fcf3fcff3fcff3fffcfcf
                    cfffcfffff3ffff8ffffcfcfffcfffc3fcffcfcffcfcff3ffffcffcfcf3fef3cfcfe3e3c3ee3ec3ec3ecc3cfc3fc3fe3ece3cfc3e7be3e7cffe3efb7b7b7ddb7e7be7ee3ebfeffecfc3b7eb7c7ebbbe7b7b7b7cb7ce7c37c7c7b7d7b7bc767cc76c77d7b7dc7c67c7c7c7c3cc3c3c3c3c3c83cc7ccc3c3c3e7cec3cf3cfe3fcfcfcfcce3efe3fe3ef3e3ec3cfcffffe3c3e3fc3fffcffcfcf3fcff3fff3fffff
                    3cf3ffcffcfffcffff3ff3fc3fffcffcffcff3fffff3ffff3fff3f3fcfcf3cfc3c3cf3ecfc3e3ec3ec3e3ec3cfe3fcfcf3cf3ffefe7bc3bcf3ecf3be3ece7bddbdbd7ece77e3fce7cc47c7dddb6b7b7b7bcccb7cb7bc7ee7cb7b7b7db7b7cb67c7b7cbbee7cc7cc7c7c7c7c77c7ccc3cc3c3cc3c7c7cec3ecc3e3fe3fe3cc3f3cf3c3b7bcf3ecfe3ee3e3efe3ef3ffc3ee3ecfe3ef3cf3ffcffffcffcffcf3ff
                    e3ffcf3ffffcff3c3ecc3ec3ecfff3ffcf3ffffcf3fffcfffcffcffcf3fcfcf3fcfc3e3e3cc3c3ef3ee7ec3efe3fcf3f3cfcc3c3e3fe7fe3fcf3fe7fc77bb7b7b7b7b7b7dbeecfec3b7cbddb6b7bb7b6bb7d9ddddbbdd7bb7dbbb7b7b7b7c7c7b7b7b7e7bb7c767c7c7c7b7c7c7c77cc3bbbecc3c3c3c3ec3ce3ef3effcfccee3fece7de3cff3e3e3eecc3e3ee3fcfce3ee3e3efe3effcff3fcf3fffffffffcf
                    cfcfffcfcfff3cffcf3ffc3e3e3e3fcffffcffffffcfff3fff3ffcffcf3f3fcfef3efecfcf7ccf3ec3c7c3ef3c3e3e3efc3fffcffb3fe3feff3fec3c7e7e7ecfc3ecebddddc3e3c3ebce7bbddddd9ddddddddbb7bddbddbdbd7d6bb7b6bc7b6c6bc7e7b7b7b7c7cc7cc7c6e67c7bc7c7bb7c7b7ecec7cb7b7c3ec3fc3cf3ce7eee7febc3ffe3efece3e3fe3e7ebfff7e7e7ce3ec3ef3fc3fcffcfff3f3f3fff3
                    c3cf3f3ff3fcff3ffffcf3fcc3e7ecf3c3fffcffcff3fcffcffff3f3ffccfcf3fcfc3c3e3ccc3ec7c7cb3fcc3efcf3c3e3ec3ff3cfe3ccf3fcff7ffe7cecc7b7bbb7b7ddd7bcbefbb7cdddd7dddbdbdbdd7db77b7b7d7d767b67b7b6b7c76b67b7b7c7be7b7bb7c7c76c77c7c7c7b7ccb7eb7ecc7b7c77c7c7cf3efcfcfe7be3b7ec3efec3fcfc3e3e3cccee7c7eff7b7ce7ce7ec3eccfeff3ff3fcfffffcfff
                    ecfcfcfcffcf3ffcf3ffcfcf3ecfc3ecfcff3ffff3ffff3fffcffcffcf3ef3fef3cfcfcfcf3b6c7ccc7ccf3fe3f3fffffcf3e3cffc3cf3cffffcf3e7cf3e7e7bd7dbdbddbc3b7bf7efebd7ddd7bd7dbd7dd7d7b7b7bbb7b7bc7c7b7b7c7b6bb7b7c7ee77e7e7c7c76c7c7cc7bbbbbb7b7bbbb7e7c7cbec7ccc3ccf3cf3e7b7b7be3be3c3fefc3fe3ecfc3c3ec3c3ffcce7ce3c3f3fff3ff3cfcffcfffcffff3f
                    e3f3cff3fcfffcf3fcf3ff3cff3e3e3e3c3cffcffffcfcfcfff3ffcffce3cfcf3fcf3c3c3cfcc3cf3fc7cfcfccfcfcfc3c3fcfc3cfcfcff3ff3fcccffc7c7bbbbb7b7d7ddcfefcfef3b7db7dbd7db77b7dc7b7ebeb7d7bbb67c7c7c7c7b6b7b7c7bc73ee7b7b7b7b7b7bc76b767b7bb7bb7dbb7cec7ec3ec3ee3ee3eee7bee3ec3ec3efee3cfcfe3c3e3ecc3efecff3e3e3cfffcfcfcfccffff3fff3fff3ffff
                    3fcc3fcff3f3ff3fffcfcfcfcfcfe3ec3ffffff3ffffffff3fcff3ff3fcff3ffcf3cfcffcf3ffffff3cf3fff3f3f3fffffef3fcfcf3c3feffffff3cf3bc7c76d7db7b7d7de3cf3cfcfbb7bb7b7b7bb7b7c3ee7c77bb7ebbd7e7ee7e7e7cb7b7b7e77ec3e77b7c6cc7bc76b7b7bb7dd7b47b7be7e7bc3ec3ee3ce7c7e7bb7b7be3e3cc3e3fcf3e3ccccfef3e3e3f3ffe3fcff3cffcffff3fcf3ffcffffcfffcff
                    fccccf3fcfcfcffcfff3ff3ff3f3cf3ececfc3fffcff3fcfcff3ffcff3cf3fcffcff3fcf3cfcf3c3fcfcf3cfcfcffcf3cf3fef3cfffceff3ffcf3ffe7c7c7bb7b6db7eee7cffcff3ff7bb7cc7cc7c7cbe7be7ceeb7ee7777ece7c7ece3e3b7e3e7c3e3e7e7cbc76b676b7bbbbbdbdbb7bebe7ebbb7be7cc3c77c7ec7b7b7be7ee3fccfcf3fefcf3f3c3c3efefeceffcfe3ecffcf3fc3feff3fcff3fcfff3fff3
                    fc3e3fcff3ff3fff3cffcffcfcfcfcff3f3cfcfcffffffff3fcfcff3ffffcff3f3fcfcfcfcf3eccc3f3cffff3effffffffcffecfc3f3f3ffff3fffc3cffcc7c7b7b7be3e3e3cffcfefc7cc76c7c6c7b7bb77e777e7e3ecce3e3e7e3e3e3cfe7cc3e3e3e7c7b7bc7b7bb7bb7b7d7d7b7bd7b7b7b7be7c3e3bececc7c7c7ee3ee3ccc3c3cfcf3fffcffffffc3c33e3fcf3ef3eff3feffef3cfcffcfffff3fffcff
                    fec3ecf3fcfcfcfcff3ff3ff3ff3f3cfe3e3fffff3ffcf3ffffff3ffcfcff3fcffcf3f3fcfcfc3c3ccf3cf3cf3cf3ff3fff3f3ef3ffccfcffcfffcfffe77e7bb7ce3e3e3ecfefcffc3fec6c3bc67bc7c7ecc3ecb7e7c3e3ee7ec3ee7c3ef3fc3e7c3e3e3ebb7b7bbbbbb7b7b7b7cb7b7ddbb7bbd7bee7eb7e37e3bcecc3ec3cf3e3feffffcff3fffcffcffffec3effcf3ecfe3ecfc3fcffff3ff3ff3fffcffff
                    e3efe3fcf3ffff3ffcffcfcffcfcffc3cfcec3cfcfffffffcf3cffffff3ffcff3fffcfef3f3fc3c6c6cc3cffcf3eccffcfcfcf3cfef3fcffffffffc3c3bb7b7e3e3e3eccff3cf3cfecc3cf3e67cc6c7cc73ee3ee7ec3e3e3e3e7e7c3ec3cfcfc3fe3cc3e77bbb7b7d7d7bbc7bbb7bb4bb7b7b47be7c7bb7ec7ccc3e33cf3fe3ec3eefe7e7e7ecc3ffffffcfffffe3f3fe3f3ffcf3cfe3cf3ffcfffcfffffff3f
                    c3c3efcfcfcf3ffcff3fff3fcf3fcffff3f3ee3fffcf3ffffffffcfcffcf3fffcf3ff3fcfcffcfc3c3cffc3e3ecf3f3cf3fffcffffffcf3f3ffcf3fffe74e3e3e3ee3c3fe3fcfcf3cfffffc7cb3b7c67cee3ec3e7c34ee7e7e3e3e343e3ef3f3fcfc3fe7eb77b7bb7bdbd7ddb7db7e67ee7db7e3e7bb7bb3bf3cfec3efe3cfe3efe3b7b7e7c7eec3ec3c3ffcf3fcfcfcfcfeffffcf3cffcfcffcfffffcff3fff
                    ccfe3f3cf3fcfcff3ffcf3fffffff3fcfecc3ccf3fffffcfffcffff3ff3fffcffffcfcf3fcf3f3fccc3fe3cfcf3fcfcffcf3fe3fc3e3fcfeffffcfc3e7e3ce3ecc3ccfe3cfef3ffff3fc3c3cbcc3c7c7c3e7c7b7ee7c7c3e7b747e7e3eb3cfcfcf3fc3e3c7e7e7e7b7b7bb7bdd7be3eb7bbee3cfcf3cf7eb3ef3f3efc3fcc3ec3e7be7bbe7be77ee3ec3ec3fffffffff3fcf3c3ffcf3cf3ffcfff3ffffffffff
                    3c3ecfefcff3f3fcffcffcfc3fcf3fcf3f3fef3efcffcfff3fff3fffcfffcff3fff3ffcff3fefefe3ffc3fcf3ffffff3ffefcfc3efcfe3e3effff3eeee3e3ec3ccc3e3fefe3fefcfcfffffec37cc3c7cc3e7b7de7c3e3ee7e7be7e3e7b3ef3fff3cf3c3e3ee7ec7eee3e7bd7b7ec3cfe3fe3efc3beee7ec3ecfcffc3fcf3e3e3ee7b7be7e7e7ce3be3ec3cfe3ccf3fcfcc3cfcfcffffcfcfcffffffff3ffcfff
                    efcff3e3f3cfefff3ff3ff3fff3ffcffcfcf3ec3ef3ffffffffcffcfffcff3ffcfffcff3feffcf3cfc3fcffcffcf3fcfe3e3e3fcfe3e3ecc3f3c3ee73ecce3ef3cfcfef3fcfcfffcffc3ef3fef3cc3ec3becebd7bee3e3e3ee7e7ee7e7ec3efcfffcfcfee3e77ec37e7ee7bdee7ee3e3ec3e3cce777c3e3ef3cfcf3fcfcfccee7b7be7e3ec3e3ec3ec3cc3e3e3fcffffffffcfff3ffcfffffff3fffcffffff3f
                    fff3fcffcfcff3fcffcffcffcffcfff3ffc3fcfe3effff3ffcfffff3fff3fffff3fff3fcfff3f3fe3fef3fcfffffcfe3ec3efe3e7e7e7c3cffcee37ce3e33e3ec3efc3fcf3ff3cfff3cfcfe3c3e3fe3e3e3e3ece3fee3ee7e73e3e7e7e3efc3f3fcf3fe33c3ec3e7e3e3e7e77e7c3cfc3ecfef3eeee3ece3ef3ffccfcf3cf33e3ee3e3cf3cfef3cf3ec3eecc3ccfc3fcffcf3cfcfcfff3fff3fffffffffcffff
                    fcffffffff3cffff3ff3ff3ff3ff3fcff3ffcf3fc3cffffffff3ffcff3fffcf3fffcffffcfcffcfcfe3fcff3cf3fcf3fe3ef3cffe7e7cce3ce3e3ec3e3eccfef3feffeffefefffcfffff3cfcfcfc3fc3c3ec77efc3e3e7e3e3ee7e3e3ee3efffff3ffc3efee3ee3e3ec3ec3eb7ec3e3ec3e3c3e737ee3c3fe3ec3fc3feffeffcc3fefcfcff3fcfc3fc3e3c3cfc3ffcf3cff3ff3ffff3fffcffffffffffffffff
                    cffcffc3fcfffc3fcffcffcfffcffff3fcfcfcf3cfeffcffcfffffffcffcfffffcff3fcff3ff3ff3cfcffc3ffcfc3fef3ffeffcfffc3e3ee3ee7c3ec3c3c3e3ccc3efc3ff3fcffffcfccfe3f3c3efefcfe3cfe77ee7e3e3e3e343e3ee7ec3e3cfffcf3ff3c3e3c3ec3ec3ee3e7c3fccfe3ec3efee3e3e3fe3fcfe3ccf3c3fc3fcfe3ff3fe3fef3feffcfeffc3efcfffcf3fffcfff3ffcfcffcfcff3ff3fff3ff
                    fffff3fffffcfffff3ff3ff3fcff3fcffff3f3fcfcf3ffffff3fcf3ffffff3fcfffffff3ffcffcffcf3fffcf3fcfcf3feff3fff3fffee7e3e7c3ee3ccfecc3fcfefcf3fefcff3ffff3ff3fccfef3e3c3cfc3e3ee77e7eee7ee3ee7e7e73ec3cffcff3cfcfffc3ec3ec3ef3ec3efec3c3ec3efe3c3e3e3ecfec3cfcf3efcfefef3cfc3ecc3ef3cfef3cf3c3cfcf3fc3f3fffcfffcffcffff3ffffffffffffffff
                    f3ffffffff3ff3cfcffcffcfff3fcfffcf3fcffff3fecf3fffffffffcf3ffffff3ffcfffcff3ffc3fcfcf3ffcf3ffcfff3fcfe3fcf3f7e7ec3ee3ccf3ef3ccc3cfcfffcfcfcffcf3fcfefcf3e3ee3fcf3e3ece3ec3ee73e347b77bd7bbd7ecf3cf3fcff3fc3cf3ec3ff3fef3ef3fcccc3fe3e3e3efefcf3ef3fef3eff3e3c3fcfc3efcf3fefef3cfcfcfcfe3fefcfffcfcffcff3fcfcf3fffcfffffffffcffcf
                    fffcffcf3ffffffff3ff3ff3fcfff3f3ffcfffc3fcff3fffcffcf3fffffcfcffffcff3fff3ffcffcff3ffffcffcf3fcfcfcf3ffefcfcc3e3ec3cfc3ec3ccf3fef3fcffff3ffcfffffcf3f3cfcc3ee3cee7e3e3e7ee77e3ee7e7ebd7dd7db7c3efffff3cffffcffcfe3eff3fcfccf3e3cfe3fe3ecc3cf3ec3efefcfc3efcfcc3c3efc3cccc3cfe3fc3f3fc3ec3fcf3eff3ff3f3fffff3fffffff3fffcffffffff
                    ffffffffffcfcff3ffcffcffff3fcfffcfff3ffcfffcfcffffffffcf3fffff3fcff3ffcf3fcff3ff3fcfcfff3ffcfff3ff3efcff3fe3ee3e3fe3efe3fef3efefccffcfcfcfcf3fcfcfccfef3fef3ef3e3e3e3ee77e3ecc3cfcfc34e7ebe7e3ef3fcffffcfe3fef3fffffcfff3f3cfcfe3efe3ef3efcccfefc3c3f3ffe3c3fefefe3ef3fcfef3cfefcccfe3cfef3fff3fefcfcfefcfcfcffcffffffffffff3fff
                    3fff3fffcffff3ffcff3ff3fcffcffcff3fcfcfffcff3fff3fcffffffcff3ffffffffffffff3ffcfcfff3fcffcff3cffcfccffc3fe3e3ecce3cfe3fef3efc3f3fc3fff3fff3fcffff3ff3fccf3cc3ec3efcfe3eee7e3fcf3e3ccc3cf3e3e3efccff3fcff3fec3ffcfcfffcfcfcffc3cfe3e3fee3e3cf3e3ccfefefefcfecc3c3e3e3efe3f3efc3f3fcf3ef3cfcfcfcffcf3ffcfffffffffff3fffffff3ffffff
                    ffffffffff3fffcfffffcffcf3ff3ff3ffffff3fff3ffcfcffff3fcffffcfffcf3fcf3fcf3ffcffff3cfcf3fcf3fffcf3fe3c3fecfeec3c3cffe3cf3ef3fcfefcfcfcffcfcfffffcfcfcfcf3efcfcf3fe3c3ef3c3fcfefefef3fcfe3e3efcf3f3cffff3cec3fcff3ff3fff3fffc3fcf3ffcfe3fefe3ecfe3fe3f3e3f3cf3fefe3efef3fecfc3fefef3effcfcf3ffffff3fcff3fcf3fcfffffffffff3ffffffcf
                    fffcffcf3ffcffff3fcff3fffcffcffcfcf3ffcf3fffffffffffffff3ffffcfffffffff3ffcfff3fcfff3fcffffcff3fceffefe3e3e3cc3fe3cfc3efcfef3ff3f3fcf3ffcffcfcf3ff3fc3fef3fc3fefcfefccc3efe3c3c3c3ef3efefcf3fcfcfffc3cfc3cccfcffcffcfffcf3feffcfef3fcf3e3ffc3e3ef3eccfecfcfef3cfcf3cfe3fc3fef3fc3ffc3ff3ffcf3fffcffcffcfffff3ff3fffffcfffffcffff
                    fffffffffffff3fffff3ffcf3ff3ff3ff3ffcfffffcffcf3fcffcffffcf3fff3fff3fcffcff3ffcffffcfff3fcff3fcf3c3e3c3e7cc3ccccfcf3eff3fc3cfefefcffcfcff3fffffcfcfcfcf3cccfef3e3c3c3ccfe3fe3fefefcef3c3f3fef3cfc3ffffc3ef3f3ffffffff3ff3efcf3ff3cfe3ecfefe3efe3cf3f3cf3e3c3cfc3fef3cfe3fef3efcfcfcffeffcfffcfcffcf3ff3ffcfffcffffcfffffffffffff
                    ff3ffffffcfffffcffffcff3ffcffcfffffcff3ffffffffffffff3fcfffffffffcffff3ff3ffcfff3ff3fcfcff3fffcfefcfc3eccf3ef3fe3fef3fecfffcf3f3fcf3fff3fefcf3ff3fcf3fefc3c3fefe3fecc3e3fe3ecc3e3e3fcfcfefefcff3fefcf3fcfcfcffcf3fcfffcfcf3fccecefe3cf3e3cfe3c3efefec3ef3fefc3efe3cfc3cfe3efcf3fcf3fcf3fff3fff3ff3ffcffffffffffcffffffffffffff3f
                    fffff3ffff3fcf3ff3fff3ffcff3ff3fcf3ffffcffcf3fffff3ffffffffcf3ffff3fcffcffcfff3ffcffcfff3ffcf3fcf3f3ec3fe3efec3fe3fcfef3cf3cfefef3ffcfcffcffffcffcf3ef3fcffef3c3ee3e3ece3ef3e3fef3fe3f3c3c3f3cfef3fffcffcfffcfffcff3ffff3fcff3e3c3fcfefcc3e3fec3cf3fcc3efef3efcf3fcc3fe3fef3fefcf3fcfffcfcfcfcffcffffcfff3fff3fffffffffffcffffff
                    fffcfffcfffffffcfff3ffcff3ffcfff3fff3fffffffffcffcffffff3ffffffcfffff3ff3ff3fffcfff3ff3ffcffffcf3fecfec3cfc3fccfcfc3f3fcfffc3e3e3fefff3fcf3fcff3fcfe3efe3fc3ccce3cc3ef3cc3ecfec3efcffeffcfcfcf3fccfcfffff3ff3f3fffffcf3cfcffcff3fcc3c3cf3fefe3ef3fef3efe3fef3fcfccfcccfe3cfef3ff3feff3ffffffff3fffcffff3ffffffffcff3fff3fffffcff
                    fcffffffffcf3fffcfcffff3ffcff3fcffcffcff3fcffffffffffcfffcf3ffff3fcf3fcfcffcf3fff3fcffcfff3fcf3fcfc3e3fcc3fcf3f3f3fefcf3cf3fe3e3eff3fcfcffcf3fcfc3eec3cfcfcfe3c3efec3efcfe3e3c3ec3e3e3e3fef3cfcf3fcffc3fcfcffffcf3fff3ffcf3c3efecfcfef3ece3e3fe3effcf3e3cc3ccf3fcf3cf3effcf3fcfcfcf3cfcf3f3f3ffcf3fcf3ffffffffffffffffffffffffff
                    ffffffff3ffffcffffffcfffcff3fffffffffffcffff3ff3fffcfff3ffffcf3ffcffcf3cf3ffffcffffffff3ffcffffcfe3ccfcf3fefcfefefcf3fcfcffefc3efe3effe3cf3fef3fefe7cfc3cf3f3fefc3e3efcf3fe3fcfeeebbbbbb7eeee3eebef3ffffffffcfffffcfcfcf3efcfe3f3e3f3efcf3ffcf3ffcf3ec3fcfef3ffcfcf3ef3ef3feff3fcfcfff3feffffcfffcffffcfffffcfffffffffcfffff3fff
                    fffffffffcf3fff3ff3ff3fcffffcf3f3f3f3fffff3fffcffcfff3fffc3ffffcff3ffcfffcf3fcffcfcf3fcffcff3f3c3ecf3f3cfcf3fcf3fcf3fcf3ffc3fef3cfff3cffc3effcfe3c3e7effefefcf3ccc3ecf3fefcfcfc3c3c3e7bdbd7b7be7e3ffcfcf3f3ff3fcf3fff3fcfcf3e3ee3fecfe3cfecf3fefcf3fcfecf3efccfc3fcffe3cffcf3ffcf3ffcfcfffcffffcffcf3fffcffffffff3fffffffffffffc
                    ffff3ffffffffcffffffffff3f3ffffffcfffcf3ffffcffffff3fffc3fcfcfff3ffff3fcffffff3fffffffffff3fcfcec3fccfcffcfcf3fcf3fcffefcffe3fcfc3cfcf3cfff3cf3cfee7c3ef3cf3fcff3fee3cffcf3ffcffffcfcce7d4bee7ec3cff3ffffcffcff3ffcf3fff3ffcfc3ffe3c3cfc3f3effcf3fcf3e3fef3fcfffff3e3fcfc3ffcfcfffcf3fffcfffcfffff3ffcfffc3ffff3ffffffffffcfffff
                    ff3ffffcffffffffcfcffcfffffcf3fcfffcfffffcfffffffffffcfcfcff3f3fffcfffff3fcf3ffcf3fcff3fcffff3e3ec3fcf3fcff3fcfcffcfcffff3cfcf3fcffcfcfc3efcfcfc3e3ecc3ff3cfcfcfec3effcf3cfcffcfcfcf3c7b47b7cc3e3cfcff3cfff3ffffcff3fcfcfcff3fcc3cfefcfe3fffcff3efffcff3fcfef3fc3fcfe3cffcff3ff3fcffffcff3f3ff3fcfffcfc3ffffcfcfffffcffffffffcff
                    3fffffff3fcff3ffffffff3fcffffffff3fff3ffffffffcff3fffcf3f3fffffcfff3fcf3ffffcfffffff3fffffcfec3e3cfcfcfff3cfff3fcff3ff3fffcff3fef3cf3f3ffcf3f3cfe3ec3ffecfcf3fcf3fe3c3fcffcfcff38f3fcceb7cec3eecff3ffcfff3fffcf3f3fcfff3ff3cffffcfe3e3c3efef3cffff3ff3fcf3fffcffccf3cff3ff3fcfcfff3fcff3fffffffffffffffcffcff3fffcffffffffffffff
                    ffffffcffff3ffffff3ffffff3ff3fcffff3fffcf3fcfff3fffcf3fcffcf3fff3ffcffffcf3ff8f3fcffffcff3ff3cfcfe3ff3fcfffcfcff3fcffffffff3cfeffcf3efefcfccfef3ec3efe3ff3fcfcfce3effeffcffff3ffcfcfcc7ee7be7e7fcffcff3fffcfffffcfffc3ffcfffcfe3c3feffcfcf3cffcf3cfcfcffcfc3f3f3f3fffecfcfcfff3fcffcfffffcffcffcf3fcff3ffcf3cffcffffffff3ffff3ff
                    ffffffffffffcffcfffffff3ffcffff3fcfffcfffffff3fffff3cfcf3fffcfcffcff3f3ffffcffffcff3fffffffcc3e3efcfcfff3fcf3fcffffcffcffcfcfff3ffcfff3f3f3fc3ef3cf3efcfefcf3f3fcfc3cf3f3ffcffcfff8fc7ec7ee3ece3c3ff3ffcfff3fcf3fcf3ffcffcf3f3eeee3f3ef3fcfcf3ffffcfff3f3fffcfcfecfe3ffff3ef3fef3fcff3fcfffffffffffffffcfffffcff3fffffffffffcffc
                    """))
            elif tiles.tile_at_location_equals(tiles.get_tile_location(player1.tilemap_location().column, 64),
                assets.tile("""
                    myTile60
                    """)) or tiles.tile_at_location_equals(tiles.get_tile_location(player1.tilemap_location().column, 64),
                assets.tile("""
                    myTile61
                    """)):
                scene.set_background_image(img("""
                    9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9dd9dd9dd1dd9dd9dd9ddd9d9dd9bd9dd9bd9ddd9dd9bd9dd9bd9b9bd9bddddd9dd9bd9b9bb6b6b6b6b6b6b6b6b6b6b6b6b6c6c6c6c6c6c66c6b6b6c6b6b6c6b6c6b6c6c6c6c6c6c6c6c6c6c6c6c6c6c6c6c6c6c68c6c68c6c6c6c6c6c6c6c6c6c6c6c6c6b6c6bbb6b6bb6b6c68b68b68b68b68b68b68b68b68b6a66a66a66a6
                    1191d919d919d919d9d9d9d9d99d99d9b99b99b99b99b9b9b9d9d9d9d9b9b9b9d9dd9dd9d9d1d9dd9dd9d9ddb9bd9db9bd9dd9d9b9bd9bd9bd9bdb9b9b9d9d9dd9bd9bdbb9b9b6b9bb6b6b6a6a6a6b6b6b6a6a6a6a6b6a6a6a6b68b6a6a6c6a6c6a6cb6a68c68c8c8c68c6c6a6c6a6a68c68c8c68c688c6c86c6a6a6a6a6a6a6a68b6a6b6a6b6b9bb6b6b6a6a6c68b8c68a68b68a68b6a6a6a66a66a6a66a66a
                    19d91d9d1d9d9d9d9d99d99d9d9b9d9d9d99d99d99b9d999d9b9b9b9b9d9d9d9bd9d9d9ddd9ddd9dd9ddddd9b9d9d9b9d9b9db9ddb9bd9bd9db9d9bdb9bd9dd9ddd9bd99b9b6b9b6b69a9a66b66b6b9a6b66b666b66a66c6b6b6a6a6b6b6a66a68b66a66cb6ca66c6a6c6a6a6a6a66c6c6a6c6a6c6a6c6a6ca68686c666c666c6c6a66a66c6a6b6b9b6b6a668a6a68b6a66c6a6c6a6a668666a66a6666a66a66
                    111d9d9d9d9d9d99d9d9d9d99b9d9d9b99db9db9bd9d9b9b9b9d9d9d9b9b99b999b9d9d99b9d9dd9dd9b99dd9dddb9b9b9bd9db9d9b9dd9dd9dd9b9d6b9bd9ddd9bd9bb9b6b9b6b6bb6b66bb6b6b6b6b6a6a6ca68b6c6a6a6c6a6b6b6b66b6c6a66ca6c6a6866c8a66ca6b66c66b6c6a6a6c6a68c86c8c6866ca6cb6a6c6a6a6a668b6b6a6b6db9b6a6a66a6b686c68a68a6a68b66a68a6a6a6a66a6a66a66a6
                    1111d919d9d9d9dd9d9d9d9d9d9d9b9d9d99d99d99b9b9d9d9b9b9b9b9d9b9b9db9d9b9b9d9b1d9dd9d9db9bd9b99b9b9b9bd9dd9bdd9bd9dd9bdd9b9b9dddd9dd9db9bd6db6b9a69a6b6b66b6b69a6a66b6a66b6c6a66b66a6b66a6a6cb6a6b6ca666a66cca6c6c6c66a6cb6a6c6a66c68b68c6a6c8b8ca6c66a6a66ca68b686ca6b86c6bb6b6bb6b6b6a686ca6a6a66c668b68a66a66a6a666a68a6a66a66a
                    1d1111dd9d1d9d9d9d9d99d9d9d9d9d9b9b9b9b9bd9d9b9b9b9d99d99d9b9d9b99b9b9dd9b9d9dd9db9b9b9d9b9b9b9b6d9b9dd9b9d9b9ddddd9d9bd9bd9d9dd9dd9d9b9b9b9a69b6b69a6b9a69a6b66bb666a66a6c6a68b86b8b6b66a6b6b6a666ca66c8668c6c6c8a6b6a6b6b6a6ca6c68b686c86c6866c6a66b6ca66a6c6a6b6b6a6a6b6b9b6b6a6866ca66868b86a6a6a6a66a66a6666a6a6a666a6a6a66
                    11111119d9d9dd9d9d99d9d9b9d99d99d9d9d9d999b9d9d99d9b9b9b9b99b99d9b9d9d9b9b9b9d9d9d9b9b9b9b9b9b69b9b9d9db9bd9db9d9d9ddd9db9bd9dddd1dddb9b9b6b9bb6b9a6b6a6b6a6b6a6b6a6a6b6c6a66c6cb68b6c6a6b6b6a66ab666c8b8b8b8c6a6a6b66b6a6b6a666a6a6c6a68b8a6ca6a68b8b666a66c6a6b6a66b6b6a9bbb6a66a6a6a68a6a66a686a6686a66a66a6a66a666a6a666698b
                    111d11d11d9d919d9dd9d9d9d9d9b9d9d99d9b9dbd9b9b9b9b99d9b9d9b9d9b9b9d9b9b9d9b9bdddb9b9b9b9b9b9b9b9b9b9bd9d9b9bd9ddd1d1ddd9dd9bdd91d1d9d9db69b9b9b9a6b6b69a6b6a6b6b66a66b6a6b6a6a668b66a6b6b6b69a6b6b8a6c6c6c6c6a68b66ca6a66b6a6b8b6b6b6a6c6c68c66c6a6b6a6a6b6a6a66a66a6a6a66b6b6a6a66c686c6a66c86cb66a6a66a68a66a6a66a6a666a6a6a66
                    1d111111119d19dd9d9d9d9d9d9d9d9b9db9bd999b9d99d9d9b9b9d9b9d9b9b9d9b9b9d9b9d9d99b9b9b9d9b9b9b9b9b9b9b9b9bd9d9bd9d9dd19d9d9bd9d9dd1d9ddd9db9bb9bb69b69bb66b6b6b6b6a6b6a6b6b66b6b6a6b8b6b6b6b9a6b6b6b6b6a6a68c686b68b86b66bb6b66a66c6a6b66ca68b6a68b66c6b6c6c6c66b6b6b6b6b6bb6a66666a6a6a6a66ca6a668a68b6a68a66a6686a66a66a69898b6a
                    911111111d19dd9d9d9d9d9d9d9b9d9d99d999dbd9d9b9b9b9d9d9b99b9b9d9b9b99d9db9d9b9b9b9b9b9b9b9b9b69b69b9b9bd9b9bd9bd9d1dddddbd9dd9dd1d1d1d1dd9b9b9b9bb6bb6b9a69898b66b6a6b6b6a6a6a66b6a6b6a6bb6a6b6bb6b6a66c6c6a6b8b6c6b6a6a6b6b6a6b8b66a6ca668b868c6c6a6a6a6a6a6a6a6a6b6a6b6a6b6a6a8b868b686a6866a6a66a6868b66a66a6a66a66a66a6a6a669
                    d911d11111d9d9d9dd9dd9d9d9d9d9d9bd9dbd999b9d9d9b9d9b9b9b9d9b9b99b9db9b9d9b9db9d9b9b9b9b9a969b9b9b9b9b9b9db9d9d9ddd119d99db9ddd9d9dd1d9d9bb9bd9b9b9b69a6b6ab6b6a6a66b6a6b6b666a6c6b6a6b6b6b6b6b69a6a6b8b6a66a6b6c6a68b6b6b6a66a6b6a66a66c6a6c8b6a6a6b666a666a6b6b6b6b6a66b66b6a66c6a68ca68b6a66a6a66a6a66a66a66a6a66a66a66a666a68
                    1d9d11111111d91d9d19d9d9b9d9d9b9d9b999bd9d9b9b9d9b9b99d9b9b9d9b9d9b9b9b9b9bd9b9b9b9b9b9b69b9b9a9b9b9b9d9d9ddb9dd9ddd1ddb9dd9ddd1d1d9dddd9b9db9b9bb6bb6b6b6b6a66a6b6a66a66a6a6b6a6a66a6a69a6b9a6a6b6b6b6a6cb6c68a68b68b6a69a6b668b6a66b6a66c6c68b66c6a6a6ca666a66a6a666a6a6a666a6a68b666a68a6a6686a6a66a6a6a6a666a6a6a66a66a6a69a
                    9119d91d11111d9d9d9d9d9dd9d99d9d9d9dd9d9b9d9bd9b9d99b9b9d99b9b9b9b99b99b9d9dd9b9b9b9b9a99b9a9b9b9a9b9b9b9b9d9d9dd91d1d9d9b9bd9dd1d1d19d9db9b9bdb99b69a9b69a66a66b666a66a6b6b68b666a6b66a66a6a6b6b66b6a66a66a6a66c68b6c6b6a6b6ca68b6b6a6b8c6a6a68b6a66b6866ca66a6b66ab68b666a6c686a68a6a6c66a68a6b66b6a666a666a6a66666a66a66986a6
                    19d191d1111119d19d9d9dd9d99d9d9d99d9b9b9d9b999d9b9b9d9d9b9b9d9b9d9b99b9d9b9d9b9b9b99b969a9b9b69b69b9b9bd9dd9ddd9ddd1d1d9b9bd9d9dd9dddd9db9d9b9b9bb9a6b6bb6b6b6b6a6a66a6b6b6a6a6ca66c6a6b6a6b66b66a6b6b6a6b66b6ca6a6c6a6a6b6a666a66c6a6b6b6a686cb6a6c68b6a6a6b6b6b9a66a66ca68b8a6a6c6c68b6a66c6b6bbb6b6a6a66a66a66a6a66a669a8b66a
                    91d9d19d11d111d9d19dd9d9d9d9d9b9db9d9d9d9bd9db9b9d9b9b9b9d9b9b9d9b9b9d9b9bddd9b9b9b9b9b9b9b69b9b9b9b9b9db9bd9bdd9dd9d1d9bd9b9dd9dd9d9ddb1b9bb9b9b9b69b69a69a66a66a6a6b66a666a6666a6a66b6a66b6a6a6b6b6a66b6a68b666c6a66b6b666a8b6ba6b6b6a66a6b8b686b6a68b8668b6b6a66c6a6a66a6c6b66c6a6a686a6a6b9b9b9b666a66a6a66a698b6a69a86b6a66
                    1191d9d91111111d9dd9d9d9d9d9bd9d99d9b9d9b99b99d9d9b9d9d9d9b99d9b99b9b9b9b9d9d9b9b9b9a9b69b9b9b9b9b69b9b9d9d9d9d9d9d1d9dd9b9bd9bddddd9d9d9bd9bd9bb6b9a6b6b6a6b66a66b66a6a6ba66ba6a666a6a66b6a66a6b6a69a6b6a6b6a6ca6a6b8b6a6a66b6a66b6a6b6a66c6b6a6a66cb68b8b6a6a66a6a6666a66a6a68a6a66a6a6b66d9bb9a69a6a6a666a69a6a66a6686a66989a
                    11d1919d9d11d111119d9d9d9d9d9d9d9d9d9d9b9d9d9b9b9b9d9b9b9b9b9b99b9b99b9bd9dd9b9b9b9b969b9b69b969a9b9b9b9b9bd9dbddd9dd1d9b9b9b9b9d9d9ddb9d9b9d9b9b9b9b9b69a96a6a6b6a6a66b666bb66b6a6a666c6a66a66b6b6a6b69a6b6a66a666c6a666a6ca666a6b6b6b66a6a6a66c6a668a6c6a66b6b6b66a6a6c6a666a66a68b666b6b9bb9bb9bb6b666a6a6b6b66a669a6989a6a66
                    119d1d1919111111d111d9dd9d9d9d9d9b9d9b9d9d9bd9d9d9d9b9d99d99b9b9b99b9d9d9d9b9b9b99a9b9b9a99a9a9b969a9b9a9b9db9d9d9dd9ddd9b9b9b9b9d9db9ddb9db9db9b9bb6b6b6b6b6b698b666a66a6b98b6a66c6b8b6a6a66b6a6b66b6b6b6b66a66ca6a66a6c6a66a6a6b6a698b6b66b68b6a6ca66b6a6b6a6b6a6a66c6a66ca66a668b86a6a9cb9bd9bb9b69a6a6989b9a666a686a6a6a669a
                    11d199dd1d1d11d1111d1d9d9d9d9d99d9d99d9d9b9d9b9b9b9b9d9b9b9b9d9b9b9b9b9b9d9b9b99a969b9b96b9b96b9a9b9b69b9b9bd9dd9b9ddd9dd9b9b9db9db9dd9d9d9dd9b9ab9b9b9a69a6b6a6a6a6a6a6b6a6b9a6b6a66a6a666a6a6b66a9a69a6b6a6b6a66b6a66c6a66a6b6b6b6a6a6b6a6a6a686666a68b68b66a66b66a6a66a668a68b8b6a6a6b6b9bdbd9b6bb6a69a6ab6b69a66a98b66b69a66
                    191d1d9199d11111111111d9d9d9d9d9d9bd9d9b9d99d9d9d99d99d9d9b9b9b9b9b9b9d9b9b9b9b9b9b9b96b9b9b9b9b9b6b9b9b9b99b9b9bd9b9dd9dd9bdb9b9b9d9bd9bdb9bd9a96b9a6b6b6b96a66b66b66b66a6b6a66a66a66b66a66b6b6a96a6b6b6b69a6b6a66a66c6a66a66a6b66b6b6b6a6b666a6aca66a68b6a6a6b6a6a666a66a6a66a66a666b6b6bb9d9bb9b69a69c9b69b9a6a6a66a69a6986a6
                    111919ddd199d111d1d11119dd9d9d9b9d99d9b9d9b9b9b9b9b9bd9b9b9d9b999b9d9b9b9b9b9b9b9b9b9a99b9b69b96b99b9b9b9bb9bd9b9d9dd9dd9dbd9b9b9db9bd9d9bdd9b9b9b9b9b9b9b6a69a69a6a6a6a66b6b6b66a66a68a66a6c6a66a6b6b6b9a6a6b666a66ca6a66a6b6b6a6a69a69a66b6a68b666a66b6c66a69a66b6a6a6a6a66a66a68a6a6a6a69bbd9bb9a6b6bb6bb9bb6b6669898a66ab69a
                    11d1d1919d1d91d11111d1d19d9d9bd9d9d9bd9d9d9d9d9d9d9d99d99d9b99b9b9b9b9b9b9b9b9b99b9b99b9a99b9a9b9a69a96b9b9b9b9b9b9b9b9dd9d9d9b9b9db9db9d9d9d9b9bb9b6b69a9b9b6b6b6b66b66a6a66a6a66a6b6b6a6b6a66b9b6b69a6a69b66a6a6c666a68b66a66b69a6a6b6b6a6a6a66a6a6a6c6a6a6b66b9896a66b66a66a68b66a66666bb9dbb9b6b6b69a69a6b9b6a6a6a6b69896a66
                    1111191d9d91d9191d11119d9d9d9d9d9d9d99d9d9b9d9b9b9b9d9b9b9b9b9d9b99b99b99b99b99b9b9b9a9b9b69b969b9b96b9b69b9b9b9b9b9d9d9bd9db9db9d9b9b9dbd9dbd9b9b9b9b9a6b9b69a9b69a69a66b6a66b6b6b6a6a66b6a6b6a6a69a6b69b6a6a6b6a6aa66c6a6a6b6a6b6b69a6b66b666a68b668b6a6b66b6b6aba66b6a6a6a66a66a66a6ab69bb9d9b9b6b6a6b6b69a6b669898698a6a969a
                    119d1d9d19d919d9d111d111d9d9d9d9d9d9d9d9b9d9b9d9d9d9d9d9d99d9b9b9d9b9b9b9b9b9b9b9b969b969b9a9b9a969a9b99a9b9b9b9b9b9bdbd9db9db9db9b9d9d9d9dd9b9b9bb9b9b6d6b6bb6b9a6b6a6a66a69a69a6b66b6b6a66b6b6b6b6b6bb6a6b66b6a6666a6b66a66a69a69a6b69a6a6a6a6c6a6a6a66b6a69a69669bb6b6b666a66a6b6a6b66a6d9bbdbb6b69a9b69a6b69a6a6a6a6b69a6ba6
                    11191919d11d9d119d9111111d9d9d9d9d9b9d9d9d9d9d9b9b9d9d9b9b9b99b9b9b9b99b99b9b9b9b9b9a9b9b9b969b9b9b69b6b9b9b9b9b9b9b9b9b9d9b9d9b9b9bdb9bdd9bd9db9b9b6b9b9b9b9b69a6b6a666a66a66a6b69a6b6a66a6b69a69a69a69a6b6bb6a66ab66a6a66b6bb6b6b69a6a6b66b66a6b66a66a6a69a6bba9ab69a69a6a66a6b6a66b68b6b9bd9b9b9a6a66b6a6b6986989b9b69a69b969
                    d191d1d19d9119d911d9d9d111d9d9d9d9d9d9b9d9b9d9b9d9d9d9d9d9d9bd99d99b9b99b9b99b9b9b9b99b9b969b9a69a9b9b99a969a9b9b9b9b9b9db9db9b9b9d9b9d9dbdd9db9b9b9b9a9b9b9a69c6b696a6b69a6b6b69a6a6b66b6b6b6a6b69a6b6a66b66a66b66a6a66b6a6b69a9b6bb69b69a6b6a66a6a6b6b66b6b696b6b6b69a6b6b6a6a666a6a6b69ab9bdb9b669b6b6a669a6a6a6a6b6a66bb9bb9
                    d1d1919d191d1d91d9111191911d9d9d99d9d9d9d9d9b9d9d9b9d9b9b9b999b9b9b99b9b9b9b99b99b9b9b9b9b9a9b99b969b9a96b9b9b9b9b9b9b9b9b9b9b9b9bb9b9bd9d9db9b9b9b9b9bb9b6b6b69a6a6a69a6a66b69a6a69a69a6a6b69a69a6b6b66a6b6a6b6a6a666a6a6b6b6a6b69a6b6b6a6b698b6b66a6a6a69a6ba69a9b9a6b69a6b666a6a666a6bb9bb9b9bdbb6b6989a6a6b69a69b69b9a9b69bb
                    919d9d19d19191d91d111d1d1d91d9d9d9d9bd9d9b9d9d9b99d9dd9d9d9bd9b99b9b9d9b99b9b9b9a969b9b69b9b96b9b6b9b96b9b9b99b9b9b9b9b9b9d9d9b9d9b9b9d9b9d9d9b9b9db9b9b9b9b9a6a669a6b66a6b69a6b69b66a66b698a66bb6b6b9a6b6a66b698b6a6a66b66a69a66a69a6b69a66a6a6b6a66b669a6b969a6b66a6b6b6b66a6a66a6a669a9b9bddb9b96b9a6a69b669a66b69a9b69b9bb9b
                    191119d919dd1d1d919d11919d19d19d9d9d99d9d9d9b9d9db9d9d99b9d9b99db9d9b9b9b9b9b99b99b9b999a9b9b99b99b9b9b9b9b9b9b9b9b9b9db9b9b9bdb9b9b9b9b9bdd9db9b9b9b9b9b6b69a69a6a666a66b6a6b9a9c9a6b6a6a6b69a96b9a6a66a66a69a8b66b66b6a69a6a69b9a6b9a6a6b69a6b66b6a6ba6b6b6a6b69a69b69a69a6a66a66b6abb6b6b9b9bd6b9a6b69b6b6a6b69a9ad69bb6b9b96
                    1d19d191dd9191911d19111d19d19dd9d9d9d9d9b9d9d9b99d9d9d9d9b99d9b99b9b99b99b9b9b9b9b9b9a9b99b96b9b9a9b69b99b9b9b9b9d9d9b9b9db9d99b9b9bd9bdb9d9db9d9b9b9bb6b9a9a6b6696bb69a669a69a6b6b6b6b69a69a6b6b6b9b6b66b6b6a66b6a6a6b69a6b69a6b6b6b69b669a6b69a6a69a66b69a6b69a6b6a6a66a86b698b6a6669b9b9bb9bd9bb6b9bb6bb69b9b9a6b96bb9b9b9ab9
                    d9d19d19d91d9d19d9d1d911119d9d9dd9d9d9b9d9d9b9d9d9bd9d9b9d9b9b9d9b99b99b9b99b9b9b9b9b9b9b9b99b9b9699a9b9a9b9b9b9d9bd9d9b9b9b9bb9b9b9b9b99dbd9d9bd9b9b9b9a66b696bba669a66a6a6bb9b9b69a69a66b6b9a9b9a69a6b6a698b6a69a66b6a6b69a6b9b9b96b6b9a6a6b6a696a66b69a6a69a6a6b66a6a66b66a6a669a6a6b6a69bd9bb9b6b6b69a69a6b9a9b9bb9b9a9a9b9a
                    911919d11d91d9d1919d91d111d19dd9d9d9bd9d9d9d9d9d9b9dd99d9bd9d9b9b9d9b9b9d9b9b99b9b9b969b9b9a9b9b9bb9b9b9b99b9b9b9d9d9bd9d9bd9b9b9b9b9b9db99b9bd9bd9b9a969b96b6a696a6a6a6b6696a66a6b6b6a6b9a6b66b6a6b669a6b6a6b69a66b9a69a9a6b69a6b6a9a9a66a66a69a6a6b6a68a66b6a66b6a6666a69a6a69a6a6b9a9b6bb9bd9b69b9a69a6bb9b9a6b6b9b9bb9b6b9b9
                    d91d119d9119119d1d191d911911d919dd9d9d9d9d99d9b9d9d9d9b9d99b9d99d9b99d9b9b9b9b9b99b9b9b9b969b9b9b99b9b969b9d9b9d9b9bd9b9b99bd9d9a9b9b9b9bbd9d9bd9b9b9b9a6b6a69b6a69a669a69aa69a69a6a666a66b9a9a69b9bbb66a66a66a6b6b9a6b6b6b9bb69b9b9a6b69a6b69a66b698b6a66b6a66a66a69a6a6a66a66a66b69a6b69b9b9bb9bb6b6b6b69a6bb9b9b9b9b9b6b9b9b6
                    1191d1111d1d9d19d9d19d191d119d9d9d9d9d9d99db9d9d9b919d9d9bd9b9b9b99b9b99b99b99b9b99b9b99b9b99b9b9b9b969b9b9b9d9b9dd9d9d9bdb9d9b9b9a9b9b99b9bb9b9d9dd9b9b9a69a6b9b9a69a66a666b6b6b696a698b6a66b6bb6b666a66a69a69a69a69b69b9b669bb6b9a69b6b6b698b6b6a6b669a6a66989a66a6896b6a69a66a69a6b9b9a9bbb9b6b9a69a69a6d9b9b9bb9bb6b9b9b9b6d
                    9d1919d91191119d919d919d119d1d19d9dd9d9d9d9d9d9b9d919d9b9d99d9d9d9bd9b9b9b99b9b99b9b99b99b9b99b9b9b9b9b9b9b9d9b9d9bd9b9bd99b9b9b9b9b9b9bb9b9b9b9b9b9db9b69a69a6b6b69c6b96ab6b69a6a6a6a6b69a69a969a69a9a69a6a6b6b9a9b6b9a6b6b9a69b9a9b6b9a69ab6b9a69a6a686a69a8a66a66a6a6989a669a9a6b69a6b6b9b9b9b6b69a69a9bbb9bb9b6b9b9b6b69a9b9
                    d1d1d1119111d1d1d191dd19d1d199dd9d9d9d9d9b9d9b9d9d9d9d9d9b9d9b9b9b99b9d9d9b9d99b9b99a9b9a9b9b9b99b9b9b9b9b9d9bd9b9d9dd9d9b9d9b9b9b69b9b9b9b9b9b9bd9db9b9b69b69b69a6b9a6a669a6a66b6b696a6a66a66bb69a6b66a66a66b6b6b6b9a6b9b9a6b9a9a6b69a69a66b9a69a66b6a6b6686b6a66a69a6a6bb69a6b669bb6b9b9bb9bb6b69a69bb6b96d6d9b9b9b6b9a9bb6b9b
                    91911191d1d119191dd919d19191d19d19d9d9d9dd9d9d9d99dd99b9d9d9bd9d9d9d9b9b9b9b9b9b9b9b99b99b9b9b9b9b99b9b9b9b9b9d9d9bd9b9bd9db9b9b99b9b9b9b9b9b9b9b9b9b9b9b9a9b69a69b6b696bb66b69a6698a6698b6b6b69a6b69a6b6a69a69a9b9b69b9a6b69bb6b9b9b66b69b9a66b6b6a669a69ab6a66a69a869b69a6b69a9a69a9b6b6b6b9b69a69bb69b9bb9bb9bb9bb9b6969b9b69
                    d111d11d119111d1191d9191d1d19d9d9dd9dd9d9d9d99d9db9dd9d9b9b999b9b9b9b9d999d9b9b99b99b9b9b999b99b99a99b9d9d9b9d9dbd9d9dd9db9b9b9b9a9a9b9b9b9b9a9b9b9b9b9a9b9b6b9b9a69a6a698b69a66a6a6b6a6a6a69a6a69a6a6b69a6a6b6b66a9bb96b9b9a69b9b69a9b9a6b69b9a96b69a86bb66a66a6a66b6a6b69a9a6b69bb6b69a69b9a69a6bb9b9bbb9db9db9b6b9a69ab69a9bb
                    11d91191191d9119d191dd1d9191d91dd9d9d9d9d9ddd9d99d9d9d9d9d9dd9d9d99d9d9b9b9b9d9b99b9b99b9b9b9b9b9b9b9b9b9b99b9d9d9d9d9b99b9b9b9b9b9b9b9b9b9a9b9b9b9b9b9b9b69b9a6b69a669a6b6a6a6b69a66a6b6698a69b6b69b69a6b696b969a9b69ab6b6b9bb69b9b6b6b9b9a6b6b69a6a6b9a9a6698966a6a669b9a669b9a6b69a6b69a6b698b99b9bb99bd9bd9bb9b9b69a69a69b96
                    191191d111d119d19d119191d91d1d919d9d9d9ddd191d9d9d919d9b9d9b9b9d9b9d9b9d9dd9d9b9db9d9b99b9b9b9b9b9b9b99d9d9d9dbd9d9dbddd9d9bd9b9b9b99b9b9b9b9b9b9b9b9b9b9b9a6b69b6a69a6b69a66b69a66a6989a6a66a6b9b6b69a6b6b6a9abb9b9bb969b9b9b9b9a9b9b9a6b69a9b6ba6986a69b9a6a6a6a669a6b9a69bb66b69a669a6a69b9a69bb9b9bbb9bb9bb9b9b69a69b69bb6b9
                    d111d1919119d19d19d91dd91d9191d9d91d9dd999d11ddd9d91d9d9d99d9d9b9d9b99b9b9d9b99d99d9d9bd99d99b99b99b9db9b9b9bd9dd9d9d9d9db99b9b9b9b9b9b9b9b9b9b9b9bd9b9b9a69b9a69a96a669a669a6a66a69a6a66a69a66a69a9a6b69a9b69b69a69b69bb9b9a9b9a9bb69a969a6b699b9b6b96bb6b698b669a6a69a6b9a69a9a6a69a669b6b6b6b9b9bbb969b9db9db9b9bb9b69a9b99a6
                    111191d1d9111919d191d91d91d1d9d19d9dd9d9dd9d9111d9dd9d9d9db9d99d9b9d9d9d9d9d9dd9db9d9d9b9b9b9db99b99b99dd9dd9d9ddd9ddd9d9db9d9b9b9b9b9b9b9b9b9b9b9d9b9b9b9b9a69a66b669a6b6a6b69a69a66a6a698a69a6b6b69a9a9b69a9b9b9b9b9a9b9b9b9a9b9b9b9b6bb9b9ab9a96b9a69b96a6b6a6a696a669a69a6b6696b6b6a69a9a9b9a9b9b9bb9bb9bd69bb69b69a9b69a69b
                    111119191d9d1d1d9d19d191d919d19dd9d9d9d19d9d9d191dd19d99b9d9bd9b9d9b9b9b9b9dd9dd9d9ddb99d9b9d99bd9b9d9b9d9d9d9d9d9d99dddd99b9b9b9b9b9b9b9b9b9b9b9d9bd9b9b9b69b969a69a6b69a96a6a698b6a696a6b6a669a69a69b9b9a9b69b9b9a9b9b9b9b9b6b9b6b9a9b9a69a96b9a9a69bb6a9b6989a66a69a6b9b6b69a6a6989a9a6b696b6b9b6b69a69b9b9bb9b9b6b9b69bb9b9b
                    191d1d1d9119191919d19dd91d9d9d191d19d19d9d9d9d9d1911d9d9d9d99d9d9d99d9d9d9d91dddddd99d9b9bd9dbd9d9b9b9d9d9d9bd9ddd9dbd9d9dd9bd9d9b9b9b9d99b9b9b9db9d9b9b9b9b9a6bb69a69b9a6a6969a6b696a6a69896a6a69a9b6b9b69b9b9b9b9b9b9b9bb9b9b9b9b9b9b69b9b6b9b9b69bb69b9a6a6a69b9b6a9b6b69b69698b6a6669b69ab9b9a9b9a69bb9bb9b9b9b9b9a6b9b69a69
                    1111119119d19d1d1d9d191d9d1919d19d9d9d9d9d9d9d9d9d119d9d9d9d99d9b9db9b9d9b9ddd1119ddd9d9d99b9d9d9d9d9d9d9dbd9dd9d9dd9d9d9b9b9b9b9d9b9d9bb9b99b9d9b9b9b9b9b9a69b69a69a6b6969a6a669a6a6989a6a6b696b9b69b9b9b9b9b9b9b9b9b9bb9b9b9b69a9a6b9a9b69b9b9b9bb9b9a6b6969b9a69a96b69a6a69a6a69a9b9a6b9a696a66b6b9b69a69b9b9bb9a6b99bb9b96b9
                    d11191d9d191d19191d9d9d919d1d19d9d19d9d9d9d9d9d9d9d1d9d9d9d9d9bd9d99d9d9b9d9d1d1d11dd9db9db9d9d9bd9bd9bd9dddd9dd9d9dd9ddd9d9b9b9b9b9b9b99b9b9b9b9d9bd9b9b9b9b69a96b9b9b9ab69b9a6a696a6a66b69a6a9a69a9b9a9b9b9b9b9b9b9b9b9b9b9a9bb9b9b9a9b9a9b9a9b69b69a9b9bb9a69b9a9b99a69b9a69a6986b6a969a69a69b9b69a69a9bb9b6b9bb9b6bb969a9b9a
                    19111d1191d191d9d91191d1d9d9d91d19dd19dd9d9d9d9d9d9191d9d99d9d9d9d9b9d9b9d9d9d111d11dd9d9b9d9b9dd9dd9d9dd9d9dd9dddd9dd9d9dbd9b9b9d9b9b9b9b9b9b9db9b9b9b9b9a96b9b69b69a6969a6b69b6b6a96b69a6a696b69a6b9a9b6b9b9bb9b9bb9b9b9b9b9b69a669a69b6b6b69b9a9b9b9b69a9a9b9a96b9a69b6966b69a6b9696a6a69a69a6969a69a6696b9b9b96b99b69a9b69a9
                    91d11911d19119111d9d19d91d9191d9d919d9d9d9d9d9d9d9d1d9dd9dd9d9d9d9d9d9b9d9b9d9d111d19ddd9d99d9d9ddd9d9d9dd1d1dd91d9dddd9d99b9b9d9b9b9b9b9b9b9b9d9bd9b9b9b9b9b9a9b9a9a9b9a69b698b69a66a9a6696a6a9a69b9b6b9b9a9a9b9b9b9b9b9b9b9b9b9b9a96d6b9b9b9a9b9b9a9b9a969b9b9b9b9b9b9a6a9a69b698a6a69b69a69a69a6a96b9b9a96b9b9b9b6b9a9b69a696
                    11911191191d11d9d1919d19d91dd9d19d9d9d191d9d9d9d9d919d9dd9ddddd9d9bd99d99d9d9d9d1d11d19dd9db9bdd9d1dd9d9d9d1911d11d1919d9b9b9b9b9b9b99b9b9b9b9b9b9b9d9b9a96b9a69a69669a9b9a9ab69a669a6669a6a96b69a6b69b96b69b69b9b9b9b9a9b9db9b9a69bb9a9b69a9b9b9b6b9b6b9bb9b9b9b9b9b9b69b6b69a98b69a96a69896b69a696b6986b6b9a9b6b9b9696b69a969a
                    191d91d11119191119d1d9d1919d919d1d91d9dd9d919d9d9d91d9d919d1191d9d99d9db9b9d9d91d1911d9d9d9d999dd9d9ddd9ddd91d19d19ddd9db9b9b9b9b9b9a9b9b9b9b9b9d9b9b9b9b9a969b69bb9a9b69a6969a669a669a6a6b6b69a69b9b9a69a9a6b9a9b9b9b9b9db9b9b9b9b9b6969a9b69a9b9b9b9b9b9b9b9b9b9b9b9b9a696a669a9a669a96a9a69a696a969a9b6969b69b9a9a9a969a969a9
                    911119191d11d119d119119d1d191d19d9d9d19d9dd9d9d9d9d19d9d9d9d9d19d9d9d99dd9d9b9dd91d1d1d9d9d9dbd9d1d1d9dd9d1d11d111119dd9d9d9b99b9b9b9b9b9b9b9b9b9b9b9b9b9a96b69a69a9b69b9b9a6b69a6b9a69696989a69b69a9b6b9a669a69a9b9b9b9b9b9d9b9b9b9b9ab69a9b9b69b9b9a9b9b9b9d9d9b9b9b9a96a969a96696a6669669a696a96a9a669a69a9b9a9696b69a969a969
                    d1d91d11911119d1191d9d1919d1d191d1919d9d919d9d9d9d9d19d9d9d9d9d1d9d9d9d9dd9d9d9d1d1191d91d9d9d9dd11d1d9dd9d1d1111d1d1d9d9d9b9b9b9b9b969b9b9b9b9b9b9d9b9a96b9a9a9b6969b9a696b9a6b9a669a6a6a6b69a69a9b69b9a69a69a6db9b9b9b9b9b9b9d9b9b9a96b9b69a9b9b9a96b9b9b9b9b9b9b9b9a669a69a69a6a969a9a6a696a96a9669b9a96a69a96b9a969a96b969a9
                    1111191d1919111191d1191d19d191d19d1d91d9d9d9d919d9d91d9d9d9d9d9d9d9d9d9d9dd9ddd911d1d11ddddd9d9dd9d191d1d1d911d1111191dd9db9b9b9b69b9a9b99a9b9b9b9b9b9b9b9b696969a9a69a9bb9a699a69b9a69b9a9a9a9b9b69a69a69b6b69b9b9b9bd9bd9d9db9b9b9b69b9a9b9b9b9b9b69b9a9b9db9b9b9a9b9b9a69a69a996a9a669a96a96b69a9a69869a9696b9b69b9a969a9a96b
                    1111119191d191d1119111191d19111119d9d91d1d91d9d9d9d919d9d9d9d9d9d9d9d9d9dd91d9dd19111d1919dd9d9dd11d1d191d1d111111d1d19dd9d99b9b99a9b99b9b9b969b9b9b9a969a9b9ab9a969bb969b69b9a9b69a69a6b696b69b69bb9a69b69a9a6b69b9d9bd9b9bd9d9d9b9b9a6b69a9b9b9b9b9a9b9b9b9b9b9b9b96b6698b69a69a6989b989a96b69a6969a69a969a9b699a9696b9a969699
                    d11191d11191d191d11d11d11191d1191d191d9d91d9d9d9d9d91d919d9d9d9d9d9d9d9d9ddd919d1d1d11d1d19dddd91d9111d1d191d91d11111d119d9db9b9b99b96b9a9b9b9a9b9b9b9b9a6969b69b6b9a9b9a9b9b69b9b96b69b9b9a99a9bb96b9b69a66b69b9a9b9d9bd9d9bd9bdb9b9b99b9a96b9b9a9b9b69a9b9a9b9b9a6b989a696a6969b69a66a9669a9a69b69a9b69a969a99a69a69a96969a9a6
                    111111191d1911191911911111d111111191d1d9d9d9d19d9d9d19d9d9d9d9d9d9d9d9dd9d9dd1d9d1d11111d1d19d1d1d1d1d111d1d1d111911191ddd9d9b99b9a9b99a969b69b99b9b9b9a969a69a9b9b969a969a99b9b9b9a9b9b9b9b9b9b9b9a969a69b9b9a69b9b9bd9d9bd9d9b9b9b9a69a69b9b69b96b9b9a969a969a9a99a69a69a69a69b69a699a69a6969a69a66969a69a696a96969a969a9b9b99
                    d19111119191d91d19d1119111111111111d9191191d9d9d19d91d9d9d19d9d9d9d9d9d9d9d9d91d9119d1d1919d1d19d19111d11191d11d11d11d119d9d9b9b9b969a969b999a9b9b99a969b9a9b9b69a9b9b9b9b9b9a99b9b99b9b9b9b9b9b9b96b9a9bb698b69a9b9bd9dbdd9dbd9d9b9b9b9b9a69b9a9b9b9a69bb69a6b9b9b69a69a69a69a99a69a6a96a9a69a69a969a9a969b9a969a9b969a969a969a
                    111111d11111911911919d11d111911d11111d1d91d91d9d9d9d19d9d9d9d9d9d9d9d9d9dd9d9d9d1d911111d1d1d9111d1d1d191d1d9d191111119dd9d9b9b9b9b9b9b9b9a9a9b9b9a99b9a9696989b969b9b9b9b9b9b9b9b9b9b9b9b99b9b9b9b9b96b69ab969a9b9b9db9d9d9d9d9b9b9b9a69b9b9b9b69a969b6969a969a69a69b696b69b69a969a969696969a69669a69a69a969b9b969a9a969a99b9b9
                    911911111191d191d91d19119111111111111111d19d91d9d9d91d919dd9dd9d9d9d9d9d9d9d9d9d9d1d1d1d11191d1d11111911d111191d1d11d1119d9b9d9b99b99b99b9b99b9b9b9b9b96b9a6b9a9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b99b9b9a99a969a9a969b9b9d9d9dbd9b9b9b9b99a969a9b9b9b9a69a9a9a69a69b69a69a69a9a696b9a669a69a9ab69b9a9a9b696969a969a9b96969b9b69b69b
                    1911d119111111d191191d911d191d191d1111111111d9191d9d91d9d9d19d19dd9d9d9d9d9d9dd9d9d91d191d1d11d11d1d1d1d11d91d1119119d1d9d9d9b99b99a99a9b96b9b9699b9b9a9b969a969b9b99b9b9b9b9b9b9b9b9b9b9d9b9d9b9b9b9b9a9b9a969b9b9d9b9d9d9d9d9db9b9bb96b9a9b9a9b69b9a696b69a9b69a69b69a6969a69a99b9a9a69a69a69896969a9a9a969a969b9b9b9a999a99b9
                    11d119111d1119111d91191d911111111919111911d119dd9191d919d19d9d9d91ddd9d9d9d9d9dd9d1d91d1d191d91d191111111d11d1d91d1d119dd9b9b9b9b9b9b9b99b99b99b9a9b69b969a969a9b9bd9d9b99b9d9d9b9d9b9b9db9db9d9d9b9b9b96b96b9b9b9b9d9ddbd9db9bd9b9b99a9b9b96969b9a669b69a96669a69b69a69a9a69b699a66969a696969a9a9a69b6969b9b9b9b9b9b9b9b9b9b99a
                    1111111111111111911d1191119119d191d11d1111191119dd9d91d9d9d9d9d1d9191d9ddddddd91d9d9d9191d1d1d191d1d19d19111111d11d11d9d9d9d9b9b9b99b99b9b9b9a9b9b99b9b9a9b9a9b9b99b9b9db9d9b9b9d9b9b9db99b9db9bb9db9b9b9b9b9a9b9b9b9bd9d9d9dd9d9d9b9b9b9a9b9a9a6969a69a9b69a9a969a6969a6969a9b9b969a6969a9a9a696b9b699a9b9b9b9b9bd9b9b9b9b99a99
                    d11911191911111111191d1191111111d1919111111111d191d9d19d19dd9199d9dd9dd99d9191d91d911d1d919191d1d191d11d1d1d91d1d919d1d9d9d9b9b9b9b99a9b99b9b9b969a9b69b969b969b9a9bd9b99bd9dd9db9b9b9b9bd9b99b9db9b9b9b9a9b969b9b9bd9b9d9db9d9b9bd9b9b9b69a69b9b69a9b9b99a9b696a69a69a96b9a69699a9a9b9a69a6969a9699a9a9b9b9b9b9b9b9b99b9b9b99b9
                    11111111111d111d111119d11d11d111911d191911111111d91d91d9d9d9dddd9d919d91d9d9d91d91d9d9d1d1dd1d1911d11d191191d1191d1d19dd9d9b9b99b99a9b99b9b99b9b9a9699a9a9a9b9a9b9b99d9bd9bd9d9b9d9b9b9b9bd9bd9b9b9b9b9a969b9a9b9b9b9bd9dbd9dbd9d9bd9b9b9b969a969a9b9b9b9a6969a69b69a6969a6969a9b69696a9b69b9a969a696969b9b9b9b9b9d9b9b9b9b9b9b9
                    d111191d11111111191d1b1111111111119191d1d191d1911191d9191d919d919d19d1d9dd9d1d91d19111919d919d1d1d9d191d1dd119d1d19d9d9d9b99b9b99b9b99b9b99a9b69b969a9696969a969b99b9bd9d9d9d9d9b9b9b9b9d9b9d9b9b9b9b9b9b9b9b9b9a9b9b9d9bd9d99b9bd9d9d9b9a9a96b9b9b99b9b969a69a9a969b9a9a969a9b99a9a69699a96969a99b9a9b9b99b9b9b9db9b9b9b99b9b9b
                    111111111191111111119b91911111111d11d1919111111d1d191d9d9d1d9d9dd9dd9d9d9d19d1d19d1d9d1d9d9d19d91119d1d1919d91d91d9d19d9d9db9d9b9b99b9b99b9b999a99b9b9a9b9b969b9b9b9bd9b9bd9bd9d9d9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b99b9d9b9d9b9bd9d9d9bdb9b99b9b9b99d9bd9b9b9a9b6969a9a969a969b969a96969a9a6969a9a969a9b9b99a9b9b9b9b9b9b9b9a9b99b9
                    1111d119111111911111b9bd119111911111111d19d19119119d9111d99d91d919d9d91d19d9d91d1191d91d19d19d1d9d91d91d1d1dd91d9d9d9d9d9b99d9b9b9b9b99db9b9b9a9b9a9b969b9b9b9b9b99b9b9dd9d9d9dbdbd9d9b9b9d9b9b9b9b9b9b9b9b9b969a9b9b9bd9bd9d9bd9bd99d9b9b9b9b9bd9d9b99b9a969a9a96969a969b9a9a99b9a9a969b9a9b69b9a969b9a9b9b9d9b9b99b9b969b9b99b
                    111111111d1191111111bd69d111d111111919191191d1111911d19d91d9d9d9d19d1d9d9d9d1d911d1d91d9dd9dd9d91dd91d919d919d9d9dd9d9d9b9d9b99b99b9d9d99b99b999b9699a9b9a9b9a9b9a9b99b9db9bd9bd99d9b9d9b9b9b9b9b9b9b99b9b9b9b9b9b9b9b9b99db9d9bd9d9db9b9b9b99b9bd9d9bd9a969a969b9a9b9b9b9b99b9b9b6969a969a699a969b9b9b99b9d9b9b99b9b969b9b99b9d
                    1111911911111111d119d6cb9111111111111111d119191d1d1911191d91d1919d199d191d19d9d91919d9d19d9d9d9d9d9d9d1d91d9dd9dd9d9d9d9d9b99b99b9d9d9dd9d9b9b9a9b9a9699b99b99b969b9b9d9b9d99d9d9dbd9db9b9b9b9b9b9b9db9b99b99b9b9d9d9d9db99b9bd9d9bd9b9d9b99b9bd9d9bd9b99b9b9b9b9b9b9b9b9b9b9b99b99a9b69a99b9a969a9b9b9b9b9b9b99a99a99a99b9b9d9b
                    111111111111d111111d9b6811d111191d111d1191d11d19191d9d1d191d9ddd19dd19d19d9d91d1d9d1d19d91d9d9d19d1d9d9dd9dd9d9d9d9d9d9b9d9db9db9d9d9d9d9d9d9b99b9b9b9a9b9a9b969b99b9b9bd9bdbd9d9d99db9d9b9b9b9b9b9d99b9b9db9bd9d9b9db99dbd9d9d9bd9d9db9b9b9b9d9d9b9bd9b9b9b99b9a99b99b9b9b99b9a969a699a969a969b99b969b9b99b99a99b99b99b99b9b9b9
                    11111d1191911111119bd9a6d11191111111111111919191d19191911d191919d919d19d91d1d9d9d19d9d9dd9d9d19d9d9d19d9d19d19d9d9d99bd9d9b9d999d9bd9dbdd9b9b9b99b99b99b9b969a9b9a9b9b99bd99d9bd9bd9d9d9b9d9d9b9d9b9dbdd9d9bd9d9bd9d9ddbd9d9dbd9d9db9b9b9b9d9d9db9dd9d9dd9d9b9b99b9b9b9b9d9b9a999a969a969a969b9b9a99b99b9b99a99b9b9b9b99a9999b9b
                    111111111d11111911d9dd6c6111111111111111d11d11d191d91d19191d1d9d1d91d91d19d9191d9d9d9d19d19d9d9dd9d9dd1d9d9d9ddd9d9d9d99b9d99bdb9d9d9d9d9dd9d9b9b9b9b9a969b9b9b9b9b9b9b99bd9b9d9d9db9b9b9b9b9bd9bdd9d99d9dd9d9bd9dbd9d9d9d9d9d9d9d9bd9d9bd9dbdd9d9b9d9d9d9bd9d9d9d9b9d99b9b9b9b9b9b9b9b9b9b9b96969b99a9b99a99b99b99b99a99b9a9999
                    11111111111119111ddd16a6a111111d11111111191191191191d91d9d19191191d911d9d191d19d19d1d9d9d9d1d9d9d9d19d9d9dd9d99d9d9d99dbd99bd99d9bd9d9d9d9d9b99b9b9b9699b99a99b9b99b9b9b99b9d9b9bd9d9d9bd9b9b9b9d9d9dd9db9d9bd99b9d9dbd9dd9bd9dbd9d9db9d9d9dd9d9bdd9dd9dbd9d9d9db9bd9bb9b9b99b69b69a969a969b69a9b969a99b9b9b9b9a9b99a99699b9b9b9
                    111111111119111d1191d6b66d111111111111191111111d1d191d9119d1d191d11d19119d19d1d191d9d9d19d9d91d19d9dd91d9d9d9dd9d9d9db999db99db9d99dd9d9d9d9db9b99b9b9b99a969a9b9a99b9b9b9b9b9d9d9b9bd9d9b9b9b9b9d9b9dbd9d9d9bd9d9bd9d9d9dd9db99db9b9d9bd9d9d9bd9d9d9bd9d9d9dbd9d9d9d99b9b9a99999a969a969b999b999a9b9b99a99699b999b99b99b9999b9b
                    1111d11911d1111119b16c9bb9111111111111111111d119191d9119d1919d119d911d9d19d19191d191919d1d19d19dd9d91d9d191dd9d9dd9d9dd9d9d9b99d9bd9dd9dd9bd99b9b99b9b9a9b9b99b969b9b99a9b9b9b9b9bd99b9b9b9b9b9b9bd9d9d9db9bd9b9bd99bd9db9b99db9b9dd9dd9dd9d9dd9d9d9dd9d9dbd9d9d9db9b9b9b99b9ab9a969b99b99a699a9b999b9699b9b9a969b9b99b9b9bb99d9
                    11111111d1111111bd9db6b68b1111111111111111d11111119119d191d119d1111111191d9dd91d19d1d1d191d191d91d1d9d19dd9d9d9d9d9d9d9d9b9d9d9b9d9d9dd9dd99b99b9b99b99b99b9a969b9b99a99b9b9b9b9d9b9d9bd9b9b9b99b99db9b99bd9b9d9b9db9d9bd9db9b9d9d9bd9d9d9ddbd9d9bd9bd9bd99d9d9dbd9d9d9b9b9b999b99b9b699a999a99b9b9a99b9b999b999b999b999b999db9b
                    11111111111111d16bd9cb6a6b91111111111111d11111119d1d91191d91919d919d91d191d91d91d1911911d1911d1d9d9d9d91d111d19dd9ddd9d9d9d9b9d9d9d9d9d9d9db9db99b9b9b99a99b96b99a9a96b9b99b9b9b9b9b9bd9b9d9b9b9b9b9bd9bd9b99b9b9b9d9b99b99b99b9b9d9d9dd9dd9d9d9d9dd9dd9d9dbd9d9d9d9db9d9b99b9a9b99a99a969a9b9a969b9699a9b9a99b99b9b9b9b9db9d9d9
                    1111111111111119b9d69a6b8bb111d1111111d11111111111911d91d91d1d11d111191d191d91d9191d1d1191d19119d9d91dd919d91d91dd9d9ddd9d9bd9b9d9b9d9d9d9d9b99b99b99b9b9b96999a9696999a969a99b9b9b9d9b9d9b99b9b9a9b99b9b99b9b9b9b9b9db9dbd9dbd9dbd9db9dd9dddd9dbd9d9d9d9bd9d9dbd9db9d9b9db9b9999a969b9b9b99b999b999b9b99999b99b99b999d9d9d9d9d9
                    111111d1111111db6b9cb6b6c6611111111d11111111111d1119191d11919d91919d1d19d191d91d1d191191119d19d1d19dd91d9d1d91d919dd19d9d9d9d9d99d9d9d9dd9b9d9b9dbd9d9b99b9b9a99b9b9a9b96b99a99b9b9b9b9b9b9b9a99b99b9b9b9b9b9b9b9b9b9b9b99b9b9d9d9d9ddd9dd9d9d9d9d9dbd9dd9d9dbd9d9d9d9d9d99b9b9a969b9b99b9b99b9b9b9a9b9b9b9b9b99bd9d9d9d9d9bd9dd
                    111d11111111119b6bbb6a9c6a6111111111111191191111111d1d191d1d11191d1919119d191d91911d191d1d19d1919d19d9d9d9d1d91dd19d9dd9dd9d9d9d9d9d9dbd9d9d9b9d999b9b9b99b9b9b9b99b9b9b99a99a9b99b9b9b9b9b9b9b9a9b9b9b9b9b9b9b9b9b9d9b9d9d9d9d9d9d9d9dd9dd9dd9d9dbd9dd9bd9d9d9d9d9dbd9bdb9d9b9b9b9b9b9b9b9b9b99b9b99999b9b9d9d9d9d9dbd9bd9d9d9d
                    1111111111111db6b969a6b86cb9111111111111111111119111911d91919d1d191d111111d1911d19191d1191d19dd1d9d19d191d9d91d19d1d19dd9d9d9d9dbd9db9d9d9b9b9d9bd9d99d9b99a99b99a99b699a969b969a9b99b9b9b9b9b9b969a99b9b9b9b9b99b9b9b9d9b9d9dbd9ddd9dd91d9d9db9d9d9d9d9d9db9d9dbd9d99d99b9b9b99b999b9b9b9b9b9b99b9db9bd9d9d9d9d9d9d9d9d9d9d9dd9
                    111111111111116c9dcb6b6c8b6b1111111111111111d191111119191d19119111191d911111d1911d1d191d1191d191919d19dd9d91d9d119d9d9d9d9d9d9d9d9d9d9d9d9d9d9b99b9b9b9b9b99b99a99a999a969b9b9b99b9a99b9b9b99a969b99a99b99b99a9b9b9b9d9b9dbd9d9dd9d9dddd9dd9d9d9bd9dd9d9db9d9bd9d9d9db9db9b9b9b99bb9d9b99b999b9b99b99d9d9d99b9d9dd9db9d9d9bd9ddd
                    1111111111119b6a168b8b6c6b8b91d11111111111d111111191d11d1911d1111d11111d1911111119191d1191d191d1d1d19d9dd9d9d19d91d19d9dd9dd9dd9d9d9d9d9d9b99d9d9d9d9d99b9b99a99b99b69b99b9b969a9699a9b99b9a99b9a9a96b99a99a99b99a99d9d9d9d9dd9d9ddd9d9dd9dd9dbd99d9bd9b9d9d9d9d9dbd9db99b999b9b99d9b99b9d9b99d9bd9d9dd9d9ddd9dd9db9d9d9dd9ddd9d
                    11d111111d111b6bb6b6c6b6c9c6111111d1111111111111d111191911111911111119191111191d11d1191d11191d19191d1d191d19d9d9dd9dd919dd9dd9dd9d9d9d9d9d9db9b9d9b9b9bd9b9b99b99b99b99a99a99a99b9a9699a99b969b9699b99a9b9a9b969a9b9b9bd9d9d9d9dd9d9ddd9dd9d9d99db9d99d9b9b9b9db9d99b9db9d9bd9d9b9b9b9b9b9bd9b9d99d9d9dd9d99d9d9d9d9dd9d9dd9d19d
                    191111d11111d6b6b6b9bc9c8b8c1111111111111111111119111111d19111d11111111d111911191919d191191d1911d19191d19d9dd9d9d9d9d9dd9d9d9d9ddd9d9db9b9d99d9d9bd99d9b99b9b99b9d9a9b99a99699b9b969b9a969b9b969b9b9b9699b969b9b999b9d9dbd9bd9bd9d9dd9dd9d9d9dbd9db9db9bd99bd9b9d9dd9d99b9b9b9b99b9b9b9d9d99d9d9dbd9dd9dd9dd9d9dd9dd9dddd9dd91d9
                    1b9d11111111b6a6bb6c6a6c8b6c9d111911111d11111191111d19111111d1111111d11191d11d11d1d191d1d1111d1191d1d9191d19d9d9d9d9dd9d9dd9ddd9d9dd9d9d9d9bd9b9d99b9b99d9b99b9b9b999b9b969b9a969b999a99b99a99a99a969b9a969b99a9b9b9b9d9d9dd9d99bdd9dd9d9dd9d9d9d9d9b9d9b9b99bd9db9db9bd9b9d999bd999b9d9b9b9db9d9d9dd9d9dd9dddd9d9d9d9d9dd191d1d
                    18b11111111168b6b6d8b6a6c68c91191111111111191111111111191d11111111911111191191919191d191919d191d11911d91d9d9d19d9d9d99d9d91d919d9d9dd9d9d9b99d9b9b9d99b9b99b9b9d9d9b99a99b99b99b99a9a9699a969a9b969b99b9b9b9a99b9b9b9d9ddd9d9bd9d99d9d9dd9ddbd9d9dbd9d9b9d9db9d9d9d9d9d9b9d9bd99b9b9d9b99d9d9d9d9dd9dddd9dd9d9dd91dddd1d19d1d9d9
                    b68d1111111d6bb6b9a6c9c6cb6cc111111d111111111111111111d1111111111111111911d111d1d11191d19111119191d191d191d19d9d9d9d9d9d9d9d9d9d9dd9d9d9bd9d9b9d99b9bd9d9b99b9d9b9d9b99b99a99a99a96999b9b9b9b99b9b99a9b99a999b99b99b9db9d9d9d9db9dbd9dd9dd9d9d9dd9d9d9bd9bd9d9d9d9db9d9bd9b99b9b9d9b99d9bd9d9dd9d9dd9191d9dd91d91dd919d91d1911db
                    b6a61111111b6d8d9b8c6b8c6b86b1111d111191191111111d11111111911111111111111111911919d11191d19d911d1d11d11d19d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9bd99bd999b9b9dbd9b9b9d9b9b99b99b99b99b9b9b9b9699b9b999a9b99a99b9b9a99a99b9d9d9dd9d9d9d9d9d9d9d9d9dd9d9d9d9d9d9d9dd9d9d9d9bd99d9bd9d9b9d9db9d9d9dd9dddd9d1d9d91d1dd1dd91d1d1191d19dc9
                    8b6a91111116c9cd9c6c9b68db8c6d191111911111111111111111119111111111111111d111111111191d111911d11119191d911d1d91d19d9d9d9d9d9d9d9d9d9d9d9d99b9d9bd99bd99d9d999d99d9b9ddd9b9b9b9b9b99b9b999a9b99a9b9a999a99b99b999b99d9d9bd9d9dd9ddd9dd9dddddd9d9d9dd9dbd9d9ddd9dd9dbd9d99bd9b99b9d9b9d9dd9dd9d9d9d9d1d9d11d19d19d191d191d1d19d1d6d
                    6986d11111d9bb6db8b8b8cc98b8b91111111111d111d11111111111111111111111d11111191d11111111191d191191d111111d19191d9dd9d19d19dd9d9d9d9d9d9d9d9dd99d99b9d9b9b9b9db9b9b9d9d99d9d9b9b99b9a999a9b99b9a999a99a99b99a99b9d9db9bd9d9d9d9ddd9dd9dd9d9d9dddd9d9dd9dd9dd9d9d9db9d9bdbd99b9d9d9bd9d9d9d9d9ddddddd19d19d91d191d191d1cb9191d119bdb
                    8ab6b11111db9a9b9c6cb6c6bc68c911111111111111111111111111111111d111d111111111119191d11911d191d11111d19111111d19191d9d9d9d9d9d9d9d9d99d9d9d9d9d9bd9d9b9d99d9d9dd9d99d9d9d9b99b9b99b9b9b99b9b9b99a99b99b9b9b9b9d9bd99d9d9d9ddddd9dd9dd9dddd9d9d9dd9d9dd9dd9dd9dd9d9d9d9999bd9d9b9d9d9dd9d9ddd9d9d919dd91d1d91d1d91d19d6bb1d19d1d9cd
                    96a66111d116c6b6b8c9c68b8b6c6b1111111d1119111111d1111d1111d111111111111111111111111111d1111191d9d191d191d911d1d191d9d9d9d9d9d9d9d9d9d9d9dd9d9d99d999d9b9b9b999b9b9b9dbd9db99b9b9999a9b999a99b99b99b99b99b99d9dd9dd9d9d9d9d9ddd9dd9dd9d9dd1d9d9d9dbd9d9dd9dd9d9d9b9bd9db9d9bd9d9d9d9dd91d9ddd9dd91d1d1911d19111d1db1c681911191dcb
                    b66a611111b6a6bc6b8d8c6b6b8c8c111d11111111111911111111111111111111111111111d111d1119111191d9111111d1911111d9191dd91d1d9dd9d9d9d99d9bd9dd9dd9d9d99bd9b9d99d9dbd9d9d9d9d9d99b99b9b9a9999a9b99b9b99a99a99b99d9bd9d9d9ddddd9d9dd9dd9dd9dd9d9d9dd9d9d9d9ddd9dd9d9d9bd9d99b9d99d9d9d9dd9d9dd9dd9d91d91d9d91dd91d1d91911b9d8cd1d91d1c6d
                    6a6b8111116b6b6ba66b6c8bcb68c61111111111111d11111111111111111119119111111d111911111111111191d19119191d191111d1911d919d19d91d9d9d9d9d9d9d9dddd9dd9d9b99b9b9b999b9b9b9d9d9dd9db99b99b9b99b9b99b9b99b99b9b9b9d9d9bd9d9d99dbdd9dd9dd9dd9ddd19d9ddd9dbd9d9d9d9d9d9dd9d9bd9d9dbd9d9dd9dddd9ddd9ddd9dd91d1d1911d91d1d1d9bdb6c911d1d9cbd
                    66a6a9d11db6b9c98cb68c6b6a6c6c11111111111d111111911911111111191111dd11111111111111111191d111911d11d11911d1911d19d1d91d9d1d9dd9d9d9d9d9d9d99d9d9d9d9d9d9d9d9db9d9d9d9bd9dd9d99b99b9b9b9b999a999b9b9b9b99bd9b9b9d9d9d9dbd9d9d9dd9d9d9d9d9dddd9d9d9d9d9d9d9d9dbd99b9d9d9db9d9d9d9dd9d9ddd9dd9d9d9dd9d91d1d11d191d111d9d8cd9d191bcb9
                    b66b6b119d68dc8b6c9cc8b9b6c8c8b1111119111111111111111d1111111111d161111111111111911d111111111d191911d1d1191d91d19191d19d9d19ddd9d9d9d9b9d9d9d9d9d9b9d9b9b9b99d9b9b9dd9dd9d9d9dd9d999b99b9b9b9b99b99b9b999bd9d99bd9bd9d9d9dd9d9dd9dd9d9d9d919dd9d9d9b9dbd9d9d9dbd9b9d9b9ab9db9d9dddd9d9d9dd9ddd9dd1d19d19d191d19d9ddd6c911d1db8db
                    9a6a6611d9ac9bb6a6d86c6cb86c6c9d11111111111111911d11111111d111d11d611111111111d1111111111911191111d119111d111919d1d191d19d91919dd9d9d9d9d9d9d9d9bd9d9bd9d9d9d9d9d9d9dd9dd9dbd9b9b9bd9b9b9999b9b99b99d9bd9d9b9dd99d9d9d9d9d9d9d9d9d9ddd9d9ddd9d9bd9bd99d9bd9bd99d9d9bd9a68b9bbba9d9d1dd1d9dd9d9d19d9d1d1d191d1911dd9bc6c19119ccdd
                    6986a6d9bd6bb6b6bbb8c6c9b8c8c8611111111111111111111111111111111d9b6d1111111111111119119111d1111d11191119119d1d11d919d19d1d1dd9d9d9d9d9d9d9d9d9bd9d9d9d9d9d9db9d9d9d9d9d9dd9999d9d9d9b9d9bdb99b9b9b9b9b99b9d9d9bd9bd9bd9bd9d9d9d9d9d99d9dd9d9d9d99b99db9d99d99db9d9d91bb6bb9d9b69dd9d9d9dd9d9dd9d1d1d19191d1d1d1d9ddb6cc1d1dbc79b
                    6a6b6a6b9bb66a9869c6c8a6b6c6a6c1111111d11111111d1111191111111119b9a6111d111911111111111d1111911191111d1d191191191d1d91d1919d91d9d9d9d9d9d9d9bd9d9d99d99d9b99d9dd9dd9dd1d9dddd9b9d9b99d9b999bd99b9d99bd9d9b9d9bd9d9d9d9d9d9db9d9bd9d9d9d9d9d9d9bd9d9d9d9bd9bd9d9d9dbba6b686db9a6a6b9d9d9d9ddd91d9d9191d1d1d91919bddb6fc6b9d9ccdbb
                    6a98989a9b6bc6cccb6c6c6cb8c66c8b111111111111111111191111d119d91d6b6a111111111d1191d1111111911111111d11911d11d1d119191d91d91d19dd9dd9d9d9d9d9d9d9d9d9d9d9d9dd9d9dd9ddd99dd9d9d9d9b9d9b99d9bd99b9d9b9b99d9bd9b9d9d9b9b9bd9db9d9bd9d9bdb9d9d99b9d99b9d9b9d9d9d9bd9dbd199b6a6a9db6b6b9cdd9d9d9d91d1d1d1d19d191d1d1db616bccb6dddc8d9d
                    66a6a6a9d9c9b8b6a6a68a6bb9bc8b69d111111111111111111111111111bb9db6861111111d111111111111111111911d11111111911919d1d19d191d919d9d19dd9dd9d9d9d9dd9dd9dbd9d9d9bd99d9d9ddd919dd9d9d9d9bd9b9b99b9d9b99d9d9b9d99d99b9d9d9d99b99d9b99d9b99d9bd9bdd9bd9d9bd9d9b9dbd9d9d99dbbb66c9b9bb6a6d69d9dddd91d9d9d19d1d1d1d191b9cddcb6c6bd9d6bbcd
                    6a6b69d91b8d6c68b9c6c6b6d96c68c611111111111d111111111111111166b9a6a6d11191111111111119111111111111191191111d11d1191d19d191dd1d19dd9dd9d9dd9dd9d9d9d9d9d9d9d9d9d9dd9d9d9dd9d9d9db9d9d9d9d9dd9db9d9b9bd9d9b9d9bd9d9b9b9d9d9b9d9d9b9d9d9b9d9d99d9d9dd9d9bd9d999d9bdddd9b9ca6db69a6b9abb9d9d9d1dd191d91d91d9191ddbb6b9b6cbcd1ddcd79d
                    9b96b9ddd6bb8b6c9c6c8c6bdb8ca6ca9111d11111111111111d1111111d8bb66a66d111111111111d111111911d111191111d11d91191191d19d19dd19191d19d19dd9d9d9d9ddd9dd9d9d9dbd9d9d9d9dd9dd9dd9dd9dd9dd9d9d9d99d9d99d9d9d9d9d9bd99d9bd9d9b9bd9d9b9d9d9b9d9d9d9dbd9db9d9bd9d9bd9d9dd9d9db9a66d9ba6b6a6b66b9a19dd91dd91dd1d191dd19b6dbddbcc6c9d9d8dbdd
                    9b9b1d9ddb69c6a6bb8c6ca9d8668c66b11111111d11111111111111d116b86a66a6b9111111911911111d111111191111191191111d11d1191d19119d1d9d9d19dd9ddd9dd9dd9dd9dd9dd9d9d9d9d9dd9dd9d19d9d9d9dd9d9dd9dddbd9bd9bd9d9bd9d9d9d9b9d99bd9d99d9b9d9b9d9d9d9bd9d9d9d9d9d9d9d9d9ddd9dd9d9b9b6b9d96b6a6b9a6a6b9d19dd91dd19d9d1d19ddbc9d9db8c6cbdbdcd9dd
                    9dd119d198bb8b6cb6a68b6b9cc8b6a6b111111111111111d1111111119b6a6b6a6a6d1111d11111111911111d1111d11d11d11d91911911d119d1d91d91d119d191d919dd91d9d91d9dd9dd9d9dd9dd9d9d9d9d9dd9dd9d9ddd9dd99d9d9d9d9d9bd9d9db9d9d9d9d9d99d9b9d9d9d9d9db9d9d9d9d9d9ddd9ddd91dd9d9d9dddb9bb6b9ba6bb6b6b6b6a6b9dd191d9d91d1d9d91db6cddd9c3cbc9d9c9bd9d
                    b99d9d9dc6a66a6b9b6c68ddb86c8c8c6d111111111111111111111111d6a66a6866a611d11111d11111111911111111111119111d11d1191d119d1d91d9d9d19d191d9d19dd91d19d919d9dd9d9dd9dd9ddddd9d9d9d9d9d9d9d9ddd9d9d9d9b9d99d9b9d9db9d9bd9d9bd9d9d9d9dd9d9dd9ddd9ddd9dd9dd9ddd9ddddddd9d9a9d9a9bd9c6b6bb6a6b6b6dd9ddd1d1dd9d1d1dd9bbc6b9ccc6bcdddcddddb
                    9a9d9dd9a6db6db6d6a6cc9d8c6c6c68a6111111111111111111111d11b66a66a6a6b6d1191191111111111111191111911911191119191d19d1d191d9d1919d19dd9d19dd9dd9d9d1d9ddd9d9dd9d9d9dd99d9dd9d9d9d9d9d9d9d9d9d9b9d9d9d9d9d9d9d9dd9d9d9dd9d9d9bd9d9dd9d9dd9d91bd9d9d9d9dd9dd9d99d9dd9bb6a6bb9da6a69a6a69b6a69d9d9d9d9d919d9d9dc9bcdbdcfcb87b9d6d9d9b
                    6db9bddb6c6ca6ab9a686bd9c68c8c8b66111111111111111111111119bb66a66a6c6a91111d11191d191d111911d19111111d1111d111d111191d19d19d1dd9d1d91d9d91d9d19d9d9d9d9d9d9d9dd9d9ddd1d9ddd9d9d9dd9d9d9d9bd9d9bd9d9b9dbd9d9d9d9dd9d9d9dd9dd9ddd9dddd9dddd9d9dd9d9dd9dd9d9ddd9d9ddb6b6b6b69b66a986b6a6b6ab6a9d19d9dd9d9d9d9bd6c7b9f8fbcdb9d1ddddb
                    999b19b6a6b69b6d6b6cc9db6a6c6c6c6c91d1111111d111111111111d6b8a6ca66a66a19191191d11111191d1111111d11d11111911111191d1191d1d19d91d19d1d91d19d19dd19d1d19d19dd9d9dd9d9d99d19d9dd9dd9bd9dbd9d9d9dd9d9bd9d9d9dd9dd9dd9dd9dd9dd9dd9d9dd9d9dd9d91dd9dd9d9dd9d9dd99dd9d9d9b6b6b6b9a6a6bb6a6b9b66a6b6d9ddd9dddddd9dcdb6b9ccf6c6b1ddd9d9bd
                    bb9d9b9b6d9bdb69b8c6ad9b8b8c6a86ca6111111d1111111111d1119d6a66a66a66a6611d11d1119191d11111d19d1119111911111d11911d11d1d19191d19d91d91d19dd9dd9d9d9d9dd9dd9dd9d9dd9d9dd9d19d9d9d9d9d9d9d9d9dd9d9dd9ddd9dd9dd9dd9dd9dd9dd9dd9dd919ddddd9ddd9d9d9dddd9d9dd9d9d9d9dd9b9a69a6b9b6b686a66b9bb6b6a69d9d9d9d99d9d9c9cbbbc3ccc7b9d9dddd9d
                    69b9b9ab6bbb9babb6a6b9dd6c6a66ca68c111111111111111d111111b96a66a66ba6a6d11911911111d19d1919111911119111d11119111d1191191d1dd91d1d191d91d191d91d1d19d9d19d9191dd9dd9dd919dd9dd9d9dd9d9d9d9d9dddd1d19dddddd9ddddd9ddddd9dd9dd9dd9dd9d9dd9d9ddddd9d9ddd9d9d9dbd9dbd9bb6a6a69bb8b6a6b6a9b6a66a6a9d9dd9d9dd91ddbb6b6bc8cc6bbd1dd9b1d9
                    a6a9bb96a9b9d69b6a68bb1b6c6c8c68c68d111d111111111111111119b6a6a6b6a66b6a911d1d191d111111111d11d19d11d11191d111d11111d11d1911d1911d1d1d19d1d1d9d9d9dd19dd9dddd91d9dd9dd9d9dd9dddd9d9dd9d9dddd91d9dd1d911911d19d1dd9d9ddddd9dd9dd9ddd19d19dd9d9dddd9d9d9d9d9d9d9b1b9bb66bb9a6b68b68b6bb6b6a666a9d9dddd9dd9d9cbcb6bfc3bcb9dd9dd9ddd
                    6a6a9a6ab9bb9cb6a6c6d916c8a6c6c6ca6b11111111111111111119db6a66b6a66a6a661111911111191191d1119111111119111191d111191111911d191d1d911911d1191911191d19dd91d19191d1191d9dddd9d19d9dddd9dddddd91d11d1911d1d1d19d1d91d11d19d9dd9d9d9dd9d9d9dd9d9d9d99d9d9dd9dbd9dbd9db9a6bb69a6b6a66a6a66a66a6b6a6b9d9d9d9d19db6c6dcc6cc6cbd9ddd9dd9d
                    6a96b6b69b9bb69a66c6d1b8a66c8c8c668b9111111111111111111116a6b68b6a66a6b6d1d111d1d11111111111111d191d11d19111191d1d1d911d1111111111d11191d11d1d1d19d111d191d1d119d1d119191d9d1d1191ddd9d191d1d9191d191d919d1d1d1d9d9d1d1d91ddd9dd9d9dd9d9dd9dd9dd9d9d9dbd9d9d9dd9bb9b69bb6a66a6a6b6a66a6b66a6b6dd9dd919dd9cbbbb6c7c6cd7d1d9ddddd9
                    a6a66a6a6bb69bad6a6a91b6c6a6c6c6a6c6d111111111111111111d9c66a6a666a666a69d11d111911d11d191191d1111111111d1d1d11911111d1191d1d191d111d1111d111911d11d911d11111d1d1d9d1dd1d111191d1d91d1d1d1d11d1d1d1dd1d1d119d91d11d19d91dd9d91d9ddd9d9dd9dd9d9d9d9dbd9d9d9d9d91d9bb9bb9b66a66b66a66a6b66a66b6a9dd9dddd9ddc9b7b6cccbc9b9dbdd9d9dd
                    66b6a6b6b9bbbb66b6c91d68c6c68c6a86c8a1111111111d11111111b6a6b66a6a6a6a6a6d1911911111911111d1111911d19191b91191d1d19d11911d1911111191191d1911d1d191d11d111d1d91119111d1191d1d1d1d91d19191d19d191d91d9191d9d1d1d19d91dd1dd91d1d9dd9d9ddd9d9d9d9d9d9d9d9d9dd9dd9dd9a9bb9b9a6b6a6a6a6b6b6a6a69a66a99dd919d199cd9bbcc6c6bdddd9b9dbbbb
                    8a6a6b6a6b9b6b6a6a611b8b8c6c6c86ca666b111111d1111111d1916b6a6a6a6698b698b911111d1d11d191d1111911d1111d11b9d111191d119d1d1911d1d1d1d1d1d11d1911911d1191d919111d1d1d1191d119191d11d191d1d191d1d1d1d1d1dd1d1d91d9d1d1d919d1d19dddddddd9d9ddd9dd9ddd9dd9ddd9dd9dddddb9b9b9a9b6a6b66b68b66a66a68b66a91d9dd9dcdcbb6b6c7cbdd9dbdb1bb6bc
                    66b66a66dbb9a6a6b6d1d9c6c6ca86ca66c8c61111111111111111d9a66698b69a8b6a6a6a111d11119111d1919d11d119191119bb91d91d119d11d91d1d9119191d1191d11d1d1d119d111d1d1d191191d1d19d1d1d19d191dd1d1dd1d91d91d919d19d91d191dd9d1ddd19ddd19d19d9d1919d9dd9dd9dd9dd9d9d9dd9d19b9bb6b9b6a66a6a6a6b6a66b66a69a6b9d91d91db9c9bcccbcc79bdd9b9dd6bb6
                    a689a6a69b6b69b6b9d1bb86ca66c868b86a6a1111111111111919bb6a6aa66a86a6a66986119111911d19111d11111911d11d1d981d1111d111d11d1d91d1dd1d119d1d9191d91d91d1d9d191d91d1d1d919d1d91d9d1d1dd19d9d19d1d191d1dd1d91d1d9ddd191d9d19dd191dd9d1d19dddddd9dd9dd9dd9dd9dd9d91dd1db9b9bb9b9b66b666a6a6a6a69a6a6a691d9dd9d9bbb7b6c7ccd1c9bdbdd6dd6c
                    6a6a666bb9b9ab6b9dd9b6ca668c6ac68b8c66d1111111111911db696b666a6b6a696a6a6b1111111d11111d11191d11d1119119b6b11d9119d19d191d1d19d91d9d1d91d1dd1d11d191d19d1d1dd19d1d1dd191dd91d9d9191d11d91d9d91d9d9d91dd191d1d9d1dd1d91d9dd9d1d19d91dd9d9dd9ddd919dd9dd9ddddd19d9d9b9b9bb6a6a6a6a666b669a66a666bb9dd91d9db6bb6bcb8cd9bdbd6dbbbbcb
                    6a66a6a6b9ab6b9bdddb9866a6ca686ca66c8a9d11111111111d9b9a6a6a96a6b6b8b6a6b61d11d111191d191911d19111911d1db6a1911d1d1d11d1d19d1d1d91d191dd9d19d9d9ddd19d1dd9d91dd9d9191ddd91dd1d1dd1dd9d1dd9d1d9ddd1d1d9dddd9d1d19d9d1ddd1d1d9d9dd1dd9d1d191d19dddd9dd9ddd9d9ddd1d9bb9a9b9b6b66b6b6a6b6a6b6a66a989a91b9dd9bcb6bc6c3cbdd9cdd9bbd6b6
                    c6a68b6a9a9b6ab9d19a6ac6b8b86cc668a6c6611111d111d1d9b6b6b698a6b669a698989a9119119111111d11d1111d1d1d1119a6611d191191d91d91d19d91dd9ddd91d19d1d1d919ddd9d1d1d9d1d1ddd9d91dd9d19d19d191d9d919d9dd9d9d9dd19d1d9d9ddd1d9d9d9d91d1d19dd1d9d9ddd9dd19ddddddd9ddd91d9ddd9a6db9c98b6a6a6b6b6a6a9a6b66a6a6b9bb9bdb6bbbc7ccb79dd6dbdc6b6bc
                    66a6a66a6bb6b9b119b6c68cb66c8c6a8b68b8b9d1111111119d69a69a89a69a69a6a6a6a6d111111d1d1919d11191d111111d1b6b691d1d1d1d11d1d19d1d1d191d91dd9ddd9191dd1d91d19d9d19d9d91d1dd9d1d191d1d1ddd1d9ddddd9dd9d1d9d1d9d1d1d19d9dd1d1d1dd9d9dd9d9dd1d19dd19dd9d9d9d1d9d9bd91d9b6b69b9a6a6a6698b6a669b966a69a669bb6cdbb8cb7dcb6c6bdddb9d6cbbbbc
                    6a666a6b9b9bb9d9dbb6a6a6b6a6c6a66c8b86a61111111191b9a69a66a66b69ab6a6b6a69b11d11111111d9d9d11d119d19191b69ab9d191191d9191d1d191d91d1d191d191dd1d19d1d19dd1d1dd1d1d9d9d91d9d1dd9d9d919d91d9d9dd91d9d91d9d19d9d9dd1d19d9d9d9dd1d91dd19d9ddd19ddd1dd1dd9dd1ddb9dd19b9a9a6b6b66b6a6a696a6a9ba66a66a6b9bcb9c9c6bd6c6bcbb1b9bddb7d6d6b
                    66a6a66a6bb69b1d9b6a66c9a68c6a68a6c6c6a6b11111111d9b9a9b69a6b9a669a66989a69d119d1911d9d9bb9d119111d1d1d6b86b99d1d1d11d1d191d1d11d1d191dd1d1d11d91d19dd1d19d919d19d1d191d1d9d91d1d1ddd1dd91d191dd1d1dd91ddd1d1d19d9dd1dd191d9d9dd9d9dd19d9dd9d9d9d9d1d9d9d9b9dd9dbb6b69a66a989a66a6a698d96b69a69a9db6dd8bccdd6cb7cb9bddd9bb6bbbbb
                    6a6a6a6b9a9bb9db9a66c6a6b6c6a86c6a6a68b66b11119119b9b69b9a69a6b9a69a6a6a6a9d111911d119d9b6b19111d1111d9b9a6a9b9d191d1191d1d191d91d91d1d191d19d1d1d1d19191d1d1d191dd91dd191d1dd9d9d919d91dd9d1d919d9d1dd91d9d9ddd1d9d9d9dd9dd9dd9d1d9ddd1d9dd191dd19d91d19d9dd1d9b969a6b6a6b6a6b6b69a6b9b9a6a6a6d9d9d9dcd6c6bbccb6bdb9bdd6bddd6dc
                    6b666b6a6b6bb9b9b6ba68b6b8a66ca68686a6a6a6119111dd9b9b9a69a6b9a6bb66a696b6b911d9d111d9b9da6911d111919d1a6b669a99d1191d111d191d1d11d1d191d1911d191191d1d1d191d91dd11dd19dd1d91d1d1d1dd1dd91d1dd1dd1d19d1dd1d1d19d9dd19dd9dd9d1d91d9dd919ddd19dd9d9ddddd9d9bd9d9db9ab69a9a66a66b9b9a66a9d9b6b66b9ddddddb6d8fd6b67ccb79dd9ccbddbb9c
                    6a6a6a66b9b69ddbb9b6a6b98b68c68ca6a6c66a681111d9d9b9b9b9b9b99b969a69a6a6a691d119d119d9b99a6d91119111dd9b66a9b6b9dd1d11d191d1d191d1911d1d1d1d191d1d1d191d91d1d1d19d919d1d191d19d19d919d91dd19d9d191dd1d919d9d9dd1d9ddd91d91dd9ddddd91ddd9d9dd9dddd9d91dd9b9dddd9b9b9a9b66b9b6b9b9a6b6b9db6a69a619d9d9d6cdfc7bccbc6bbbdbdc7dd6d6bc
                    66a666a6a9abbd9db9866c6a6c8c6a666c6c6a66a6b11d1d91b69a6b9b9a99ab69a669a69a6111d99d119b9d9c9b9d1d1d1d19d9a6b9a6b999d1d91d1111911d1d1d91d919d1dd1d91d91d9d1d19d9dd1ddd1d19ddd9d1d1d1ddd1dd19dd1d9ddd9191ddd1dd99d9d19d1d91dd9d1d9191dd9d1d919dd19d9ddd99b9b9bd9dd9b9ad6bb6a6a69b9a96b6a9b9a6b6a9dddd9dccb9f8bb7c6cc7c6d9b6b6bddb7b
                    b66a6a698b69d9bb6bab6a6b68b8c68a6c8b868a66b1919d19a9a99b9b99db69a6a6a6b6a69b19d9d91d9bdbb6a9b1111119ddb6b6a9b6a9bd9d1111d9d1d1d19111d11d11d9191d1d1d91b9d1dd1d19d19d19dd1911d19d9d19d19d91d9d1d191dddd19d9d1b9dd1dd9d1dd91dd9dddd9d919ddddd9d9d1d9d91bb6b9dddd9bb9b69b69a69a9b96a69a61b96b6a69d9d9dd8cbdfcc6cbc3b9cbbdbbbbd9bdc9
                    8a6b69a8b9bb9bb9b96a6b68b8c68a6c8b6a6a6b6a69d9b9d69a6b9dd9ab9b6a6969a69b69a9d19d9d9b99d9a66a9d91d91119b98989a66b99b1d1911d111d11d19d191d91d1d1d1919d9d9dd919d1d19d1d91d1ddd19dd1d1d19d1dd1d19d9dd91919d1d1d99b19d91d9d9ddd91d19d1ddddd9d9d1ddd19d9dd9a69a9d9d9d9bb9bb69a66a9dbb6b6a6b9bb6a69a9dddddbc6b6f87bc9cbdcbd6b9b6bdb9b6b
                    b6a6a86b6b9bd9bbb8b68b6a6c6c6c8b68a668b868b9b99d9a969a99d969a6969aa669b9a6b99d9d9bdd9bdb6a66d9d111d1d1bb6ab96b9a9d9d9d1d191d91911d11d1d11d191d91d1d9b9b9dd1d9d9d1d91d19d191dd19d19d91d91d9d1d1d99dddd1d9d91d9bdd1dd9ddd19ddd9d19d919d9dd19d9d9d19bd9b69a9bddddb99d9a9a6b6b6d99b69a69b9d9a6b66db9d9db6dbc8fcbc7c6b6bdbbbbbd9dbdbb
                    66666a6a69ad9bb698c6a6a6c6a8c6a68b86a68bb68a9b9db9bb69b9da989a6a669a6b9a698b9d9d9d9d9d16b69a9d9d9d11b99b66a6a6a69b9d9d9d9d911d1d91d191191d91d11d191b9d9b99dd9d9d991d1d1d1d191d1d91ddd1dd1d9d9d1b9d191dd1ddd19999d9dd99dd19d1d9dd1ddd1d99dd19dd9dd9d9ab6a9d9199bbdb96b69a69a9db9a6b69d9b96b6a6bbbbb9bbb6cfc6bb6cbcbc76c97b7bb7db9
                    ba6a6986ab9ddb9ab6a66c6b8a66c86c68b86a66a6a699d9a969a9b9d6a6b69a9a69a9a69a9a9d9db9d9a91b6a669d99d91d9b9a9a69b66b9d9b9d9d9d9d1111d111d1d1d9dd1911dd9d9b9d9d9d9d9bd9dd91d919d1d91d1d119d19d911d9d9b9ddd9199d9ddbd9dd19b9d9dd9d1d19d919d9b9d9b9d91dddd96b69d9db9b9d9bb9a9a6b69d9b9a69ab9b9ba669a6b9cddb8c7cfc7bdbb6c76dbbbbd6bd6b9d
                    66a6a6a66b9d9bb6a6b8a6a666c8c6a8b86a6c6a666cbd9a9b9a69b9d9b69a6989a66b69a6699d9d9ddb9dd698ab99bd9d9b9bb66a9b6a9a9b9db9d9d9d9d9d191d911191d991d1919d9b9bd9b9d9b99d9dd1d1d1d1d1d19d19d1d1d1d9dd9d9d9d91d1d9d9d99b9b9d9d9dd9d19d9dd9ddddd9b9d9d9dd9d99a9a6d9b9a9b9bb9b6b69b6a9bb9b6b6b6dbd96b8b9bbb6d6ccccc3c6bd6dbbbb9cb7bb6bbccdb
                    6a66a66a9bddb9b6b68b668b8ca68c6c6a6c6a66ba66a9b96a69a9bd9a69a69a6b69a69a69a6b9d9d9d9a9d9a66a6d99d9d9d9a6b69b98b69ab9a9d9db9d9d9d1111d1d1d9db11d1d9d9d999b9d9d9db9d9d9d91d919d1d1d1d191919d9d91d99b9d1d99b91ddd9d9dd9b991b9dd1d9d9d1919d9d9d9d9d9dd9b69b9d9b6b9a9b9a9b9a6991d9d9a69a9d9bb6bb6bd6cccb3c6ccf6bbdb9b79bbbb9bdcb6bb9d
                    66a69a6a69d9db9a6c6a6c6ca66c6a68c6a6a68a66a669d9d69a699db6989a69a69a69a69a69b9dd9d9a61bb6a69a9d9b9db9a69a69ba69a66a66dd9d9d9d9dd9d1191119d99dd9d9d9bd9dbd9dd9b9d9d9d9dd91dd1d91919d91ddd9d9bdd9dbd99d1d9db1d9d9b99b9d9dd9d9d9d9d9b9dd9d9bd9db9d9d9b9a6ddbd9b6a9b9b9a9b9abd9b9d9ba69d9d9bb69ab6bc3ccccc9c8cbb9bdb9bbd9bd6bb7bb7bd
                    a698a669ad1b9bb6b6a68a6868c8c68a68686b66a66a6a9b9b9b9a19b6a9a69a69a69a6989a9b9d91d9b6d9b6b6a69b9d9b9b9b69a9b98a69a69a9d9d9b9bd9dd9d1d1d9d9db9d19ddd9dd999b9dd9d9db9d9d9d9d9d1d1dd9dd91d19b9d9d9d99dbd9d999d199b9db9d9bd9d9d91d9d99ddd9b9d9d9d9bdddb9a99d99b9a69a69b69b699dd9bd9a69dbdd9b8bc6bdc3cf6c67bfc7bbbd9bbb6bdddbd9bb9dd9
                    6a6a6b8a619bb96a6a66b6ca6c6a6a6c6a6a68a669a6a6a69a99a9d9a96b69a6969a69a69a669bd91db9a91b6a669a9d91a6db6a6b9bb69a669a69d9d9d9d9d9dd9d191d9d9d99dd919d9d9dd9d99d9d9dd9d9d9d9d919d9dd9d9d9d9d99dd9d9d99dd9dbdd9dd9d99d9b1dd9d9dd9d9bd99dddd9d9db9d99db96bddb9bb69b9b9b9a9bdd9b9bd96ad9d9db9cb8b6bcf6ccccb6cfb6d9bb79bcd9b6dbb9bdbdb
                    6b6698969dd9bbb686a6c868b8c68c6a6c6cb66aa68b669a69b99b9a69a9a696a696b69a69b9a99dd9a69d16a69a699d9db999b69a99a6a6ba6b6bd9db9d9d9d9d19dd9dd9d9ddd9dddd9d9b9d9d9d9d9d9bd9bd9d9dd1d19d9d9dd9bd9b9d9d9bd9dd99d9d99b9b9db99d9dd9b9dd919bd9d919b9d9d9bdd9a6b9d9dd9a9b9b9b9a9b91d9dd9bbb619ddd9b6cccb9ccc8c3bbbf6bbbdd79ddb6bdd6d6ddd9db
                    69a6a6ab91bb9b6a6b6c6a6a68b8b868c6a66a666b66a6a6a6a6a6b9b9b969a969a69a69a69a96bdd9b9b19a698b6a9dd9a61d9a6bb96b6969a6999d9d9d9b9d9d9d91d9d9db9d91d919d9d9d9bd9ddd9dd9d9d9d9d9d9d9dd9d9d9d99d9d9d9d9d9d9dd9d1bd9dd99d9bdd9dddd9dddd9d9d9bd9dd9b9dd19b9bd9d9b9b99d9a9b9b9d9d9b9d99a9db19ddcbc87bb3c8fcc9d6fc6b9db9bd9bbbbbd6bbb6db6
                    a66a666ad9b9ba66b6a6a6c6c68c68b8b86a68a6a6a6a666b6b69a69d9d9d9a69a69a69a9b669a99db69dd9b6a69a99dd9b9d9a69a9a69a6a669aa9dd9d9dd9d9ddd19dd9d9dd9d1d1d9d9dd9d9d9d9dd9d9d9d9db9d9dd19d9d9dd9d9d9d9db9d9d9d9dd9d9d9d9db9d99dd9d91d9d9dd9b9b99b9d9bd9d9b9a9dd9dd9a9d9a96b99d1db9bdbb9a9d9dd9b6bfcc7b8c3cc7ddc8cbbdddbdbbb676ddcbdbddcb
                    69a69a969b9bb6ba6b6a66a68a6ca6c68b68b6a66a698b6a699dd1111db9b969a69a96b6699a969b99a9ddb69a6a6a99d9a91a69a9d6b6a69a9a6999d9dbd9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9dd9d9d9dd9d99dd9dd9dd9db9dbd9d9d9ddd9d9dd9d9d9d9d9d9d1d1d91dd9d9b9b9b9b9bd991dd9d619dd9b9b91b9a96a9d99b9b999b619ddd9bb8c8b9ccccc6cb9cfc7d9bd6d6dbcbbd9b6c9b9cb
                    69b6a6a6b9b9b9b6b6a68a6a6c6868a6c6a6a66a6b6a6a69adb111119191b9a9b9a69a99a69a69a9a69dd9b6a696b69ddb61d9a6b9b9696a6b9d6a9b9d9d9d9d9d9dd9d9ddd9dd9d9dd9dd9d9d9d9d9ddd9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9d9dd9d9d9d9d9d9d9d9d9d9ddd9d9d99b99b99b9d9dd9d9d9dd9dd9b9d9b96b99d9db9a9bdb9bd9b19da9ffc7bfc6cccb9bcf6bdb9bd9db6cb6dbbbdddcbd
                    6a69869a9bdb9a69986a6668b8a6a66a686a6a66a66986a6191119d1ddd9d9b98b69a66969a9b9b9b9bdd16a69a69ab999a9d69a69b9aa69a69b9b99bd9dd9d9ddd9dd9d99d9d9d9d9dd9d9d9db9d9d9d9dd9dbd9bd9d9d9d9d9d9d9d9d9d9d9dbd9d9dddd9dd9dbd9dbdddd1919d9d9bd99b9b9b9b9bddd9bb9bdd9db9dd9a9b9a9d9b9b9b99b9b9d9dd9cbc8c6bc6c3c6bdb3fcc9cd9ddbdcb7bb6bb9dd7d9
                    6a6a6a6a9b9b9bbaba96ca6a666c6c68a6a666a66a6a9a69d11d9d9b99b9bdd9a6b969a9a6969a69a9d919b69a6a6961bb619a969b9a669a69b9a69b9d9d9d9d99d9d9d9dd9d919d9d9d9d9bd9d9d9dddd9dd99d9d9d9d9d9ddd9d9d9dd9dd9d9d9d9d9d91d9d9d9dd9d9d19ddd19d9b99bd9b9b9b99d9dd9b9dd9dd9dd9b9b9b9b9db9b9b9db9bdb9ddbbc6f3cd6ccccbcb9bf8bb7bbd9d9c79bbddd9bd9bdb
                    66a69a66b9b9b9b966b86a66ca6a6a6b686ca66a68b6a69d1d9bdbb9ad9b999d9b8b9a969a9a699a99ddd9a98b69a69d9a9db9a9b9a969a6b9a9b9a99bd9ddd9db9d9d9d9dddd9d9dd9dd9b99b9d9d9d9dd9dd9bd99d9db9d99d9dd9d9d9d9d9d9d9d9dd9d9d9d9d9d9dd9d1919d9b99b99d9b9b99b9d19d9bdd1dd9d9dd9b9a9b9d9bd9b9b9db99b9dd9bcccc6bbf6c6cddd8fc6b6d9ddbbdbb6bc6bdbdbb9b
                    b66a669a9b9bb9a6ba6a66a66868b6a6cb666a6a6a669ab11db9b9b9b9b9abb9d96a69a9b69b9a69d9d9d9a69a6a69a9a9619a69b9b9ab69a9bd9b9b999d9d9d9dd9dd9dd9d9dd9d9dd99b9db9d9dd9199d9d9d9d9bd9d9d9dbd9b9bd9dddd9dd9dd9d9dd19ddd9d9dd9d1d1dddd99b9bb9b9b99b9ddd9bd9d9d9d9dbddd9a9b99d9a9b9b9db9b9bd9d9bb6c8ccbcccc7c9b9fcfbcbbdd9db9bbb6ccb9b97dbc
                    6a69a6a66b9b9a9b66b6a66a6ab6a9199bd99a66a6b999119b9b9b9b9bb8b69b9d96a9669b969b99b9b9da6b6969a6b96b9d9b69b9a969a66b9d9a99bb9b9d9d9d9d99d9dd9d9ddd9dd9d9b99b9b9ddbd9d9d9d9d99ddd9b9b999d99d9d9d9d9b9d9dd9d9d9d99d9d9d9d919d919b9b99b9d99b9bdd91d99bd9ddd9d9d19b9b9b9d9b99d9b9d9b9b9ddb9bcf3cc76c3bb6bdb3cf6b6b9dbdbd9dbcc7b7bbbb7b
                    698a669a9a9b9b6bb6a66a6a668b11db9d1bb99a669db1d1d9d9d9bba69b6a9a9db969b9a9a9a9b9a9bd9969a6a69a9a9b9d9b9a9d9bb69a9b9b6b699b99b9d9d9b9b9bd99d9d9d91d9d9b9b99d9b99d9dd9d9dd9db99d9d9d9db9b9bd99d9d9d9bd9d9d9d9d9bd9d9dd1dd19dd9b9b9b9b9b9b9d91d9d9d9ddd9d9dd9d9b99b9d9b9a9d9d9b9b9bd9dbb8ccc87bccc6bbb7c8fcbc7cdd6d9bd9b6cb6bbb79bb
                    8a669a66a69bbb9a666a66a6a6b9d99d11d99a69d9a9dd19db9bb9a66ab6a689b9d9b9b9696999d9b99dba6a9a9a69669a9b9a69dd99a9a69b9b9a6a99b9d9bd9b99b999d9d9d91dd9d9b999bd9bd9d9d9d9ddd9d9dd9d9d9d9b9d9d99db9d9b9d99d9d9d9d9d9d91bd9d9d9d19b9b9b9b9b9b9b1d91d9bdd9d9dd9dd19b9a9d9b9b9b9d9b9b9b9a9d99bc6f3cb9cc6bb9cbcfcc6bbc9bbddd9bdcbdc6bdbbbb
                    669a8b69a6a99a96a6a6a66b6a9d1d11d9bbb9ba6a6b9d9db9b9bc6cb6b68b6a9b9bd99b9a9b9d9a69bd69b69669a6b9a9d9b9b9b1a696b69b9d69a9b99b9b9d9d9b9db9b9bd9d99d9b99bd9b9b99b9dd9d9d9dd9d9d9bd9b9bd9d9b9d9d9bd9d9b9bd9d9dd9b9ddd91d91dd9d99d999a99b99dd91d99b19dd9d9d9d9d9b9b9d9b9b99d9b9b9b9a9dddbcccccfbd8cbbb7b6838c7b6bbd6b9bddb79bdbd6d9bd
                    6a6a69a8969a9b6b69b96a6a69d1191d1b9a8666a66b9dd9a9bbb6a6a96c68c6c9b9bdd9b9bdd9a9b9b9b69a69a69b9a969b9b9a999ba96a9d9b9b699a99b999b9b9b99b9d9d9d9d9d9b99b999d9d9d9d9b9d9d9dd9ddd9d9b99d9b9db9d9d9d9b9d99d9dd9dd9d9dd19dd9dd9b9b9a99b99bd9d19d9d9dd9d9ddddd9b9b9d9bdd99bd9b9b9b9b9b99b9c6c3b8dd3c7dd6bccfccb6bb9dcbdb9d6bb9b9bdbbb9
                    6a66a666a9a69b9b9a6a66a6b91dddd9bb66ca6a6a6d9b9a9b698a66c6a8b8b68a6a99dd9d99d6969a9b9a69a69a6989b9b9b99b9db69a9b6d9dd9a69b9b9b9b99d99b9d9bd9d9db9b9db99bdb9b9d9d9b9d9d9dd919d9d9b9d9b99b99b9b9d9b9d9dbdd9dd9d9b99ddd9d9d9d9d9b9b9b9d9dd19d9dbd9d99d9d9d9b9d9b9d9d9b9b9b9b9b9d9a6dddbccccc3b9cbd9cbb3ccc6bbd6dd6d9dbbbdbdddb79bdb
                    669a69a6986b9b9a6b66a66a91d9d9db6a6a66a669d9a6b9b6ab66ca6b6c6c8c6b66b9bd9db9b9a9a969a9b69a69a9a69a9d9bd9a99a6969bddddd9b99a99b99b9b9b9b9b9dd91b9d9b99bd999b99d9b9d9b9ddd91d9dd9d99b99b9db9d9d9b9d99d9d9d9d9d9b9d919ddd9d9d9d99d9d9d9d9d9d9bd9d9db9d9bd199db9d9dd9b9d9b9b9b9b9b9999d6c6c6cb9bb6bd6bd8c3ccc6dbddbddd6cd9d9d9bbbb9b
                    ba66a66a6b9a69b9b69a6b69dd9b9a98c6c68c6a6da68c6a6b66a86b6cb86a6a68a6dd9b99a9b96969b969a9a9b69a9b99d9b1d9b699a6b9b19119d9b9b9b9bd9b9d9b9d999dd9d9b9b9b99b9b9db9bd99b9d9d9dddd9dd9dd9b9db99b9d9d9d9bd9d9d9d9dd9d9bddd9d9d9d9bd9bd9d9b9d9d9b999bd99d9bd9d9dd9b9bd99b9b9b9b9b9b9b9a6db9ccb3cc6bbdbd6b6bccc6b6e9b9ddddd6cbddbdbd6bdbd
                    66989a69a9b9a69a9a6b6a6dd9ab6cc6c6a6c6a6d6b8b86a6a6a6b6a6b8b8686c6bb9b9abb6b9a9a9b9b9a96969a6969a9b9d1d99a9a99a99dd9dd19a699b99b99b9bd99bdb9d9db9a6b9b9d9d999d99bd9d9dd1d9d9d9d9bd9d9b9bd9d9b9d9b99bdd9d9dd9d9b9d9dd9d9b9b9d9d9d9dd9dddd9dbd9d9b9d99d9d9b9d9d9bd9b9b9b99b9d9b99b9dac6ccc6bb6b6dbbb6c6cbb7bddb9b6b9bb979b9bdbd9b9
                    b6a6a66a998b6bb6969a69a9b6b6c6ca6c6c8c6b9a6b8c686a668c6b6a66cca6a68b9bb6869a6969a99b9b9a69a9b69a9b9dd91d9b9b69b9b9b91d9a69a99b99b9d999bd99b9b9b9a6b9a99b9b9b9b9d99b9dd9d91d9dd9d9d9b9b999b9d9bd9b9b99d9bd9d9d9dd9d9d9b99b9d9b9dd9d9d9d9d9d99d9d9b9db9d9b9b9b9b9d9d9b9b9b9b9b9a9b99ccc7b8bdbddbd6c7bcc7b6bb9bdd9bcdcbdbbbb9b7ddbd
                    698989a9bb68b69aba69a69da68c6a68c6c6a6a6bb68b8ca66ca6a68b6c8b686cb6b9b6a6a6a69a969d9a9b9b6969a96b9b9dd19a9b9b99bd9a91d9bb6a6b9b9b9b9b9b9b9b9abb6a9b6a6d99d9d9d9b9d9d9dd1d9dd9d9dd9d9b9b9b9d9d9b99d9d9d9d9d9ddd9d9dd9d9b9b9d9d9d9dbd9dd9d9dbd9b9bd9bdd9babbb9a9b9b9b9b9b9b9b9b9b9bbc6b6bc9b9b97bc6bc6bbdbbbb9ddbc7b79bb6b7db9bd9b
                    6a6a6a699a6b6a8696b6a9b66cb8c6c6c8c686c6d6a6c668ca668b6c68b68ca66a6bb9a66c66a9b9a19a96969a9a9b69a99d9bd9b69a9b9d9a9b19a69a699b9b99b9b9d9a9b9b99b999a6b9b9bd9bd9d9d9d9d99dd9dd9d9d9b9b9b99db9b99bd9b9db9d9bd99dd9d9d9d9d9bd9b9b9d9d9d9d9dbd9dd9d99b9dd9a66a6bbbb9bd9d9d9b9b9b99b99b8bbb6bdbd7bb9cbb6b7b9b9b9dd97bb9bdb9bbbdbdddbd
                    9b69b69db9bb6b6b9a9a69bca68b68c8b68ac6cb9c6a6a6c668a6c8b8b8b666ca6b9a6b6a6a6b69a9d99a9a9a9b9a9b969da699b9a669b9b9a69db6989a6a99b9b9b9db9a6d9d9b9bdb9a6b9bd9d9d9d9dd9dddd9d9d9ddd9d9b9a9b9d9d9bd9d9dd9dd9d99db9ddd9dd9db9d9b9b9b9d9dd9dd9d9d9dd9dd9dd9b6cb6b698b69b9b9bb9b9bd9b9b9cc7b6bdd79bd6bc6b7bbddbd6dddbd9bbd9bb7b6b6db9bd
                    99a99b9d9b99d9b9b9b9a9b66c6c8b8b8cc68b8b6b96c68a8c6c6a66c6b8ca866a6b69c6b6b6a69b9d9b969a969b969a9d9b9a9a699a69a9b69a9b9a6a69b9a99d9ab9b9b9bdd9bb9a666b6a99d9d9d9dd91b9d9d9d9d99dba9ba6a9b9bdd9d9bd9dd9d9dbddd9d9dd9d9d9d9d9d9d9db9b9d9bdd9dd9dd9dd9dbb6a6b6bab9ab9bd9b9b9d9d9b9b9ccb6cb19bb9dbc6bbbb6d9b6b7d9bdbd6dbbd6bbbdddd6d
                    d9db9d9bd9bb9a9a9b99bb6ca6a6c6c6c68b68b6a9ba6a66c6a6a6ca6a6b66a6c6b6a6b6a69a69a99d9a9a969dd9b9b9db9a69d9a6a9a69a9a9b6a6b69a69a9b9bb9b9db6bd9db9bb6ab6a96b9b9dbdddd91dd9dbd9bdbb9b9b6b96bb9b9d9d9ddd9dddd9d9d9d9d9dd9db9bd9db9bddd9bdbd99bd9dd9dd9db9b6c6b9a9b9b9b9a9b9b9bbd9b9a9ac9db7dddbbdb9cb7b6bddbdcbb9bbd6dd9b9dbb6b9b9dbb
                    9d9d9bd9ab9a6b6b6b9a96b66b6b8c68b8b8c68bbb6b68ca6a686c66b6b6a6c6a6bb6bb6b6a6b96b9b9b69b9b9d9b9d9b9a69a9a69669a696b9a6969a69a69b9d9da9d9a69b9b9a9a66b66a9a99dd9d9dddd9d9b9dd9d9ab6bb68bb9bbbb9bd9d9dd9d9dd9ddd91dd9dd9dd9ddddd99d9b999bdb9d9d9bddd9bdba6bb6bd9b9b9b9b9a9b99b9bb9b6bdbd9d9d9b9bb6bbbbd9dd79cddb6bd9ddbdb6bbdddbb9d
                    b9d9d9a9b6b6bb6a9a9b9b9ab6a66ca6c6c6ca6b69b6a66868ca6a6a6bb6b6a6b69a6b6a698b69a9a9a69a9b9bd9d9b9a69a6d969a9a69bb9b96b6a69a69a69ddb9b9da6a9bdbb986b69a6a66b9dd9d9dd9dddd9dd91d99b9b6a6b6b9b6a69bd9d9d9dd9bd9d9dd9dd91d9dd9d9d9ddb9dbdbd9d9d9dd9d9bb9d66b6b9b9bdd9b9b9b9b9bbd9b9a6bd6d6dd1db6db6bb76bdbd9bcc9bbd6ddb9d9bbb79dd7ddd
                    6b9b9b9b9a6b6a6b6b9bb9a99b6ca66c6a6a66b6bb98b8a6ca66c6a6b9a6b6b6a6b6b6b9ab6a6a9b9b69899a999dd9a69a699b9a69a9699a69b9a9b9a9a69b9dd9b9b96b6b9b9a6bb6a6b69a69a9dd9d9d1d9ddd1dddd9d9bd9bb6bb9b96ab99ddddbd9d9dd9dd9d9ddd9dddddd9d9b9d9d9d9d9d9dbdddd9bb9abb6bb9dd9b9b9a9b9a9b9bd9b9b6dbdd9d9ddbdbb7b9bd7b9dd6bd6bdbd9dddbb9bdbd9b9bd
                    86a6d9b9b6b6a66a6b6b699b9b9a66ca6b6b6c6bb6a6c66a66ca686a6b9a9a6b6b9a9a6b6b66a969a9b9ab9b9add9a9a9b9a99b9d9b6bb99dd9a69b9b69b9bdd19b9b9b9a9d9b6b98b69a9a69a9b9d9ddd9dd9d9d9d9db9dd9d9b99b9bb66a9dd9d9d9bdd9db9b9dd9d9dd9d9d91dddd9dd9d9bdb9d9d9d9bd9bb6bb9bd9bd9b9a9b9a9b9d9bdb9bb9b9dd1b9bd6d9bdbb9bdd9bcdbd79bbbd9bb6bd9bdbbd9d
                    8b6b9d9b9b9a6b6b6b6a6a9b9b9b6a66a6b6c6a6b9b6ca6c8a66a6b6b6b6b69a9a6b9bb6b6a98bb9699a99b6999db96b69b9dd9d9b999ddb19a9b9db69b9b9d19b9b9b9a69bd9b9a6ba9a69ab9a9b9d9d1d9dddd9dd9b9a9dd9d9dbdd9a6b6a99dbd9d9dddd9b9d9dd9dd9d9ddd9bd9dd9bdb9b9d9bd9ddb9ddb9b9b9d9d9d9bb9b6b9b9b9bd9bdb9ddd9d9bbb9dbd9b6bdd9bbdc9b6dbb9dbbb9bddb9b9dddd
                    68a6a9d9b9b9b69a6b6b9bb9b9a9b6b6b6a6a6b9bb8c68c6a68c6a6a6b9b9a6a6b9bb69a6a6a668b9ab99b9b9bd99b99b99d9ddd9a9ad999db99a999b9bd9dd9d9bd9b99bd9b9b9b96b69bb96b6b9b9dd9dbd9d9dd9a6abb9dbd9d9d9d9b986a9b9dd9dd9ddddddd9ddd9ddd9d9d99d9bd99b9b9bd9ddd9ddbd9bb9bd9dbdbd9b9a9b9b9bd9b9d9bdd9ddddddbdd9bdbbdb9dbd6cd6dbdddd9bbdb9ddd6bdd9d
                    b66a6a9bd9b9b9a6b9a6a69a9b9b99b9a6b6b6bb9b6c6c6a6c6a68b6b9a6a6b6b6b9b9bb9668b8a6b969b9b9b99b9b9d9dd9d9d9d9d9ddbd99bd9bdb9dd9dd91dd9d9dd9d9d9b9b9a99b9b9b9b99a9b1dd9dd9dd9bb8c66b9d9db9dddd19b9a6b9b191ddd1919d9ddd9ddd9dd9bda9bb9bdbd9dd9dd9ddd9d9db9db9dbd9d9b9a9b9b9b9dbd9dbb19dd91db9b96ddd9bd6ddb9bb6dcb9d9dbd9b9bdb9bbdb9bd
                    6a686b69b9b9a9b9a6b66b9b9a9b9b9b9b9b9b9b9a6a6a686a66a66a6ad66a6b69b9bb9bbba68b66a9b9a99bd9dbdd9db9ddd9dd9d9d9d99bdd9d9d919dd9ddd9d9dd9ddd9ddd9d9b9b9b9b9b9b9b9d1d9bd9db9db6c6cb9b9b9ba999b9b9b9b9a9bdd9d9dddd1dd9ddd9ddd9d99b9b9d9d9d9d9d9ddd9dddd9d9d9d9dd9bddb9bb9b9bb99dd99b1d9ddd9ddddcb9dd9bbd9bbd6db6cddb9ddd7dbd9ddb9dbdd
                    6b6c6a6a9b9b9b9b6b6b9a9b9b9b9b9b9b9b9b9b9b66c68b86ca6a66a66a6b6b9ab9b9b99a66c6a66a9b9b9b9d999dd9dd99db9d9d9d9dbd9d9dd9dd9d9dd19dddd9dd9d9d9d9d9dd9ddd9d9d9b9b9d1dd9dd9bd9a6c86c9bdb9c6ab9b9d9b99a69b99dd1d9d9d9dd91d1d9dd9dbd9dd9ddddddbdd9ddd9d9dd9dbddbd9d9d9d9b9b9d9bdb9dbbd9ddd9db9d9d6bd9ddb9ddd6dbddb6dddd9db9bd9ddbdbd9bd
                    86a6a6b6b9a99b9b9b9a9bb69b9b9b9b9b9b9a9b9bbb6a68b8668b6a6bb6b6a6b9bb9b9db9a6a66a66a999b9b9bdb9d9d9dd9d9dbd9dd9d9dd9d9d9dddd9d919d9dd9dd9ddd9dbd9ddd9bd9bd9d9ad9d9dd9bbba6b8cb6ab9bab6a66a9ba9a9a9b99b9b99d9d9dd91d9d9dd9dbd9d9d9dd9d9d9dd91d9dddd9dbd9d9d9dbd9bd9d9db9b99bd9b9ddd9d1dddddbdb9dddddd9bdd9dd6dd9bdddddddbd9d9ddb7d
                    68b66a66a69ab9b9b9a9b9b9a9b9a9b9a9a9a9b9b99b6a6c6a6a6a6b6b6b6a9bb69b9db9b9b66a6a6b6bb9b9b9bd9d9bd9d9ddd9d9d9dddd9dddddd9d9dd1d9d9d9dd9dd9d9b9d9d9d9d9b9b9b9a9b1dd9bb9b6b6cc6cb6bb986c6b6b9b6b6b969b9dbd9b9d9dd9dddddd9dd9d9d9ddddddd9dd9ddd91bd9d9d9dd9d9d9d9d9bdb9b9bdb9b9b9dd1dddd9d9d9d9bdd9d9dbdd9dd9dbddd9d9bd9b9dddddd79bd
                    6a6a68a66a969a6b9b9b9a9b9b9b9b9a9b6b9b9a9ab99b6a68b6a66a69a6b6b69bb9b9b9a9b9a666a69a6a9b9b9b9b9d9dbd9d9ddd9d9d9dd9d919dd919d9d9dd9dd91d9dbd9dbd9d9db9b9b9bb9bb9b9db9bb8bb6c86c6b6bcc8cbb6b6a6b9abb9d9d9ddd9d9dd9d919dd9dddd9dd9d9dd9ddddd9dbd9d9dbd9d9ddbdb9bdd99dbdb9b9b9bdb1d9d19ddddbddb9ddddd9d9bdddddb9ddbddd6ddd9d9d9dbb9d
                    6a6b666a6b6a9b9a9b9b9b9b9b9b9a99b9b6b9b6b69a9b9b6a6a6a6bbb9a9b9a9b9bd9ba6a6b69a6a6a69c9b9b9b9d9bd99d9dd9d9ddd9d9dd9d9d9dddd9dd9d919dd9dd9d9bd99bdd9b9b9b9b9a9dbbdbbbbb66a6ccc6a6b68c666b6a6b6a666a9b9bd99bdbd9dd9d9d9dd9d9d9d9ddddddd9dd9d9d9d9d9d9dbd9d99dd9d9dbd9bb9bddb9b9ddd91dd9db9d9ddd9d9dddd9d9d9d9dd9d9ddd9d9dddddb9ddd
                    6b86a6a6a6b6b69b6bb9a9bb9a9a9b9b9b99a69a9a6b9a99b9b66b6969a69a9bb9b9da9c668b6a69a69a6b9a9d9b9d9d9dbd9d9d9dd9dddd9d1dddd9d9dd9dd9dddd9d9d9d9d9ddd9d9dbd9dd9b9db9d6b9b6b8bc8c86bb6bcc6cca6ad6a6b6c86b9d99dbd9d9d9ddd9dd9dd9d9dddd9d9d91dd9dd9ddbd9d9db9db9bd9bd9dbd9d9bdd9d9b9dd91d1ddb9dddd9dd9ddd9ddddddd9dd9bdd9b9dddd9ddd9dddd
                    6a66a66a66a9a9a9b69a9b9b9b6b69a9b9b9b9a6b6b69bb9a99b9b9ab9b9b6b9b9bb9c6c6c6a69a69a6b9a6b9b9db9b9b9d9d9ddd9d9d9d9d9d9d9d19d9dd9ddd9d91dd9dbd9d9d9d9d9d9d9bd9d9dbd9db6a6c6c6c6cb6bb68cb6b6b6c6b68ca6a9bdbd9d9d9dd9d9d9ddd9d9d9d9ddd1ddd9dd9dbd9d9ddb9b9b9d9a9d9bd9d9bd91db9bbdddd1dd9ddd9d9dd9ddd1bd9d9d9d9ddddb9dbddd9dddd9bddd9d
                    69a66a66a666b69a9b9b6b9c9b9a6b6b9b9b9b9b9b9a69a69a9b9b9b9a9b9b9a9b9bbb6a6a66a6b9c9b9b6b9abb9b9bd9b9dbd99d9d9d9d9dd9d9d9dddd9dd9ddd9d9d9dd9dd9d9dddd9dd9dd9d9db9bdbb6bc6bc6bc6bb6a6c6c6cb6c6c6c8c66a69d99d9bd9bd9dd9dd9dddddddddd9d19dd9d9d9d9dd9b9bd9b9bbba9bd9ddbdddd9bdd91191d9db9d9ddddddd9d9ddd1dddddd9d9ddd9d9dd9d9ddd9d9dd
                    a66a6b6a69ab69a69b9b9bbb6a69a69a9b9d9d9b9b9bb9b9b6b9b9b9b9b9b9b9b9b9b9a6b6a6b6b6b9b9b9b6b69a9b9b9b9d99dbd9dbd9dd9dd9ddd99d9d9dd9d9ddbd9d9d9dd9dd9d9dd9d9d9bdddd9d9c8c6c6cc6bb6b6cc8bb6a6b8c6c8c6c86a9bd9bd9d9ddd9dd9dd9d9d9d9d91d19dd9d9d9d9d9bd9b9b9bd9a66d9dd9d9d9d1b9dd1dd1d1dd9dddd9d9d9dddd9d9d9d9d9ddddd9dddd1ddddb9dddd9d
                    69a6b6a6a669a6bbb9a9b969a6a69a6b9b9bb9b9b9a96a6b99b9b9b9b9b9b9b9b9b9a6b6b6b6a9a6a6b6b9b99b9b9b9b9b9b9bd99bd9d9d9d9dd99dd9dddd9dd9d9d9d9dbd9d9dd9ddd9dd9bdbd1b9ddbb8c6cbb68b6bb6a6c6c6c6b6c6ca6c8c6b6a9d9d9dbd9d9d9dd9dddd9ddddd19dd9dd9ddbdbdb9bdbd9db9bb6d9dbddddddd9dd9d191d1d9d1d9ddddd1d1d9dddddddd9dd9d9ddd9d9d9d9ddd9d9ddd
                    9a6a666b6ab6a6969a9b9bb9a6bb6b9b6b9b9d9b9b9b9b9a6b9a9b9b9bd9b9b9bb9b9b9a6b6b6b6b69a9a9a6ab9a9b9ba9b9bd9dbd9d9bd9d9bd9d9dd99d9d9d9dd9dd9d9d9dd9dd9d9d9dd99d9d9db9b6c6b6b6c6bb6a6c6b6b6ab6b8b6c6c6c88b69dbd9d9dd9ddd9ddd9d91dd91d91d9d9dd9d9d99d9d99bdb9b9b9dddd9dd9d9dd9dd1dd19d9d1ddd9dd9dd9ddd9d9d9d9ddddddd9d9ddddddb9d9dddd9d
                    a966a6a6b669a9ab6b69b99b9b96b9a99a9b9b9d9b9a9b69b9b9b9b9b9b9d9b9b9b9a9b6b9a9a66a6a69b6b69a9b9a9b9a9b9b9d9d9bd9db9d9d9dd9dd9d9d9dd9dd9dd9ddd9dd9d9dd9d9bd9bddd9ddb6b6bbb6ccb6b6bb6bb8b6cb8cb6c8c8c6c6bb99d9d9d9d9d9dd9ddddd91d19ddd9dd9bd9b9bbdb9ddd9d9bdddd9ddd1dddd9dddd911d1dd1d9ddd9dd1ddd9dddddddddd9d19ddddd19d9ddd1dd9ddd9
                    b6a6a66a6a6a6b96b9b9abb9b9a9a69a9b9a9b9bd9d9b9b9b9b9b9a9b9a9b9d9b9b9bb9b9b69b9a696b9a9b9a6b9b9a6b9a9b9b9b9d9d9d9dbd9d9db9d9dd9d9db9d9d9d9d9d9d9dd9bd9dd9d9d1dd9b9bcc6b6a6b6bb6bb6b6b6b6b6c6a6b6c6c6a96d9dbd9dd9ddd9ddd91d1dd9ddd9dd9bd9d9dbd99dd9b9dbdd9ddddd9d9d9ddd9d11dd19d1d9db9dddd19d1dd9dd9dd9d1dd9ddd9dd9dddd9d9d9dd9d1d
                    6c966a6c66a969a9b8b9b99b9b9b9b9b9b9b9b9b9b9d9b9b9b9b9b9b9a6bbb9bd9b9b9b9b9b9a9b6a9a9b6b6b9b9bb9b6b69bd9d9bd9d9dbd9d9dbd9ddd9dbd9ddd9dbdd9dd9dd9dbd9dd9ddddd9dbbbc86bb6c6a6b9ab6bb6acb6cbb6bb6b8b6a68a9a9d9dd9dd9d9dd9ddd9d191d9dd9bd9d9bd9d9dd9bddd9d9ddd919dddd9d9ddd1d911dd19ddbd1d9d9ddd9d9dddddd1d9d1ddddddddd9ddd1dddd1d9d9
                    c8bb6a6cc66ab6ccc6a6b9a9b9b99b9b9b9b9b9b9b9bd9d9b9b9b9b9a9b969a9bdd9b9b9b9b9b9b9b69b9a6b9a9b9b69a9b9b9b9d9dbd9d9d9dbd9dd9d9d9dd9d9d9dd9dd9dd9dbd9d9d9d99d91d9b9b6cc6b6a6bbbb9bb9cb6b6a6b6a6bb6c6a86c6b6d9d9db9d9ddd91d91d1ddddd9db9b9bd9d9dd9dd9b9dbdd9ddddd19ddddd9d191dd9d1ddd9d9dddd1d9dddd9dd919ddd9d9d9d19d9dd19d9d9d9ddddd
                    8b6b6b8c8cb669cf8c6b9a9b9b9b9b9d9d9d9b9b9b9b9d9d9b9bb9b9b9b9a9b9b9ddd9db9b9b9a9b9b9a9b9b9b9b69bb9b9b9b9bbd9d9ddd9dd9d9d9d9dbd9dd9d9d9d9b9db9db9d9dd9dbdd91dbdb9bc6bb6bbb6b9bb9b6b6b6b6bb6bb6a6a66c8b6a9b9bd9d9dd9d9ddddd9d9d9d9d9d9dd9d9dbd9db9ddd9d9ddd9d19db19d9dd1dd1d1d19d9ddddd91d9ddd9dddddddd19ddddddd91dd19dddddddd9d9dd
                    6b89a6b8c6b6aa8cccc6b9b9a9b9b9b9b9b9bd9db9b9b9dbdd9b9b9b9d9b9b9b9b99dd9d9db9b9b9b9b9b9b9b9a9b9b9b9b9b9d9d9d9db9d9d9d9d9dbd9dd9d9ddbd9ddd9d9d9dd9d9dbd9d9d1d9dbbb6b6bc6b6dbb9bb9b9a6bb9b9b9b9b6c8c6a6a6b9b9d9dbd9dddd9d91ddd9ddd9ddd9dd9d9d9dddd9bd9dd9ddd9dd9dd9ddd1d191d19d1ddd9d1d1d1dd1dd19d9191d91dd9dd9dddd9ddd9d9d9ddddd9d
                    a6cb9bccc69a96ff8c8b9b9b9b9bd9bdb9b9b9b99d9d9d9d9ddd9d9d9b9d9d9d9dbd9dddd9dd9b9a9b9d9b9b9b9b9d9b9b9b9bb9bd9d9dd9dd9ddbd9d9d9dd9d9d9dd9d9dbddd9dd9d9d9d9dddbdb9b6bbb6bbbb69bb9bbbb9b9ab9ab6bb6a6b6c686a699b9d9d9d9d9ddd9b9a9b99bd9d9d9dbd9dd9d9dd9dd9dd9ddd9dd9dddd191dd19d1dd191dd9d9d9d9d9dddd1dddddd9ddd91d191ddd9ddd1d919d1d1
                    68b6b8f66c9b9bcc3cc8d9b9b9d9bd9b9b9b9b9bb9bdbdb9d9d91dd9dd9dbd9dbd9d9d99dd9d9dd9d9b9d9d9d9d9d9d9bd9bd9db9b9bd9bd9dd9d9d9dbd9d9ddd9d9dd9dd9d9d9d9dbd9dddd119bb9dc6b9c9b9bbd9bb99b6bb9b9b6d9b6b6b8c6ab66a6a9dbd9ddd9d9b9ab6b6abb9bd9ddbd9dd9d9dbd9ddddd9dd9dd9dddd91d1d91d1dd19ddd1d1dd1dd1dd191dd91d9dddd91dddddd9ddd19dd1ddd19d9
                    c6c6c6cc6cd8cc838c8c6d9b9b9b9d9d9db9bb9b9b9b99ddbd9db9dd9ddd9dd9d9d9dddd9dd9d9dd91dd9d9dd9dd9dbd9b99b9b9d9bd9b9b9db9bbb9b9dd9d9d9ddd9dd9ddd9dd9d9ddd9d9d9bd9bdb9bbbb9bb9b9bd9bb9b9bb6b9b9a9bb6a6bb6bb6a6b999dd9d9dab6a66a6a66a69bd9d9dd9dbdd9ddd9b9d9dd9dd9ddd91d1191d1dd19d1d19d9dd9d1d91dddd9ddddd9d91ddd919ddd919dd19d9d9dddd
                    8cb9b6b6c6bcc6fcf6c6d9a9b9bdb9bd9d9d9b9bb9b9bd9b9b9bd9b91bd919dddd9dd99dd9d9dd9dd9ddddd9dd9dd9d9d9dbd9b9bd9b9b9b9b9d9d9dd9d9ddd9dd9dd9dd9ddd9dddd9d9ddd1d1bdd9db9b9bb9bb9bd9bdb9bb99b9bb9bb6b6b6b6988b66a6a9b9bba698b6b6b66b69a9bdd9dd9d9d9d9d9ddd9ddddd9dd9dd1d19d1d19d1d1dd9ddddd1d19ddd91d1d19d191dddd91ddd9d1ddd19ddd1dd19d1
                    c68b6abc8c6f8cc8ccc8b9b9b9b9b9b9bdb9db9b9b9b9b9b9b9b9d9db9dddd9d9dd9ddd9bd9bd9d9dd9d9d9dd9d9d9dbd9d9b9bb9bb9a9b9b9dbd9d9d9db9b9db9d9dd9dd9d919d9dd9dd9d1d9d9bdb9bdb9bd9bd9db9b9b9bb9bb9bb9b9a9a69aa6b8a66a69ab969a6a698a6a69a86b99dd9dd9dd9dbd9d9ddbd9bdd9ddd191d1dd1dd19d9d1dd19d19dd1d1d1d9d9dd1dddd91d1d9d1d19d19dd1d9d19dd19
                    8c6cc86c8cccc6fc838c6b9b9d9b9b9b99dbd9d9bd9bd9bd9b9b9bb9d9d99dd9d9dd99bd9dbd9b9d9d9dd9dd9ddd9d9d9bd9bd9db9b9b9bb9b99d9dbd9dd9dbd9ddd9dddd19ddd9d9ddd9dd9dddd9b9bb9bd9bb9bd9bd9b9d9b9d9b9b9a6b6bba66b666a6b6a96aa6a66a6a66b6a6bb9bd9dd9dd9dd9dd9dd9d9ddd9dddd91d191d9d91dd1dd9d1dd1dd19d9d9d1d1d19d9d191d9dd1d9dd19dd1d9d1d91d9dd
                    c8c8c8cc3c83c8c3cccc6bb9bb9b9bdb9b99d9bd9d9d9d9bd9b9b9b9b9bd9bd9d9d9dd9d9b9d9db9bd9d9d9dd9d9dbd9dd9d9d9b9d9b9b99d9dbd9d9dd9dd9ddd9dddd919dd9d9dddd91d11d19dbd9db9d9db9db9dbd9bdbdb9bb9b9b9b9b9b96bb6aa66a698b96986b9a66b98b6b69b9dbd91d9dd9d9dd9bd9dd9dddd1d1d1dd1d1d1d1d91d1d9d19d1dd1d1d19d9ddd1d1dddd1d9d1d19dd1d9d1d91dddd19
                    c6c6cfc8f6cf8fcf8c8c8b6b9b9bb9b9bbbb9bd9dbd9bd9b9bb9bb9bd9d9d9bd9dbd9bd9dd9db9d9d9bd9dd9d9d9d9dd9b9db9dd9d9dddddbdd9dd9d9dd9ddd9dd9d9d1dd9dd9dd9d91d1d91dd9b9dbddb9bdb9dd9d9dd9d9bd9bd9b9b9b9b9a9b696b6a6a6a6b9a9b6a6b9a6b99dddd9d9db9bd9bd9b9bd9dbddd9d19d19d19d19d19d91dd19dd1dd9d91d91d1d1d191d9d919d91d19d1d19d1dd9dddd91dd1
                    8c6b9c8fccc8cc3cf83fc6c9b9b9b9bb9b9b9b9b9d9dd9ddb9b9b9b9b9bdb9d9b99bd9db9d9d9dbd9ddddd9d9d9dbd9bd9d9d9bd9dbd9d9d9d9dd9ddd9dd9d91d91d19d9dd9ddddd1dd911dd9dddbd9d9dd9d9d9dbdd9dbd99bd9b9dbd9bd9b9b9bb9a9b9b69a6b69a969a69b9db9d9ddd9d9d9bd9bddb9bd9dd9d1d1d1d1d91dd1d1d1dd19dd1d9d1d1d1d1d9d19d1d1d1d1dd1d19d1d9ddd19d1d19d1d9d9d
                    6c8bb6cc83cc3c8c8ccf6c8b9b9b9b9b9b9bb9b9b9b9bb99d9b9bd9d9d9b9db9bdb9b9d9db9bb9d9dd9d9ddd9bd9d9d9d9bdbd9d9d9d9d9dd9dd9dd9dd9dd9dd91d9ddd19ddd9d9d91d1d9d1dd9d9dd9db9dbd9dd9d9dbd9bd9b9db9b9b9b9b9b99b99b9b9b9999a99b9b9d9dd9dddd9d9dbdbb9bd9b9d9dddd91d19d19d91dd19d9d19ddddd19d1d91d919d11d91d9d9d9dd91d91dd1d1919dd19dd1d91d1d1
                    a6b6cc6fcc9b8cf8fcc8c8b8bbbb9b9bd9a9b9bb9b9b9bbb9bd9b9bb9bd9b9d9d9b9db9b9bd9d9bd9dd919d9dd9d9dd9dd9d9d9dbd9dd9d9dd9dd9d9d9d9ddd91dddd9dddd9d1d1dd19ddd9ddd9dd9dbdd9d9ddbdddbd9d9dbd9bd9d9dbd9bd9b9bd9b9d999b9bd9d9dd1ddd9ddd9d9ddbd9b99db9bd9bd9d9d1d1dd1dd1dd191d1d1dd19d9ddd191d11d1d19d1dd1d1d1d11d1d1d19d9ddd1d191d9d1dd9dd9
                    b9bb6cc6c6bc6c6cc6cfcc6b698ccb9b9c8c9a9b9bb9b9b9b9bb9d9bd9bd9bd9bd9b9b9d9d9dbd9db9ddbd9b9bd9bd9d9dd9dd9d9dd9dddd9dd9dd9ddddd9d9dd9d91d191d19d9d91d9d9ddd9dd9ddd9d9dddd9d9d9dd9dbd99d9bdbb99bd9bd9b9bd9d9bdd9dd9d9d9d99d9dd9dd9d9d9b9b9a9bd9d9ddddd1d9d19d9d91ddd1d9d9d9dd1d191dd1d9d191dd191d9dd9d19d9d19dd1d1d19d19ddd1d9d1d191
                    b6b9d9c9bf6c6db6cc838c6bbc6c8c9db8cc8d9b9b9bb9b9a9b9b9b9b9b9d9bd9dd9dd9bd9bd9db9d9b9d9bd9db9d9dbd9dd9dddd9dd9d9d9d9d9dd9d9d91ddddd1d9dd19dd1d1dd9dddd9d9ddddd9ddddd9d9ddd9d9dbd9d9dbd9b9dbd9bd9bd9d9bdb9d9bd9dbdd9d9dd9d9dd9dd9bd9db9dd9d9dbd9d919d1d1dd1d1d191d9d1dddd19d1d1d191d11ddd19ddd1d91d191d11d1d91d9d1d1ddd19d1d9d9ddd
                    9b9bb9b6c6cdd9bb6cfc8c68c8b8c8bb9c8c6a9db9b9bb9b9b9b9bd9d9dbdd9bd9bd9d9d9dd9d9d9dd9db9b9b9d9bd9d9d9d9d9d9d9dd9d9dd9dd9dd9ddd9d9d9d9dd19d1d9d9d9dd9d9d9ddd9d9ddd9d9dd9dd9ddbdd9d9db9db9d9b9db9d9d9bd9d9d9bd9dbd9d9dbd9ddd9d9d9dbd9b9db9bd9d9ddd1dd1d9d919d19ddd191d9d91dd1d91d91d19d9191d1d19dddd91dd19d9d1d1d1d9d9d19dd19d1d1d19
                    bdb9c6bb6cd9b9b6c8c8fc6cc6cc6c6c8c6c6c9b9db9b9b9b9b9b9bb9bd9b9d9b9b9b9ddbd9dbd9d9bd9dbdd9bdb9db9dbd9d9d9ddd9dd9d9dd9dd9dd9d9ddd91dd191d1d11dddd19dd9ddd91dddd9dd9dd9dbdd9dd9dd9dbd9bd9bdd9bd9d9dbd9bd9bd9b9d99d9bd9dd9d9d9d9d9d9dd9d9d9dd919d9d9d91d1ddd1dd19dddddddd191d1d11d1d1d1dd1d9d9dd91911dd1dd1d19d9d91d1d9dd19dddd9d9d1
                    9b6cbb6b6c6bb6b6c6cc6cc8c6c8c6c8c6c8c6b9b9db9b9b9b9b9bd9db9d9dbd9d9dbdb9d9d9d9ddd9db9d9bd9b9d9d9d9d9dd9dd9dd9dddd9dd9dd9dddd9d1dd91ddd19d9d919d9dd91d9ddd9d9dd9ddd9ddd9dd9dd9dbd99d9bd99bd9d9dbd99d9d9bda9b9bdbd9d9d9dbd9dbdbd9bd9bdd9d9dddddd1d1dd9d19d9d9dd19d19d191d19119d19d91d19d1d1d1d1d1dd19d91d91d1d1dd191d19dd1d91dd1dd
                    a6c6b68bb6b6a6b8cc9bd6c6ccc8c6cc8c6c8b8d9b99d9bdb9bdb9db9db9db9b9bd999d9d9dd9d9bd9dd9d9d9d9b9bd9d9dd9dd9d9d9d9d9dd9dd9dd9d9d19d9dd9191dd1d1ddd9dd9dd91d9ddd19ddd9ddd9dd9dd9dbd9ddbd9d9ddd9ddd9d9dddd9d99b9b9d99d9ddbd9d9dbd9d9dd9dd9ddddd9dd9d9d9d1d9d1d1d1d9d1d91d1d1d1d1d1d1d1d19d1d9d919191d91d11d191dd91d91ddd9dd19d1dd9dd91
                    9bd9b9b868c6c6c8c8b9b6c6c66b6c8c6c8cb6b9b9bdbd99d9d9d9b9d9db9d9bd9bbdbd9db9dbd9d9d9d9dbd9bdd9d9bdd9dd9dddd9ddd9d9dd9dd9dd1d9ddd191dd1d919d9d9ddd91ddddddd9d91d9ddd9dd9dd9dbd9dd9dd91ddd9ddd9dd9dd9d9ddbd9b9bbdd9dd9d9dbd9d9ddd9dd9dd9d9d9dd91dd1d9d1dd9d9d91dd91dd191d919d9d9d91d91d91d1d1ddd1d1d9d19d1d91dd1d9d191d1dd9d91d19dd
                    d9db9a6cbb8c8fc8c6c6c6c66bb9c6c8c8c6b9b9b9d9d9dbd9bd9d9db9d9b9b9b9b99db9d9db9dbd9bdbd9d9dd9bdbd9d9d9dd9d9dd9d91dd9dd9dd9d9dd19ddd1d9d1ddddddd9ddd9d9d9d9dddd9ddd9dd9dd9dd9dddddd9ddd9ddd9dd9d9d9dd9dbd9db9b99b9dbd9dd9d9ddd9d9d9dd9dd9ddd9dd9d9d91d9d1d1d1dd1ddd11d1d11d11d1d1dd1dd1d1191d91d9191d1d1d91dd19d1d9ddd9d9d1ddd9ddd9
                    db9bb6bb6b6b8c8c6c6c8c6cc69c6c6c6c6c6cba9c9b9d9d9dd9dbd9ddbd9dbd9dbdb9dbdb9d9b9dbd9d9bd9b9b99d9bd9bd9bd9bd9ddd9d9dddd9dd19d9dd19191d19d1919d1d9ddddddddd9d9ddd9dd9ddd9dd91d9d9ddd9d9d9d9d9dd9ddd9db9d9d9d9dbd9d99d9b9d9d99d9dd9d9dd9dd9d9d9dd9dddddd9d9dd9d9d9119d191d9d19d19d19d19119dd1d1d11dd19d9d1dd9dd19dd1d1dd1dd9d191dd1d
                    9b9b9b9c69b9ccc8c6cc6c6c9ab6c8cb9b8c8c66abba9dbdd9dbd9dd9d9dd9d9bd9d9d9d9d9dd9d99d9bd9dbd9dbdbd9d9dbd9bd9d9d9d9dd9d9dd9d9d1d19d1dd19dd19ddd9dd19dd9dd9ddd1dd9ddd91d9ddddddddd19d91dddd9ddd9d9d9b9d9d9b9b9b9d9b9db9d9db9bd9d9d9dd9d9d9d9dd9d9ddd9d9d1dd1d1d1d11d111d19d1d91ddd1d1191dd1d19d19d919dd1d9d91d19dd19d9d9d9d1d9ddd9d9d
                    b9bb6a6bc9bb66c83c6c8cc8c66bb6b9b6ccc8c66b6b9b19d9d9dd9d9d9d9dbdd9d9bdb9dbd9bdbd9bd9d9d9dbd9d9d9bd9d9d9d9dbd9dd9ddd9d91d19d91d19d1dd19dd191d19dd91dd91d9d9d9dd91ddddd19ddd9d9dddd9d99dd9d9db9bd9b9bb9b9bdb9b9bd9bdb9b9b9b9b9bd9bd9d9dbd9dddd9d9dd19d9d9d9d191d19d9ddd19ddd9d19191d1919d1d191dddd19d1dddd9dd19dddd1dd19dddd91dddd
                    9db6b6b9a9b9b6c6c8c8c8cc6c89b9b6bdd96ccc6b6a69d9dd9d9d9dd9dbd9d9d9ddd9dd9d9dd9d9dd9dd9db9d9d9d9d9db9bdb9d9d9d9dd9d9ddd9dd1d1d91d19d9d1d9ddd9dddddd9dd9dddd91d1dd9d191dd19ddddd9d9dddd9dd9db9db9bdb99bdb9b9b9b9b9b9b9b9b9b9bd9b9d9bdb9d9d9d9dd91d9ddd1d1d1d1d191d1d919dd191d11d1dd1d1d1d91ddd9191ddd9d91d1d9ddd919d9ddd9d91dd9d9d
                    d9b9bb6b6db9db9bb6b6c838c6cb9b6a9b9b6c86b68b6bd9d9dd9dd9dbd9dd9ddd9d9d9d9dd9dd9d9dd9dd9dd9dd9dbd9d9d9d9ddd91dd9dddd191d191d91dd9d1d1d9dd19ddd9d9d91ddd9d9ddd9d191d1dd9dddd9d9dddd9d9ddbdb9db9bd9b9bd9b9b9d9dbd9b9b9bdb9b9b9b9db9bd9d9dd9d9d9dd9ddd9d9d91d9191dd9d1ddd19dd1191d9119d19d1d9d91dddd9d1d1d9d9dd19dddddd9ddd1dd9dddd1
                    9d9b9a9b9b9d99b9b9bb6cb6cb6b6a6bb6db9b6c6cc6cb9ddd9dd9dd9ddd9dd9d9d9ddd91bdd9dddd9dd9dd9dd9d9dd9dd9dd919ddd9dddd9d9d1d1d1d1dd91d19d9dd9ddd9d1d91dd9d9ddd1d11d1d1d9d91dd9d9ddd9d9ddddbd9d9b9db9b9db9b9b9b9bb99b9db9d9b9db9d9bd99d9d9bd9dbdddd9ddd9ddd1d1d1d1dd91dd9d9ddd11d1d11d1d19dd19d1d1d919d19d9dd1dd19dd19d19d19d9d9dddd9dd
                    ddd9d9b9d9b9dd9d9d99d9bb69b9b6b6b6b9b9bb6c8c69b9d9dd9d9dd9d9d9d9dd9dd9dd9d9dd9d9dd9dd9dd9dddd9dd9ddddddd9d919d91d11d19d9d9d91dd9ddd19dd9d1d9ddd9ddddd19d919d919d1dddd9dddd9d9ddd9d9d9d9dd9b9d9db99b9b9bdb99bb9b9b9b9b9b9b9b99bdd9dd9dd9d9d9dd9d9dd9191d919d91dd9d1d19119191d9d9d9d1d9dd19d9dddd1dddd9d9d9ddd9ddd9ddddddddd9d1d9d
                    9bdd9ddd9dd9bd9db9bd9b99b9b9b9bb6b9bb99bb6c6ab9b9d9dddd9d9dd9ddd9dd9d9d9ddd9d9dd9dd9dd9ddd9ddddddd9d9d9ddddddd1d19d9d1d1d1dd9ddd9d9dd91d9ddd9d91d9d91d1d1dd1dd1d9d9ddd9d9dd9dd9dd9dbd9db9dbdb9bdbd9bdb99b9b9b9b9bdb9db9db9dbd9b9dbd9d9d9d9d9d9dd9d1dd191dd1dd9dd19dd1d1d1dd1d1d1d191d19dddd19d9d9d91dd1ddd91dd9ddd9d9d9d91dd9ddd
                    9b9bb19dd9dd9d9ddd9bdddd9dbd9d9d9bb9bb9b9db9d6dbbbd99d9ddd9dd9d9dd9ddd9dd9dd9dd9d9dd9ddd9d19d919d1dd1dd191d91d9dd1d1d9d9d9d9dd9dddd91dddd9d91dddd1d19dd91d9d19ddddd9d9dd9d9dd9d9dbd9dbd9bd9d9d99d9d9d9bd9bdb9bdb99b9b9d9bd99bd9d9d9bdb9bdbd9dbdd1d19dddd9d9d1d19dd19d19d919d919d9ddd9ddd9d9dddddd1dd9d9d91dd9ddd9ddddd1ddd9ddd9d
                    ba6b6bd9ddd9ddbd9dd99d9dd9d9db9dd9b99b9b9b9b9ba69b9bd9d9d9d9dddd9dd9d9dd9d9dd9dddd9dd19d1d1d1d1d9d19d191d1d191d919d9ddddd9dd9dd9d9ddd9d9dd1dd919d91dd191dd1d91d9d9dddd9dddd9dddbdd9d9dbd9bdb9dbd9bd9dd9bd99db99b9bd9db9b9b9d9bdb9bd99d9d9d9d9d19d9d19d9dd1d9d9dd19d1d91ddd1d1dd1d191dd91ddd19d919d9ddddddd9ddd9dd19d9d9d9ddd91dd
                    9b9b6a9dd9dd9d9d9d9dd9b9bdddddd9d9dd9b9d9bd9d9bb69a9bddd9ddd9d9dd9dddd9dddd9dd9d9d1d9dd19d9d9191d191d9dd9d9ddd9dd9dd9d9d9dd9dd9dddd9dddd919d1dd1ddd9dddd9d91dd9ddd9d9dd9d9dbd9dd9dbdb9d9d9d9dd9dd9dd9bd9ddd9dd9dd9b9b9d9bdb9bd99d9ddd9ddd9bdd9dd9d9ddd19d9ddd19dd1d91dd19d9d9d9d9ddd91dd9d9ddddddddd9d9d9ddd9dd19ddddddddd9ddd9d
                    a6d9b6b9dd19dd9dd9d9dddb9b99d9ddddd9dbd9b9d9b999bb9b9d9ddd9dddd9ddd9d919d9dd91d1d9d1d19d1d1d1ddd9dd9dd9d19dd9dd9dd9dd9ddd9ddd91d9ddd9d91ddd191d9d91d9d91dddd9ddd9dd9d9dbdd9ddd9bd9d9db9bdbddbdd9bd9dbd9d9b9d9dd9ddddd9bd99bd9d9ddd9ddd9b9bd9b99d9d9d99dddd919dd19d1dd9dd1d1d1dd1dd9ddd9dddd9d9d9d9ddd1ddd19ddd9ddd9d9d9d9dd19dd9
                    c6ab9bb9b9dd9dd9d9dbd99d9dbd9d9d9d9dd9dbd9dd9ddb9b9d9dd9d9dd9d91d9d191dddd1d1d9d119d1d1d9d9d9d9dd9dd9dd9dd9d9d9d9dd9dd9ddd9ddd9ddd91d1dd919ddd9ddddd1ddd9d9dd9d9dd9dddd9d9dd9bdd9bdb9dd9d9d9d9bdd9b9d9ab9bb9b9b9b999bdd9dbd9d9db9db9db9bd99d9db9bd9ddd9d91dd1d9d19d91d19d9d9d9d9dd19ddd9d9dddd1ddd9d9d9d9ddd9ddd9dddd1ddd19dddd1
                    8c8c6b6b9b9dd9d9dbd9ddbd9d9b9db9bd9bddd9ddbdb9bd9bd9d9b9b9ddd1dd1d9dddd919d9d1d19d1d9d9dddddddd9dd9d9d9d9d9dd9ddd9dd9dd9ddd9dddd9d1d9d91ddd19ddd919d9d9dddd9dddd9ddbd9dbddbddd9bd9bd9bdbddbd9dd9bb9bbb9bb9db9bb9dbdb9b9bd9d9db9db9d9d9bd9dbbb9dbd9d9ddd1d191d1d1dd1dd9dddddddddd9d9dd9dddd19d9d9dddddddddd9dd19ddd9d9d9d9ddd9d9d
                    c8c6c9a6b9b99dbd9d9d9d9db9d9b9d9b9d9d9dd9d9ddd19d9b9bddddb9d9d19d1d1191dd11d19dddd9d9dd9d919d9dd9d9dd9dd9dd9dd9d9d9dd191d9dd9d9dd19d1d1d91d9dd91dddddddd9ddd9d9dbd9dd9d9d9d9bd9dbd9dbd9d9d9dbd9d9bb9b9b9b9b9bdb9b9b9bb9d9bdb9bd9db9bdb9b9b9b9dbd9ddd9d9d1ddd9d9d9d9d91d9d9d9d9191ddd9dd9d9dddddd9d9d9d9d9dd19ddd9dddddddd9ddddd9
                    c6c8c6b9a9bbb9d9dd9dbd9d9dbddbd9dbddb9d9ddd9d9ddd9bb9b9d91dd19d1d9d9dd9b9b9d91d919ddd91ddd9ddd9dd9d9dd9dd9d9d9ddddd9d9dd91dd1dd19ddd9d9ddd91dddd9d9d9d9dd9d9ddbdd9d9dbddbd9d9dbd9dbd9d9dbd9d9dbbd9b9b9b9d9dbd9bd9bd9d9b9b9d9bd9b9d9d9bd9bd9bd9d9dd9ddd1d9d91d1dd1dddd9ddddd1dddd9d9ddd9ddd9d9d9dddd1ddd1d9ddd9ddd9d9d9d9dd9d9dd1
                    b6b6c8b9bb99db9d9bd9d9d9db99d9ddd9d9dddd9d9d9d9b9d9bb9a9dd9dd1d911dd9b9db6a9d9dd91d91dd9d91d9dd9dddd9d9d9dd9dd9d9dddddddd9d9d9ddd191d1d19ddd9d9dddddddd9dddd9dd9dddd9d9d9ddbd9d9d9d9dbd9d9dbdbd9b9bd9d9db9d9b9d9bd9dbd9db9bd9bd9bdb9d9bd9dbd9dddd91dd9d1d1dd9d9d9d9ddd9d9d9d9d9ddddd9ddd9dddddd9d9d9d9d9ddd9dd9dddddd9dd1dddd9d9
                    b9bb6b6c9b9b9d9bdd9dd9dbd9db9db9dd9ddd9ddddddbddd9d9b9bb9dd191ddd9d9b9b9bb6b91ddd9ddd9dd1d9dd9dd9d9d9dd9d9dd9dddd9d9d9d9ddddd19d9ddd9d9ddd91dddd9d9d9d9dd9d9d9dd9d9bddbdd9d9dbddbdbd9dddbdd9d9d9dbd9dbd9db9d9dbd9db9d9b9bd9bd9d9d9dbd9d9d9d9dd9dddd9d1d9d9d1ddddddd9ddddddd9ddd9d9ddd9dddd9d9d91dddddddd9ddd9dd9d9d9ddd9d9d91dd1
                    9b99b9a9b9b9bdd9d9d9dbd9dddd9d9d9dd9d9d99d9d9d9d9dddd9d9bd9dd9d9dbd9db9b9a9bb9d9ddd9dd9d9dd9dd9dd9ddd9dddd9ddd9d91dd1ddd9d9d9dd1d9d1dddd91dd9d9dddddddd9dd9ddd9ddbdd9d9d9dbdd9d9d9d9db9d9d9dbd9dddddd9dd9dbdbd9db9db9bdb9bd99bdb9d9d9ddd91ddd9dd9dddd9dddd9d9d9d9d9dd9d9d9ddd9dddd9ddd9d9dddddd9d9d9d9d9dd9ddddddddd9d1dddddd9dd
                    9b9b9b9b9b9d9d9d9ddbdd9d9d9bd9dbd9dbd9ddd9bd9dddd9b9b9bd9dd9d9dd99dbd9dd9bb69ddd9d1d91ddd9ddddd9dd9dddd9dddd9dddd9d9d9d1d1d1d9d9d1d9d91ddd9ddddd9d9d9d9dd9dd9dbd9d9dddd9dd9d9dbd9dddddd9ddd9dddd9d9b9db9b9d99b9b9b9d9d9d9d9bd9d9dbdddd9dd9d9ddd9d9d9dd9d9dddd9dddddd91dddd9ddd9d9dd9d9ddd9d9d9ddddddddddd91d9d9d9d9dd9d9d9d9dd9d
                    ddd9d9d9d9dbd9bddbd9d9ddd9dd9dbd9db9db9bbd9bb9b9b9dd9bd9d9d9dd9bdb9d9bd9d9bbd9dd9d9bb9b9dd19d91d1dd9d9dd9d9ddd9dddddd19d9d9dd1ddd9dddd9d9ddd9d9dddddd9dd91bddd9dddd9d9ddbdd9ddd9dd9d9d9dd9ddd9dd9d9b9bd9db9bd9dd9dbdb9bdb9d9dbd9d9b99db9dddd9d9ddd91d91dd9d9ddd9d9d9dd9d9dd9ddddd9ddddd9dddd9dd9d9d9d9d9ddd9ddddddd91ddddddddddd
                    99ddbd9dbd9d9dd9d9dddd9d9dbdb9d9bd9d9db9b9b9bb9a9b9bd9dbdd9db9db9bb9bd9dd99b9b9bd9d9b9b9b1d1d1d9d91d1d1dd1dd9dd9d9d9d9ddd1d9d9d91dd9d1dddd9dddd9d9d9ddd9ddd9d9dd9d9dd9d9d9ddbd9dd9ddddddddd9dd9dbd9dd9db9dbd9bd9bd9d9d9d9bdb9d9ddd9dd9dd9b9d9dd9d9d9dd9ddd9dd9ddddddddd9dddd9d9d91d9d9dd9d9ddd9ddddddddd9dddd9d9d9ddd9d9d9d9d9d9
                    bd9b9db9d9dbd9dbd9d9d9dddd9d9dbb9bbbd9d9bb9b9b9bb9b9bd9d9bdb9ab9b9bb9bb9bdd9bd9d9dd91dd9d9b9191d1d19d9d919d91d1d1d1d91d9d9dd1dddd9dd9d9d9ddd9ddddd9dd9ddd9dddd9dd9dd9ddd9d9dd9dd91bd9d9d9d9b9d9d9db9d9d9bd9bd9dd9d9d9dbdd9d9ddd9d9dddd9ddd9dd9d9dd9dd9d9d9dd9dd9d9d9d9ddd9d9dddddbdddd9dddd9dddd9d9d9d9ddd9d9ddddd9ddddddddddddd
                    9b9d9d9dbd9d9bd9d9d9dd9d9d9db99b9b9abb9d9db9b9b9db9b9bd9bd99d9bbbb9bb9bb9d9bd9ddd9ddd9dd9bbb91dd9dd1d1ddddddd9d9d99ddd91dd9d9d9d91ddddddd9d9dd9d9dd9ddd9dd9d9dd9ddbddbd9ddd9dd9dddddd9ddddbdd9dd9dd9db9bd9d9dd9d9dddd9d9dd91d9d9db9d9db99dd9d9d9d9bd9bdd9dd9dddd9ddddd9ddd9dd9d9d9d9d9dd9d9dd9ddddddddd9dddddd9d9dd9d9d9d9d9d9dd
                    9bb9b9bd9b9dbd9d9dbd9dbddbdd9dbdb9b9b6bbb9dbddd9d9ddd9dd9dddbd999b9b9b9b9bdd9d9d9bd9bd9b9d9bb9d1d919d99d9d9d9dd9dddd9dd9ddddddddd9d9d9d9ddddd9ddd9ddd9dd9dddd9ddbd9d9dddbd9ddddd9d9bddd9b999dbd9bd9bd9b9b9dbd9dbd9d9dddd9dd9b9bd9db9d9ddb9d9dbd9bd9d9d9dbddd9d9ddd9d9dd9d9dddd9dddd9ddd9dddd9dd9d9d9d9dd9d9d9dddd91ddddddd9ddd9d
                    b9dbdbd9d9d9d9dbd9d9bdd9d9d9d9d9b9bb9b9a9a9b9b9b9bd9dd9dd9d9dddd9db9bd9d9d9dd9dbd9bb9bb9ba99b9d9d9dd91dd9dd9dd9dd9d9dddd9d9d9d9d9ddd9ddd9d9d91d9ddd9dd19dd9d9dbd9dddd9d9d9dd9d9dd9d9d9bd9dbb9dbb9bb9bbdbd9d9bd9bdbdd9d9bd9bbdd9db9dd9db9dd9bd9bd9bd9dbdd9d9dddd9d9ddd9dddd9d9dd9d9dd9dbdd9ddd9dddd9ddd9dddddd9d9ddd9d9d9d9dd9ddd
                    9b99b9db9bdb9d99db9dd9d9dd9dbd9d9d9b9bb9bb9bb9b9bd9bd9b9db9d9d9dd9dd9bdbdb9b9bb9bb9bba6bb6ab9d9b9d9d9b9bd9dd9dd9dd91d9d9dddd9dddd9d9dd9ddddddd9dd91d19d9d9d9dd9dd9d9d9ddddd9dd9dbddd9db9db9bd9b9ab9b9b9b9bb9b9d9d9dbda6bbb99d9a9bd9bd9dd9bd9b9b9d9bd9d9dd9dd9d9dddd9ddd9d9ddbddd9ddbddd9dd9dddd9d9dd9ddd9d9dddddd9dd9ddd9ddddd9d
                    9bdbd9b9d9d9dbdb9d9bd9dbd9dd9dbd9bd9b9b9b9b9b9bb9bbb9bdb9dbb9b9bbd9dd9b99db9bb9a9a9a6b6a9b6cb9d9bbd9dd9d9d9d9d9d9dd9dddd9d9dd9d9dddd9dd9d9d9dddddd9d9bd9dbdbd9d9dd9dbd9d9d9dbdd9d9dbb9dbdb9bb9bad9bbb9bb9b9dbdbbdb9d9cb9b9bda9bd9bd9bd9db9bb9dbd9d9bd9dbdd9dbdd9d9dd9d9ddbd9d9d9dbdd9d9dddd9d9ddddd9dd9dddd9d9d9ddddd9dddd9d9ddd
                    9d99bd9dbd9bd99d9bd9db9d9dbdd9d9d9bd9b9b9bb9bb9bb9bba9a9b9bd9bd99bd9bd9bb9bd9b9b9bb9b9b6b6b6a69bd9bbd9dd9dd9ddddd9dd9d9dd9dd9ddd9d9dd9dddddd9d9d9d9dd9dbd9dd9dbd9dbdd9dbddbd9d9dbd9b9b9d9ab9bb9b6bb9bdb9bdb9b9d9bd9bb9a9b9b9bb9b9dbb9bb9db9b9bd9bdd9dbd9d9ddd9dddbd9dddbd9dddd9ddd9ddddd9dddddd9d9ddd9dd9d9dddddd9d9ddd9dddddd9b
                    9bbd9bd99bd9bdbd9d9dbd9bd9d9dddddd9d9dd9d9b9d9b9b9b9b6bbb9d9bd9db9bb9bd9db9b9b9bb9b9bb9bb6b9bba9b99d9bddd9ddd9d9dd9dd9d9dd9ddd9dd9dd91dd9d9ddd9d9db9bd9d9d9dbdd9d9d9ddd9d9d9dbdbd9bddbdbb9bb9bb9b9db9b9bd9bddb9d9bd9ab9bb9bb6cb9ab9bb9bb9ab9d9b9d9bd9dd9ddbd9dd9d9ddbd9ddd9d9ddbd9dd9d9dd9d9d9dddd9ddd9ddddd9d9ddddd9ddd9d9d9bdd
                    bd9bd9bdb9d9d99dbdb99d9db9bd9b9d9dd9db9db9d9b9d9db9b9d9b9abb9bbddd9d9d9bd9bdbd9d9b9b9b9b9b9a966a9db9b99d91d91dd9d9d9ddd9ddd9d9dd91dddd9d9dd9d9dbd9dd9bd9dbd9d9ddbdd9d9bd9dbd9d9d9bd9b9d9ab9bbb9adb9b9bd9bd9bd9bdd9bb9b6d9bb6b9bb9b9b9bd9b9bdb9db9bd9bd9dbd9dd9dd9dd9d9d9d9ddd9dd9dd9ddd9dddddd9d9dd9ddd9d9ddddd9d9d9d9d9dbd9dd9d
                    9bd9b9d9d9bdb9db99dbdb9b9d9bd9d9d9dd9dd9d9dbd9db9d9db9b9b9d9b9a9b9b9bb9b9d9b9b9bd9b9b9b9d9b9bbb6a9ddddddd9bd9d9ddddd9d91bd9dddd9dd999d9db9d9dbd9db9dbd9dbd9dd9d9d9dbdd9dbd9dbdb9db9b9bb9b9b9b9b9b9bdb9bb9bd9bb9bb9bb9bd9cb6bbb9bb9bdb9dbdb9b9bbdd9bdd9dd9dd9dd9bdd9ddddddd9dbd9dd9ddd9ddd9d9ddddd9dd9ddddd9d9ddddddddddbd9dbd9dd
                    """))
forever(on_forever5)

def on_forever6():
    if world_gen_done == 1:
        if controller.A.is_pressed():
            if inmenu == 0 and inbuild == 0:
                if tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile9
                        """)):
                    
                    def on_throttle3():
                        global inmenu, myMenu
                        inmenu = 1
                        myMenu = miniMenu.create_menu(miniMenu.create_menu_item("stone wall", assets.tile("""
                                myTile8
                                """)),
                            miniMenu.create_menu_item("blk stone wall", assets.tile("""
                                myTile7
                                """)),
                            miniMenu.create_menu_item("wooden backing", assets.tile("""
                                myTile17
                                """)),
                            miniMenu.create_menu_item("wooden floor", assets.tile("""
                                myTile18
                                """)),
                            miniMenu.create_menu_item("wooden ceiling", assets.tile("""
                                myTile23
                                """)),
                            miniMenu.create_menu_item("wooden roof", assets.tile("""
                                myTile21
                                """)))
                        myMenu.set_title("crafting")
                        myMenu.y = 80
                        myMenu.x = 55
                        myMenu.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
                        
                        def on_button_pressed8(selection52, selectedIndex52):
                            global stone_wall, stone, blk_stone_wall, blk_stone, wdBacking, wood, wdfloor, wdciling, wood_roof, inmenu
                            if selectedIndex52 == 0:
                                if stone >= 15:
                                    stone_wall += 3
                                    stone += -15
                                    player1.say_text("Crafted 3 stone walls")
                                else:
                                    game.show_long_text("you do not have stone (15) ", DialogLayout.BOTTOM)
                            elif selectedIndex52 == 1:
                                if blk_stone >= 15:
                                    blk_stone_wall += 3
                                    blk_stone += -15
                                    player1.say_text("crafted 3 black stone walls")
                                else:
                                    game.show_long_text("you do not have black stone (15)", DialogLayout.BOTTOM)
                            elif selectedIndex52 == 2:
                                if wood >= 15:
                                    wdBacking += 3
                                    wood += -15
                                    player1.say_text("crafted 3 wood backing")
                                else:
                                    game.show_long_text("you do not have wood (15)", DialogLayout.BOTTOM)
                            elif selectedIndex52 == 3:
                                if wood >= 15:
                                    wdfloor += 3
                                    wood += -15
                                    player1.say_text("crafted 3 wood floors")
                                else:
                                    game.show_long_text("you do not have wood (15)", DialogLayout.BOTTOM)
                            elif selectedIndex52 == 4:
                                if wood >= 15:
                                    wdciling += 3
                                    wood += -15
                                    player1.say_text("crafted 3 wood ceiling")
                                else:
                                    game.show_long_text("you do not have wood (15)", DialogLayout.BOTTOM)
                            elif selectedIndex52 == 5:
                                if wood >= 15:
                                    wood_roof += 3
                                    wood += -15
                                    player1.say_text("crafted 3 wood roofs")
                                else:
                                    game.show_long_text("you do not have wood (15)", DialogLayout.BOTTOM)
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            inmenu = 0
                        myMenu.on_button_pressed(controller.A, on_button_pressed8)
                        
                    timer.throttle("action", 500, on_throttle3)
                    
            if inmenu == 0 and inbuild == 1:
                if dirt >= 1:
                    if buildM == 1:
                        
                        def on_throttle4():
                            global dirt
                            tiles.set_wall_at(select.tilemap_location(), True)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile1
                                    """))
                            dirt += -1
                        timer.throttle("action", 500, on_throttle4)
                        
                if wood >= 1:
                    if buildM == 2:
                        
                        def on_throttle5():
                            global wood
                            tiles.set_wall_at(select.tilemap_location(), True)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile9
                                    """))
                            wood += -1
                        timer.throttle("action", 500, on_throttle5)
                        
                if stone_wall >= 1:
                    if buildM == 3:
                        
                        def on_throttle6():
                            global stone_wall
                            tiles.set_wall_at(select.tilemap_location(), True)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile8
                                    """))
                            stone_wall += -1
                        timer.throttle("action", 500, on_throttle6)
                        
                if blk_stone_wall >= 1:
                    if buildM == 4:
                        
                        def on_throttle7():
                            global blk_stone_wall
                            tiles.set_wall_at(select.tilemap_location(), True)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile7
                                    """))
                            blk_stone_wall += -1
                        timer.throttle("action", 500, on_throttle7)
                        
                if wdBacking >= 1:
                    if buildM == 5:
                        
                        def on_throttle8():
                            global wdBacking
                            tiles.set_wall_at(select.tilemap_location(), False)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile17
                                    """))
                            wdBacking += -1
                        timer.throttle("action", 500, on_throttle8)
                        
                if wdfloor >= 1:
                    if buildM == 6:
                        
                        def on_throttle9():
                            global wdfloor
                            tiles.set_wall_at(select.tilemap_location(), True)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile18
                                    """))
                            wdfloor += -1
                        timer.throttle("action", 500, on_throttle9)
                        
                if wdciling >= 1:
                    if buildM == 7:
                        
                        def on_throttle10():
                            global wdciling
                            tiles.set_wall_at(select.tilemap_location(), True)
                            select.start_effect(effects.ashes, 200)
                            tiles.set_tile_at(select.tilemap_location(),
                                assets.tile("""
                                    myTile23
                                    """))
                            wdciling += -1
                        timer.throttle("action", 500, on_throttle10)
                        
forever(on_forever6)

def on_forever7():
    music.set_volume(25)
    music.play(music.create_song(hex("""
            00280004080c0300001c00010a006400f401640000040000000000000000000000000005000004200104000800010a0c001000010a14001800010a1c002000010a24002800010a2c003000010a34003800010a3c004000010a44004800010a4c005000010a54005800010a5c006000010a64006800010a6c007000010a74007800010a7c008000010a84008800010a8c009000010a94009800010a9c00a000010aa400a800010aac00b000010ab400b800010abc00c000010ac400c800010acc00d000010ad400d800010adc00e000010ae400e800010cec00f000010cf400f800010cfc000001010c04010801010c0c011001010c14011801010c1c012001010c24012801010a2c013001010a34013801010a3c014001010a44014801010a4c015001010a54015801010a5c016001010a64016801010a6c017001010a74017801010a7c018001010a07001c00020a006400f401640000040000000000000000000000000000000003510200000400021e2a04000800030a20250c001000030a202514001800030a222718001c0001201c002000020a2720002400012924002800020a2528002c0002272a2c003000030a202730003400012534003800010a38003c0001253c004000020a2c40004400012244004800010a48004c000225294c005000030a1b1e54005800010a58005c0001275c006000030a1d2764006800020a2268006c00021d296c007000020a2270007400012574007800010a78007c000220247c008000020a2284008800020a2988008c0001278c009000020a249000940002222794009800010a9c00a000040a1b2529a000a400031d2025a400a800010aa800ac000120ac00b000020a29b000b400011db400b800020a24bc00c000020a20c000c4000124c400c800020a29c800cc00021e24cc00d000010ad000d4000124d400d800020a25dc00e000030a2024e000e4000122e400e800020c24e800ec000122ec00f000020c20f000f4000122f400f800020c25f800fc00022427fc000001030c22270001040102202904010801030c1e2a08010c01021e2a0c011001020c271001140102222514011801010c18011c010220251c012001030c222420012401012024012801020a2228012c01011e2c013001020a2530013201012034013801020a2238013c01021e273c014001010a40014401021e2444014801010a48014c0101224c015001010a50015401012554015801030a202258015c0101275c016001020a2260016401012764016801020a2268016c01021e276c017001010a70017401012274017801010a78017c010220257c018001010a08001c000e050046006603320000040a002d000000640014000132000201000230000000280001192800500001195000800001198000b0000119b000e0000119e00010010119100140010119400170010119
            """)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.create_song(hex("""
            00780004080200
            """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever7)

def on_forever8():
    if world_gen_done == 1:
        if tiles.tile_at_location_equals(player1.tilemap_location(),
            assets.tile("""
                myTile50
                """)) or tiles.tile_at_location_equals(player1.tilemap_location(),
            assets.tile("""
                myTile44
                """)):
            
            def on_throttle11():
                scene.camera_shake(2, 100)
                player1.ay = 200
                player1.start_effect(effects.fire, 100)
                player_health.value += -5
                controller.move_sprite(player1, 20, 20)
            timer.throttle("action", 500, on_throttle11)
            
        else:
            player1.ay = 500
            if inmenu == 0:
                controller.move_sprite(player1, 70, 0)
            else:
                controller.move_sprite(player1, 0, 0)
forever(on_forever8)

def on_forever9():
    global stone, blk_stone, sticks, dirt
    if world_gen_done == 1:
        if controller.A.is_pressed():
            if inbuild == 0:
                if tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile13
                        """)):
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    stone += 1
                    
                    def on_throttle12():
                        pass
                    timer.throttle("action", 500, on_throttle12)
                    
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile14
                        """)):
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    blk_stone += 1
                    
                    def on_throttle13():
                        pass
                    timer.throttle("action", 500, on_throttle13)
                    
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile10
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile91
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile11
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile70
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile74
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile77
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile78
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile79
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile80
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile81
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile82
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile83
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile86
                        """)) or tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile87
                        """)))))))))))))):
                    location6 = 0
                    
                    def on_throttle14():
                        global wood, treeseed
                        tiles.set_wall_at(select.tilemap_location(), False)
                        select.start_effect(effects.ashes, 200)
                        tiles.set_tile_at(select.tilemap_location(),
                            assets.tile("""
                                transparency16
                                """))
                        wood += randint(3, 5)
                        if Math.percent_chance(35):
                            treeseed += randint(1, 3)
                    timer.throttle("action", location6, on_throttle14)
                    
                elif False:
                    pass
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile19
                        """)):
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    sticks += 3
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile16
                        """)):
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    stone += 1
                    
                    def on_throttle15():
                        pass
                    timer.throttle("action", 500, on_throttle15)
                    
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile3
                        """)):
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    stone += 1
                    
                    def on_throttle16():
                        pass
                    timer.throttle("action", 500, on_throttle16)
                    
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile6
                        """)):
                    if tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile33
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile42
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile39
                            """)) or tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile52
                            """)))):
                        tiles.set_tile_at(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                transparency16
                                """))
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    stone += 1
                    
                    def on_throttle17():
                        pass
                    timer.throttle("action", 500, on_throttle17)
                    
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile57
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile56
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile55
                        """)) or tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile53
                        """)))):
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    stone += 1
                    
                    def on_throttle18():
                        pass
                    timer.throttle("action", 500, on_throttle18)
                    
                elif tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile65
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile64
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile61
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile60
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile15
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile1
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile24
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile25
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile62
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile63
                        """)) or (tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile75
                        """)) or tiles.tile_at_location_equals(select.tilemap_location(),
                    assets.tile("""
                        myTile76
                        """)))))))))))):
                    if tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile26
                            """)) or tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile28
                            """)) or tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile46
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile66
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile71
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile2
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile84
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                        assets.tile("""
                            myTile84
                            """)) or False))))):
                        tiles.set_tile_at(select.tilemap_location().get_neighboring_location(CollisionDirection.TOP),
                            assets.tile("""
                                transparency16
                                """))
                    if tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile31
                            """)) or (tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile29
                            """)) or tiles.tile_at_location_equals(select.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM),
                        assets.tile("""
                            myTile4
                            """))):
                        tiles.set_tile_at(select.tilemap_location().get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                transparency16
                                """))
                    else:
                        pass
                    tiles.set_wall_at(select.tilemap_location(), False)
                    select.start_effect(effects.ashes, 200)
                    tiles.set_tile_at(select.tilemap_location(),
                        assets.tile("""
                            transparency16
                            """))
                    dirt += randint(1, 3)
                    
                    def on_throttle19():
                        pass
                    timer.throttle("action", 500, on_throttle19)
                    
                else:
                    pass
forever(on_forever9)

def on_forever10():
    info.set_score(inbuild)
forever(on_forever10)

def on_update_interval2():
    if world_gen_done == 1:
        if player1.y <= 2000:
            for value142 in tiles.get_tiles_by_type(assets.tile("""
                myTile1
                """)):
                if tiles.tile_at_location_equals(value142.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(25):
                        tiles.set_tile_at(value142.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile4
                                """))
            for value143 in tiles.get_tiles_by_type(assets.tile("""
                myTile64
                """)):
                if tiles.tile_at_location_equals(value143.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(50):
                        tiles.set_tile_at(value143.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile4
                                """))
            if Math.percent_chance(25):
                tileUtil.replace_all_tiles(assets.tile("""
                        myTile4
                        """),
                    assets.tile("""
                        myTile29
                        """))
                tileUtil.replace_all_tiles(assets.tile("""
                        myTile29
                        """),
                    assets.tile("""
                        myTile31
                        """))
            for value15 in tiles.get_tiles_by_type(assets.tile("""
                myTile31
                """)):
                if tiles.tile_at_location_equals(value15.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(25):
                        tiles.set_tile_at(value15.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile32
                                """))
        if player1.y >= 3000:
            for value144 in tiles.get_tiles_by_type(assets.tile("""
                myTile55
                """)):
                if tiles.tile_at_location_equals(value144.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile54
                        """)) or tiles.tile_at_location_equals(value144.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        transparency16
                        """)):
                    if Math.percent_chance(25):
                        tileUtil.cover_tile(value144.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile48
                                """))
            if Math.percent_chance(25):
                tileUtil.replace_all_tiles(assets.tile("""
                        myTile48
                        """),
                    assets.tile("""
                        myTile51
                        """))
                tileUtil.replace_all_tiles(assets.tile("""
                        myTile51
                        """),
                    assets.tile("""
                        myTile58
                        """))
            for value152 in tiles.get_tiles_by_type(assets.tile("""
                myTile58
                """)):
                if tiles.tile_at_location_equals(value152.get_neighboring_location(CollisionDirection.BOTTOM),
                    assets.tile("""
                        myTile54
                        """)):
                    if Math.percent_chance(25):
                        tileUtil.cover_tile(value152.get_neighboring_location(CollisionDirection.BOTTOM),
                            assets.tile("""
                                myTile59
                                """))
game.on_update_interval(20000, on_update_interval2)
