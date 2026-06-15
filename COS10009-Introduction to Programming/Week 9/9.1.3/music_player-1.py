import pygame
import sys

WIN_WIDTH = 1200
WIN_HEIGHT = 750

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE  = (30, 177, 250)
GOLD = (255, 215, 0)
DARK_BLUE = (20, 100, 160)
GREEN = (50, 200, 100)
RED = (220, 60, 60)
GREY = (180, 180, 180)
DARK_GREY = (60, 60, 60)

ALBUM_IMG_SIZE  = 220
MARGIN = 20
GRID_START_X = 30
ALBUMS_PER_PAGE = 4


class Track:
    def __init__(self, title, location):
        self.title = title
        self.location = location


class Album:
    def __init__(self, title, artist, image_path, tracks):
        self.title = title
        self.artist = artist
        self.tracks = tracks
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (ALBUM_IMG_SIZE, ALBUM_IMG_SIZE))
        except:
            self.image = pygame.Surface((ALBUM_IMG_SIZE, ALBUM_IMG_SIZE))
            self.image.fill((100, 100, 100))


selected_album_idx = -1
current_track_idx = -1
albums = []
current_page = 0
sort_mode = "default"
playlist = []
playlist_idx = -1
view_mode = "albums"
show_sort_menu = False
playlist_playing = False


def init():
    global track_font, title_font, small_font, heading_font
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("My Music Player")

    track_font = pygame.font.SysFont("Arial", 18)
    title_font = pygame.font.SysFont("Arial", 22, bold=True)
    small_font = pygame.font.SysFont("Arial", 15)
    heading_font = pygame.font.SysFont("Arial", 28, bold=True)
    return screen


def load_albums(filename):
    global albums
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        line_idx   = 0
        num_albums = int(lines[line_idx].strip())
        line_idx  += 1

        i = 0
        while i < num_albums:
            title = lines[line_idx].strip(); line_idx += 1
            artist = lines[line_idx].strip(); line_idx += 1
            img_path = lines[line_idx].strip(); line_idx += 1

            num_tracks = int(lines[line_idx].strip()); line_idx += 1
            tracks = []
            j = 0
            while j < num_tracks:
                t_title = lines[line_idx].strip(); line_idx += 1
                t_loc = lines[line_idx].strip(); line_idx += 1
                tracks.append(Track(t_title, t_loc))
                j += 1

            albums.append(Album(title, artist, img_path, tracks))
            i += 1
    except:
        pass


def get_sorted_albums():
    result = list(albums)
    if sort_mode == "title":
        i = 0
        while i < len(result) - 1:
            j = 0
            while j < len(result) - 1 - i:
                if result[j].title.lower() > result[j + 1].title.lower():
                    result[j], result[j + 1] = result[j + 1], result[j]
                j += 1
            i += 1
    elif sort_mode == "artist":
        i = 0
        while i < len(result) - 1:
            j = 0
            while j < len(result) - 1 - i:
                if result[j].artist.lower() > result[j + 1].artist.lower():
                    result[j], result[j + 1] = result[j + 1], result[j]
                j += 1
            i += 1
    return result


def get_page_albums():
    sorted_list = get_sorted_albums()
    start = current_page * ALBUMS_PER_PAGE
    end = start + ALBUMS_PER_PAGE
    return sorted_list[start:end], sorted_list


def total_pages():
    pages = len(albums) // ALBUMS_PER_PAGE
    if len(albums) % ALBUMS_PER_PAGE != 0:
        pages += 1
    return max(1, pages)


def area_clicked(mx, my, left, top, width, height):
    return (left <= mx <= left + width) and (top <= my <= top + height)


def get_album_rect(idx):
    col = idx % 2
    row = idx // 2
    x = GRID_START_X + col * (ALBUM_IMG_SIZE + MARGIN)
    y = 80 + row * (ALBUM_IMG_SIZE + MARGIN + 30)
    return x, y


def get_track_start_x():
    return GRID_START_X + 2 * (ALBUM_IMG_SIZE + MARGIN) + 30


def play_track(album_idx, track_idx):
    global current_track_idx, selected_album_idx, playlist_playing
    selected_album_idx = album_idx
    current_track_idx  = track_idx
    playlist_playing   = False
    track = get_sorted_albums()[album_idx].tracks[track_idx]
    try:
        pygame.mixer.music.load(track.location)
        pygame.mixer.music.play()
    except:
        pass


def play_playlist_track(idx):
    global playlist_idx, playlist_playing, current_track_idx, selected_album_idx
    if idx < 0 or idx >= len(playlist):
        playlist_playing = False
        return
    playlist_idx  = idx
    playlist_playing = True
    item = playlist[idx]
    try:
        pygame.mixer.music.load(item["track"].location)
        pygame.mixer.music.play()
    except:
        pass


def handle_mouse_click(pos):
    global selected_album_idx, current_track_idx, current_page
    global view_mode, show_sort_menu, sort_mode, playlist_playing

    mx, my = pos
    page_albums, sorted_albums = get_page_albums()

    if show_sort_menu:
        if area_clicked(mx, my, 20, 55, 130, 32):
            sort_mode = "default"
            show_sort_menu = False
            return
        if area_clicked(mx, my, 20, 92, 130, 32):
            sort_mode = "title"
            show_sort_menu = False
            return
        if area_clicked(mx, my, 20, 129, 130, 32):
            sort_mode = "artist"
            show_sort_menu = False
            return
        show_sort_menu = False
        return

    if area_clicked(mx, my, 20, 15, 90, 35):
        show_sort_menu = not show_sort_menu
        return
    if area_clicked(mx, my, WIN_WIDTH - 230, 15, 100, 35):
        view_mode = "albums"
        return
    if area_clicked(mx, my, WIN_WIDTH - 120, 15, 100, 35):
        view_mode = "playlist"
        return

    if view_mode == "playlist":
        i = 0
        while i < len(playlist):
            py = 120 + i * 50
            if area_clicked(mx, my, 500, py, 300, 35):
                play_playlist_track(i)
                return
            if area_clicked(mx, my, WIN_WIDTH - 110, py, 80, 35):
                playlist.pop(i)
                if playlist_idx >= len(playlist):
                    playlist_idx = len(playlist) - 1
                return
            i += 1
        if area_clicked(mx, my, 500, WIN_HEIGHT - 80, 120, 38):
            if playlist:
                play_playlist_track(0)
            return
        if area_clicked(mx, my, 635, WIN_HEIGHT - 80, 80, 38):
            pygame.mixer.music.stop()
            return

    if view_mode == "albums":
        if area_clicked(mx, my, 30, WIN_HEIGHT - 55, 120, 35) and current_page > 0:
            current_page -= 1
            return
        if area_clicked(mx, my, 300, WIN_HEIGHT - 55, 120, 35) and current_page < total_pages() - 1:
            current_page += 1
            return

        i = 0
        while i < len(page_albums):
            ax, ay   = get_album_rect(i)
            real_idx = current_page * ALBUMS_PER_PAGE + i
            if area_clicked(mx, my, ax, ay, ALBUM_IMG_SIZE, ALBUM_IMG_SIZE):
                if selected_album_idx != real_idx:
                    selected_album_idx = real_idx
                    current_track_idx = -1
                return
            i += 1

        if selected_album_idx != -1:
            album = sorted_albums[selected_album_idx]
            track_x = get_track_start_x()
            i = 0
            while i < len(album.tracks):
                ty = 120 + i * 50
                if area_clicked(mx, my, track_x, ty, 300, 35):
                    play_track(selected_album_idx, i)
                    return
                if area_clicked(mx, my, track_x + 310, ty, 100, 35):
                    playlist.append({"album": album.title, "track": album.tracks[i]})
                    return
                i += 1


def draw_button(screen, text, x, y, w, h, color, text_color=BLACK):
    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=8)
    label = small_font.render(text, True, text_color)
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))


def draw_top_bar(screen):
    pygame.draw.rect(screen, DARK_BLUE, (0, 0, WIN_WIDTH, 60))
    draw_button(screen, "Sort", 20, 15, 90, 35, DARK_GREY, WHITE)
    draw_button(screen, "Albums", WIN_WIDTH - 230, 15, 100, 35,
                GOLD if view_mode == "albums" else DARK_GREY,
                BLACK if view_mode == "albums" else WHITE)
    draw_button(screen, "Playlist", WIN_WIDTH - 120, 15, 100, 35,
                GOLD if view_mode == "playlist" else DARK_GREY,
                BLACK if view_mode == "playlist" else WHITE)


def draw_sort_menu(screen):
    if show_sort_menu:
        options = [("Default", "default"), ("By Title", "title"), ("By Artist", "artist")]
        k = 0
        while k < len(options):
            label, mode = options[k]
            color = GOLD if sort_mode == mode else DARK_GREY
            draw_button(screen, label, 20, 55 + k * 37, 130, 32, color, WHITE)
            k += 1


def draw_albums(screen):
    page_albums, _ = get_page_albums()
    i = 0
    while i < len(page_albums):
        album = page_albums[i]
        ax, ay = get_album_rect(i)
        real_idx = current_page * ALBUMS_PER_PAGE + i

        screen.blit(album.image, (ax, ay))
        if real_idx == selected_album_idx:
            pygame.draw.rect(screen, GOLD, (ax - 4, ay - 4, ALBUM_IMG_SIZE + 8, ALBUM_IMG_SIZE + 8), 4)

        name_label = small_font.render(album.title[:28], True, WHITE)
        screen.blit(name_label, (ax, ay + ALBUM_IMG_SIZE + 4))
        i += 1

    page_label = small_font.render("Page " + str(current_page + 1) + " / " + str(total_pages()), True, WHITE)
    screen.blit(page_label, (170, WIN_HEIGHT - 43))

    prev_color = DARK_BLUE if current_page > 0 else DARK_GREY
    next_color = DARK_BLUE if current_page < total_pages() - 1 else DARK_GREY
    draw_button(screen, "< Prev", 30, WIN_HEIGHT - 55, 120, 35, prev_color, WHITE)
    draw_button(screen, "Next >", 300, WIN_HEIGHT - 55, 120, 35, next_color, WHITE)


def draw_tracks(screen):
    sorted_albums = get_sorted_albums()
    track_x = get_track_start_x()

    if selected_album_idx == -1:
        hint = title_font.render("Click an album to see tracks", True, WHITE)
        screen.blit(hint, (track_x, 120))
        return

    if selected_album_idx >= len(sorted_albums):
        return

    album = sorted_albums[selected_album_idx]
    heading = title_font.render(album.title + " - " + album.artist, True, GOLD)
    screen.blit(heading, (track_x, 80))

    i = 0
    while i < len(album.tracks):
        ty = 120 + i * 50
        track = album.tracks[i]
        color = GOLD if i == current_track_idx and not playlist_playing else WHITE
        label = ("> " if i == current_track_idx and not playlist_playing else str(i + 1) + ". ") + track.title
        txt = track_font.render(label[:35], True, color)
        screen.blit(txt, (track_x, ty + 8))
        draw_button(screen, "+ Playlist", track_x + 310, ty, 100, 35, GREEN, BLACK)
        i += 1


def draw_playlist(screen):
    heading = heading_font.render("Playlist", True, GOLD)
    screen.blit(heading, (500, 70))

    if not playlist:
        empty = track_font.render("Playlist is empty. Add tracks from Albums view.", True, GREY)
        screen.blit(empty, (500, 120))
    else:
        i = 0
        while i < len(playlist):
            py = 120 + i * 50
            item = playlist[i]
            color = GOLD if i == playlist_idx and playlist_playing else WHITE
            label = str(i + 1) + ".  " + item["track"].title + "   [" + item["album"] + "]"
            txt = track_font.render(label[:55], True, color)
            screen.blit(txt, (500, py + 8))
            draw_button(screen, "Remove", WIN_WIDTH - 110, py, 80, 35, RED, WHITE)
            i += 1

        draw_button(screen, "Play All", 500, WIN_HEIGHT - 80, 120, 38, GREEN, BLACK)
        draw_button(screen, "Stop",     635, WIN_HEIGHT - 80, 80,  38, RED,   WHITE)

    if playlist_playing and not pygame.mixer.music.get_busy():
        next_idx = playlist_idx + 1
        if next_idx < len(playlist):
            play_playlist_track(next_idx)


def main():
    screen = init()
    load_albums("albums.txt")
    clock = pygame.time.Clock()

    while True:
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_mouse_click(event.pos)

        if view_mode == "albums":
            draw_albums(screen)
            draw_tracks(screen)
        elif view_mode == "playlist":
            draw_playlist(screen)

        draw_top_bar(screen)
        draw_sort_menu(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()