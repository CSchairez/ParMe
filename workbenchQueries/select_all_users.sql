SELECT user_id AS "User ID", name, email, IF(admin = true, "Admin" , "Not Admin") AS Admin
FROM parme.user
WHERE user_id = 25;