import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "In a world where toys are living things who pretend to be lifeless when "
                        "humans are present, a group of toys, owned by six-year-old Andy Davis, are "
                        "caught off-guard when Andy's birthday party is moved up a week.", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        112)

avatar = media.Movie("Avatar", 
                     "No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que parecem ser "
                     "primitivos, mas são altamente evoluídos. Como o ambiente do planeta é tóxico, "
                     "foram criados os avatares, corpos biológicos controlados pela mente humana que se "
                     "movimentam livremente em Pandora.", 
                     "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=xTWLBuTak6I",
                     120)

forest_gump = media.Movie("Forest Gump",
                          "O filme começa com uma pena caindo aos pés de Forrest Gump, sentado numa parada"
                          " de ônibus em Savannah, na Georgia. Forrest pega a pena e coloca-a dentro de "
                          "um livro, e então começa a contar a história de sua vida a uma mulher sentada"
                          " próxima a ele.",
                          "https://upload.wikimedia.org/wikipedia/pt/c/c0/ForrestGumpPoster.jpg",
                          "https://www.youtube.com/watch?v=bLvqoHBptjg",
                          130)

prision_break = media.TvShow("Prision Break",
                             "Prison Break (Prison Break: Em Busca da Verdade no Brasil e Fuga da Prisão"
                             " em Portugal) é uma aclamada série de televisão norte-americana de ação, crime"
                             " e drama transmitida originalmente pela Fox desde 29 de agosto de 2005. Em 2015,"
                             " a Fox anunciou uma quinta temporada com 9 episódios, que estreou a 4 de abril de"
                             " 2017. A FOX confirmou, recentemente, a produção da sexta temporada da série, mas "
                             "não divulgou muitos detalhes a respeito",
                             "01",
                             "02",
                             "Local",
                             45,
                             "https://images-na.ssl-images-amazon.com/images/I/51GD8o2DwHL.jpg",
                             "https://www.youtube.com/watch?v=FeXRfJNSU1A")

movies = [toy_story, avatar, forest_gump, prision_break]
fresh_tomatoes.open_movies_page(movies)