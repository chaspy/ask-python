insert into auth_user(id, password, is_superuser, 
username,first_name, last_name, email, is_staff, is_active,
date_joined)
-- password is hogehoge
values(1,'pbkdf2_sha256$120000$9DUqKL62jJMy$M17aEpPlwMoq/AhQy8GVrF0c9kzNRK45AavNQ38u3yo=',
false, 'dummy','dummy', 'dummy', 'dummy@email.com', 
false, true, now());