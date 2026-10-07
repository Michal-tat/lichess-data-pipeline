CREATE TABLE IF NOT EXISTS silver.games (
    id              TEXT,
    rated           BOOLEAN,
    created_at      DOUBLE PRECISION,
    last_move_at    DOUBLE PRECISION,
    turns           BIGINT,
    victory_status  TEXT,
    winner          TEXT,
    increment_code  TEXT,
    white_id        TEXT,
    white_rating    BIGINT,
    black_id        TEXT,
    black_rating    BIGINT,
    moves           TEXT,
    opening_eco     TEXT,
    opening_name    TEXT,
    opening_ply     BIGINT
);