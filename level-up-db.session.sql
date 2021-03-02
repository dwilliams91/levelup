SELECT
                    g.id,
                    g.title,
                    g.description,
                    g.gametype_id,
                    g.number_of_players,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    levelupapi_game g
                JOIN
                    levelupapi_gamer gr ON g.gamer_id = gr.id
                JOIN
                    auth_user u ON gr.user_id = u.id