# This is the script used to generate the visualization gif for the README
# Obviously not meant for anything other than posterity

theme_fivethirtyeight <- function(base_size = 12, base_family = "sans") {
  (theme_foundation(base_size = base_size, base_family = base_family)
   + theme(
     line = element_line(colour = "black"),
     rect = element_rect(fill = "white",
                         linetype = 0, colour = NA),
     text = element_blank(),
     axis.title = element_blank(),
     axis.text = element_text(),
     axis.ticks = element_blank(),
     axis.line = element_blank(),
     legend.background = element_rect(),
     legend.position = "bottom",
     legend.direction = "horizontal",
     legend.box = "vertical",
     panel.grid = element_blank(),
     panel.grid.major =element_blank(),
     panel.grid.minor = element_blank(),
     # unfortunately, can't mimic subtitles
     plot.title = element_text(hjust = 0, size = rel(1.5), face = "bold"),
     plot.margin = unit(c(1, 1, 1, 1), "lines"),
     strip.background = element_rect()))
}
pal <- c("#99B898", "#FECEA8", "#FF847C", "#E84A5F", "#2A363B")

library(dplyr); library(ggplot2); library(reshape2);
library(tweenr); library(ggthemes); library(gganimate)

create_perm_ani <- function(csv_path, gif_path, size=1.8){
  perms <- read.csv(csv_path, header=FALSE)
  perms <- as.data.frame(lapply(perms, as.factor))
  perms$iter <- seq(1,nrow(perms))
  perms <- melt(perms, id.vars=c("iter"))
  perms$ease <- 'sine-in-out'
  perms$time <- perms$iter
  
  colnames(perms) <- c("x", "group", "y", "ease", "time")
  perms$y <- as.numeric(perms$y)
  perms$group <- as.numeric(perms$group)
  
  perms_dt <- tween_elements(perms, 'time', 'group', 'ease', nframes = 384)
  
  p <- ggplot(data=perms_dt, aes(x=x, y=y, col=.group,frame=.frame, cumulative = TRUE)) +
    geom_path(size=size, lineend="round", linejoin="round", alpha=0.9) +
    theme_fivethirtyeight() +
    guides(col=FALSE) +
    coord_cartesian(xlim=c(1,max(perms$time))) +
    scale_color_manual(values=c(pal[5],pal[3],pal[1],pal[4], pal[2])) 
  
  animation::ani.options(interval = 1/24, ani.width=960, ani.height=480)
  gg_animate(p, gif_path, title_frame = F)
  
}

# Create 3 level perm viz
create_perm_ani("perms_3.csv", "perms_three.gif")

# Create 4 level perm viz
create_perm_ani("perms.csv", "perms_four.gif")

# Create 5 level perm viz
create_perm_ani("perms_5.csv", "perms_five.gif", size=0.8)
