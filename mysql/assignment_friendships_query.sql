SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON friendships.friend_id = users2.id
ORDER BY friend_last_name;