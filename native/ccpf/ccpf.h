#pragma once

int cpf_validate(char* cpf);
// 'cpf' must have space for 11 chars
void cpf_generate(char* cpf);
int cpf_has_mask(char* cpf);
void cpf_mask(char* cpf);
void cpf_unmask(char* cpf);
