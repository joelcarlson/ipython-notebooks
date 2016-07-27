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

perms <- read.csv("perms.csv", header=FALSE)
perms <- as.data.frame(lapply(perms, as.factor))
perms$iter <- seq(1,nrow(perms))
perms <- melt(perms, id.vars=c("iter"))

ggplot(data=perms, aes(x=iter, y=value, col=variable, group=variable)) +
  geom_line(size=1.8, lineend="round", linejoin="round", alpha=0.9) +
  theme_fivethirtyeight() +
  guides(col=FALSE) +
  coord_cartesian(xlim=c(0,max(perms$iter))) +
  scale_color_manual(values=c(pal[5],pal[3],pal[1],pal[4]))

perms_cp <- perms
perms_cp$ease <- 'sine-in-out'
perms_cp$time <- perms_cp$iter

colnames(perms_cp) <- c("x", "group", "y", "ease", "time")
perms_cp$y <- as.numeric(perms_cp$y)
perms_cp$group <- as.numeric(perms_cp$group)

perms_dt <- tween_elements(perms_cp, 'time', 'group', 'ease', nframes = 384)

p <- ggplot(data=perms_dt, aes(x=x, y=y, col=.group,frame=.frame, cumulative = TRUE)) +
  geom_path(size=1.8, lineend="round", linejoin="round", alpha=0.9) +
  theme_fivethirtyeight() +
  guides(col=FALSE) +
  coord_cartesian(xlim=c(1,max(perms_cp$time))) +
  scale_color_manual(values=c(pal[5],pal[3],pal[1],pal[4])) 

animation::ani.options(interval = 1/24, ani.width=960, ani.height=480)
gg_animate(p, 'perms_four_blank.gif', title_frame = F)