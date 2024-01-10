/*
** This file implements a DuckDB extension with multiple entrypoints.
**
** The default entrypoint, duckdb_ext_init, has a single function "a".
** The 1st alternate entrypoint, duckdb_ext_b_init, has a single function "b".
** The 2nd alternate entrypoint, duckdb_ext_c_init, has a single function "c".
**
** Compiling instructions:
**     https://www.sqlite.org/loadext.html#compiling_a_loadable_extension
**
*/

#include "duckdbext.h"

duckdb_EXTENSION_INIT1

// SQL function that returns back the value supplied during duckdb_create_function()
static void func(duckdb_context *context, int argc, duckdb_value **argv) {
  duckdb_result_text(context, (char *) duckdb_user_data(context), -1, duckdb_STATIC);
}


// The default entrypoint, since it matches the "ext.dylib"/"ext.so" name
#ifdef _WIN32
__declspec(dllexport)
#endif
int duckdb_ext_init(duckdb *db, char **pzErrMsg, const duckdb_api_routines *pApi) {
  duckdb_EXTENSION_INIT2(pApi);
  return duckdb_create_function(db, "a", 0, 0, "a", func, 0, 0);
}

// Alternate entrypoint #1
#ifdef _WIN32
__declspec(dllexport)
#endif
int duckdb_ext_b_init(duckdb *db, char **pzErrMsg, const duckdb_api_routines *pApi) {
  duckdb_EXTENSION_INIT2(pApi);
  return duckdb_create_function(db, "b", 0, 0, "b", func, 0, 0);
}

// Alternate entrypoint #2
#ifdef _WIN32
__declspec(dllexport)
#endif
int duckdb_ext_c_init(duckdb *db, char **pzErrMsg, const duckdb_api_routines *pApi) {
  duckdb_EXTENSION_INIT2(pApi);
  return duckdb_create_function(db, "c", 0, 0, "c", func, 0, 0);
}
