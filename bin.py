import path_finding as pf

maze = pf.maze.create_wall_maze( 20, 12 )
filled = pf.short_path.fill_shortest_path(maze.board, maze.start, maze.end)
path = pf.short_path.backtrack_to_start(filled, maze.end)

finder = pf.draw.Finder()
finder.set_board(filled)
finder.set_path(path)
finder.run()

