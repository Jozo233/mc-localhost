#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void
crash (void)
{
  memset(NULL, '$', 1);
}

void
setup (void)
{
  char *port = (char*) malloc(100);
  char *playerCount = (char*) malloc(100);
  char *warez = (char*) malloc(6);
  
  printf ("Write port: ");
  scanf ("%s", port);

  if (atoi(port) > 65535 || atoi(port) <= 0) crash ();

  printf ("How many players will play: ");
  scanf ("%s", playerCount);

  if (atoi(playerCount) <= 0) crash ();

  printf ("Enable warez: [true/false] ");
  scanf ("%s", warez);

  if (!strcmp (warez, "true") || !strcmp (warez, "false")) {}
  else crash ();

  FILE *propertiesFile = fopen ("server.properties", "w");
  fprintf (propertiesFile, "query.port=");
  fprintf (propertiesFile, port);
  fprintf (propertiesFile, "\nmax-players=");
  fprintf (propertiesFile, playerCount);
  fprintf (propertiesFile, "\nonline-mode=");
  fprintf (propertiesFile, warez);
  fprintf (propertiesFile, "\n");
  fclose (propertiesFile);
  
  printf ("server.properties was generated\n");
}

void
run (void)
{
  char *ram = (char*) malloc(100);
  char *cmd = (char*) malloc(100);

  printf ("Write how many GB you want to give to server: ");
  scanf ("%s", ram);

  if (atoi (ram) <= 0) crash ();
  sprintf (cmd, "java -Xms%dG -Xmx%dG -jar server.jar nogui", atoi (ram), atoi (ram));

  system(cmd);
}

int
main(int argc, char **argv)
{
  int value;

  printf("\n\e[32;1m[1]\e[0m: Generate server.properties\n");
  printf("\e[32;1m[2]\e[0m: Run server\n");
  printf("\e[32;1m[3]\e[0m: Get free bitcoin\n\n>> ");

  scanf("%d", &value);

  switch (value)
    {
    case 1:
      setup ();
      break;

    case 2:
      run ();
      break;

    default:
      crash ();
    }

  return 0;
}
