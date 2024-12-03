```plaintext
+------------------------+
|    CutleryHunt         |
+------------------------+
| - screen               |
| - font1, font2, font3  |
| - timer                |
| - db                   |
| - sounds               |
| - fork_pic, knife_pic  |
| - knight_pic, ...      |
| - clock_time           |
| - score_check          |
| - end_time             |
| - x_knight, y_knight   |
| - skeletons1, skeletons2 |
| - points               |
| - x_fork, y_fork, ...  |
| - knife_line, spoon_line|
| - arrow_left, ...      |
+------------------------+
| + __init__(self)       |
| + download_pics()      |
| + download_voices()    |
| + play_sound()         |
| + create_database()    |
| + draw_screen()        |
| + clock()              |
| + show_stats()         |
| + cycle()              |
| + initialize_game()    |
| + initial_text()       |
| + countdown()          |
| + maingame()           |
| + end_text()           |
| + close_program()      |
+------------------------+
```



title Main Game Loop

participant Player as P
participant Game as G
participant Pygame as PG
participant SoundManager as SM
participant Random as R

P -> G: Start maingame()
loop Main Loop
    G -> G: draw_screen()
    G -> PG: clock()

    opt Display points
        G -> PG: render("POINTS {points}")
        G -> PG: blit(temp_surface)
    end

    alt Points reach limit
        G -> G: Increase difficulty level
        G -> SM: play_sound("surprise")
        opt Show "LEVEL" text
            G -> PG: render(f"LEVEL {difficulty_level}")
            G -> PG: blit(new_level_text)
        end
    end

    G -> PG: blit(knight_pic)
    G -> PG: blit(fork_pic, knife_pic, spoon_pic)

    loop Handle keypress events
        P -> G: Key press/release
        G -> G: Update knight position
        G -> G: Handle quit event
    end

    alt Collision with fork/knife/spoon
        G -> R: Generate new position
        G -> SM: play_sound("wump")
        G -> G: Update points
    end

    loop Handle skeleton movement
        G -> R: Update skeleton positions
        alt Collision with knight
            G -> SM: play_sound("crush")
            G -> PG: wait(1200ms)
            G -> G: end_text()
        end
        G -> PG: blit(skeleton_pic)
    end

    G -> PG: flip display
    G -> PG: tick(loop_speed)
end
