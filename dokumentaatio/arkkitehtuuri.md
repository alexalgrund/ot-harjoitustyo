```mermaid
classDiagram
    class CutleryHunt {
        +screen
        +font1, font2, font3
        +timer
        +db
        +sounds
        +fork_pic, knife_pic
        +knight_pic, ...
        +clock_time
        +score_check
        +end_time
        +x_knight, y_knight
        +skeletons1, skeletons2
        +points
        +x_fork, y_fork, ...
        +knife_line, spoon_line
        +arrow_left, ...
        +__init__(self)
        +download_pics()
        +download_voices()
        +play_sound()
        +create_database()
        +draw_screen()
        +clock()
        +show_stats()
        +cycle()
        +initialize_game()
        +initial_text()
        +countdown()
        +maingame()
        +end_text()
        +close_program()
    }
```
Alla oleva sekvensikaavio kuvaa pelin päätoiminnallisuutta, siis funktiota maingame().

```mermaid
graph TD
    A[maingame] --> B[draw_screen]
    A --> C[clock]
    A --> D[Render points and level]
    D --> D1[Update points text]
    D --> D2[Check points limit]
    D --> D3[Update level: difficulty level and loop speed]
    D --> D4[Display LEVEL: difficulty_level if applicable]
    A --> E[Render graphics]
    E --> E1[Display knight]
    E --> E2[Display fork]
    E --> E3[Display knife]
    E --> E4[Display spoon]
    A --> F[Handle user input]
    F --> F1[Arrow keys: up, down, left, right]
    F --> F2[Quit event]
    A --> G[Knight movement]
    G --> G1[Horizontal: left, right]
    G --> G2[Vertical: up, down]
    A --> H[Item collection]
    H --> H1[Fork]
    H --> H2[Knife]
    H --> H3[Spoon]
    A --> I[Skeletons]
    I --> I1[Initialize positions: skeletons1, skeletons2]
    I --> I2[Move skeletons]
    I --> I3[Collision detection]
    I3 --> I31[Skeleton 1 collision]
    I3 --> I32[Skeleton 2 collision]
    A --> J[End text on collision]
    A --> K[Update display]
    A --> L[Timer tick: loop speed]
