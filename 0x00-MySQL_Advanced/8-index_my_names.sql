-- Script to create index on names and first letter 

CREATE INDEX idx_name_first ON names(name(1))
