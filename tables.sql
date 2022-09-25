CREATE TABLE "user" (
  "id" serial,
  "full_name" text,
  "email" text,
  "hashed_password" text,
  "is_active" boolean,
  "is_superuser" boolean
);