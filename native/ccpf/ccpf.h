#pragma once

int cpf_validate(char* cpf);
// 'cpf' must have space for 11 chars
void cpf_generate(char* cpf);
// returns 2 if format is invalid
int cpf_has_mask(char* cpf, int size);
void cpf_mask(char* cpf);
void cpf_unmask(char* cpf);
