-- t-sql script to create the tables for the caselist scraper

create table teams (
    team_id int primary key,
    team_school varchar(255),
    team_code4 varchar(4),
    team_code2 varchar(2),
    team_code2_alt varchar(2)
);

create table caselist (
    round_id int primary key identity(1,1),
    tournament_name varchar(255),
    round_name varchar(255),
    aff_team int,
    neg_team int,
    aff_doc varchar(255),
    neg_doc varchar(255),
    yt_link varchar(255),
    foreign key(aff_team) references teams(team_id),
    foreign key(neg_team) references teams(team_id)
);